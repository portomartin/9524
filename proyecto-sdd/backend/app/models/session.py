from datetime import datetime, timezone
from typing import Optional
from sqlmodel import SQLModel, Field
import uuid


def generate_session_id() -> str:
    return f"ses-{uuid.uuid4().hex[:8]}"


class ExchangeSession(SQLModel, table=True):
    __tablename__ = "exchange_sessions"

    id: str = Field(default_factory=generate_session_id, primary_key=True, index=True)
    offer_id: Optional[str] = Field(default=None, foreign_key="teaching_offers.id")
    title: str
    teacher_id: str = Field(foreign_key="users.id", index=True)
    student_id: str = Field(foreign_key="users.id", index=True)
    date: str  # YYYY-MM-DD
    start_time: str  # HH:MM
    duration_minutes: int = Field(default=60)
    modality: str = Field(default="Virtual")
    exchange_type: str = Field(default="CREDITS")  # CREDITS o RECIPROCAL
    credit_cost: int = Field(default=1)  # 1 si es por créditos, 0 si es recíproco
    status: str = Field(default="SOLICITADA", index=True)  # SOLICITADA, ACEPTADA, FINALIZADA, CANCELADA
    rated: bool = Field(default=False)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
