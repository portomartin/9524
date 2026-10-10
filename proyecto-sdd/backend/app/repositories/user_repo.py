import json
from typing import Optional, Dict, Any, List
from sqlmodel import Session, select
from ..models import User


class UserRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_by_email(self, email: str) -> Optional[User]:
        stmt = select(User).where(User.email == email.strip().lower())
        return self.session.exec(stmt).first()

    def get_by_id(self, user_id: str) -> Optional[User]:
        stmt = select(User).where(User.id == user_id)
        return self.session.exec(stmt).first()

    def create(self, user: User) -> User:
        user.email = user.email.strip().lower()
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user

    def update_profile(self, user: User, update_data: Dict[str, Any]) -> User:
        if "name" in update_data and update_data["name"] is not None:
            user.name = update_data["name"].strip()
        if "description" in update_data and update_data["description"] is not None:
            user.description = update_data["description"].strip()
        if "general_location" in update_data and update_data["general_location"] is not None:
            user.general_location = update_data["general_location"].strip()
        if "teaching_topics" in update_data and update_data["teaching_topics"] is not None:
            val = update_data["teaching_topics"]
            user.teaching_topics = json.dumps(val) if isinstance(val, list) else str(val)
        if "learning_topics" in update_data and update_data["learning_topics"] is not None:
            val = update_data["learning_topics"]
            user.learning_topics = json.dumps(val) if isinstance(val, list) else str(val)

        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user
