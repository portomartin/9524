import json
from typing import Dict, Any, Optional, List
from fastapi import HTTPException, status
from sqlmodel import Session

from ..models import User, TeachingOffer, LearningNeed
from ..repositories.user_repo import UserRepository
from ..repositories.catalog_repo import CatalogRepository
from ..security import hash_password, verify_password, create_access_token


class AuthService:
    def __init__(self, session: Session):
        self.session = session
        self.user_repo = UserRepository(session)
        self.catalog_repo = CatalogRepository(session)

    def _parse_topics(self, topics_str: Optional[str]) -> List[str]:
        if not topics_str:
            return []
        try:
            val = json.loads(topics_str)
            return val if isinstance(val, list) else [str(val)]
        except Exception:
            return []

    def format_user(self, user: User) -> Dict[str, Any]:
        teaching_list = self._parse_topics(user.teaching_topics)
        learning_list = self._parse_topics(user.learning_topics)
        rep = self.catalog_repo.get_user_reputation(user.id)

        return {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "role": user.role,
            "description": user.description or "",
            "bio": user.description or "",
            "generalLocation": user.general_location or "",
            "general_location": user.general_location or "",
            "skillsToTeach": teaching_list,
            "teachingTopics": teaching_list,
            "teaching_topics": teaching_list,
            "skillsToLearn": learning_list,
            "learningTopics": learning_list,
            "learning_topics": learning_list,
            "creditBalance": user.credit_balance,
            "credit_balance": user.credit_balance,
            "reputationScore": rep["score"],
            "reviewsCount": rep["reviewsCount"],
            "agendaPublic": True,
            "status": "ACTIVO" if user.is_active else "INACTIVO",
            "isActive": user.is_active,
            "createdAt": user.created_at.isoformat() if user.created_at else "",
        }

    def register(self, data: Dict[str, Any]) -> Dict[str, Any]:
        email = data.get("email", "").strip().lower()
        if not email or "@" not in email:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail={"code": "INVALID_EMAIL", "message": "El formato del email no es válido.", "fields": {"email": email}},
            )

        password = data.get("password", "")
        if len(password) < 6:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail={"code": "WEAK_PASSWORD", "message": "La contraseña debe tener al menos 6 caracteres.", "fields": {}},
            )

        name = data.get("name", "").strip()
        if not name:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail={"code": "MISSING_NAME", "message": "El nombre es obligatorio.", "fields": {"name": name}},
            )

        existing = self.user_repo.get_by_email(email)
        if existing:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail={"code": "EMAIL_ALREADY_EXISTS", "message": "Ya existe una cuenta con este correo.", "fields": {"email": email}},
            )

        teaching = data.get("skillsToTeach") or data.get("teaching_topics") or []
        learning = data.get("skillsToLearn") or data.get("learning_topics") or []

        user = User(
            email=email,
            password_hash=hash_password(password),
            name=name,
            description=data.get("description") or data.get("bio", ""),
            role="USER",
            general_location=data.get("generalLocation") or data.get("general_location", ""),
            teaching_topics=json.dumps(teaching) if isinstance(teaching, list) else str(teaching),
            learning_topics=json.dumps(learning) if isinstance(learning, list) else str(learning),
            credit_balance=1,  # 1 crédito de bienvenida según MVP V3
            is_active=True,
        )
        created_user = self.user_repo.create(user)
        token = create_access_token({"sub": created_user.id, "email": created_user.email, "role": created_user.role})

        return {
            "access_token": token,
            "token_type": "bearer",
            "user": self.format_user(created_user),
        }

    def login(self, email: str, password: str) -> Dict[str, Any]:
        user = self.user_repo.get_by_email(email)
        if not user or not verify_password(password, user.password_hash):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail={"code": "INVALID_CREDENTIALS", "message": "Email o contraseña incorrectos.", "fields": {}},
            )

        if not user.is_active:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail={"code": "ACCOUNT_DISABLED", "message": "Tu cuenta se encuentra temporalmente desactivada.", "fields": {}},
            )

        token = create_access_token({"sub": user.id, "email": user.email, "role": user.role})
        return {
            "access_token": token,
            "token_type": "bearer",
            "user": self.format_user(user),
        }

    def update_profile(self, user: User, update_data: Dict[str, Any]) -> Dict[str, Any]:
        # Normalizar claves de frontend (bio -> description, generalLocation -> general_location)
        if "bio" in update_data and "description" not in update_data:
            update_data["description"] = update_data["bio"]
        if "generalLocation" in update_data and "general_location" not in update_data:
            update_data["general_location"] = update_data["generalLocation"]
        if "skillsToTeach" in update_data and "teaching_topics" not in update_data:
            update_data["teaching_topics"] = update_data["skillsToTeach"]
        if "skillsToLearn" in update_data and "learning_topics" not in update_data:
            update_data["learning_topics"] = update_data["skillsToLearn"]

        updated_user = self.user_repo.update_profile(user, update_data)
        return self.format_user(updated_user)

    def create_offer(self, user: User, data: Dict[str, Any]) -> Dict[str, Any]:
        title = data.get("title", "").strip()
        if not title:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail={"code": "MISSING_TITLE", "message": "El título de la propuesta es obligatorio.", "fields": {}},
            )

        offer = TeachingOffer(
            user_id=user.id,
            author_name=user.name,
            title=title,
            description=data.get("description", "").strip(),
            category=data.get("category", "General"),
            level=data.get("level", "Inicial"),
            modality=data.get("modality", "Virtual"),
            duration_minutes=int(data.get("durationMinutes") or data.get("duration_minutes") or 60),
            status="ACTIVE",
        )
        created = self.catalog_repo.create_offer(offer)
        return {
            "id": created.id,
            "title": created.title,
            "description": created.description,
            "category": created.category,
            "level": created.level,
            "modality": created.modality,
            "durationMinutes": created.duration_minutes,
            "authorDisplayName": created.author_name,
            "userId": created.user_id,
            "status": created.status,
            "createdAt": created.created_at.isoformat() if created.created_at else "",
        }

    def update_offer(self, user: User, offer_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        offer = self.catalog_repo.get_offer_by_id(offer_id)
        if not offer:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={"code": "OFFER_NOT_FOUND", "message": "Propuesta no encontrada.", "fields": {"offerId": offer_id}},
            )

        if offer.user_id != user.id and user.role != "ADMIN":
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail={"code": "FORBIDDEN", "message": "Solo podés modificar tus propias propuestas.", "fields": {}},
            )

        updated = self.catalog_repo.update_offer(offer, data)
        return {
            "id": updated.id,
            "title": updated.title,
            "description": updated.description,
            "category": updated.category,
            "level": updated.level,
            "modality": updated.modality,
            "durationMinutes": updated.duration_minutes,
            "authorDisplayName": updated.author_name,
            "userId": updated.user_id,
            "status": updated.status,
            "updatedAt": updated.created_at.isoformat() if updated.created_at else "",
        }

    def create_need(self, user: User, data: Dict[str, Any]) -> Dict[str, Any]:
        title = data.get("title", "").strip()
        if not title:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail={"code": "MISSING_TITLE", "message": "El título del aprendizaje buscado es obligatorio.", "fields": {}},
            )

        need = LearningNeed(
            user_id=user.id,
            author_name=user.name,
            title=title,
            description=data.get("description", "").strip() or data.get("goal", "").strip(),
            category=data.get("category", "General"),
            level=data.get("level", "Inicial"),
            modality=data.get("modality", "Virtual"),
            status="ACTIVE",
        )
        created = self.catalog_repo.create_need(need)
        return {
            "id": created.id,
            "title": created.title,
            "description": created.description,
            "category": created.category,
            "level": created.level,
            "modality": created.modality,
            "authorDisplayName": created.author_name,
            "userId": created.user_id,
            "status": created.status,
            "createdAt": created.created_at.isoformat() if created.created_at else "",
        }

    def update_need(self, user: User, need_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        need = self.catalog_repo.get_need_by_id(need_id)
        if not need:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={"code": "NEED_NOT_FOUND", "message": "Necesidad de aprendizaje no encontrada.", "fields": {"needId": need_id}},
            )

        if need.user_id != user.id and user.role != "ADMIN":
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail={"code": "FORBIDDEN", "message": "Solo podés modificar tus propias necesidades.", "fields": {}},
            )

        updated = self.catalog_repo.update_need(need, data)
        return {
            "id": updated.id,
            "title": updated.title,
            "description": updated.description,
            "category": updated.category,
            "level": updated.level,
            "modality": updated.modality,
            "authorDisplayName": updated.author_name,
            "userId": updated.user_id,
            "status": updated.status,
        }
