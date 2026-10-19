"""
Backend Mock Rápido — Proyecto WBS Clásico
Endpoints stubs y mocks correspondientes a los tickets Jira del proyecto WBSO (1.3 a 1.12),
incluyendo la especificación de 'Publicar una propuesta' (POST /me/teaching-offers y catálogos).
"""

from datetime import datetime, timezone
import json
from typing import Any, Dict, List, Optional
from fastapi import FastAPI, File, Form, HTTPException, Request, Response, UploadFile, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, ConfigDict, Field

app = FastAPI(
    title="API Mock — Proyecto WBS Clásico (WBSO)",
    description=(
        "Servidor mock ultra-rápido para pruebas del frontend independiente. "
        "Basado en las Historias de Usuario HU 1.3 a 1.12 del tablero Jira WBSO, "
        "con soporte exacto para la especificación 'Publicar una propuesta' (POST /me/teaching-offers)."
    ),
    version="1.1.0",
)

# CORS dinámico con regex para soportar credenciales y cualquier origen de frontend sin conflicto con '*'
app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=r".*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Modelo base permisivo: acepta cualquier campo adicional sin lanzar error 422
class PermissiveModel(BaseModel):
    model_config = ConfigDict(extra="allow")


# --- Modelos de Request Dummy ---
class RegisterRequest(PermissiveModel):
    email: Optional[str] = "demo@intercambio.test"
    password: Optional[str] = "password123"
    name: Optional[str] = "Usuario Demo"


class LoginRequest(PermissiveModel):
    email: Optional[str] = "demo@intercambio.test"
    password: Optional[str] = "password123"


class PasswordRecoverRequest(PermissiveModel):
    email: Optional[str] = "demo@intercambio.test"


class ProfileUpdateRequest(PermissiveModel):
    name: Optional[str] = "Martín WBS"
    bio: Optional[str] = "Compartiendo conocimientos en la plataforma."
    teaching_topics: Optional[List[str]] = Field(default_factory=lambda: ["Python", "Gestión de proyectos"])
    learning_topics: Optional[List[str]] = Field(default_factory=lambda: ["Inglés", "Diseño UX"])
    level: Optional[str] = "Intermedio"
    modality: Optional[str] = "Virtual"
    location: Optional[str] = "Buenos Aires"


class AvailabilitySlotRequest(PermissiveModel):
    day_of_week: Optional[str] = "Lunes"
    start_time: Optional[str] = "18:00"
    end_time: Optional[str] = "20:00"


class PublicationCreateRequest(PermissiveModel):
    title: Optional[str] = "Clases de Álgebra"
    description: Optional[str] = "Refuerzo de álgebra para secundaria..."
    interest_id: Optional[int] = 1
    subinterest_id: Optional[int] = 2
    level_taught: Optional[str] = "beginner"
    language: Optional[str] = "es"
    max_students: Optional[int] = 1
    modality: Optional[str] = "in_person"
    location: Optional[Dict[str, str]] = Field(
        default_factory=lambda: {"province": "Buenos Aires", "city": "La Plata", "zone": "Centro"}
    )
    credits_cost: Optional[int] = 2
    time_zone: Optional[str] = "America/Argentina/Buenos_Aires"
    availability: Optional[List[Dict[str, str]]] = Field(
        default_factory=lambda: [{"day": "mon", "start_time": "18:00", "end_time": "19:00"}]
    )
    duration_minutes: Optional[int] = 60


class SessionRequestCreate(PermissiveModel):
    publication_id: Optional[str] = "pub-101"
    target_user_id: Optional[str] = "usr-lucia"
    proposed_date: Optional[str] = "2026-11-01"
    start_time: Optional[str] = "18:00"
    modality: Optional[str] = "Virtual"
    message: Optional[str] = "Hola, me gustaría coordinar una sesión."


class StatusUpdateRequest(PermissiveModel):
    status: Optional[str] = "ACEPTADA"


class CreditTransferRequest(PermissiveModel):
    session_id: Optional[str] = "ses-201"
    amount: Optional[int] = 1
    recipient_id: Optional[str] = "usr-lucia"


class RatingCreateRequest(PermissiveModel):
    session_id: Optional[str] = "ses-201"
    rating: Optional[int] = 5
    comment: Optional[str] = "Excelente sesión, muy clara la explicación y puntual."


class ReportCreateRequest(PermissiveModel):
    target_type: Optional[str] = "PUBLICATION"
    target_id: Optional[str] = "pub-101"
    reason: Optional[str] = "Contenido fuera de los términos de la plataforma."
    details: Optional[str] = "Detalles opcionales de la denuncia."


# --- Endpoints Generales ---
@app.get("/", tags=["General"])
def root():
    return {
        "status": "ok",
        "service": "WBS Mock Backend",
        "version": "1.1.0",
        "swagger_docs": "/docs",
        "health": "/health",
    }


@app.get("/health", tags=["General"])
def health():
    return {"status": "ok", "mode": "mock-all-200"}


# ============================================================================
# CATÁLOGOS ESPECÍFICOS DEL PDF (HU [1.4] WBSO-44, 46, 47, 49)
# ============================================================================

INTERESTS_DATA = [
    {"interest_id": 1, "interest_name": "Matemática"},
    {"interest_id": 2, "interest_name": "Idiomas"},
    {"interest_id": 3, "interest_name": "Tecnología y Programación"},
    {"interest_id": 4, "interest_name": "Música y Arte"},
    {"interest_id": 5, "interest_name": "Ciencias y Naturaleza"},
]

