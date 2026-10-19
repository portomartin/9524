# Proyecto WBS clásico

Proyecto de planificación independiente construido con el enfoque tradicional del WBS original.

- **Estructura de desglose del trabajo (WBS):** [`wbs-original.md`](wbs-original.md).
- **Historias de usuario (USM):** [`historias-de-usuario.md`](historias-de-usuario.md).
- **Backlog:** [`backlog.md`](backlog.md).
- **Scrum en Jira:** [`jerarquia-jira.md`](jerarquia-jira.md).
- **Proceso de sincronización:** [`skills/crear-jira-desde-wbs-original/SKILL.md`](skills/crear-jira-desde-wbs-original/SKILL.md).
- **Proyecto Jira:** `WBSO` — `WBS Original Histórico`.
- **Tablero:** [WBSO board](https://martinporto.atlassian.net/jira/software/projects/WBSO/boards/35/backlog).
- **Especificación Técnica de API (Mini-SDD):** [`docs/sdd-especificacion-api.md`](docs/sdd-especificacion-api.md).
- **Backend Mock (FastAPI):** [`backend/README.md`](backend/README.md) (`backend/main.py`).

---

## 🚀 API Mock para Frontend (Deploy en Producción)

Para el equipo de Frontend que implementa las pantallas basadas en los tickets de Jira (`WBSO-33` a `WBSO-110`):

- **URL Base:** `https://nine524.onrender.com`
- **Documentación Interactiva (Swagger UI):** [https://nine524.onrender.com/docs](https://nine524.onrender.com/docs)
- **Contrato OpenAPI (JSON):** [https://nine524.onrender.com/openapi.json](https://nine524.onrender.com/openapi.json)
- **Healthcheck:** [https://nine524.onrender.com/health](https://nine524.onrender.com/health)

### Pautas para el desarrollador de Frontend
1. **Respuestas garantizadas:** Todos los endpoints devuelven `200 OK` con estructuras JSON de ejemplo para simular usuarios, publicaciones, búsqueda, compatibilidades, sesiones, créditos, historial, notificaciones y administración.
2. **Tolerancia a campos:** Los endpoints de mutación (`POST`, `PUT`, `PATCH`) aceptan campos extra sin lanzar error `422`.
3. **CORS abierto:** La API tiene habilitado `Access-Control-Allow-Origin: *` para consumir desde cualquier puerto o localhost (ej. Vite, Webpack, etc.).
4. **Ruta comodín:** Cualquier petición enviada a `/api/...` no mapeada explícitamente es capturada y responde `200 OK`.
5. **Ajustes:** Si los nombres de los atributos en el response difieren de los esperados por tus componentes, se pueden ir ajustando en `backend/main.py` bajo demanda.

---

Este proyecto no gobierna el alcance del producto vigente y no debe mezclar issues, estados, sprints ni estimaciones con el proyecto SDD.
