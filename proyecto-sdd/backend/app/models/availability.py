from datetime import datetime, timezone
from sqlmodel import SQLModel, Field
import uuid


def generate_slot_id() -> str:
    return f"slot-{uuid.uuid4().hex[:8]}"


class AvailabilitySlot(SQLModel, table=True):
    __tablename__ = "availability_slots"

    id: str = Field(default_factory=generate_slot_id, primary_key=True, index=True)
    user_id: str = Field(foreign_key="users.id", index=True)
    date: str = Field(index=True)  # YYYY-MM-DD
    start_time: str  # HH:MM
    duration_minutes: int = Field(default=60)  # Mínimo 60 min según MVP V3
    is_booked: bool = Field(default=False, index=True)
    is_public: bool = Field(default=True)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