SUBINTERESTS_MAP = {
    1: [
        {"subinterest_id": 1, "subinterest_name": "Álgebra"},
        {"subinterest_id": 2, "subinterest_name": "Cálculo"},
        {"subinterest_id": 3, "subinterest_name": "Geometría"},
    ],
    2: [
        {"subinterest_id": 4, "subinterest_name": "Inglés"},
        {"subinterest_id": 5, "subinterest_name": "Francés"},
        {"subinterest_id": 6, "subinterest_name": "Alemán"},
        {"subinterest_id": 7, "subinterest_name": "Portugués"},
    ],
    3: [
        {"subinterest_id": 8, "subinterest_name": "Python"},
        {"subinterest_id": 9, "subinterest_name": "Desarrollo Web Frontend"},
        {"subinterest_id": 10, "subinterest_name": "FastAPI y Backend"},
        {"subinterest_id": 11, "subinterest_name": "Bases de Datos SQL"},
    ],
    4: [
        {"subinterest_id": 12, "subinterest_name": "Guitarra clásica y eléctrica"},
        {"subinterest_id": 13, "subinterest_name": "Dibujo e ilustración"},
        {"subinterest_id": 14, "subinterest_name": "Fotografía digital"},
    ],
    5: [
        {"subinterest_id": 15, "subinterest_name": "Huerta orgánica y botánica"},
        {"subinterest_id": 16, "subinterest_name": "Física experimental"},
    ],
}

LEVELS_DATA = [
    {"value": "beginner", "label": "Principiante"},
    {"value": "intermediate", "label": "Intermedio"},
    {"value": "advanced", "label": "Avanzado"},
]

LANGUAGES_DATA = [
    {"value": "es", "label": "Español"},
    {"value": "en", "label": "Inglés"},
    {"value": "pt", "label": "Portugués"},
    {"value": "fr", "label": "Francés"},
    {"value": "de", "label": "Alemán"},
]

MODALITIES_DATA = [
    {"value": "online", "label": "Virtual"},
    {"value": "in_person", "label": "Presencial"},
]

DURATIONS_DATA = [
    {"value": 30, "label": "30 minutos"},
    {"value": 45, "label": "45 minutos"},
    {"value": 60, "label": "1 hora"},
    {"value": 90, "label": "1 hora y media"},
    {"value": 120, "label": "2 horas"},
]


@app.get("/interests", tags=["Catálogos del PDF (WBSO-44)"], summary="[1.4.2] Catálogo de intereses (WBSO-44)")
@app.get("/api/v1/interests", tags=["Catálogos del PDF (WBSO-44)"], include_in_schema=False)
def get_interests():
    return INTERESTS_DATA


@app.get("/interests/{interest_id}/subinterests", tags=["Catálogos del PDF (WBSO-44)"], summary="[1.4.2] Subintereses por interés (WBSO-44)")
@app.get("/api/v1/interests/{interest_id}/subinterests", tags=["Catálogos del PDF (WBSO-44)"], include_in_schema=False)
def get_subinterests(interest_id: int):
    if interest_id not in SUBINTERESTS_MAP:
        # Devuelve vacío si no tiene subintereses definidos
        return []
    return SUBINTERESTS_MAP[interest_id]


@app.get("/levels", tags=["Catálogos del PDF (WBSO-46)"], summary="[1.4.4] Catálogo de niveles (WBSO-46)")
@app.get("/api/v1/levels", tags=["Catálogos del PDF (WBSO-46)"], include_in_schema=False)
def get_levels():
    return LEVELS_DATA


@app.get("/languages", tags=["Catálogos del PDF (WBSO-45)"], summary="[1.4.3] Catálogo de idiomas (WBSO-45)")
@app.get("/api/v1/languages", tags=["Catálogos del PDF (WBSO-45)"], include_in_schema=False)
def get_languages():
    return LANGUAGES_DATA


@app.get("/modalities", tags=["Catálogos del PDF (WBSO-47)"], summary="[1.4.5] Catálogo de modalidades (WBSO-47)")
@app.get("/api/v1/modalities", tags=["Catálogos del PDF (WBSO-47)"], include_in_schema=False)
def get_modalities():
    return MODALITIES_DATA


@app.get("/durations", tags=["Catálogos del PDF (WBSO-49)"], summary="[1.4.6] Catálogo de duraciones en minutos numéricos (WBSO-49)")
@app.get("/api/v1/durations", tags=["Catálogos del PDF (WBSO-49)"], include_in_schema=False)
def get_durations():
    return DURATIONS_DATA


# ============================================================================
# CREACIÓN DE PROPUESTAS SEGÚN PDF (POST /me/teaching-offers - 201 Created)
# ============================================================================

offer_counter = 1


