from typing import Dict, Any
from fastapi import APIRouter, Depends, Body
from sqlmodel import Session

from ..database import get_session
from ..models import User
from ..security import get_current_user
from ..services.auth_service import AuthService

router = APIRouter(tags=["Gestión de Propuestas Propias"])


@router.post("/api/v1/teaching-offers", summary="Publicar propuesta de enseñanza", status_code=201)
def create_teaching_offer(
    data: Dict[str, Any] = Body(...),
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session),
) -> Dict[str, Any]:
    service = AuthService(session)
    return service.create_offer(current_user, data)


@router.patch("/api/v1/teaching-offers/{offerId}", summary="Actualizar propuesta de enseñanza")
def update_teaching_offer(
    offerId: str,
    data: Dict[str, Any] = Body(...),
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session),
) -> Dict[str, Any]:
    service = AuthService(session)
    return service.update_offer(current_user, offerId, data)


@router.post("/api/v1/learning-needs", summary="Publicar aprendizaje buscado", status_code=201)
def create_learning_need(
    data: Dict[str, Any] = Body(...),
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session),
) -> Dict[str, Any]:
    service = AuthService(session)
    return service.create_need(current_user, data)


@router.patch("/api/v1/learning-needs/{needId}", summary="Actualizar aprendizaje buscado")
def update_learning_need(
    needId: str,
    data: Dict[str, Any] = Body(...),
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session),
) -> Dict[str, Any]:
    service = AuthService(session)
    return service.update_need(current_user, needId, data)
