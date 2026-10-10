from typing import List, Optional, Dict, Any
from sqlmodel import Session
from ..repositories.catalog_repo import CatalogRepository
from ..models import TeachingOffer, LearningNeed


class CatalogService:
    def __init__(self, session: Session):
        self.repo = CatalogRepository(session)

    def _format_offer(self, offer: TeachingOffer) -> Dict[str, Any]:
        return {
            "id": offer.id,
            "title": offer.title,
            "description": offer.description,
            "category": offer.category,
            "level": offer.level,
            "modality": offer.modality,
            "durationMinutes": offer.duration_minutes,
            "duration_minutes": offer.duration_minutes,
            "authorDisplayName": offer.author_name or "Usuario Intercambia",
            "author_name": offer.author_name or "Usuario Intercambia",
            "userName": offer.author_name or "Usuario Intercambia",
            "userId": offer.user_id,
            "user_id": offer.user_id,
            "publishedAt": offer.created_at.isoformat() if offer.created_at else "",
            "createdAt": offer.created_at.isoformat() if offer.created_at else "",
            "status": offer.status,
        }

    def _format_need(self, need: LearningNeed) -> Dict[str, Any]:
        return {
            "id": need.id,
            "title": need.title,
            "description": need.description,
            "category": need.category,
            "level": need.level,
            "modality": need.modality,
            "authorDisplayName": need.author_name or "Usuario Intercambia",
            "author_name": need.author_name or "Usuario Intercambia",
            "userName": need.author_name or "Usuario Intercambia",
            "userId": need.user_id,
            "user_id": need.user_id,
            "publishedAt": need.created_at.isoformat() if need.created_at else "",
            "createdAt": need.created_at.isoformat() if need.created_at else "",
            "status": need.status,
        }

    def get_offers(
        self,
        category: Optional[str] = None,
        level: Optional[str] = None,
        modality: Optional[str] = None,
    ) -> List[Dict[str, Any]]:
        offers = self.repo.list_active_offers(category=category, level=level, modality=modality)
        return [self._format_offer(o) for o in offers]

    def get_offer_detail(self, offer_id: str) -> Optional[Dict[str, Any]]:
        offer = self.repo.get_offer_by_id(offer_id)
        if not offer:
            return None
        return self._format_offer(offer)

    def get_needs(
        self,
        category: Optional[str] = None,
        level: Optional[str] = None,
        modality: Optional[str] = None,
    ) -> List[Dict[str, Any]]:
        needs = self.repo.list_active_needs(category=category, level=level, modality=modality)
        return [self._format_need(n) for n in needs]

    def get_need_detail(self, need_id: str) -> Optional[Dict[str, Any]]:
        need = self.repo.get_need_by_id(need_id)
        if not need:
            return None
        return self._format_need(need)

    def search(
        self,
        query: Optional[str] = None,
        content_type: Optional[str] = None,  # "offers", "needs", or None for all
        category: Optional[str] = None,
        level: Optional[str] = None,
        modality: Optional[str] = None,
        page: int = 1,
        page_size: int = 20,
    ) -> Dict[str, Any]:
        items = []

        if content_type != "needs":
            offers = self.repo.list_active_offers(
                category=category, level=level, modality=modality, search_query=query
            )
            for o in offers:
                item = self._format_offer(o)
                item["itemType"] = "OFFER"
                items.append(item)

        if content_type != "offers":
            needs = self.repo.list_active_needs(
                category=category, level=level, modality=modality, search_query=query
            )
            for n in needs:
                item = self._format_need(n)
                item["itemType"] = "NEED"
                items.append(item)

        total_items = len(items)
        start = (page - 1) * page_size
        end = start + page_size
        paginated_items = items[start:end]
        total_pages = (total_items + page_size - 1) // page_size if total_items > 0 else 0

        return {
            "items": paginated_items,
            "pagination": {
                "page": page,
                "pageSize": page_size,
                "totalItems": total_items,
                "totalPages": total_pages,
            },
        }

    def get_rankings(self) -> List[Dict[str, Any]]:
        return self.repo.get_rankings()

    def get_reputation(self, user_id: str) -> Dict[str, Any]:
        return self.repo.get_user_reputation(user_id)
