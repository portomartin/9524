from typing import List, Dict, Any
from fastapi import APIRouter, Depends, Body
from sqlmodel import Session

from ..database import get_session
from ..models import User
from ..security import get_current_user
from ..services.availability_service import AvailabilityService

router = APIRouter(tags=["Agenda y Disponibilidad"])


@router.get("/api/v1/me/availability", summary="Consultar franjas de disponibilidad propias")
def get_my_availability(
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session),
) -> List[Dict[str, Any]]:
    service = AvailabilityService(session)
    return service.get_my_slots(current_user)


@router.post("/api/v1/me/availability", summary="Agregar franja de disponibilidad propia", status_code=201)
def add_availability_slot(
    data: Dict[str, Any] = Body(...),
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session),
) -> Dict[str, Any]:
    service = AvailabilityService(session)
    return service.create_slot(current_user, data)


@router.patch("/api/v1/me/availability/{availabilityId}", summary="Modificar franja de disponibilidad propia")
def update_availability_slot(
    availabilityId: str,
    data: Dict[str, Any] = Body(...),
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session),
) -> Dict[str, Any]:
    service = AvailabilityService(session)
    return service.update_slot(current_user, availabilityId, data)


@router.delete("/api/v1/me/availability/{availabilityId}", summary="Eliminar franja de disponibilidad propia")
def delete_availability_slot(
    availabilityId: str,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session),
) -> Dict[str, Any]:
    service = AvailabilityService(session)
    return service.delete_slot(current_user, availabilityId)


@router.put("/api/v1/me/availability-visibility", summary="Modificar visibilidad pública de la agenda")
def update_availability_visibility(
    data: Dict[str, Any] = Body(...),
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session),
) -> Dict[str, Any]:
    service = AvailabilityService(session)
    # Soporta claves "public", "isPublic", "visible"
    is_public = data.get("public")
    if is_public is None:
        is_public = data.get("isPublic")
    if is_public is None:
        is_public = data.get("visible", True)

    return service.set_visibility(current_user, bool(is_public))


@router.get("/api/v1/public/users/{userId}/availability", summary="Consultar agenda pública de disponibilidad de un usuario")
def get_public_user_availability(
    userId: str,
    session: Session = Depends(get_session),
) -> List[Dict[str, Any]]:
    service = AvailabilityService(session)
    return service.get_public_slots(userId)
