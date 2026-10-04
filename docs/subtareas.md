# Subtareas técnicas del MVP V3

**Fuente de verdad:** [`mvp-v3.md`](mvp-v3.md)  
**Backlog de origen:** [`backlog.md`](backlog.md)  
**Estado:** derivación local; no sincronizada con Jira.

Cada historia aprobada tiene una subtarea Backend/API REST y una subtarea Frontend. Los endpoints son propuestas técnicas y deben validarse contra el contrato definitivo.

## Convenciones transversales

- Prefijo sugerido: `/api/v1`.
- La visibilidad pública no expone acuerdos, participantes ni disponibilidad tomada.
- `GUEST` solo puede consultar recursos públicos.
- Las operaciones de `USER` requieren autenticación.
- Las operaciones de `ADMIN` requieren permiso administrativo.
- La disponibilidad se persiste por fecha y hora concreta; no se persisten recurrencias.
- Los errores usan `{ code, message, fields }` cuando corresponda.
- Las subtareas Frontend deben consultar y aplicar `convenciones-frontend`.

## E1. Descubrimiento y acceso público

### HU01 — Explorar como GUEST

- **Backend/API REST:** Implementar los siguientes endpoints públicos:
  ```http
  GET /api/v1/public/offers
  GET /api/v1/public/learning-needs
  GET /api/v1/public/offers/{offerId}
  ```
  Request: sin body. Response: `200 OK` con contenido público o `404 Not Found` si el recurso no existe o no es público. Validar que no se filtren datos privados.
- **Frontend:** Crear navegación pública, listados y detalle de propuestas. Incluir estados de carga, vacío y error; no exigir autenticación para explorar.

### HU02 — Consultar confianza pública

- **Backend/API REST:** Implementar:
  ```http
  GET /api/v1/public/users/{userId}/reputation
  GET /api/v1/public/rankings
  GET /api/v1/public/trending
  ```
  Response: `200 OK`; aplicar paginación si corresponde y excluir acuerdos y datos privados.
- **Frontend:** Mostrar reputación, rankings y trending públicos con mensajes claros cuando no haya datos.

### HU03 — Registrarse cuando sea necesario

- **Backend/API REST:** Implementar:
  ```http
  GET /api/v1/public/auth-requirement
  POST /api/v1/users
  Content-Type: application/json
  ```
  Request body:
  ```json
  {
    "email": "...",
    "password": "..."
  }
  ```
  Response: `201 Created`, `400 Bad Request` o `409 Conflict`. No almacenar contraseñas en texto plano.
- **Frontend:** Interceptar acciones protegidas, conservar el contexto de navegación y ofrecer login o registro breve.

### HU04 — Autenticarse

- **Backend/API REST:** Implementar:
  ```http
  POST /api/v1/auth/login
  POST /api/v1/auth/logout
  ```
  Login request body:
  ```json
  { "email": "...", "password": "..." }
  ```
  Login response: `200 OK` con cookie segura o `401 Unauthorized`. Logout invalida la sesión.
- **Frontend:** Crear login, logout, protección de rutas y estados de error; mantener el estado `USER` de forma segura.

## E2. Perfil, propuestas y necesidades

### HU05 — Completar el perfil

- **Backend/API REST:** Implementar:
  ```http
  GET /api/v1/me/profile
  PATCH /api/v1/me/profile
  Content-Type: application/json
  ```
  `GET` obtiene el perfil completo del usuario autenticado y no recibe body. `PATCH` actualiza parcialmente el perfil y recibe únicamente los campos que se desean modificar.
  Request body sugerido:
  ```json
  {
    "name": "...",
    "description": "...",
    "generalLocation": "...",
    "teachingTopics": [],
    "learningTopics": []
  }
  ```
  Response: `200 OK`, `400 Bad Request` o `401 Unauthorized`.
- **Frontend:** Crear perfil editable con guardado parcial, visibilidad diferenciada y estados de carga, éxito y error.

### HU06 — Publicar una propuesta

- **Backend/API REST:** Implementar:
  ```http
  POST /api/v1/teaching-offers
  GET /api/v1/teaching-offers/{offerId}
  PATCH /api/v1/teaching-offers/{offerId}
  Content-Type: application/json
  ```
  Request body:
  ```json
  {
    "topic": "...",
    "categoryId": "...",
    "description": "...",
    "level": "...",
    "modality": "...",
    "durationMinutes": 60,
    "creditCost": 1,
    "status": "..."
  }
  ```
  Response: `201 Created`, `200 OK`, `400 Bad Request` o `422 Unprocessable Entity`.
