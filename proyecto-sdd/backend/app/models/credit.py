from datetime import datetime, timezone
from typing import Optional
from sqlmodel import SQLModel, Field
import uuid


def generate_movement_id() -> str:
    return f"mov-{uuid.uuid4().hex[:8]}"


class CreditMovement(SQLModel, table=True):
    __tablename__ = "credit_movements"

    id: str = Field(default_factory=generate_movement_id, primary_key=True, index=True)
    user_id: str = Field(foreign_key="users.id", index=True)
    session_id: Optional[str] = Field(default=None, foreign_key="exchange_sessions.id")
    amount: int  # +1 o -1
    balance_after: int
    reason: str  # INITIAL_GRANT, SESSION_PAYMENT, SESSION_EARNING, REFUND
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