@app.post(
    "/me/teaching-offers",
    status_code=status.HTTP_201_CREATED,
    tags=["HU [1.4] Sistema de publicaciones"],
    summary="[1.4.1 a 1.4.9] Publicar propuesta docente - Contrato PDF (WBSO-43 a 50)",
)
@app.post(
    "/api/v1/me/teaching-offers",
    status_code=status.HTTP_201_CREATED,
    tags=["HU [1.4] Sistema de publicaciones"],
    include_in_schema=False,
)
async def create_teaching_offer(
    request: Request,
    data: Optional[str] = Form(None),
    image: Optional[UploadFile] = File(None),
):
    global offer_counter
    offer_counter += 1

    parsed_data: Dict[str, Any] = {}

    content_type = request.headers.get("content-type", "")

    # 1. Si viene como multipart/form-data con parte 'data' (lo especificado en el PDF)
    if data:
        try:
            parsed_data = json.loads(data)
        except Exception:
            raise HTTPException(
                status_code=422,
                detail={
                    "message": "The given data was invalid.",
                    "errors": {"data": ["La parte 'data' debe ser un string JSON válido."]},
                },
            )
    # 2. Si el frontend envía JSON directo por Content-Type: application/json
    elif "application/json" in content_type:
        try:
            parsed_data = await request.json()
        except Exception:
            parsed_data = {}
    # 3. Fallback por si envía campos form directos
    else:
        try:
            form = await request.form()
            for key, val in form.items():
                if key != "image":
                    try:
                        parsed_data[key] = json.loads(val)
                    except Exception:
                        parsed_data[key] = val
        except Exception:
            parsed_data = {}

    # Validaciones mínimas según CA5 del PDF (solo para proteger si manda campos vacíos críticos)
    title = parsed_data.get("title", "Clases de Álgebra")
    description = parsed_data.get("description", "Refuerzo de álgebra para secundaria...")
    interest_id = parsed_data.get("interest_id", 1)

    now_iso = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    image_url = "https://cdn.lerna.app/ofertas/1/portada.png" if image else None

    # Respuesta 201 exacta requerida por la sección 3.4 del PDF
    return {
        "id": offer_counter,
        "title": title,
        "description": description,
        "image_url": image_url,
        "interest_id": interest_id,
        "subinterest_id": parsed_data.get("subinterest_id", 2),
        "level_taught": parsed_data.get("level_taught", "beginner"),
        "language": parsed_data.get("language", "es"),
        "max_students": parsed_data.get("max_students", 1),
        "modality": parsed_data.get("modality", "in_person"),
        "location": parsed_data.get(
            "location",
            {"province": "Buenos Aires", "city": "La Plata", "zone": "Centro"}
            if parsed_data.get("modality") == "in_person"
            else None,
        ),
        "credits_cost": int(parsed_data.get("credits_cost", 2)),
        "time_zone": parsed_data.get("time_zone", "America/Argentina/Buenos_Aires"),
        "availability": parsed_data.get(
            "availability",
            [{"day": "mon", "start_time": "18:00", "end_time": "19:00"}],
        ),
        "duration_minutes": int(parsed_data.get("duration_minutes", 60)),
        "status": "active",
        "moderation_status": "active",
        "moderation_reason": None,
        "created_at": now_iso,
        "updated_at": now_iso,
    }


# ============================================================================
# HU [1.3] Sistema de usuarios (WBSO-7: WBSO-33 a WBSO-42)
# ============================================================================

@app.post("/api/v1/auth/register", tags=["HU [1.3] Sistema de usuarios"], summary="[1.3.1] Módulo de registro (WBSO-33)")
def register_user(payload: Optional[RegisterRequest] = None):
    return {
        "status": "success",
        "message": "Usuario registrado exitosamente",
        "token": "jwt-dummy-token-wbso-33",
        "user": {
            "id": "usr-wbso-demo",
            "email": payload.email if payload else "demo@intercambio.test",
            "name": payload.name if payload else "Usuario Demo",
            "role": "USER",
            "credits": 5,
        },
    }


@app.post("/api/v1/auth/login", tags=["HU [1.3] Sistema de usuarios"], summary="[1.3.2] Módulo de inicio y cierre de sesión (WBSO-34)")
def login_user(payload: Optional[LoginRequest] = None):
    return {
        "status": "success",
        "message": "Sesión iniciada correctamente",
        "token": "jwt-dummy-token-wbso-34",
        "user": {
            "id": "usr-wbso-demo",
            "email": payload.email if payload else "demo@intercambio.test",
            "name": "Martín Demo",
            "role": "USER",
            "credits": 5,
        },
    }


@app.post("/api/v1/auth/logout", tags=["HU [1.3] Sistema de usuarios"], summary="[1.3.2] Cierre de sesión (WBSO-34)")
def logout_user():
    return {"status": "success", "message": "Sesión cerrada correctamente"}


@app.post("/api/v1/auth/recover-password", tags=["HU [1.3] Sistema de usuarios"], summary="[1.3.3] Recuperación de contraseña (WBSO-35)")
def recover_password(payload: Optional[PasswordRecoverRequest] = None):
    return {
        "status": "success",
        "message": "Se han enviado instrucciones de recuperación a la casilla de correo provista.",
    }


@app.get("/api/v1/users/me", tags=["HU [1.3] Sistema de usuarios"], summary="[1.3.4 a 1.3.8] Perfil de usuario (WBSO-36, 38, 39, 41, 42)")
@app.get("/users/me", tags=["HU [1.3] Sistema de usuarios"], include_in_schema=False)
def get_user_profile():
    return {
        "id": "usr-wbso-demo",
        "name": "Martín Demo",
        "email": "demo@intercambio.test",
        "bio": "Entusiasta de la gestión de proyectos ágiles y el desarrollo de software.",
        "location": "Buenos Aires, Argentina",
        "teaching_topics": ["Gestión de proyectos", "Scrum y WBS", "Python inicial"],
        "learning_topics": ["Inglés conversacional", "Diseño UX/UI", "Fotografía digital"],
        "level": "Intermedio",
        "modality": "Virtual",
        "credit_balance": 5,
        "rating_average": 4.9,
        "completed_sessions_count": 12,
    }


@app.put("/api/v1/users/me", tags=["HU [1.3] Sistema de usuarios"], summary="[1.3.4] Actualización de perfil (WBSO-36)")
@app.put("/users/me", tags=["HU [1.3] Sistema de usuarios"], include_in_schema=False)
def update_user_profile(payload: Optional[ProfileUpdateRequest] = None):
    data = payload.model_dump() if payload else {}
    return {
        "status": "success",
        "message": "Perfil actualizado correctamente",
        "profile": {
            "id": "usr-wbso-demo",
            "name": data.get("name", "Martín Demo"),
            "bio": data.get("bio", "Bio actualizada"),
            "teaching_topics": data.get("teaching_topics", ["Python"]),
            "learning_topics": data.get("learning_topics", ["Inglés"]),
            "level": data.get("level", "Intermedio"),
            "modality": data.get("modality", "Virtual"),
            "location": data.get("location", "Buenos Aires"),
        },
    }


