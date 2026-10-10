from typing import Dict, Any
from fastapi import APIRouter, Depends, Body
from sqlmodel import Session

from ..database import get_session
from ..models import User
from ..security import get_current_user
from ..services.auth_service import AuthService

router = APIRouter(tags=["Cuentas y Autenticación"])


@router.post("/api/v1/users", summary="Registrar nuevo usuario", status_code=201)
def register_user(
    data: Dict[str, Any] = Body(...),
    session: Session = Depends(get_session),
) -> Dict[str, Any]:
    service = AuthService(session)
    return service.register(data)


@router.post("/api/v1/auth/login", summary="Iniciar sesión")
def login(
    data: Dict[str, Any] = Body(...),
    session: Session = Depends(get_session),
) -> Dict[str, Any]:
    service = AuthService(session)
    email = data.get("email", "")
    password = data.get("password", "")
    return service.login(email, password)


@router.post("/api/v1/auth/logout", summary="Cerrar sesión")
def logout() -> Dict[str, Any]:
    return {"message": "Sesión cerrada correctamente."}


@router.get("/api/v1/me/profile", summary="Consultar perfil del usuario autenticado")
def get_my_profile(
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session),
) -> Dict[str, Any]:
    service = AuthService(session)
    return service.format_user(current_user)


@router.patch("/api/v1/me/profile", summary="Actualizar perfil del usuario autenticado")
def update_my_profile(
    data: Dict[str, Any] = Body(...),
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session),
) -> Dict[str, Any]:
    service = AuthService(session)
    return service.update_profile(current_user, data)
