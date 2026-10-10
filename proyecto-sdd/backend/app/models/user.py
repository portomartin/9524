from datetime import datetime, timezone
from typing import Optional
from sqlmodel import SQLModel, Field
import uuid


def generate_user_id() -> str:
    return f"usr-{uuid.uuid4().hex[:8]}"


class User(SQLModel, table=True):
    __tablename__ = "users"

    id: str = Field(default_factory=generate_user_id, primary_key=True, index=True)
    email: str = Field(unique=True, index=True)
    password_hash: str
    name: str
    description: Optional[str] = Field(default="")
    role: str = Field(default="USER")  # "USER" o "ADMIN"
    general_location: Optional[str] = Field(default="")
    teaching_topics: str = Field(default="[]")  # JSON string con lista de temas
    learning_topics: str = Field(default="[]")  # JSON string con lista de temas
    credit_balance: int = Field(default=1)  # 1 crédito de cortesía inicial
    is_active: bool = Field(default=True)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