@app.get("/api/v1/users/me/availability", tags=["HU [1.3] Sistema de usuarios"], summary="[1.3.9] Configuración de disponibilidad horaria (WBSO-37)")
def get_user_availability():
    return {
        "user_id": "usr-wbso-demo",
        "slots": [
            {"id": "slot-1", "day": "mon", "day_of_week": "Lunes", "start_time": "18:00", "end_time": "20:00", "status": "AVAILABLE"},
            {"id": "slot-2", "day": "wed", "day_of_week": "Miércoles", "start_time": "19:00", "end_time": "21:00", "status": "AVAILABLE"},
            {"id": "slot-3", "day": "sat", "day_of_week": "Sábados", "start_time": "10:00", "end_time": "13:00", "status": "AVAILABLE"},
        ],
    }


@app.post("/api/v1/users/me/availability", tags=["HU [1.3] Sistema de usuarios"], summary="[1.3.9] Agregar disponibilidad horaria (WBSO-37)")
def add_user_availability(payload: Optional[AvailabilitySlotRequest] = None):
    data = payload.model_dump() if payload else {}
    return {
        "status": "success",
        "message": "Franja horaria agregada",
        "slot": {
            "id": "slot-new-99",
            "day": "mon",
            "day_of_week": data.get("day_of_week", "Lunes"),
            "start_time": data.get("start_time", "18:00"),
            "end_time": data.get("end_time", "20:00"),
            "status": "AVAILABLE",
        },
    }


@app.get("/api/v1/users/me/credits", tags=["HU [1.3] Sistema de usuarios"], summary="[1.3.10] Visualización del saldo de créditos (WBSO-40)")
def get_user_credits_summary():
    return {
        "user_id": "usr-wbso-demo",
        "balance": 5,
        "available_credits": 4,
        "reserved_credits": 1,
        "currency_restriction": "Los créditos no son convertibles a dinero de curso legal.",
    }


# ============================================================================
# HU [1.4] Sistema de publicaciones (WBSO-8: WBSO-43 a WBSO-52)
# ============================================================================

@app.get("/api/v1/categories", tags=["HU [1.4] Sistema de publicaciones"], summary="[1.4.2] Catálogo de categorías (WBSO-44)")
def list_categories():
    return {
        "categories": [
            {"id": "cat-tech", "name": "Tecnología y Programación", "description": "Desarrollo web, lenguajes, cloud y datos"},
            {"id": "cat-lang", "name": "Idiomas", "description": "Inglés, Francés, Alemán, Portugués y conversación"},
            {"id": "cat-mgmt", "name": "Gestión y Negocios", "description": "Agilidad, liderazgo, finanzas y proyectos"},
            {"id": "cat-art", "name": "Arte y Diseño", "description": "Diseño gráfico, UI/UX, fotografía e ilustración"},
            {"id": "cat-well", "name": "Bienestar y Estilo de Vida", "description": "Yoga, cocina saludable, meditación y huertas"},
        ]
    }


@app.get("/api/v1/publications", tags=["HU [1.4] Sistema de publicaciones"], summary="[1.4.1 a 1.4.9] Listar publicaciones (WBSO-43, 52)")
@app.get("/publications", tags=["HU [1.4] Sistema de publicaciones"], include_in_schema=False)
def list_publications(category: Optional[str] = None, modality: Optional[str] = None):
    return {
        "total": 3,
        "items": [
            {
                "id": "pub-101",
                "title": "Conversación en inglés orientada a entrevistas de trabajo",
                "description": "Simulación práctica de entrevistas técnicas y preguntas frecuentes en inglés.",
                "author": {"id": "usr-tomas", "name": "Tomás R.", "reputation": 4.8},
                "category": "Idiomas",
                "level": "Intermedio",
                "modality": "Virtual",
                "duration_minutes": 45,
                "credit_value": 1,
                "status": "PUBLISHED",
                "created_at": "2026-10-15T10:00:00Z",
            },
            {
                "id": "pub-102",
                "title": "Introducción práctica a FastAPI y arquitectura limpia",
                "description": "Aprende a estructurar un backend en capas con FastAPI, Pydantic y SQLModel.",
                "author": {"id": "usr-lucia", "name": "Lucía M.", "reputation": 4.9},
                "category": "Tecnología y Programación",
                "level": "Inicial",
                "modality": "Virtual",
                "duration_minutes": 60,
                "credit_value": 1,
                "status": "PUBLISHED",
                "created_at": "2026-10-16T14:30:00Z",
            },
            {
                "id": "pub-103",
                "title": "Tu primera huerta urbana en macetas",
                "description": "Tips básicos de riego, tipos de sustrato y siembra de aromáticas en departamentos.",
                "author": {"id": "usr-elena", "name": "Elena P.", "reputation": 4.7},
                "category": "Bienestar y Estilo de Vida",
                "level": "Inicial",
                "modality": "Presencial",
                "duration_minutes": 90,
                "credit_value": 2,
                "status": "PUBLISHED",
                "created_at": "2026-10-17T09:15:00Z",
            },
        ],
    }


