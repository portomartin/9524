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
- Los ejemplos de request deben usar valores representativos y cada subtarea Backend/API REST debe indicar explícitamente el tipo de los path params, query params, headers y propiedades JSON (`string`, `integer`, `number`, `boolean`, `date`, `time`, `string[]`, etc.).
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
    "email": "martin@example.com",
    "password": "Password123!"
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
  {
    "email": "martin@example.com",
    "password": "Password123!"
  }
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
    "name": "Martín Porto",
    "description": "Me interesa compartir conocimientos prácticos.",
    "generalLocation": "Buenos Aires",
    "teachingTopics": [
      "Gestión de proyectos",
      "Jira",
      "Planificación de software"
    ],
    "learningTopics": [
      "Inglés conversacional",
      "Diseño UX"
    ]
  }
  ```
  `teachingTopics` y `learningTopics` son arrays de strings (`string[]`). Para el MVP no se modelan como objetos ni requieren un catálogo formal.
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
    "topic": "Jira",
    "categoryId": "cat-01",
    "description": "Aprendé a organizar un proyecto en Jira.",
    "level": "Intermedio",
    "modality": "online",
    "durationMinutes": 60,
    "creditCost": 1,
    "status": "PUBLISHED"
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
    "topic": "Inglés",
    "objective": "Conversar con fluidez",
    "level": "Básico",
    "modality": "online",
    "availabilitySummary": "Martes 18:00"
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
  - `GET` lista las franjas del usuario autenticado. No recibe body. Ejemplo: `GET /api/v1/me/availability`.
  - `POST` crea una franja nueva. No recibe `availabilityId`; recibe la fecha, hora y duración en el body.
  - `PATCH` modifica una franja existente. `availabilityId` es el identificador `string` de la franja, por ejemplo `av-123`; viaja en el path: `PATCH /api/v1/me/availability/av-123`.
  - `DELETE` elimina una franja existente usando el mismo `availabilityId`: `DELETE /api/v1/me/availability/av-123`.

  Request body para `POST` o `PATCH`:
  ```json
  {
    "date": "2026-10-15",
    "startTime": "18:00",
    "durationMinutes": 60
  }
  ```
  `date` es `date` con formato `YYYY-MM-DD`; `startTime` es `time` con formato `HH:mm`; `durationMinutes` es `integer`. `POST` responde `201 Created`; `PATCH` responde `200 OK`; `DELETE` responde `204 No Content`. Todos pueden responder `400 Bad Request` o `409 Conflict`. Rechazar recurrencias.
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
    "offerId": "of-123",
    "proposedDate": "2026-10-15",
    "startTime": "18:00",
    "durationMinutes": 60,
    "modality": "online",
    "exchangeType": "RECIPROCAL",
    "reciprocalOfferId": "of-456",
    "creditCost": 1,
    "message": "Me interesa intercambiar esta sesión."
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
    "comment": "Muy clara y útil."
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
    "targetType": "OFFER",
    "targetId": "of-123",
    "reasonCode": "INAPPROPRIATE",
    "description": "Contenido no pertinente."
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

## Tipos de datos de los contratos Backend/API REST

Además de los ejemplos JSON, las subtareas usan estos tipos para sus parámetros y respuestas:

| HU | Tipos relevantes |
|---|---|
| HU01 | `offerId: string`; resultados públicos: `array<object>` |
| HU02 | `userId: string`; `page/pageSize: integer`; rankings y trending: `array<object>` |
| HU03 | `email: string(email)`; `password: string`; usuario creado: `object` sin credenciales |
| HU04 | `email/password: string`; cookie de sesión segura |
| HU05 | `name/description/generalLocation: string`; `teachingTopics/learningTopics: string[]` |
| HU06 | campos descriptivos: `string`; `durationMinutes/creditCost: integer` |
| HU07 | campos descriptivos: `string`; `needId: string` |
| HU08 | `query/type: string`; `page/pageSize: integer`; resultados: `array<object>` |
| HU09 | filtros textuales: `string`; `creditMax: number` |
| HU10 | `page/pageSize: integer`; compatibilidades: `array<object>` |
| HU11 | `availabilityId: string`; `date: date`; `startTime: time`; `durationMinutes: integer` |
| HU12 | `userId: string`; `isPublic: boolean`; franjas: `array<object>` |
| HU13 | IDs: `string`; `proposedDate: date`; `startTime: time`; duración y créditos: `integer` |
| HU14 | `sessionId: string`; `reason: string` opcional; fechas de transición: `date-time` |
| HU15 | `sessionId: string`; estado: `string` enumerado |
| HU16 | IDs y `Idempotency-Key: string`; créditos: `integer` |
| HU17 | filtros: `string/date`; paginación: `integer`; historial: `array<object>` |
| HU18 | IDs: `string`; `score: integer` de 1 a 5; `comment: string` opcional |
| HU19 | campos de denuncia: `string` |
| HU20 | filtros, motivos e IDs: `string`; paginación: `integer` |

Los parámetros también deben documentarse con su propósito y un ejemplo concreto:

| HU | Ejemplos de parámetros |
|---|---|
| HU01 | `offerId=of-123` identifica una propuesta pública |
| HU02 | `userId=usr-123`; `page=1&pageSize=20` |
| HU03 | `email=martin@example.com`; `password=Password123!` |
| HU04 | `email=martin@example.com`; cookie segura de sesión |
| HU05 | `teachingTopics=["Jira", "Gestión de proyectos"]`; `learningTopics=["Inglés"]` |
| HU06 | `topic=Jira`; `durationMinutes=60`; `creditCost=1` |
| HU07 | `topic=Inglés`; `objective=Conversar con fluidez` |
| HU08 | `query=Ingles&type=offer&page=1&pageSize=20` |
| HU09 | `date=2026-10-15`; `time=18:00`; `creditMax=2` |
| HU10 | `page=1&pageSize=20` |
| HU11 | `availabilityId=av-123`; `date=2026-10-15`; `startTime=18:00` |
| HU12 | `userId=usr-123`; `isPublic=true` |
| HU13 | `offerId=of-123`; `proposedDate=2026-10-15`; `startTime=18:00` |
| HU14 | `sessionId=ses-123`; `reason=Imprevisto personal` |
| HU15 | `sessionId=ses-123`; transición `EN_CURSO` → `FINALIZADA` |
| HU16 | `sessionId=ses-123`; `Idempotency-Key=transfer-ses-123-001` |
| HU17 | `type=session`; `from=2026-10-01`; `page=1&pageSize=20` |
| HU18 | `sessionId=ses-123`; `score=5`; `comment=Muy clara y útil` |
| HU19 | `targetType=OFFER`; `targetId=of-123`; `reasonCode=INAPPROPRIATE` |
| HU20 | `status=ACTIVE`; `page=1&pageSize=20`; `reason=Incumplimiento` |

## Exclusiones técnicas

No se generan subtareas para comunidades, badges, IA avanzada, validación documental, recurrencias, clases grupales, equipos de enseñanza, sesiones con más de dos participantes, chat completo, videollamadas ni calendarios externos.