- **Frontend:** Crear alta, borrador, edición, vista previa y publicación de propuesta individual; mostrar la vista pública apta para `GUEST`.

### HU07 — Registrar un aprendizaje buscado

- **Backend/API REST:** Implementar:
  ```http
  POST /api/v1/learning-needs
  GET /api/v1/learning-needs/{needId}
  PATCH /api/v1/learning-needs/{needId}
  Content-Type: application/json
  ```
  Request body:
  ```json
  {
    "topic": "...",
    "objective": "...",
    "level": "...",
    "modality": "...",
    "availabilitySummary": "..."
  }
  ```
  Response: `201 Created`, `200 OK`, `400 Bad Request` o `404 Not Found`.
- **Frontend:** Crear formulario de aprendizaje buscado, edición, pausa y eliminación lógica; validar objetivo y campos mínimos.

## E3. Búsqueda y compatibilidad

### HU08 — Buscar aprendizajes

- **Backend/API REST:** Implementar:
  ```http
  GET /api/v1/public/search?query={query}&type={type}&page={page}&pageSize={pageSize}
  ```
  Request: parámetros `query`, `type`, `page` y `pageSize`; sin body. Response: `200 OK` con resultados públicos o `400 Bad Request` para filtros inválidos.
- **Frontend:** Crear buscador público con resultados diferenciados, estado vacío, paginación y error.

### HU09 — Filtrar resultados

- **Backend/API REST:** Extender la búsqueda con:
  ```http
  GET /api/v1/public/search?categoryId={categoryId}&level={level}&modality={modality}&date={date}&time={time}&creditMax={creditMax}
  ```
  Request: parámetros de query indicados; sin body. Response: `200 OK`. Validar combinaciones y filtros inválidos.
- **Frontend:** Crear filtros combinables, filtros activos, limpiar filtros y conservarlos al paginar.

### HU10 — Encontrar compatibilidades

- **Backend/API REST:** Implementar:
  ```http
  GET /api/v1/me/compatibilities?page={page}&pageSize={pageSize}
  ```
  Request: parámetros `page` y `pageSize`; sin body. Comparar temas, niveles, objetivos, modalidad y franjas libres. Response: `200 OK` o `401 Unauthorized`.
- **Frontend:** Mostrar coincidencias, criterios que las explican y acción para iniciar una solicitud; evitar presentarlas como garantía.

## E4. Agenda y sesiones

### HU11 — Gestionar disponibilidad

- **Backend/API REST:** Implementar:
  ```http
  GET /api/v1/me/availability
  POST /api/v1/me/availability
  PATCH /api/v1/me/availability/{availabilityId}
  DELETE /api/v1/me/availability/{availabilityId}
  Content-Type: application/json
  ```
  Request body para alta o modificación:
  ```json
  {
    "date": "YYYY-MM-DD",
    "startTime": "HH:mm",
    "durationMinutes": 60
  }
  ```
  Response: `201 Created`, `200 OK`, `204 No Content`, `400 Bad Request` o `409 Conflict`. Rechazar recurrencias.
- **Frontend:** Crear agenda inicialmente vacía, carga de una o múltiples franjas concretas y ayudas masivas sin crear reglas recurrentes.

### HU12 — Publicar la agenda

- **Backend/API REST:** Implementar:
  ```http
  GET /api/v1/public/users/{userId}/availability
  PUT /api/v1/me/availability-visibility
  Content-Type: application/json
  ```
  Request body de visibilidad:
  ```json
  {
    "isPublic": true
  }
  ```
  Response: devolver solo franjas libres y ocultar franjas comprometidas.
- **Frontend:** Crear control activar/desactivar, agenda pública para `GUEST` y `USER`, vista privada propia y mensajes de privacidad.

### HU13 — Crear una sesión solicitada

- **Backend/API REST:** Implementar:
  ```http
  POST /api/v1/sessions
  Content-Type: application/json
  ```
  Request body:
  ```json
  {
    "offerId": "...",
    "proposedDate": "YYYY-MM-DD",
    "startTime": "HH:mm",
    "durationMinutes": 60,
    "modality": "...",
    "exchangeType": "...",
    "reciprocalOfferId": "...",
    "creditCost": 1,
    "message": "..."
  }
  ```
  Crear la sesión con estado `SOLICITADA`. Response: `201 Created`, `400 Bad Request`, `409 Conflict` o `401 Unauthorized`.
