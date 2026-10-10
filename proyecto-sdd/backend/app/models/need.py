from datetime import datetime, timezone
from sqlmodel import SQLModel, Field
import uuid


def generate_need_id() -> str:
    return f"need-{uuid.uuid4().hex[:8]}"


class LearningNeed(SQLModel, table=True):
    __tablename__ = "learning_needs"

    id: str = Field(default_factory=generate_need_id, primary_key=True, index=True)
    user_id: str = Field(foreign_key="users.id", index=True)
    author_name: str = Field(default="")
    title: str = Field(index=True)
    description: str
    category: str = Field(index=True)
    level: str = Field(default="Inicial")
    modality: str = Field(default="Virtual")
    status: str = Field(default="ACTIVE", index=True)  # ACTIVE, PAUSED, ARCHIVED
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
