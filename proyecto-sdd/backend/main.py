import json
import os
import re
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.routing import APIRoute

from app.seed import seed_database


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Inicializa las tablas y datos semilla al arrancar
    seed_database()
    yield


app = FastAPI(title="9524 API", version="0.1.0", lifespan=lifespan)

default_cors = (
    "http://localhost:5171,http://localhost:5172,http://localhost:5173,"
    "http://127.0.0.1:5171,http://127.0.0.1:5172,http://127.0.0.1:5173"
)
allowed_origins = [
    origin.strip()
    for origin in os.getenv("CORS_ORIGINS", default_cors).split(",")
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


from app.routers.public_catalog import router as public_catalog_router
from app.routers.auth import router as auth_router
from app.routers.user_offers import router as user_offers_router
from app.routers.availability import router as availability_router
from app.routers.sessions import router as sessions_router

# Registrar routers con implementación real
app.include_router(public_catalog_router)
app.include_router(auth_router)
app.include_router(user_offers_router)
app.include_router(availability_router)
app.include_router(sessions_router)





async def backlog_stub() -> dict:
    return {}


# Snapshot de las rutas y verbos de Jira BH95.
# Solo registra como stubs las rutas que aún no tienen implementación real en app.routes.
backlog_endpoints = json.loads(
    Path(__file__).with_name("backlog_endpoints.json").read_text(encoding="utf-8")
)

registered_routes = {
    (method, route.path)
    for route in app.routes
    if isinstance(route, APIRoute)
    for method in route.methods
}

for endpoint in backlog_endpoints:
    method = endpoint["method"]
    path = endpoint["path"]
    if (method, path) in registered_routes:
        continue  # Ruta ya implementada de verdad

    parameters = [
        {"name": name, "in": "path", "required": True, "schema": {"type": "string"}}
        for name in re.findall(r"\{(\w+)\}", path)
    ] + [
        {"name": name, "in": "query", "required": False, "schema": {"type": "string"}}
        for name in endpoint["queryParams"]
    ]
    app.add_api_route(
        path,
        backlog_stub,
        methods=[method],
        status_code=200,
        name=method.lower() + "_" + re.sub(r"\W+", "_", path),
        tags=["Backlog — stubs pendientes"],
        summary=f"{method} {path}",
        description=(
            "Stub de demostración: devuelve {} con 200 OK. "
            "Pendiente de implementación en próximas fases. Tickets: "
            + ", ".join(endpoint["issues"])
        ),
        openapi_extra={"parameters": parameters},
    )

