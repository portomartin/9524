import json
from datetime import datetime
from sqlmodel import Session, select

try:

    from .database import engine, init_db
    from .models import (
        User,
        TeachingOffer,
        LearningNeed,
        AvailabilitySlot,
        ExchangeSession,
        CreditMovement,
        Review,
    )
except ImportError:
    from app.database import engine, init_db
    from app.models import (
        User,
        TeachingOffer,
        LearningNeed,
        AvailabilitySlot,
        ExchangeSession,
        CreditMovement,
        Review,
    )



def seed_database():
    """Siembra datos iniciales de prueba en la base de datos de manera idempotente."""
    init_db()

    with Session(engine) as session:
        # 1. Usuarios iniciales
        existing_user = session.exec(select(User).where(User.id == "usr-1")).first()
        if not existing_user:
            users = [
                User(
                    id="usr-1",
                    email="juancarlos@example.com",
                    password_hash="password123",  # En fase 3 se aplica hash
                    name="Juan Carlos Pérez",
                    description="Desarrollador web frontend apasionado por Vue y la accesibilidad. Busco mejorar mi inglés técnico.",
                    role="USER",
                    general_location="Buenos Aires",
                    teaching_topics=json.dumps(["Vue 3", "JavaScript Moderno", "CSS / Tailwind", "Diseño Accesible"]),
                    learning_topics=json.dumps(["Inglés para IT", "Docker Básico", "Python"]),
                    credit_balance=4,
                    is_active=True,
                ),
                User(
                    id="usr-2",
                    email="elena@example.com",
                    password_hash="password123",
                    name="Elena Rostova",
                    description="Traductora e instructora de inglés técnico para profesionales de software. Quiero aprender Vue.",
                    role="USER",
                    general_location="Córdoba",
                    teaching_topics=json.dumps(["Inglés para IT", "Conversación fluida", "Entrevistas en inglés"]),
                    learning_topics=json.dumps(["Vue 3", "Desarrollo Frontend"]),
                    credit_balance=6,
                    is_active=True,
                ),
                User(
                    id="usr-3",
                    email="carlos@example.com",
                    password_hash="password123",
                    name="Carlos Mendoza",
                    description="Ingeniero de infraestructura y DevOps. Me encanta enseñar Linux y Docker.",
                    role="USER",
                    general_location="Mendoza",
                    teaching_topics=json.dumps(["Docker Básico", "Linux Sysadmin", "Git y GitHub"]),
                    learning_topics=json.dumps(["Diseño Accesible", "Figma"]),
                    credit_balance=2,
                    is_active=True,
                ),
                User(
                    id="usr-demo",
                    email="demo@9524.test",
                    password_hash="demo1234",
                    name="Martín Demo",
                    description="Me gusta aprender y compartir herramientas digitales.",
                    role="USER",
                    general_location="Buenos Aires",
                    teaching_topics=json.dumps(["Gestión de proyectos", "Planillas"]),
                    learning_topics=json.dumps(["Inglés", "Fotografía"]),
                    credit_balance=1,
                    is_active=True,
                ),
                User(
                    id="usr-admin",
                    email="admin@example.com",
                    password_hash="adminpassword",
                    name="Laura Moderadora",
                    description="Administradora de la plataforma y defensora de la comunidad.",
                    role="ADMIN",
                    general_location="",
                    teaching_topics="[]",
                    learning_topics="[]",
                    credit_balance=10,
                    is_active=True,
                ),
            ]
            session.add_all(users)
            session.commit()

        # 2. Propuestas de Enseñanza iniciales
        existing_offer = session.exec(select(TeachingOffer).where(TeachingOffer.id == "off-1")).first()
        if not existing_offer:
            offers = [
                TeachingOffer(
                    id="off-1",
                    user_id="usr-1",
                    author_name="Juan Carlos Pérez",
                    title="Desarrollo de SPAs modernas con Vue 3 y Vite",
                    description="Sesión práctica individual para dominar Composition API, reactividad profunda, Pinia y mejores prácticas de arquitectura frontend.",
                    category="Programación",
                    level="INTERMEDIO",
                    modality="VIRTUAL",
                    duration_minutes=60,
                    status="ACTIVE",
                ),
                TeachingOffer(
                    id="off-2",
                    user_id="usr-2",
                    author_name="Elena Rostova",
                    title="Inglés técnico para entrevistas de trabajo en IT",
                    description="Simulación 1 a 1 de entrevistas técnicas en inglés, preparación de preguntas situacionales y vocabulario clave de la industria.",
                    category="Idiomas",
                    level="TODOS",
                    modality="VIRTUAL",
                    duration_minutes=60,
                    status="ACTIVE",
                ),
                TeachingOffer(
                    id="off-3",
                    user_id="usr-3",
                    author_name="Carlos Mendoza",
                    title="Fundamentos de Docker y Contenedores desde cero",
                    description="Aprende a crear Dockerfiles optimizados, gestionar volúmenes, redes y levantar entornos con docker-compose paso a paso.",
                    category="DevOps",
                    level="PRINCIPIANTE",
                    modality="VIRTUAL",
                    duration_minutes=60,
                    status="ACTIVE",
                ),
                TeachingOffer(
                    id="off-4",
                    user_id="usr-1",
                    author_name="Juan Carlos Pérez",
                    title="Fundamentos de Accesibilidad Web (WCAG 2.1)",
                    description="Cómo diseñar interfaces usables para todos: contraste de colores, navegación por teclado y semántica HTML accesible.",
                    category="Diseño",
                    level="PRINCIPIANTE",
                    modality="VIRTUAL",
                    duration_minutes=60,
                    status="ACTIVE",
                ),
                TeachingOffer(
                    id="offer-vue-basics",
                    user_id="usr-2",
                    author_name="Lucía M.",
                    title="Introducción práctica a Vue 3",
                    description="Aprendé a construir componentes, manejar estado reactivo y organizar una aplicación pequeña con Composition API.",
                    category="Desarrollo web",
                    level="Inicial",
                    modality="Virtual",
                    duration_minutes=60,
                    status="ACTIVE",
                ),
            ]
            session.add_all(offers)
            session.commit()

        # 3. Necesidades de Aprendizaje iniciales
        existing_need = session.exec(select(LearningNeed).where(LearningNeed.id == "nd-1")).first()
        if not existing_need:
            needs = [
                LearningNeed(
                    id="nd-1",
                    user_id="usr-1",
                    author_name="Juan Carlos Pérez",
                    title="Inglés conversacional fluido para reuniones de equipo",
                    description="Mejorar pronunciación y vocabulario para participar activamente en dailies y demos en inglés.",
                    category="Idiomas",
                    level="INTERMEDIO",
                    modality="VIRTUAL",
                    status="ACTIVE",
                ),
                LearningNeed(
                    id="nd-2",
                    user_id="usr-2",
                    author_name="Elena Rostova",
                    title="Arquitectura de Componentes en Vue 3",
                    description="Comprender patrones de inyección de dependencias, composables reusables y slots avanzados.",
                    category="Programación",
                    level="PRINCIPIANTE",
                    modality="VIRTUAL",
                    status="ACTIVE",
                ),
                LearningNeed(
                    id="nd-3",
                    user_id="usr-3",
                    author_name="Carlos Mendoza",
                    title="Diseño de Interfaces Accesibles en Figma",
                    description="Aprender a estructurar design systems considerando estándares de contraste y navegación.",
                    category="Diseño",
                    level="PRINCIPIANTE",
                    modality="VIRTUAL",
                    status="ACTIVE",
                ),
            ]
            session.add_all(needs)
            session.commit()

        # 4. Agenda inicial
        existing_slot = session.exec(select(AvailabilitySlot).where(AvailabilitySlot.id == "slot-1")).first()
        if not existing_slot:
            slots = [
                AvailabilitySlot(
                    id="slot-1",
                    user_id="usr-1",
                    date="2026-10-15",
                    start_time="10:00",
                    duration_minutes=60,
                    is_booked=False,
                    is_public=True,
                ),
                AvailabilitySlot(
                    id="slot-2",
                    user_id="usr-2",
                    date="2026-10-16",
                    start_time="15:00",
                    duration_minutes=60,
                    is_booked=False,
                    is_public=True,
                ),
                AvailabilitySlot(
                    id="slot-3",
                    user_id="usr-3",
                    date="2026-10-17",
                    start_time="18:00",
                    duration_minutes=60,
                    is_booked=False,
                    is_public=True,
                ),
            ]
            session.add_all(slots)
            session.commit()

        # 5. Movimientos de Crédito iniciales
        existing_mov = session.exec(select(CreditMovement).where(CreditMovement.id == "mov-1")).first()
        if not existing_mov:
            movs = [
                CreditMovement(
                    id="mov-1",
                    user_id="usr-1",
                    amount=1,
                    balance_after=4,
                    reason="INITIAL_GRANT",
                ),
                CreditMovement(
                    id="mov-2",
                    user_id="usr-2",
                    amount=1,
                    balance_after=6,
                    reason="INITIAL_GRANT",
                ),
                CreditMovement(
                    id="mov-3",
                    user_id="usr-demo",
                    amount=1,
                    balance_after=1,
                    reason="INITIAL_GRANT",
                ),
            ]
            session.add_all(movs)
            session.commit()


if __name__ == "__main__":
    seed_database()
    print("Base de datos inicializada y sembrada con éxito.")
