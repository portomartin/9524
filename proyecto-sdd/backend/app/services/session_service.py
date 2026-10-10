from typing import Dict, Any, List, Optional
from fastapi import HTTPException, status
from sqlmodel import Session, select

from ..models import ExchangeSession, User, AvailabilitySlot, Review, CreditMovement
from ..repositories.session_repo import SessionRepository
from ..repositories.user_repo import UserRepository
from ..repositories.availability_repo import AvailabilityRepository


class SessionService:
    def __init__(self, session: Session):
        self.session = session
        self.repo = SessionRepository(session)
        self.user_repo = UserRepository(session)
        self.avail_repo = AvailabilityRepository(session)

    def _get_user_name(self, user_id: str) -> str:
        user = self.user_repo.get_by_id(user_id)
        return user.name if user else "Usuario"

    def format_session(self, s: ExchangeSession, current_user_id: Optional[str] = None) -> Dict[str, Any]:
        teacher_name = self._get_user_name(s.teacher_id)
        student_name = self._get_user_name(s.student_id)

        counterpart = teacher_name if current_user_id == s.student_id else student_name

        return {
            "id": s.id,
            "offerId": s.offer_id,
            "offer_id": s.offer_id,
            "title": s.title,
            "teacherId": s.teacher_id,
            "teacher_id": s.teacher_id,
            "teacherName": teacher_name,
            "studentId": s.student_id,
            "student_id": s.student_id,
            "studentName": student_name,
            "counterpart": counterpart,
            "participantIds": [s.teacher_id, s.student_id],
            "date": s.date,
            "proposedDate": s.date,
            "startTime": s.start_time,
            "start_time": s.start_time,
            "durationMinutes": s.duration_minutes,
            "duration_minutes": s.duration_minutes,
            "modality": s.modality,
            "exchangeType": s.exchange_type,
            "exchange_type": s.exchange_type,
            "creditCost": s.credit_cost,
            "credit_cost": s.credit_cost,
            "status": s.status,
            "rated": s.rated,
            "createdAt": s.created_at.isoformat() if s.created_at else "",
        }

    def create_session(self, current_user: User, data: Dict[str, Any]) -> Dict[str, Any]:
        title = data.get("title", "").strip() or "Sesión de intercambio de aprendizaje"
        teacher_id = data.get("teacherId") or data.get("teacher_id")
        student_id = data.get("studentId") or data.get("student_id")

        # Si el usuario no especificó roles, determinamos por quién llama
        if not teacher_id and not student_id:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail={"code": "MISSING_PARTICIPANTS", "message": "Se requiere especificar al menos un participante contraparte.", "fields": {}},
            )

        if not student_id:
            student_id = current_user.id
        elif not teacher_id:
            teacher_id = current_user.id

        if teacher_id == student_id:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail={"code": "SAME_USER", "message": "No podés realizar un intercambio con vos mismo.", "fields": {}},
            )

        exchange_type = (data.get("exchangeType") or data.get("exchange_type") or "CREDITS").upper()
        credit_cost = 1 if exchange_type == "CREDITS" else 0

        # Regla de créditos: verificar saldo del estudiante
        student = self.user_repo.get_by_id(student_id)
        if not student:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={"code": "STUDENT_NOT_FOUND", "message": "Estudiante no encontrado.", "fields": {}},
            )

        if exchange_type == "CREDITS" and student.credit_balance < credit_cost:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail={
                    "code": "INSUFFICIENT_CREDITS",
                    "message": "No contás con créditos suficientes para solicitar esta sesión.",
                    "fields": {"creditBalance": student.credit_balance, "creditCost": credit_cost},
                },
            )

        date = data.get("date") or data.get("proposedDate") or ""
        start_time = data.get("startTime") or data.get("start_time") or ""

        # Si se indicó una franja horaria existente, marcarla como comprometida
        slot_id = data.get("slotId") or data.get("slot_id")
        if slot_id:
            slot = self.avail_repo.get_slot_by_id(slot_id)
            if slot:
                if slot.is_booked:
                    raise HTTPException(
                        status_code=status.HTTP_409_CONFLICT,
                        detail={"code": "SLOT_ALREADY_BOOKED", "message": "El horario seleccionado ya fue tomado.", "fields": {}},
                    )
                slot.is_booked = True
                self.session.add(slot)
                if not date:
                    date = slot.date
                if not start_time:
                    start_time = slot.start_time

        new_session = ExchangeSession(
            offer_id=data.get("offerId") or data.get("offer_id"),
            title=title,
            teacher_id=teacher_id,
            student_id=student_id,
            date=date or "2026-10-20",
            start_time=start_time or "10:00",
            duration_minutes=int(data.get("durationMinutes") or data.get("duration_minutes") or 60),
            modality=data.get("modality", "Virtual"),
            exchange_type=exchange_type,
            credit_cost=credit_cost,
            status="SOLICITADA",
            rated=False,
        )
        created = self.repo.create(new_session)
        return self.format_session(created, current_user.id)

    def confirm_session(self, current_user: User, session_id: str) -> Dict[str, Any]:
        s = self.repo.get_by_id(session_id)
        if not s:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={"code": "SESSION_NOT_FOUND", "message": "Sesión no encontrada.", "fields": {"sessionId": session_id}},
            )

        if current_user.id not in [s.teacher_id, s.student_id] and current_user.role != "ADMIN":
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail={"code": "FORBIDDEN", "message": "No sos participante de esta sesión.", "fields": {}},
            )

        if s.status != "SOLICITADA":
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail={"code": "INVALID_STATE", "message": f"No se puede confirmar una sesión en estado {s.status}.", "fields": {}},
            )

        updated = self.repo.update_status(s, "ACEPTADA")
        return self.format_session(updated, current_user.id)

    def cancel_session(self, current_user: User, session_id: str) -> Dict[str, Any]:
        s = self.repo.get_by_id(session_id)
        if not s:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={"code": "SESSION_NOT_FOUND", "message": "Sesión no encontrada.", "fields": {"sessionId": session_id}},
            )

        if current_user.id not in [s.teacher_id, s.student_id] and current_user.role != "ADMIN":
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail={"code": "FORBIDDEN", "message": "No sos participante de esta sesión.", "fields": {}},
            )

        if s.status in ["FINALIZADA", "CANCELADA"]:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail={"code": "INVALID_STATE", "message": f"No se puede cancelar una sesión que ya está {s.status}.", "fields": {}},
            )

        # Liberar posibles franjas horarias que hubieran quedado comprometidas
        slots = self.session.exec(
            select(AvailabilitySlot).where(
                AvailabilitySlot.user_id == s.teacher_id,
                AvailabilitySlot.date == s.date,
                AvailabilitySlot.start_time == s.start_time,
            )
        ).all()
        for slot in slots:
            slot.is_booked = False
            self.session.add(slot)

        updated = self.repo.update_status(s, "CANCELADA")
        return self.format_session(updated, current_user.id)

    def complete_session(self, current_user: User, session_id: str) -> Dict[str, Any]:
        s = self.repo.get_by_id(session_id)
        if not s:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={"code": "SESSION_NOT_FOUND", "message": "Sesión no encontrada.", "fields": {"sessionId": session_id}},
            )

        if current_user.id not in [s.teacher_id, s.student_id] and current_user.role != "ADMIN":
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail={"code": "FORBIDDEN", "message": "No sos participante de esta sesión.", "fields": {}},
            )

        if s.status != "ACEPTADA":
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail={"code": "INVALID_STATE", "message": f"Solo se puede finalizar una sesión que esté ACEPTADA (actual: {s.status}).", "fields": {}},
            )

        # 1. Marcar como finalizada
        updated = self.repo.update_status(s, "FINALIZADA")

        # 2. Transferencia de créditos atómica si es por créditos
        if updated.exchange_type == "CREDITS" and updated.credit_cost > 0:
            student = self.user_repo.get_by_id(updated.student_id)
            teacher = self.user_repo.get_by_id(updated.teacher_id)
            if student and teacher:
                self.repo.transfer_credits_atomic(updated, student, teacher, updated.credit_cost)

        return self.format_session(updated, current_user.id)

    def transfer_credits(self, current_user: User, session_id: str) -> Dict[str, Any]:
        s = self.repo.get_by_id(session_id)
        if not s:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={"code": "SESSION_NOT_FOUND", "message": "Sesión no encontrada.", "fields": {"sessionId": session_id}},
            )

        if s.exchange_type != "CREDITS" or s.credit_cost <= 0:
            return {"message": "La sesión es recíproca o sin costo de créditos.", "transferred": False}

        student = self.user_repo.get_by_id(s.student_id)
        teacher = self.user_repo.get_by_id(s.teacher_id)
        if not student or not teacher:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Participantes no encontrados.")

        transferred = self.repo.transfer_credits_atomic(s, student, teacher, s.credit_cost)
        return {
            "sessionId": s.id,
            "transferred": transferred,
            "message": "Transferencia ejecutada con éxito." if transferred else "La transferencia ya había sido ejecutada previamente (idempotente).",
            "studentBalance": student.credit_balance,
            "teacherBalance": teacher.credit_balance,
        }

    def get_user_sessions(self, current_user: User, status: Optional[str] = None) -> List[Dict[str, Any]]:
        sessions = self.repo.get_user_sessions(current_user.id, status=status)
        return [self.format_session(s, current_user.id) for s in sessions]

    def get_history(
        self,
        current_user: User,
        status: Optional[str] = None,
        page: int = 1,
        page_size: int = 20,
    ) -> Dict[str, Any]:
        items, total = self.repo.get_user_history(current_user.id, status=status, page=page, page_size=page_size)
        total_pages = (total + page_size - 1) // page_size if total > 0 else 0
        return {
            "items": [self.format_session(s, current_user.id) for s in items],
            "pagination": {
                "page": page,
                "pageSize": page_size,
                "totalItems": total,
                "totalPages": total_pages,
            },
        }

    def get_credit_movements(self, current_user: User, page: int = 1, page_size: int = 20) -> Dict[str, Any]:
        items, total = self.repo.get_user_credit_movements(current_user.id, page=page, page_size=page_size)
        formatted = []
        for m in items:
            formatted.append({
                "id": m.id,
                "userId": m.user_id,
                "sessionId": m.session_id,
                "amount": m.amount,
                "balanceAfter": m.balance_after,
                "reason": m.reason,
                "createdAt": m.created_at.isoformat() if m.created_at else "",
            })
        total_pages = (total + page_size - 1) // page_size if total > 0 else 0
        return {
            "items": formatted,
            "pagination": {
                "page": page,
                "pageSize": page_size,
                "totalItems": total,
                "totalPages": total_pages,
            },
        }

    def create_rating(
        self,
        current_user: User,
        session_id: str,
        data: Dict[str, Any],
    ) -> Dict[str, Any]:
        s = self.repo.get_by_id(session_id)
        if not s:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={"code": "SESSION_NOT_FOUND", "message": "Sesión no encontrada.", "fields": {"sessionId": session_id}},
            )

        if current_user.id not in [s.teacher_id, s.student_id]:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail={"code": "FORBIDDEN", "message": "Solo los participantes de la sesión pueden calificar.", "fields": {}},
            )

        if s.status != "FINALIZADA":
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail={"code": "SESSION_NOT_FINISHED", "message": "Solo podés calificar una sesión que haya FINALIZADO.", "fields": {}},
            )

        if self.repo.has_user_reviewed(session_id, current_user.id):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail={"code": "ALREADY_REVIEWED", "message": "Ya calificaste esta sesión.", "fields": {}},
            )

        rating = int(data.get("rating") or data.get("score") or 5)
        if rating < 1 or rating > 5:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail={"code": "INVALID_RATING", "message": "La calificación debe ser un valor de 1 a 5 estrellas.", "fields": {}},
            )

        reviewee_id = s.teacher_id if current_user.id == s.student_id else s.student_id
        review = Review(
            session_id=s.id,
            reviewer_id=current_user.id,
            reviewee_id=reviewee_id,
            rating=rating,
            comment=data.get("comment", "").strip(),
        )
        created_rev = self.repo.create_review(review, s)

        return {
            "id": created_rev.id,
            "sessionId": created_rev.session_id,
            "reviewerId": created_rev.reviewer_id,
            "revieweeId": created_rev.reviewee_id,
            "rating": created_rev.rating,
            "score": created_rev.rating,
            "comment": created_rev.comment,
            "createdAt": created_rev.created_at.isoformat() if created_rev.created_at else "",
            "message": "Calificación registrada con éxito.",
        }