@app.post("/api/v1/publications", tags=["HU [1.4] Sistema de publicaciones"], summary="[1.4.1 a 1.4.7] Crear publicación (WBSO-43)")
def create_publication(payload: Optional[PublicationCreateRequest] = None):
    data = payload.model_dump() if payload else {}
    return {
        "status": "success",
        "message": "Publicación creada exitosamente y validada contra políticas",
        "publication": {
            "id": "pub-new-202",
            "title": data.get("title", "Nueva publicación"),
            "description": data.get("description", "Descripción de la oferta de enseñanza"),
            "category_id": data.get("category_id", "cat-tech"),
            "level": data.get("level", "Inicial"),
            "modality": data.get("modality", "Virtual"),
            "duration_minutes": data.get("duration_minutes", 60),
            "credit_value": data.get("credit_value", 1),
            "status": "PUBLISHED",
            "created_at": "2026-10-18T23:00:00Z",
        },
    }


@app.get("/api/v1/publications/{publication_id}", tags=["HU [1.4] Sistema de publicaciones"], summary="[1.4.3] Detalle de publicación (WBSO-45)")
@app.get("/publications/{publication_id}", tags=["HU [1.4] Sistema de publicaciones"], include_in_schema=False)
def get_publication_detail(publication_id: str):
    return {
        "id": publication_id,
        "title": "Conversación en inglés orientada a entrevistas de trabajo",
        "description": "Simulación práctica de entrevistas técnicas y preguntas frecuentes en inglés.",
        "author": {"id": "usr-tomas", "name": "Tomás R.", "reputation": 4.8, "location": "Buenos Aires"},
        "category": "Idiomas",
        "level": "Intermedio",
        "modality": "Virtual",
        "duration_minutes": 45,
        "credit_value": 1,
        "status": "PUBLISHED",
        "created_at": "2026-10-15T10:00:00Z",
    }


@app.put("/api/v1/publications/{publication_id}", tags=["HU [1.4] Sistema de publicaciones"], summary="[1.4.8] Modificar publicación (WBSO-52)")
def update_publication(publication_id: str, payload: Optional[PublicationCreateRequest] = None):
    data = payload.model_dump() if payload else {}
    return {
        "status": "success",
        "message": "Publicación actualizada correctamente",
        "publication_id": publication_id,
        "updated_fields": data,
    }


@app.delete("/api/v1/publications/{publication_id}", tags=["HU [1.4] Sistema de publicaciones"], summary="[1.4.8] Eliminar publicación (WBSO-52)")
def delete_publication(publication_id: str):
    return {"status": "success", "message": f"Publicación {publication_id} eliminada correctamente"}


# ============================================================================
# HU [1.5] Sistema de búsqueda y compatibilidad (WBSO-9: WBSO-51 a WBSO-58)
# ============================================================================

@app.get("/api/v1/search", tags=["HU [1.5] Sistema de búsqueda y compatibilidad"], summary="[1.5.1 a 1.5.3] Buscador y filtros de aprendizajes (WBSO-51, 53, 54)")
@app.get("/search", tags=["HU [1.5] Sistema de búsqueda y compatibilidad"], include_in_schema=False)
def search_publications(q: Optional[str] = "", category: Optional[str] = None, level: Optional[str] = None, modality: Optional[str] = None):
    return {
        "query": q,
        "filters_applied": {"category": category, "level": level, "modality": modality},
        "total_results": 2,
        "results": [
            {
                "id": "pub-101",
                "title": "Conversación en inglés orientada a entrevistas de trabajo",
                "category": "Idiomas",
                "modality": "Virtual",
                "level": "Intermedio",
                "author": "Tomás R.",
                "credit_value": 1,
            },
            {
                "id": "pub-102",
                "title": "Introducción práctica a FastAPI y arquitectura limpia",
                "category": "Tecnología",
                "modality": "Virtual",
                "level": "Inicial",
                "author": "Lucía M.",
                "credit_value": 1,
            },
        ],
    }


@app.get("/api/v1/compatibilities", tags=["HU [1.5] Sistema de búsqueda y compatibilidad"], summary="[1.5.4 a 1.5.7] Motor de compatibilidad y perfiles compatibles (WBSO-55 a 58)")
def get_compatibilities():
    return {
        "user_id": "usr-wbso-demo",
        "compatibilities": [
            {
                "candidate_user": {"id": "usr-tomas", "name": "Tomás R.", "reputation": 4.8},
                "compatibility_score": 95,
                "reasons": ["Coincidencia horaria en día Miércoles 19:00", "Buscas aprender lo que él enseña (Inglés)"],
                "is_reciprocal": True,
                "reciprocal_match_details": "Tomás desea aprender Gestión de Proyectos, que tú enseñas.",
                "publication": {"id": "pub-101", "title": "Conversación en inglés orientada a entrevistas"},
            },
            {
                "candidate_user": {"id": "usr-lucia", "name": "Lucía M.", "reputation": 4.9},
                "compatibility_score": 88,
                "reasons": ["Coincidencia en modalidad Virtual", "Disponibilidad compatible los Sábados"],
                "is_reciprocal": False,
                "publication": {"id": "pub-102", "title": "Introducción práctica a FastAPI"},
            },
        ],
    }


# ============================================================================
# HU [1.6] Sistema de solicitudes y sesiones (WBSO-10: WBSO-59 a WBSO-67)
# ============================================================================

@app.post("/api/v1/requests", tags=["HU [1.6] Sistema de solicitudes y sesiones"], summary="[1.6.1] Formulario de solicitud (WBSO-59)")
def create_session_request(payload: Optional[SessionRequestCreate] = None):
    data = payload.model_dump() if payload else {}
    return {
        "status": "success",
        "message": "Solicitud enviada correctamente. El crédito queda en estado reservado.",
        "request": {
            "id": "req-301",
            "publication_id": data.get("publication_id", "pub-101"),
            "proposed_date": data.get("proposed_date", "2026-11-01"),
            "start_time": data.get("start_time", "18:00"),
            "modality": data.get("modality", "Virtual"),
            "status": "SOLICITADA",
            "created_at": "2026-10-18T23:05:00Z",
        },
    }


