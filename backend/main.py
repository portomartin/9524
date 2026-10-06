import json
import os
import re
from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.routing import APIRoute

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
    allow_methods=["GET", "POST", "PUT", "PATCH", "DELETE"],
    allow_headers=["Content-Type", "Authorization", "Idempotency-Key"],
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


async def backlog_stub() -> dict:
    return {}


async def list_public_offers() -> list[dict]:
    return [{
        "id": "offer-vue-basics",
        "title": "Introducción práctica a Vue 3",
        "description": "Aprendé a construir componentes, manejar estado reactivo y organizar una aplicación pequeña con Composition API.",
        "category": "Desarrollo web",
        "level": "Inicial",
        "modality": "Virtual",
        "durationMinutes": 60,
        "authorDisplayName": "Lucía M.",
        "publishedAt": "2026-10-05T14:30:00Z",
    }]


# Snapshot de las rutas y verbos de Jira BH95. No implementa reglas del producto.
backlog_endpoints = json.loads(
    Path(__file__).with_name("backlog_endpoints.json").read_text(encoding="utf-8")
)
for endpoint in backlog_endpoints:
    is_public_offers = endpoint["method"] == "GET" and endpoint["path"] == "/api/v1/public/offers"
    parameters = [
        {"name": name, "in": "path", "required": True, "schema": {"type": "string"}}
        for name in re.findall(r"\{(\w+)\}", endpoint["path"])
    ] + [
        {"name": name, "in": "query", "required": False, "schema": {"type": "string"}}
        for name in endpoint["queryParams"]
    ]
    app.add_api_route(
        endpoint["path"],
        list_public_offers if is_public_offers else backlog_stub,
        methods=[endpoint["method"]],
        status_code=200,
        name=endpoint["method"].lower() + "_" + re.sub(r"\W+", "_", endpoint["path"]),
        tags=["Backlog — stubs"],
        summary=f"{endpoint['method']} {endpoint['path']}",
        description=(
            ("Listado de propuestas con datos de ejemplo. " if is_public_offers else "Stub de demostración: devuelve {} con 200 OK. ")
            +
            "No valida datos, autentica ni persiste cambios. Tickets: "
            + ", ".join(endpoint["issues"])
        ),
        openapi_extra={"parameters": parameters},
    )