- **Frontend:** Crear resumen de solicitud, validar franja libre y mostrar confirmación antes de enviar.

### HU14 — Gestionar el estado de una sesión

- **Backend/API REST:** Implementar:
  ```http
  POST /api/v1/sessions/{sessionId}/confirm
  POST /api/v1/sessions/{sessionId}/start
  POST /api/v1/sessions/{sessionId}/cancel
  ```
  Request: actor autenticado y, para cancelar, motivo opcional; sin body obligatorio. Registrar actor, fecha, motivo y transición. Response: `200 OK`, `400 Bad Request`, `403 Forbidden` o `409 Conflict`.
- **Frontend:** Crear acciones con confirmación, mostrar estados `SOLICITADA`/`CONFIRMADA`/`EN_CURSO`/`CANCELADA` y detalle visible solo a participantes.

### HU15 — Finalizar una sesión

- **Backend/API REST:** Implementar:
  ```http
  POST /api/v1/sessions/{sessionId}/complete
  ```
  Request: sin body; solo participantes autorizados. Marcar la sesión como `FINALIZADA` únicamente desde `EN_CURSO`. Response: `200 OK`, `400 Bad Request`, `403 Forbidden` o `409 Conflict`; impedir doble finalización.
- **Frontend:** Mostrar completar solo cuando corresponda y habilitar historial, créditos y calificaciones después del éxito.

## E5. Créditos, historial y reputación

### HU16 — Intercambiar con créditos

- **Backend/API REST:** Implementar:
  ```http
  POST /api/v1/sessions/{sessionId}/credit-transfer
  Idempotency-Key: {key}
  ```
  Request: sin body; derivar participantes y cantidad de la sesión. Response: `201 Created`, `400 Bad Request`, `409 Conflict` o `422 Unprocessable Entity`; impedir saldo negativo.
- **Frontend:** Mostrar costo, saldo y resultado de transferencia sin presentar créditos como dinero.

### HU17 — Consultar historial

- **Backend/API REST:** Implementar:
  ```http
  GET /api/v1/me/history?type={type}&status={status}&from={from}&to={to}&page={page}&pageSize={pageSize}
  GET /api/v1/me/credit-movements
  ```
  Request: parámetros de filtro y paginación; sin body. Response: `200 OK`; restringir al usuario autenticado.
- **Frontend:** Crear historial de sesiones, aprendizajes, intercambios, créditos y calificaciones con paginación, vacío y error.

### HU18 — Calificarse mutuamente

- **Backend/API REST:** Implementar:
  ```http
  POST /api/v1/sessions/{sessionId}/ratings
  GET /api/v1/public/users/{userId}/reputation
  Content-Type: application/json
  ```
  Request body de calificación:
  ```json
  {
    "score": 5,
    "comment": "..."
  }
  ```
  Response: `201 Created`, `400 Bad Request`, `403 Forbidden` o `409 Conflict`; permitir una calificación por participante.
- **Frontend:** Crear calificación posterior a la sesión, comentario opcional, confirmación y reputación pública.

## E6. Seguridad y administración

### HU19 — Denunciar contenido o usuarios

- **Backend/API REST:** Implementar:
  ```http
  POST /api/v1/reports
  Content-Type: application/json
  ```
  Request body:
  ```json
  {
    "targetType": "...",
    "targetId": "...",
    "reasonCode": "...",
    "description": "..."
  }
  ```
  Response: `201 Created`, `400 Bad Request` o `409 Conflict`; no revelar datos innecesarios.
- **Frontend:** Crear advertencias, denuncia de propuestas o usuarios, motivos y confirmación.

### HU20 — Administrar seguridad

- **Backend/API REST:** Implementar:
  ```http
  GET /api/v1/admin/users
  GET /api/v1/admin/teaching-offers
  GET /api/v1/admin/reports
  ```
  y acciones protegidas para ocultar propuestas y suspender o reactivar cuentas. Request: filtros administrativos y motivo cuando corresponda. Response: `200 OK`, `403 Forbidden` o `404 Not Found`. Auditar actor, fecha y motivo.
- **Frontend:** Crear panel administrativo básico con revisión, filtros, detalle, confirmación y errores de autorización.

## Exclusiones técnicas

No se generan subtareas para comunidades, badges, IA avanzada, validación documental, recurrencias, clases grupales, equipos de enseñanza, sesiones con más de dos participantes, chat completo, videollamadas ni calendarios externos.