@app.get("/api/v1/requests/received", tags=["HU [1.6] Sistema de solicitudes y sesiones"], summary="[1.6.2] Solicitudes recibidas (WBSO-60)")
def list_received_requests():
    return {
        "items": [
            {
                "id": "req-201",
                "requester": {"id": "usr-carlos", "name": "Carlos G."},
                "publication_title": "Scrum y WBS práctico",
                "proposed_date": "2026-11-05",
                "start_time": "19:00",
                "modality": "Virtual",
                "status": "PENDIENTE",
            }
        ]
    }


@app.get("/api/v1/requests/sent", tags=["HU [1.6] Sistema de solicitudes y sesiones"], summary="[1.6.3] Solicitudes enviadas (WBSO-61)")
def list_sent_requests():
    return {
        "items": [
            {
                "id": "req-301",
                "recipient": {"id": "usr-tomas", "name": "Tomás R."},
                "publication_title": "Conversación en inglés para entrevistas",
                "proposed_date": "2026-11-01",
                "start_time": "18:00",
                "modality": "Virtual",
                "status": "SOLICITADA",
            }
        ]
    }


@app.patch("/api/v1/requests/{request_id}/status", tags=["HU [1.6] Sistema de solicitudes y sesiones"], summary="[1.6.4] Estados de las solicitudes (WBSO-62)")
def update_request_status(request_id: str, payload: Optional[StatusUpdateRequest] = None):
    new_status = payload.status if payload else "ACEPTADA"
    return {
        "status": "success",
        "message": f"Estado de la solicitud {request_id} actualizado a {new_status}",
        "request_id": request_id,
        "new_status": new_status,
    }


@app.get("/api/v1/sessions", tags=["HU [1.6] Sistema de solicitudes y sesiones"], summary="[1.6.5 a 1.6.7] Agenda de sesiones (WBSO-63 a 65)")
def list_sessions():
    return {
        "sessions": [
            {
                "id": "ses-501",
                "title": "Conversación en inglés para entrevistas",
                "partner": {"id": "usr-tomas", "name": "Tomás R."},
                "date": "2026-10-25",
                "start_time": "18:00",
                "end_time": "18:45",
                "modality": "Virtual",
                "status": "CONFIRMADA",
            },
            {
                "id": "ses-499",
                "title": "Introducción práctica a FastAPI",
                "partner": {"id": "usr-lucia", "name": "Lucía M."},
                "date": "2026-10-10",
                "start_time": "17:00",
                "end_time": "18:00",
                "modality": "Virtual",
                "status": "FINALIZADA",
                "is_rated": True,
            },
        ]
    }


@app.post("/api/v1/sessions/{session_id}/complete", tags=["HU [1.6] Sistema de solicitudes y sesiones"], summary="[1.6.8] Confirmación de sesión completada (WBSO-66)")
def complete_session(session_id: str):
    return {
        "status": "success",
        "message": f"Sesión {session_id} marcada como completada. Se habilita la transferencia de créditos y calificación.",
        "session_id": session_id,
        "status": "FINALIZADA",
    }


@app.get("/api/v1/sessions/conflicts-check", tags=["HU [1.6] Sistema de solicitudes y sesiones"], summary="[1.6.9] Control de superposición de horarios (WBSO-67)")
def check_schedule_conflicts(date: str = "2026-11-01", start_time: str = "18:00", duration_minutes: int = 60):
    return {
        "has_conflict": False,
        "message": "Horario disponible, no presenta superposiciones.",
    }


# ============================================================================
# HU [1.7] Sistema de créditos virtuales (WBSO-11: WBSO-68 a WBSO-75)
# ============================================================================

@app.get("/api/v1/credits/balance", tags=["HU [1.7] Sistema de créditos virtuales"], summary="[1.7.1, 1.7.2] Saldo y asignación inicial (WBSO-68, 69)")
def get_credits_balance():
    return {
        "current_balance": 5,
        "initial_grant": 5,
        "available": 4,
        "reserved": 1,
        "rule": "Los créditos son internos y no poseen valor dinerario ni rescate en moneda.",
    }


@app.post("/api/v1/credits/reserve", tags=["HU [1.7] Sistema de créditos virtuales"], summary="[1.7.3] Reserva de créditos (WBSO-70)")
def reserve_credit(amount: int = 1):
    return {
        "status": "success",
        "message": f"{amount} crédito reservado preventivamente.",
        "reserved_amount": amount,
    }


@app.post("/api/v1/credits/transfer", tags=["HU [1.7] Sistema de créditos virtuales"], summary="[1.7.4, 1.7.7, 1.7.8] Transferencia de créditos (WBSO-71, 74, 75)")
def transfer_credit(payload: Optional[CreditTransferRequest] = None):
    amount = payload.amount if payload else 1
    return {
        "status": "success",
        "message": f"Transferencia de {amount} crédito realizada exitosamente.",
        "new_balance": 4,
    }


@app.post("/api/v1/credits/cancel-hold", tags=["HU [1.7] Sistema de créditos virtuales"], summary="[1.7.5] Cancelación de movimientos y liberación de crédito (WBSO-72)")
def cancel_credit_hold(amount: int = 1):
    return {
        "status": "success",
        "message": f"Reserva de {amount} crédito cancelada y restituida al saldo disponible.",
    }


