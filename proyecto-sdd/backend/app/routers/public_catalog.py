from typing import List, Optional, Dict, Any
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session
from ..database import get_session
from ..services.catalog_service import CatalogService

router = APIRouter(tags=["Catálogo Público"])


@router.get("/api/v1/public/offers", summary="Listar propuestas de enseñanza públicas")
def list_public_offers(
    category: Optional[str] = None,
    level: Optional[str] = None,
    modality: Optional[str] = None,
    session: Session = Depends(get_session),
) -> List[Dict[str, Any]]:
    service = CatalogService(session)
    return service.get_offers(category=category, level=level, modality=modality)


@router.get("/api/v1/teaching-offers/{offerId}", summary="Consultar detalle de propuesta de enseñanza")
def get_teaching_offer_detail(
    offerId: str,
    session: Session = Depends(get_session),
) -> Dict[str, Any]:
    service = CatalogService(session)
    offer = service.get_offer_detail(offerId)
    if not offer:
        raise HTTPException(
            status_code=404,
            detail={
                "code": "OFFER_NOT_FOUND",
                "message": f"No se encontró la propuesta con ID {offerId}.",
                "fields": {"offerId": offerId},
            },
        )
    return offer


@router.get("/api/v1/public/learning-needs", summary="Listar aprendizajes buscados públicos")
def list_public_learning_needs(
    category: Optional[str] = None,
    level: Optional[str] = None,
    modality: Optional[str] = None,
    session: Session = Depends(get_session),
) -> List[Dict[str, Any]]:
    service = CatalogService(session)
    return service.get_needs(category=category, level=level, modality=modality)


@router.get("/api/v1/learning-needs/{needId}", summary="Consultar detalle de aprendizaje buscado")
def get_learning_need_detail(
    needId: str,
    session: Session = Depends(get_session),
) -> Dict[str, Any]:
    service = CatalogService(session)
    need = service.get_need_detail(needId)
    if not need:
        raise HTTPException(
            status_code=404,
            detail={
                "code": "NEED_NOT_FOUND",
                "message": f"No se encontró la necesidad con ID {needId}.",
                "fields": {"needId": needId},
            },
        )
    return need


@router.get("/api/v1/public/search", summary="Buscar contenido público con filtros y paginación")
def search_public_content(
    query: Optional[str] = None,
    type: Optional[str] = None,
    categoryId: Optional[str] = None,
    level: Optional[str] = None,
    modality: Optional[str] = None,
    page: int = 1,
    pageSize: int = 20,
    session: Session = Depends(get_session),
) -> Dict[str, Any]:
    service = CatalogService(session)
    return service.search(
        query=query,
        content_type=type,
        category=categoryId,
        level=level,
        modality=modality,
        page=page,
        page_size=pageSize,
    )


@router.get("/api/v1/public/rankings", summary="Consultar rankings públicos de la comunidad")
def get_public_rankings(
    session: Session = Depends(get_session),
) -> List[Dict[str, Any]]:
    service = CatalogService(session)
    return service.get_rankings()


@router.get("/api/v1/public/users/{userId}/reputation", summary="Consultar reputación pública de un usuario")
def get_public_user_reputation(
    userId: str,
    session: Session = Depends(get_session),
) -> Dict[str, Any]:
    service = CatalogService(session)
    return service.get_reputation(userId)


@router.get("/api/v1/public/auth-requirement", summary="Verificar requisito de autenticación")
def get_auth_requirement() -> Dict[str, Any]:
    return {
        "required": False,
        "role": "GUEST",
        "message": "La exploración de propuestas, necesidades y rankings es libre según MVP V3.",
    }
