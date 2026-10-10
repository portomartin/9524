from datetime import datetime, timezone
from typing import Optional
from sqlmodel import SQLModel, Field
import uuid


def generate_review_id() -> str:
    return f"rev-{uuid.uuid4().hex[:8]}"


class Review(SQLModel, table=True):
    __tablename__ = "reviews"

    id: str = Field(default_factory=generate_review_id, primary_key=True, index=True)
    session_id: str = Field(foreign_key="exchange_sessions.id", index=True)
    reviewer_id: str = Field(foreign_key="users.id", index=True)
    reviewee_id: str = Field(foreign_key="users.id", index=True)
    rating: int = Field(ge=1, le=5)  # 1 a 5 estrellas
    comment: Optional[str] = Field(default="")
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