@app.get("/api/v1/credits/movements", tags=["HU [1.7] Sistema de créditos virtuales"], summary="[1.7.6] Historial de créditos (WBSO-73)")
def get_credit_movements():
    return {
        "movements": [
            {"id": "mov-1", "date": "2026-10-10", "type": "EXPENSE", "amount": -1, "description": "Sesión recibida: FastAPI inicial"},
            {"id": "mov-2", "date": "2026-10-08", "type": "INCOME", "amount": +1, "description": "Sesión dictada: Gestión de proyectos"},
            {"id": "mov-3", "date": "2026-10-01", "type": "INITIAL_GRANT", "amount": +5, "description": "Asignación inicial de bienvenida"},
        ]
    }


# ============================================================================
# HU [1.8] Sistema de historial (WBSO-12: WBSO-76 a WBSO-81)
# ============================================================================

@app.get("/api/v1/history/summary", tags=["HU [1.8] Sistema de historial"], summary="[1.8.1 a 1.8.6] Historial general de actividad (WBSO-76 a 81)")
def get_activity_history():
    return {
        "total_activities": 4,
        "items": [
            {"type": "SESSION_TAUGHT", "date": "2026-10-08", "title": "Gestión de proyectos y WBS", "partner": "Carlos G.", "credits": "+1"},
            {"type": "SESSION_LEARNED", "date": "2026-10-10", "title": "Introducción práctica a FastAPI", "partner": "Lucía M.", "credits": "-1"},
            {"type": "RATING_GIVEN", "date": "2026-10-10", "title": "Calificación a Lucía M.", "score": 5},
            {"type": "REQUEST_ACCEPTED", "date": "2026-10-12", "title": "Solicitud de inglés aceptada", "partner": "Tomás R."},
        ],
    }


@app.get("/api/v1/history/sessions", tags=["HU [1.8] Sistema de historial"], summary="[1.8.2, 1.8.3, 1.8.4] Historial de sesiones y conocimientos (WBSO-77 a 79)")
def get_session_history():
    return {
        "taught_sessions": [
            {"id": "ses-h1", "title": "Gestión de proyectos y WBS", "date": "2026-10-08", "student": "Carlos G.", "status": "COMPLETADA"}
        ],
        "learned_sessions": [
            {"id": "ses-h2", "title": "Introducción práctica a FastAPI", "date": "2026-10-10", "instructor": "Lucía M.", "status": "COMPLETADA"}
        ],
    }


# ============================================================================
# HU [1.9] Sistema de calificaciones y reputación (WBSO-13: WBSO-82 a WBSO-88)
# ============================================================================

@app.post("/api/v1/ratings", tags=["HU [1.9] Sistema de calificaciones y reputación"], summary="[1.9.1 a 1.9.3, 1.9.6, 1.9.7] Formulario y registro de calificación (WBSO-82, 83, 84, 87, 88)")
def submit_rating(payload: Optional[RatingCreateRequest] = None):
    data = payload.model_dump() if payload else {}
    return {
        "status": "success",
        "message": "Calificación registrada correctamente. Se actualizó la reputación del usuario evaluado.",
        "rating_id": "rat-701",
        "score": data.get("rating", 5),
        "comment": data.get("comment", "Excelente"),
    }


@app.get("/api/v1/users/{user_id}/reputation", tags=["HU [1.9] Sistema de calificaciones y reputación"], summary="[1.9.4, 1.9.5] Calificación promedio y reputación (WBSO-85, 86)")
def get_user_reputation(user_id: str):
    return {
        "user_id": user_id,
        "average_score": 4.85,
        "total_reviews": 14,
        "reviews": [
            {"author": "Elena P.", "score": 5, "comment": "Muy claro, paciente y organizado.", "date": "2026-10-05"},
            {"author": "Tomás R.", "score": 4.7, "comment": "Puntual y con buen material de apoyo.", "date": "2026-09-28"},
        ],
    }


# ============================================================================
# HU [1.10] Sistema de notificaciones (WBSO-14: WBSO-89 a WBSO-95)
# ============================================================================

@app.get("/api/v1/notifications", tags=["HU [1.10] Sistema de notificaciones"], summary="[1.10.1 a 1.10.7] Listado de notificaciones (WBSO-89 a 95)")
def list_notifications():
    return {
        "unread_count": 2,
        "notifications": [
            {
                "id": "notif-1",
                "type": "NEW_REQUEST",
                "title": "Nueva solicitud recibida",
                "message": "Carlos G. te solicitó una sesión de Scrum y WBS.",
                "created_at": "2026-10-18T10:00:00Z",
                "read": False,
            },
            {
                "id": "notif-2",
                "type": "CREDIT_TRANSFER",
                "title": "Crédito recibido",
                "message": "Recibiste +1 crédito por completar tu sesión con Lucía M.",
                "created_at": "2026-10-17T18:00:00Z",
                "read": False,
            },
            {
                "id": "notif-3",
                "type": "SESSION_REMINDER",
                "title": "Recordatorio de sesión",
                "message": "Tu sesión con Tomás R. comienza en 24 horas.",
                "created_at": "2026-10-16T15:00:00Z",
                "read": True,
            },
        ],
    }


@app.patch("/api/v1/notifications/{notification_id}/read", tags=["HU [1.10] Sistema de notificaciones"], summary="Marcar notificación como leída")
def mark_notification_read(notification_id: str):
    return {"status": "success", "message": f"Notificación {notification_id} marcada como leída"}


# ============================================================================
# HU [1.11] Sistema de seguridad y moderación (WBSO-17: WBSO-96 a WBSO-103)
# ============================================================================

@app.get("/api/v1/security/categories", tags=["HU [1.11] Sistema de seguridad y moderación"], summary="[1.11.1] Categorías de aprendizaje permitidas (WBSO-96)")
def get_permitted_categories():
    return {
        "permitted": ["Tecnología", "Idiomas", "Gestión", "Diseño", "Ciencias", "Artes", "Oficios", "Bienestar"],
        "prohibited_policy": "No se permite contenido ilegal, engañoso o con fines de explotación económica directa.",
    }


