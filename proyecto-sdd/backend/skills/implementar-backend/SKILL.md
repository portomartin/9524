---
name: implementar-backend
description: Procedimiento paso a paso para implementar y evolucionar el backend de Intercambia en FastAPI + SQLModel de forma incremental.
---

# Skill: Implementar Backend Incremental

Usar este skill para guiar cualquier desarrollo, refactor o implementación de endpoints en el backend (`proyecto-sdd/backend/`).

## 1. Fuente de Verdad y Reglas

- **Especificación técnica:** Seguir estrictamente [`proyecto-sdd/backend/docs/especificacion-tecnica-backend.md`](../../docs/especificacion-tecnica-backend.md).
- **Convenciones de código:** Respetar [`proyecto-sdd/backend/skills/convenciones-backend/SKILL.md`](../convenciones-backend/SKILL.md).
- **Alcance funcional:** [`proyecto-sdd/docs/mvp-v3.md`](../../../docs/mvp-v3.md).

## 2. Pautas Obligatorias de Implementación

1. **No romper stubs existentes:** Las rutas aún no implementadas de `backlog_endpoints.json` deben continuar respondiendo como stubs hasta que se active su implementación real.
2. **Arquitectura en capas:**
   - Crear routers en `app/routers/`.
   - Lógica de negocio en `app/services/`.
   - Consultas a BD en `app/repositories/`.
   - Modelos en `app/models/`.
3. **Persistencia dual transparente:**
   - Usar `SQLModel`.
   - Local: `sqlite:///./app.db`.
   - Cloud: si `DATABASE_URL` está definido en el entorno, conectarse a PostgreSQL.
4. **Verificación continua:**
   - Tras cada cambio, verificar que la API inicia correctamente:
     ```powershell
     cd proyecto-sdd/backend
     uvicorn main:app --reload --port 8000
     ```
   - O mediante el script raíz: `.\start-servers.ps1`
   - Comprobar que `/docs` responde y lista los endpoints con sus esquemas actualizados.
5. **No introducir dinero real ni roles separados:**
   - El rol siempre es `USER`.
   - Los créditos son enteros internos (1 hora = 1 crédito).

## 3. Hoja de Ruta de Fases

- **Fase 1:** Infraestructura y Datos Semilla (`database.py`, `models/`, `seed.py`).
- **Fase 2:** Catálogo y Búsqueda Pública (`GET` de ofertas, necesidades, filtros y rankings).
- **Fase 3:** Cuentas, Autenticación y Gestión de Propuestas (JWT, registro, perfil, CRUD propio).
- **Fase 4:** Agenda y Franjas de Disponibilidad (disponibilidad privada y agenda pública libre).
- **Fase 5:** Sesiones, Transacción de Créditos y Calificaciones (máquina de estados, UoW y reseñas).

