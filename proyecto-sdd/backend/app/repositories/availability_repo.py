from typing import List, Optional, Dict, Any
from sqlmodel import Session, select, col
from ..models import AvailabilitySlot, User


class AvailabilityRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_user_slots(self, user_id: str) -> List[AvailabilitySlot]:
        stmt = (
            select(AvailabilitySlot)
            .where(AvailabilitySlot.user_id == user_id)
            .order_by(col(AvailabilitySlot.date).asc(), col(AvailabilitySlot.start_time).asc())
        )
        return list(self.session.exec(stmt).all())

    def get_public_user_slots(self, user_id: str) -> List[AvailabilitySlot]:
        # Verificar que el usuario tenga la agenda activa y pública
        user = self.session.exec(select(User).where(User.id == user_id)).first()
        if not user or not user.is_active or not user.agenda_public:
            return []

        stmt = (
            select(AvailabilitySlot)
            .where(
                AvailabilitySlot.user_id == user_id,
                AvailabilitySlot.is_booked == False,
                AvailabilitySlot.is_public == True,
            )
            .order_by(col(AvailabilitySlot.date).asc(), col(AvailabilitySlot.start_time).asc())
        )
        return list(self.session.exec(stmt).all())

    def get_slot_by_id(self, slot_id: str) -> Optional[AvailabilitySlot]:
        stmt = select(AvailabilitySlot).where(AvailabilitySlot.id == slot_id)
        return self.session.exec(stmt).first()

    def create_slot(self, slot: AvailabilitySlot) -> AvailabilitySlot:
        self.session.add(slot)
        self.session.commit()
        self.session.refresh(slot)
        return slot

    def update_slot(self, slot: AvailabilitySlot, update_data: Dict[str, Any]) -> AvailabilitySlot:
        for field, value in update_data.items():
            if value is not None and hasattr(slot, field):
                setattr(slot, field, value)
        self.session.add(slot)
        self.session.commit()
        self.session.refresh(slot)
        return slot

    def delete_slot(self, slot: AvailabilitySlot) -> None:
        self.session.delete(slot)
        self.session.commit()

    def set_agenda_visibility(self, user: User, is_public: bool) -> User:
        user.agenda_public = is_public
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user
