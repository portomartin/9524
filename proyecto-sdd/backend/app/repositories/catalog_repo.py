from typing import List, Optional
from sqlmodel import Session, select, col
from ..models import TeachingOffer, LearningNeed, User, Review


class CatalogRepository:
    def __init__(self, session: Session):
        self.session = session

    def list_active_offers(
        self,
        category: Optional[str] = None,
        level: Optional[str] = None,
        modality: Optional[str] = None,
        search_query: Optional[str] = None,
    ) -> List[TeachingOffer]:
        stmt = select(TeachingOffer).where(TeachingOffer.status == "ACTIVE")
        if category:
            stmt = stmt.where(col(TeachingOffer.category).ilike(f"%{category}%"))
        if level:
            stmt = stmt.where(col(TeachingOffer.level).ilike(f"%{level}%"))
        if modality:
            stmt = stmt.where(col(TeachingOffer.modality).ilike(f"%{modality}%"))
        if search_query:
            stmt = stmt.where(
                col(TeachingOffer.title).ilike(f"%{search_query}%")
                | col(TeachingOffer.description).ilike(f"%{search_query}%")
            )
        stmt = stmt.order_by(col(TeachingOffer.created_at).desc())
        return list(self.session.exec(stmt).all())

    def get_offer_by_id(self, offer_id: str) -> Optional[TeachingOffer]:
        stmt = select(TeachingOffer).where(TeachingOffer.id == offer_id)
        return self.session.exec(stmt).first()

    def list_active_needs(
        self,
        category: Optional[str] = None,
        level: Optional[str] = None,
        modality: Optional[str] = None,
        search_query: Optional[str] = None,
    ) -> List[LearningNeed]:
        stmt = select(LearningNeed).where(LearningNeed.status == "ACTIVE")
        if category:
            stmt = stmt.where(col(LearningNeed.category).ilike(f"%{category}%"))
        if level:
            stmt = stmt.where(col(LearningNeed.level).ilike(f"%{level}%"))
        if modality:
            stmt = stmt.where(col(LearningNeed.modality).ilike(f"%{modality}%"))
        if search_query:
            stmt = stmt.where(
                col(LearningNeed.title).ilike(f"%{search_query}%")
                | col(LearningNeed.description).ilike(f"%{search_query}%")
            )
        stmt = stmt.order_by(col(LearningNeed.created_at).desc())
        return list(self.session.exec(stmt).all())

    def get_need_by_id(self, need_id: str) -> Optional[LearningNeed]:
        stmt = select(LearningNeed).where(LearningNeed.id == need_id)
        return self.session.exec(stmt).first()

    def get_user_by_id(self, user_id: str) -> Optional[User]:
        stmt = select(User).where(User.id == user_id)
        return self.session.exec(stmt).first()

    def get_user_reputation(self, user_id: str) -> dict:
        stmt = select(Review).where(Review.reviewee_id == user_id)
        reviews = list(self.session.exec(stmt).all())
        if not reviews:
            return {"userId": user_id, "score": 5.0, "reviewsCount": 0}
        score = sum(r.rating for r in reviews) / len(reviews)
        return {"userId": user_id, "score": round(score, 1), "reviewsCount": len(reviews)}

    def get_rankings(self) -> List[dict]:
        stmt = select(User).where(User.role == "USER", User.is_active == True)
        users = list(self.session.exec(stmt).all())
        rankings = []
        for u in users:
            rep = self.get_user_reputation(u.id)
            rankings.append({
                "userId": u.id,
                "name": u.name,
                "score": rep["score"],
                "reviewsCount": rep["reviewsCount"],
                "teachingTopicsCount": len(eval(u.teaching_topics)) if u.teaching_topics else 0,
            })
        rankings.sort(key=lambda x: (x["score"], x["reviewsCount"]), reverse=True)
        return rankings
