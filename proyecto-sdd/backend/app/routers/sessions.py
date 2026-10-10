from typing import List, Dict, Any, Optional
from fastapi import APIRouter, Depends, Body, Query
from sqlmodel import Session

from ..database import get_session
from ..models import User
from ..security import get_current_user
from ..services.session_service import SessionService

router = APIRouter(tags=["Sesiones, Créditos y Calificaciones"])


@router.post("/api/v1/sessions", summary="Crear sesión solicitada", status_code=201)
def create_session(
    data: Dict[str, Any] = Body(...),
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session),
) -> Dict[str, Any]:
    service = SessionService(session)
    return service.create_session(current_user, data)


@router.get("/api/v1/sessions", summary="Listar sesiones del usuario autenticado")
def list_my_sessions(
    status: Optional[str] = Query(None, description="Filtrar por estado (SOLICITADA, ACEPTADA, FINALIZADA, CANCELADA)"),
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session),
) -> List[Dict[str, Any]]:
    service = SessionService(session)
    return service.get_user_sessions(current_user, status=status)


@router.get("/api/v1/sessions/{sessionId}", summary="Consultar detalle de una sesión")
def get_session_detail(
    sessionId: str,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session),
) -> Dict[str, Any]:
    service = SessionService(session)
    s = service.repo.get_by_id(sessionId)
    if not s:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail={"code": "SESSION_NOT_FOUND", "message": "Sesión no encontrada.", "fields": {}})
    return service.format_session(s, current_user.id)


@router.post("/api/v1/sessions/{sessionId}/confirm", summary="Aceptar sesión solicitada")
def confirm_session(
    sessionId: str,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session),
) -> Dict[str, Any]:
    service = SessionService(session)
    return service.confirm_session(current_user, sessionId)


@router.post("/api/v1/sessions/{sessionId}/cancel", summary="Cancelar sesión de intercambio")
def cancel_session(
    sessionId: str,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session),
) -> Dict[str, Any]:
    service = SessionService(session)
    return service.cancel_session(current_user, sessionId)


@router.post("/api/v1/sessions/{sessionId}/complete", summary="Finalizar sesión y transferir créditos")
def complete_session(
    sessionId: str,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session),
) -> Dict[str, Any]:
    service = SessionService(session)
    return service.complete_session(current_user, sessionId)


@router.post("/api/v1/sessions/{sessionId}/credit-transfer", summary="Ejecutar transferencia de créditos idempotente")
def transfer_session_credits(
    sessionId: str,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session),
) -> Dict[str, Any]:
    service = SessionService(session)
    return service.transfer_credits(current_user, sessionId)


@router.get("/api/v1/me/history", summary="Consultar historial de actividad")
def get_my_history(
    status: Optional[str] = Query(None, description="Filtrar por estado"),
    page: int = Query(1, ge=1),
    pageSize: int = Query(20, ge=1, le=100),
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session),
) -> Dict[str, Any]:
    service = SessionService(session)
    return service.get_history(current_user, status=status, page=page, page_size=pageSize)


@router.get("/api/v1/me/credit-movements", summary="Consultar saldo y libro de movimientos de créditos")
def get_my_credit_movements(
    page: int = Query(1, ge=1),
    pageSize: int = Query(20, ge=1, le=100),
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session),
) -> Dict[str, Any]:
    service = SessionService(session)
    return service.get_credit_movements(current_user, page=page, page_size=pageSize)


@router.post("/api/v1/sessions/{sessionId}/ratings", summary="Registrar calificación", status_code=201)
def rate_session(
    sessionId: str,
    data: Dict[str, Any] = Body(...),
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session),
) -> Dict[str, Any]:
    service = SessionService(session)
    return service.create_rating(current_user, sessionId, data)
