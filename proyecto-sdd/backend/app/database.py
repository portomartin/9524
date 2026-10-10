from typing import Generator
from sqlmodel import SQLModel, create_engine, Session
from .config import SETTINGS_DATABASE_URL

# Configuración del motor: si es SQLite, requiere check_same_thread=False
connect_args = {}
if SETTINGS_DATABASE_URL.startswith("sqlite"):
    connect_args["check_same_thread"] = False

engine = create_engine(
    SETTINGS_DATABASE_URL,
    echo=False,
    connect_args=connect_args
)


def init_db() -> None:
    """Crea todas las tablas si no existen."""
    # Importar los modelos para que SQLModel los registre en su metadata
    from . import models  # noqa: F401
    SQLModel.metadata.create_all(engine)


def get_session() -> Generator[Session, None, None]:
    """Dependency inyectable para FastAPI."""
    with Session(engine) as session:
        yield session
