# Instrucciones del proyecto

## Fuente de verdad

- Existen tres versiones de la especificación: `proyecto-sdd/mvp-v1.md`, `proyecto-sdd/mvp-v2.md` y `proyecto-sdd/mvp-v3.md`.
- La fuente activa de verdad es `proyecto-sdd/mvp-v3.md` (**MVP V3**).
- V1 y V2 se conservan como versiones históricas y de comparación.
- Los skills y procesos automáticos deben partir de `proyecto-sdd/mvp-v3.md` salvo que el usuario indique explícitamente otra versión para una comparación o migración.
- La selección de V3 como fuente debe reflejarse progresivamente en el backlog, la WBS, las decisiones registradas y los demás documentos derivados.

## Dominio

- El rol de la plataforma es **USER**.
- Una misma persona puede enseñar o aprender según la actividad, sin cambiar de rol técnico.
- Los créditos son internos de la plataforma: no son dinero ni pueden convertirse en dinero.

## Arquitectura y Backend

- La arquitectura técnica aprobada para el backend es la definida en `proyecto-sdd/backend/docs/especificacion-tecnica-backend.md`:
  - Framework: FastAPI (Python).
  - Persistencia: SQLModel con soporte dual (SQLite `sqlite:///./app.db` en local, PostgreSQL vía `DATABASE_URL` en Render/Cloud).
  - Patrón de diseño: Arquitectura en capas (Routers -> Services -> Repositories -> Models).
  - Implementación incremental guiada por el skill `proyecto-sdd/backend/skills/implementar-backend/SKILL.md` respetando `proyecto-sdd/backend/skills/convenciones-backend/SKILL.md`.
  - No rediseñar ni proponer otros stacks o arquitecturas salvo solicitud explícita del usuario.

## Forma de trabajo

- Los skills de documentación y planificación SDD están en `proyecto-sdd/skills/`; el proceso clásico independiente está en `proyecto-wbs/skills/`; los skills de implementación y publicación de frontend están en `proyecto-sdd/frontend/skills/` (incluyendo la especificación viviente `frontend-v3-agentic-spec`); y los de backend, en `proyecto-sdd/backend/skills/`.
- La evolución y nuevas ideas de experiencia de usuario para el frontend `v3` se gestionan e iteran sobre `proyecto-sdd/frontend/skills/frontend-v3-agentic-spec/SKILL.md`.
- Diferenciar épicas, historias de usuario, criterios de aceptación y tareas técnicas.
- Mantener el alcance del MVP explícito.
- No modificar la especificación automáticamente: proponer cambios y esperar confirmación cuando afecten el alcance o las reglas del producto.
- Escribir la documentación en español claro y consistente.


