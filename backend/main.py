import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.routing import APIRoute
from pydantic import BaseModel

app = FastAPI(title="9524 API", version="0.1.0")

allowed_origins = [
    origin.strip()
    for origin in os.getenv(
        "CORS_ORIGINS", "http://localhost:5173,http://127.0.0.1:5173"
    ).split(",")
    if origin.strip()
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_methods=["GET"],
    allow_headers=["Content-Type"],
)


@app.get("/")
def root() -> dict[str, object]:
    return {
        "name": app.title,
        "version": app.version,
        "docs": app.docs_url,
        "openapi": app.openapi_url,
        "endpoints": [
            {"method": method, "path": route.path}
            for route in app.routes
            if isinstance(route, APIRoute) and route.include_in_schema
            for method in sorted(route.methods)
        ],
    }


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/api/hello")
def hello() -> dict[str, str]:
    return {"message": "Hola desde el backend Python"}


class PublicOffer(BaseModel):
    id: str
    title: str
    description: str
    category: str
    level: str
    modality: str
    durationMinutes: int
    authorDisplayName: str
    publishedAt: str


@app.get(
    "/api/v1/public/offers",
    response_model=list[PublicOffer],
    tags=["Catálogo público"],
    summary="Listar propuestas públicas de enseñanza",
    description="Demo con datos de ejemplo, sin persistencia. No requiere autenticación.",
)
def list_public_offers() -> list[PublicOffer]:
    return [
        PublicOffer(
            id="offer-vue-basics",
            title="Introducción práctica a Vue 3",
            description="Aprendé a construir componentes y manejar estado reactivo.",
            category="Desarrollo web",
            level="Inicial",
            modality="Virtual",
            durationMinutes=60,
            authorDisplayName="Lucía M.",
            publishedAt="2026-10-05T14:30:00Z",
        )
    ]
