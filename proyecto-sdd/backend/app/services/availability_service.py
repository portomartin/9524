from typing import Dict, Any, List, Optional
from fastapi import HTTPException, status
from sqlmodel import Session

from ..models import AvailabilitySlot, User
from ..repositories.availability_repo import AvailabilityRepository


class AvailabilityService:
    def __init__(self, session: Session):
        self.session = session
        self.repo = AvailabilityRepository(session)

    def _format_slot(self, slot: AvailabilitySlot) -> Dict[str, Any]:
        return {
            "id": slot.id,
            "userId": slot.user_id,
            "user_id": slot.user_id,
            "date": slot.date,
            "startTime": slot.start_time,
            "start_time": slot.start_time,
            "durationMinutes": slot.duration_minutes,
            "duration_minutes": slot.duration_minutes,
            "isBooked": slot.is_booked,
            "is_booked": slot.is_booked,
            "isPublic": slot.is_public,
            "is_public": slot.is_public,
            "createdAt": slot.created_at.isoformat() if slot.created_at else "",
        }

    def get_my_slots(self, user: User) -> List[Dict[str, Any]]:
        slots = self.repo.get_user_slots(user.id)
        return [self._format_slot(s) for s in slots]

    def get_public_slots(self, user_id: str) -> List[Dict[str, Any]]:
        slots = self.repo.get_public_user_slots(user_id)
        return [self._format_slot(s) for s in slots]

    def create_slot(self, user: User, data: Dict[str, Any]) -> Dict[str, Any]:
        date = data.get("date", "").strip()
        start_time = data.get("startTime") or data.get("start_time", "")
        start_time = start_time.strip() if isinstance(start_time, str) else ""

        if not date or not start_time:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail={"code": "MISSING_DATE_OR_TIME", "message": "Fecha y hora de inicio son obligatorias.", "fields": {}},
            )

        duration = int(data.get("durationMinutes") or data.get("duration_minutes") or 60)
        # Regla explícita MVP V3: "La unidad mínima de disponibilidad es una hora"
        if duration < 60:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail={"code": "INVALID_DURATION", "message": "La unidad mínima de disponibilidad es de 60 minutos.", "fields": {"duration": duration}},
            )

        is_public = data.get("isPublic") if data.get("isPublic") is not None else data.get("is_public", True)

        slot = AvailabilitySlot(
            user_id=user.id,
            date=date,
            start_time=start_time,
            duration_minutes=duration,
            is_booked=False,
            is_public=bool(is_public),
        )
        created = self.repo.create_slot(slot)
        return self._format_slot(created)

    def update_slot(self, user: User, slot_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        slot = self.repo.get_slot_by_id(slot_id)
        if not slot:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={"code": "SLOT_NOT_FOUND", "message": "Franja horaria no encontrada.", "fields": {"slotId": slot_id}},
            )

        if slot.user_id != user.id and user.role != "ADMIN":
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail={"code": "FORBIDDEN", "message": "Solo podés modificar tus propias franjas horarias.", "fields": {}},
            )

        # Regla MVP V3: franjas comprometidas no se pueden alterar
        if slot.is_booked:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail={"code": "SLOT_BOOKED", "message": "No podés modificar una franja comprometida en una sesión acordada.", "fields": {}},
            )

        update_fields = {}
        if "date" in data:
            update_fields["date"] = data["date"]
        if "startTime" in data or "start_time" in data:
            update_fields["start_time"] = data.get("startTime") or data.get("start_time")
        if "durationMinutes" in data or "duration_minutes" in data:
            duration = int(data.get("durationMinutes") or data.get("duration_minutes"))
            if duration < 60:
                raise HTTPException(
                    status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                    detail={"code": "INVALID_DURATION", "message": "La unidad mínima de disponibilidad es de 60 minutos.", "fields": {}},
                )
            update_fields["duration_minutes"] = duration
        if "isPublic" in data or "is_public" in data:
            update_fields["is_public"] = bool(data.get("isPublic") if data.get("isPublic") is not None else data.get("is_public"))

        updated = self.repo.update_slot(slot, update_fields)
        return self._format_slot(updated)

    def delete_slot(self, user: User, slot_id: str) -> Dict[str, Any]:
        slot = self.repo.get_slot_by_id(slot_id)
        if not slot:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={"code": "SLOT_NOT_FOUND", "message": "Franja horaria no encontrada.", "fields": {"slotId": slot_id}},
            )

        if slot.user_id != user.id and user.role != "ADMIN":
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail={"code": "FORBIDDEN", "message": "Solo podés eliminar tus propias franjas horarias.", "fields": {}},
            )

        # Regla MVP V3: franjas comprometidas no se pueden eliminar
        if slot.is_booked:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail={"code": "SLOT_BOOKED", "message": "No podés eliminar una franja comprometida en una sesión acordada.", "fields": {}},
            )

        self.repo.delete_slot(slot)
        return {"message": "Franja horaria eliminada correctamente.", "id": slot_id}

    def set_visibility(self, user: User, is_public: bool) -> Dict[str, Any]:
        updated_user = self.repo.set_agenda_visibility(user, is_public)
        return {
            "userId": updated_user.id,
            "agendaPublic": updated_user.agenda_public,
            "message": "Visibilidad de agenda actualizada correctamente.",
        }
