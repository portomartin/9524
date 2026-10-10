from datetime import datetime, timezone
from typing import Optional
from sqlmodel import SQLModel, Field
import uuid


def generate_offer_id() -> str:
    return f"offer-{uuid.uuid4().hex[:8]}"


class TeachingOffer(SQLModel, table=True):
    __tablename__ = "teaching_offers"

    id: str = Field(default_factory=generate_offer_id, primary_key=True, index=True)
    user_id: str = Field(foreign_key="users.id", index=True)
    author_name: str = Field(default="")
    title: str = Field(index=True)
    description: str
    category: str = Field(index=True)
    level: str = Field(default="Inicial")
    modality: str = Field(default="Virtual")
    duration_minutes: int = Field(default=60)
    status: str = Field(default="ACTIVE", index=True)  # ACTIVE, PAUSED, ARCHIVED
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