@app.get("/api/v1/security/prohibited-words", tags=["HU [1.11] Sistema de seguridad y moderación"], summary="[1.11.2, 1.11.3] Palabras prohibidas y filtro de publicaciones (WBSO-97, 98)")
def get_prohibited_words():
    return {
        "prohibited_words_count": 45,
        "sample": ["estafa", "piramidal", "dinero fácil", "cripto-burbuja"],
        "filter_status": "ACTIVE",
    }


@app.post("/api/v1/reports", tags=["HU [1.11] Sistema de seguridad y moderación"], summary="[1.11.4, 1.11.5] Sistema y registro de denuncias (WBSO-99, 100)")
def submit_report(payload: Optional[ReportCreateRequest] = None):
    data = payload.model_dump() if payload else {}
    return {
        "status": "success",
        "message": "Denuncia radicada con éxito. Será evaluada por el equipo de moderación.",
        "report_id": "rep-901",
        "status": "PENDING_REVIEW",
    }


@app.get("/api/v1/legal/terms", tags=["HU [1.11] Sistema de seguridad y moderación"], summary="[1.11.6, 1.11.8] Términos, condiciones y protección de datos (WBSO-101, 103)")
def get_legal_terms():
    return {
        "version": "1.0",
        "privacy_policy": "Los datos de contacto personales solo se comparten una vez confirmada la sesión.",
        "terms": "La plataforma utiliza un sistema de créditos no monetarios destinados al intercambio libre de saberes.",
    }


# ============================================================================
# HU [1.12] Panel de administración (WBSO-15: WBSO-104 a WBSO-110)
# ============================================================================

@app.get("/api/v1/admin/users", tags=["HU [1.12] Panel de administración"], summary="[1.12.1] Gestión de usuarios (WBSO-104)")
def admin_list_users():
    return {
        "users": [
            {"id": "usr-1", "name": "Martín Demo", "email": "demo@intercambio.test", "status": "ACTIVE", "reports_count": 0},
            {"id": "usr-2", "name": "Usuario Dudoso", "email": "spam@test.com", "status": "SUSPENDED", "reports_count": 3},
            {"id": "usr-3", "name": "Lucía M.", "email": "lucia@test.com", "status": "ACTIVE", "reports_count": 0},
        ]
    }


@app.get("/api/v1/admin/publications", tags=["HU [1.12] Panel de administración"], summary="[1.12.2] Gestión de publicaciones (WBSO-106)")
def admin_list_publications():
    return {
        "publications": [
            {"id": "pub-101", "title": "Conversación en inglés", "author": "Tomás R.", "status": "PUBLISHED"},
            {"id": "pub-102", "title": "Introducción a FastAPI", "author": "Lucía M.", "status": "PUBLISHED"},
            {"id": "pub-999", "title": "Propuesta observada por palabras clave", "author": "Spammer", "status": "FLAGGED"},
        ]
    }


@app.get("/api/v1/admin/reports", tags=["HU [1.12] Panel de administración"], summary="[1.12.3] Gestión de denuncias (WBSO-105)")
def admin_list_reports():
    return {
        "reports": [
            {"id": "rep-901", "target_type": "PUBLICATION", "target_id": "pub-999", "reason": "Spam comercial", "status": "OPEN"},
        ]
    }


@app.patch("/api/v1/admin/users/{user_id}/status", tags=["HU [1.12] Panel de administración"], summary="[1.12.4] Gestión de cuentas suspendidas (WBSO-107)")
def admin_update_user_status(user_id: str, status: str = "SUSPENDED"):
    return {
        "status": "success",
        "message": f"Usuario {user_id} cambiado a estado {status}",
        "user_id": user_id,
        "new_status": status,
    }


@app.post("/api/v1/admin/categories", tags=["HU [1.12] Panel de administración"], summary="[1.12.5] Gestión de categorías (WBSO-108)")
def admin_manage_category(name: str = "Nueva Categoría", description: str = "Descripción de la categoría"):
    return {
        "status": "success",
        "message": f"Categoría '{name}' creada o actualizada",
        "category_id": "cat-custom-1",
    }


@app.post("/api/v1/admin/prohibited-words", tags=["HU [1.12] Panel de administración"], summary="[1.12.6] Gestión de palabras prohibidas (WBSO-109)")
def admin_add_prohibited_word(word: str = "prohibida"):
    return {
        "status": "success",
        "message": f"Palabra '{word}' agregada al filtro de moderación",
    }


@app.get("/api/v1/admin/audit-log", tags=["HU [1.12] Panel de administración"], summary="[1.12.7] Registro de decisiones administrativas (WBSO-110)")
def admin_audit_log():
    return {
        "entries": [
            {"id": "log-1", "admin": "admin@intercambio.test", "action": "SUSPEND_USER", "target": "usr-2", "date": "2026-10-18T12:00:00Z"},
            {"id": "log-2", "admin": "admin@intercambio.test", "action": "HIDE_PUBLICATION", "target": "pub-999", "date": "2026-10-18T12:05:00Z"},
        ]
    }


# ============================================================================
# Fallback / Stubs comodín para rutas adicionales
# ============================================================================

@app.api_route("/api/{path_name:path}", methods=["GET", "POST", "PUT", "PATCH", "DELETE"], include_in_schema=False)
async def api_catch_all(path_name: str, request: Request):
    return {
        "status": "ok",
        "mock_fallback": True,
        "received_path": f"/api/{path_name}",
        "method": request.method,
        "message": "Respuesta dummy automática 200 OK generada para la ruta solicitada.",
    }
