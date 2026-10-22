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
- **Especificación y Convenciones Búsqueda y Compatibilidad (1.5):** [docs/especificacion-1.5-busqueda-compatibilidad.md](docs/especificacion-1.5-busqueda-compatibilidad.md).
- **Estrategia de Mock Data y Seeding (40 usuarios, SQLite local):** [`docs/estrategia-mock-data-seeding.md`](docs/estrategia-mock-data-seeding.md).
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

### 📦 Catálogo de Datos y Registros Mockeados

- **👤 Usuario Autenticado (`GET /api/v1/users/me`):**
  - **ID:** `usr-wbso-demo` | **Nombre:** Martín Demo (`demo@intercambio.test`)
  - **Créditos:** 5 (4 disponibles, 1 reservado) | **Reputación:** 4.9 estrellas (12 sesiones completadas).
  - **Enseña:** *Gestión de proyectos, Scrum y WBS, Python inicial*.
  - **Aprende:** *Inglés conversacional, Diseño UX/UI, Fotografía digital*.
  - **Disponibilidad:** 3 franjas semanales (Lunes 18-20h, Miércoles 19-21h, Sábados 10-13h).
  - *Otros usuarios presentes en datos:* `usr-tomas` (Tomás R.), `usr-lucia` (Lucía M.), `usr-elena` (Elena P.), `usr-carlos` (Carlos G.).

- **🏷️ Categorías (`GET /api/v1/categories`):**
  - 5 categorías: `cat-tech` (Tecnología), `cat-lang` (Idiomas), `cat-mgmt` (Gestión), `cat-art` (Arte y Diseño), `cat-well` (Bienestar).

- **📢 Propuestas de Enseñanza (`GET /api/v1/publications`):**
  - `pub-101`: *Conversación en inglés orientada a entrevistas* (Tomás R. - 45 min, 1 crédito, Virtual, Intermedio).
  - `pub-102`: *Introducción práctica a FastAPI y arquitectura limpia* (Lucía M. - 60 min, 1 crédito, Virtual, Inicial).
  - `pub-103`: *Tu primera huerta urbana en macetas* (Elena P. - 90 min, 2 créditos, Presencial, Inicial).
  - *(Admin)* `pub-999`: Propuesta observada por palabras clave (`FLAGGED`).

- **🤝 Compatibilidades / Matching (`GET /api/v1/compatibilities`):**
  - **Match Recíproco (95%):** Con Tomás R. (Tomás enseña inglés y quiere aprender gestión; coinciden Miércoles 19h).
  - **Match Unidireccional (88%):** Con Lucía M. (Coincidencia en modalidad Virtual y sábados).

- **📅 Solicitudes y Sesiones (`GET /api/v1/requests/...` y `GET /api/v1/sessions`):**
  - **1 Solicitud recibida:** De Carlos G. para *Scrum y WBS* (`PENDIENTE`).
  - **1 Solicitud enviada:** A Tomás R. para *Conversación en inglés* (`SOLICITADA`).
  - **2 Sesiones pactadas:** `ses-501` con Tomás R. (`CONFIRMADA`, 25/Oct) y `ses-499` con Lucía M. (`FINALIZADA`, ya calificada).

- **💰 Créditos Virtuales (`GET /api/v1/credits/...`):**
  - Saldo: 5 créditos.
  - Libro mayor: 3 movimientos (-1 sesión recibida, +1 sesión enseñada, +5 bienvenida).

- **⭐ Calificaciones y Reputación (`GET /api/v1/users/{id}/reputation`):**
  - Promedio: 4.85 / 5.0 (14 evaluaciones).
  - Reseñas de ejemplo de Elena P. (5/5) y Tomás R. (4.7/5).

- **🔔 Notificaciones (`GET /api/v1/notifications`):**
  - 3 alertas: nueva solicitud de Carlos G. (no leída), crédito recibido (no leída), recordatorio de sesión (leída).

- **🛡️ Moderación y Admin (`GET /api/v1/admin/...`):**
  - 1 denuncia abierta (`rep-901`), 3 usuarios listados (`usr-1`, `usr-2` suspendido, `usr-3`) y 2 registros de auditoría.

---

Este proyecto no gobierna el alcance del producto vigente y no debe mezclar issues, estados, sprints ni estimaciones con el proyecto SDD.
