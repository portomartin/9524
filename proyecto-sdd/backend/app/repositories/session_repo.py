from datetime import datetime, timezone
from typing import List, Optional, Dict, Any, Tuple
from sqlmodel import Session, select, col

from ..models import ExchangeSession, CreditMovement, Review, User, AvailabilitySlot


class SessionRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, session_id: str) -> Optional[ExchangeSession]:
        stmt = select(ExchangeSession).where(ExchangeSession.id == session_id)
        return self.session.exec(stmt).first()

    def get_user_sessions(self, user_id: str, status: Optional[str] = None) -> List[ExchangeSession]:
        stmt = select(ExchangeSession).where(
            (ExchangeSession.teacher_id == user_id) | (ExchangeSession.student_id == user_id)
        )
        if status:
            stmt = stmt.where(ExchangeSession.status == status.upper())
        stmt = stmt.order_by(col(ExchangeSession.date).desc(), col(ExchangeSession.start_time).desc())
        return list(self.session.exec(stmt).all())

    def get_user_history(
        self,
        user_id: str,
        status: Optional[str] = None,
        page: int = 1,
        page_size: int = 20,
    ) -> Tuple[List[ExchangeSession], int]:
        stmt = select(ExchangeSession).where(
            (ExchangeSession.teacher_id == user_id) | (ExchangeSession.student_id == user_id)
        )
        if status:
            stmt = stmt.where(ExchangeSession.status == status.upper())
        else:
            # Historial por defecto: sesiones finalizadas o canceladas
            stmt = stmt.where(ExchangeSession.status.in_(["FINALIZADA", "CANCELADA"]))

        stmt = stmt.order_by(col(ExchangeSession.date).desc(), col(ExchangeSession.start_time).desc())
        all_items = list(self.session.exec(stmt).all())
        total = len(all_items)
        start = (page - 1) * page_size
        return all_items[start : start + page_size], total

    def create(self, exc_session: ExchangeSession) -> ExchangeSession:
        self.session.add(exc_session)
        self.session.commit()
        self.session.refresh(exc_session)
        return exc_session

    def update_status(self, exc_session: ExchangeSession, new_status: str) -> ExchangeSession:
        exc_session.status = new_status
        self.session.add(exc_session)
        self.session.commit()
        self.session.refresh(exc_session)
        return exc_session

    def transfer_credits_atomic(
        self,
        exc_session: ExchangeSession,
        student: User,
        teacher: User,
        amount: int = 1,
    ) -> bool:
        """
        Ejecuta la transferencia de créditos de forma atómica e idempotente.
        Retorna True si transfirió, o False si ya estaba transferido.
        """
        if amount <= 0:
            return True

        # Idempotencia: Verificar si ya existe movimiento para esta sesión
        existing_mov = self.session.exec(
            select(CreditMovement).where(CreditMovement.session_id == exc_session.id)
        ).first()
        if existing_mov:
            return False  # Ya fue transferido previamente

        now = datetime.now(timezone.utc)

        # 1. Descontar del alumno
        student.credit_balance -= amount
        mov_student = CreditMovement(
            user_id=student.id,
            session_id=exc_session.id,
            amount=-amount,
            balance_after=student.credit_balance,
            reason="SESSION_PAYMENT",
            created_at=now,
        )

        # 2. Acreditar al profesor
        teacher.credit_balance += amount
        mov_teacher = CreditMovement(
            user_id=teacher.id,
            session_id=exc_session.id,
            amount=amount,
            balance_after=teacher.credit_balance,
            reason="SESSION_EARNING",
            created_at=now,
        )

        self.session.add(student)
        self.session.add(teacher)
        self.session.add(mov_student)
        self.session.add(mov_teacher)
        self.session.commit()
        return True

    def get_user_credit_movements(
        self,
        user_id: str,
        page: int = 1,
        page_size: int = 20,
    ) -> Tuple[List[CreditMovement], int]:
        stmt = (
            select(CreditMovement)
            .where(CreditMovement.user_id == user_id)
            .order_by(col(CreditMovement.created_at).desc())
        )
        all_movs = list(self.session.exec(stmt).all())
        total = len(all_movs)
        start = (page - 1) * page_size
        return all_movs[start : start + page_size], total

    def has_user_reviewed(self, session_id: str, reviewer_id: str) -> bool:
        stmt = select(Review).where(
            Review.session_id == session_id,
            Review.reviewer_id == reviewer_id,
        )
        return self.session.exec(stmt).first() is not None

    def create_review(self, review: Review, exc_session: ExchangeSession) -> Review:
        exc_session.rated = True
        self.session.add(review)
        self.session.add(exc_session)
        self.session.commit()
        self.session.refresh(review)
        return review
