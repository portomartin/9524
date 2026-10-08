# Subtareas técnicas del MVP V3

**Fuente de verdad:** [`mvp-v3.md`](mvp-v3.md)  
**Backlog de origen:** [`backlog.md`](backlog.md)  
**Estado:** derivación local actualizada el 2026-10-05 según el criterio de granularidad revisado. Jira conserva la sincronización anterior de 45 subtareas hasta una solicitud externa de actualización.

La cantidad de subtareas se decide según el trabajo real de cada HU. No existe un mínimo obligatorio de Backend y Frontend. Los endpoints son propuestas técnicas y deben validarse contra el contrato definitivo.

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

## Descomposición decidida

| HU | Subtareas técnicas |
|---|---|
| [1.1.0] | [1.1.1] Backend: listar propuestas públicas; [1.1.2] Backend: listar aprendizajes buscados públicos; [1.1.3] Backend: consultar detalle público; [1.1.4] Frontend: explorar contenido público |
| [1.2.0] | [1.2.1] Backend: consultar reputación; [1.2.2] Backend: consultar rankings; [1.2.3] Backend: consultar trending; [1.2.4] Frontend: mostrar confianza pública |
| [1.3.0] | [1.3.1] Backend: implementar registro; [1.3.2] Frontend: conservar contexto y registrar |
| [1.4.0] | [1.4.1] Backend: implementar autenticación; [1.4.2] Frontend: gestionar sesión y rutas protegidas |
| [2.1.0] | [2.1.1] Backend: gestionar perfil; [2.1.2] Frontend: crear edición de perfil |
| [2.2.0] | [2.2.1] Backend: gestionar propuestas; [2.2.2] Frontend: crear edición y publicación |
| [2.3.0] | [2.3.1] Backend: gestionar necesidades; [2.3.2] Frontend: crear flujo de aprendizaje buscado |
| [3.1.0] | [3.1.1] Backend: implementar búsqueda pública; [3.1.2] Frontend: crear buscador |
| [3.2.0] | [3.2.1] Backend: aplicar filtros; [3.2.2] Frontend: gestionar filtros combinables |
| [3.3.0] | [3.3.1] Backend: calcular compatibilidades; [3.3.2] Frontend: explicar coincidencias |
| [4.1.0] | [4.1.1] Backend: gestionar franjas; [4.1.2] Backend: procesar carga múltiple sin recurrencia; [4.1.3] Frontend: crear agenda y carga asistida |
| [4.2.0] | [4.2.1] Backend: consultar agenda pública; [4.2.2] Backend: modificar visibilidad; [4.2.3] Frontend: publicar y consultar agenda |
| [4.3.0] | [4.3.1] Backend: crear sesión solicitada; [4.3.2] Backend: controlar disponibilidad y concurrencia; [4.3.3] Frontend: crear solicitud y resumen |
| [4.4.0] | [4.4.1] Backend: aceptar sesión solicitada; [4.4.2] Backend: pasar sesión confirmada a `EN_CURSO`; [4.4.3] Backend: cancelar sesión de intercambio; [4.4.4] Backend: aplicar privacidad y efectos sobre la franja; [4.4.5] Frontend: gestionar acciones de sesión |
| [4.5.0] | [4.5.1] Backend: finalizar sesión; [4.5.2] Frontend: completar y habilitar acciones posteriores |
| [5.1.0] | [5.1.1] Backend: gestionar saldo y libro de movimientos; [5.1.2] Backend: ejecutar transferencia idempotente; [5.1.3] Frontend: mostrar créditos y resultado |
| [5.2.0] | [5.2.1] Backend: consultar historial propio; [5.2.2] Frontend: crear historial de actividad |
| [5.3.0] | [5.3.1] Backend: registrar calificación; [5.3.2] Backend: consultar reputación; [5.3.3] Frontend: calificar y consultar reputación |
| [6.1.0] | [6.1.1] Backend: gestionar denuncias; [6.1.2] Frontend: crear flujo de denuncia |
| [6.2.0] | [6.2.1] Backend: consultar recursos administrativos; [6.2.2] Backend: ocultar propuestas; [6.2.3] Backend: suspender o reactivar cuentas; [6.2.4] Frontend: crear panel administrativo |

**Resultado:** 54 subtareas para 20 HU. Once HU requieren dos subtareas, cinco HU requieren tres, tres HU requieren cuatro y una HU requiere cinco. La descomposición aplica mayor detalle Backend cuando hay contratos o responsabilidades independientes y mantiene Frontend agrupado por pantalla o flujo. La numeración no fija una especialidad: refleja el orden de la descomposición decidida.

## [1.0.0] Descubrimiento y acceso público

### [1.1.0] — Explorar como GUEST

- **[1.1.1] [Backend] Listar propuestas de enseñanza públicas:** Implementar:
  ```http
  GET /api/v1/public/offers
  ```
  Request: sin body. Response: `200 OK` con propuestas públicas. Validar que no se filtren datos privados.
- **[1.1.2] [Backend] Listar aprendizajes buscados públicos:** Implementar:
  ```http
  GET /api/v1/public/learning-needs
  ```
  Request: sin body. Response: `200 OK` con aprendizajes buscados públicos. Excluir necesidades pausadas o privadas según las reglas vigentes.
- **[1.1.3] [Backend] Consultar detalle público de una propuesta:** Implementar:
  ```http
  GET /api/v1/public/offers/{offerId}
  ```
  `offerId` es `string`. Request: sin body. Response: `200 OK` o `404 Not Found` si el recurso no existe o no es público. Validar privacidad.
- **[1.1.4] [Frontend] Explorar contenido público:** Crear navegación, listados y detalle de propuestas y aprendizajes buscados. Incluir estados de carga, vacío y error; no exigir autenticación para explorar.

### [1.2.0] — Consultar confianza pública

- **[1.2.1] [Backend] Consultar reputación pública:** Implementar:
  ```http
  GET /api/v1/public/users/{userId}/reputation
  ```
  `userId` es `string` y viaja en el path. Request: sin body. Response: `200 OK` con reputación pública o `404 Not Found`; no exponer acuerdos ni datos privados.
- **[1.2.2] [Backend] Consultar rankings públicos:** Implementar:
  ```http
  GET /api/v1/public/rankings
  ```
  Request: sin body. Response: `200 OK` con rankings públicos o `400 Bad Request` si los parámetros de paginación son inválidos; aplicar paginación si corresponde.
- **[1.2.3] [Backend] Consultar contenido trending:** Implementar:
  ```http
  GET /api/v1/public/trending
  ```
  Request: sin body. Response: `200 OK` con contenido trending público o `400 Bad Request` si los parámetros opcionales son inválidos; excluir acuerdos y datos privados.
- **[1.2.4] [Frontend] Mostrar confianza pública:** Mostrar reputación, rankings y trending con mensajes claros cuando no haya datos.

### [1.3.0] — Registrarse cuando sea necesario

- **[1.3.1] [Backend] Registrar usuario y resolver requisito de autenticación:** Implementar:
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

  Checklist técnica histórica:
  - [ ] [1.3.1.1] Validar los datos mínimos de registro y evitar credenciales duplicadas.
  - [ ] [1.3.1.2] Mantener la creación de cuenta separada de la exploración pública.
- **[1.3.2] [Frontend] Convertir acción protegida en registro:** Interceptar acciones protegidas, conservar el contexto de navegación y ofrecer login o registro breve.

### [1.4.0] — Autenticarse

- **[1.4.1] [Backend] Gestionar autenticación de usuario:** Implementar:
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

  Checklist técnica histórica:
  - [x] [1.4.1.1] Implementar inicio de sesión con credenciales validadas y sesión segura.
  - [x] [1.4.1.2] Invalidar la sesión en el cierre de sesión.
  - [ ] [1.4.1.3] Mantener recuperación de contraseña como pendiente hasta definir su alcance.
- **[1.4.2] [Frontend] Gestionar acceso autenticado:** Crear login, logout, protección de rutas y estados de error; mantener el estado `USER` de forma segura.

## [2.0.0] Perfil, propuestas y necesidades

### [2.1.0] — Completar el perfil

- **[2.1.1] [Backend] Consultar y actualizar perfil:** Implementar:
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

  Checklist técnica histórica:
  - [ ] [2.1.1.1] Persistir y editar los datos básicos del perfil.
  - [ ] [2.1.1.2] Persistir `teachingTopics` y `learningTopics` como `string[]`.
  - [ ] [2.1.1.3] Mantener la información pública separada de la privada.
- **[2.1.2] [Frontend] Editar perfil:** Crear perfil editable con guardado parcial, visibilidad diferenciada y estados de carga, éxito y error.

### [2.2.0] — Publicar una propuesta

- **[2.2.1] [Backend] Gestionar propuestas de enseñanza:** Implementar:
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

  Checklist técnica histórica:
  - [ ] [2.2.1.1] Gestionar el alta, edición, borrador y publicación de una propuesta.
  - [ ] [2.2.1.2] Persistir descripción, nivel, modalidad y duración estimada.
  - [ ] [2.2.1.3] Persistir y validar el valor en créditos.
  - [ ] [2.2.1.4] Validar `categoryId` como referencia de categoría sin introducir todavía un catálogo independiente.
  - [ ] [2.2.1.5] Validar el contenido mínimo antes de publicar.
- **[2.2.2] [Frontend] Crear y publicar propuesta:** Crear alta, borrador, edición, vista previa y publicación de propuesta individual; mostrar la vista pública apta para `GUEST`.

### [2.3.0] — Registrar un aprendizaje buscado

- **[2.3.1] [Backend] Gestionar aprendizajes buscados:** Implementar:
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

  Checklist técnica histórica:
  - [ ] [2.3.1.1] Gestionar el alta, edición, pausa y eliminación lógica de una necesidad.
  - [ ] [2.3.1.2] Persistir objetivo, nivel, modalidad y resumen de disponibilidad.
  - [ ] [2.3.1.3] Validar los campos mínimos del aprendizaje buscado.
- **[2.3.2] [Frontend] Crear y mantener aprendizaje buscado:** Crear formulario, edición, pausa y eliminación lógica; validar objetivo y campos mínimos.

## [3.0.0] Búsqueda y compatibilidad

### [3.1.0] — Buscar aprendizajes

- **[3.1.1] [Backend] Buscar contenido público:** Implementar:
  ```http
  GET /api/v1/public/search?query={query}&type={type}&page={page}&pageSize={pageSize}
  ```
  Request: parámetros `query`, `type`, `page` y `pageSize`; sin body. Response: `200 OK` con resultados públicos o `400 Bad Request` para filtros inválidos.
- **[3.1.2] [Frontend] Crear buscador público:** Crear resultados diferenciados, estado vacío, paginación y error.

### [3.2.0] — Filtrar resultados

- **[3.2.1] [Backend] Aplicar filtros a la búsqueda:** Extender la búsqueda con:
  ```http
  GET /api/v1/public/search?categoryId={categoryId}&level={level}&modality={modality}&date={date}&time={time}&creditMax={creditMax}
  ```
  Request: parámetros de query indicados; sin body. Response: `200 OK`. Validar combinaciones y filtros inválidos.
- **[3.2.2] [Frontend] Gestionar filtros combinables:** Crear filtros activos, limpiar filtros y conservarlos al paginar.

### [3.3.0] — Encontrar compatibilidades

- **[3.3.1] [Backend] Calcular compatibilidades:** Implementar:
  ```http
  GET /api/v1/me/compatibilities?page={page}&pageSize={pageSize}
  ```
  Request: parámetros `page` y `pageSize`; sin body. Comparar temas, niveles, objetivos, modalidad y franjas libres. Response: `200 OK` o `401 Unauthorized`.
- **[3.3.2] [Frontend] Explicar compatibilidades:** Mostrar coincidencias, criterios que las explican y acción para iniciar una solicitud; evitar presentarlas como garantía.

## [4.0.0] Agenda y sesiones

### [4.1.0] — Gestionar disponibilidad

- **[4.1.1] [Backend] Gestionar franjas:** Implementar:
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

  Checklist técnica histórica:
  - [ ] [4.1.1.1] Persistir disponibilidades como franjas explícitas de fecha y hora.
  - [ ] [4.1.1.2] Gestionar alta, modificación y eliminación de franjas.
  - [ ] [4.1.1.3] Validar duración, conflictos y rechazo de recurrencias persistidas.
- **[4.1.2] [Backend] Procesar carga múltiple sin recurrencia:** Implementar una operación que reciba franjas concretas ya expandidas, sin persistir una regla recurrente.
  ```http
  POST /api/v1/me/availability/batch
  Content-Type: application/json
  ```
  Request body sugerido:
  ```json
  {
    "slots": [
      { "date": "2026-10-15", "startTime": "18:00", "durationMinutes": 60 },
      { "date": "2026-10-17", "startTime": "10:00", "durationMinutes": 60 }
    ]
  }
  ```
  `slots` es `array<object>` de fechas y horas concretas. Responder `201 Created` con franjas creadas o `409 Conflict` con las posiciones rechazadas. Validar el lote de forma determinista y probar que no se almacene ninguna recurrencia.
- **[4.1.3] [Frontend] Crear agenda y carga asistida:** Crear agenda inicialmente vacía, carga de una o múltiples franjas concretas y ayudas masivas sin crear reglas recurrentes. Consultar y aplicar el skill `convenciones-frontend`.

### [4.2.0] — Publicar la agenda

- **[4.2.1] [Backend] Consultar agenda pública:** Implementar:
  ```http
  GET /api/v1/public/users/{userId}/availability
  Content-Type: application/json
  ```
  `userId` es `string`. Request: sin body. Response: `200 OK` con solo franjas libres o `404 Not Found`; nunca exponer acuerdos, participantes ni franjas comprometidas.
- **[4.2.2] [Backend] Modificar visibilidad de la agenda:** Implementar:
  ```http
  PUT /api/v1/me/availability-visibility
  Content-Type: application/json
  ```
  Request body de visibilidad:
  ```json
  {
    "isPublic": true
  }
  ```
  `isPublic` es `boolean`. Response: `200 OK`, `400 Bad Request` o `401 Unauthorized`. La agenda desactivada no debe mostrarse públicamente.

  Checklist técnica histórica:
  - [ ] [4.2.2.1] Activar o desactivar la visibilidad pública de la agenda.
- **[4.2.3] [Frontend] Publicar y consultar agenda:** Crear control activar/desactivar, agenda pública para `GUEST` y `USER`, vista privada propia y mensajes de privacidad.

### [4.3.0] — Crear una sesión solicitada

- **[4.3.1] [Backend] Crear sesión solicitada:** Implementar:
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
- **[4.3.2] [Backend] Controlar disponibilidad y concurrencia:** Aplicar sobre:
  ```http
  POST /api/v1/sessions
  Content-Type: application/json
  ```
  Request: reutilizar `proposedDate: date`, `startTime: time` y `durationMinutes: integer` del body de creación; no recibe un body adicional. Response: `201 Created` cuando la sesión puede comprometer la franja o `409 Conflict` cuando la franja está tomada o cambia durante la operación. Probar dos solicitudes concurrentes y garantizar que solo una pueda comprometer la misma franja.
- **[4.3.3] [Frontend] Crear solicitud y resumen:** Crear resumen de solicitud, validar franja libre y mostrar confirmación antes de enviar. Consultar y aplicar el skill `convenciones-frontend`.

### [4.4.0] — Gestionar el estado de una sesión

- **[4.4.1] [Backend] Aceptar sesión solicitada:** Implementar:
  ```http
  POST /api/v1/sessions/{sessionId}/confirm
  ```
  Request: actor autenticado; sin body obligatorio. Solo la persona autorizada puede aceptar una sesión `SOLICITADA`. Registrar actor, fecha y transición. Response: `200 OK`, `400 Bad Request`, `403 Forbidden` o `409 Conflict`. Probar la transición válida, permisos y estados incompatibles.
- **[4.4.2] [Backend] Pasar sesión confirmada a `EN_CURSO`:** Implementar:
  ```http
  POST /api/v1/sessions/{sessionId}/start
  ```
  Request: actor autenticado; sin body obligatorio. Permitir la transición únicamente cuando la sesión esté `CONFIRMADA` y corresponda iniciarla. Registrar actor, fecha y transición. Response: `200 OK`, `400 Bad Request`, `403 Forbidden` o `409 Conflict`. Probar inicio válido, inicio anticipado y repetición de la operación.
- **[4.4.3] [Backend] Cancelar sesión de intercambio:** Implementar:
  ```http
  POST /api/v1/sessions/{sessionId}/cancel
  ```
  Request: actor autenticado y `reason: string` opcional; sin body obligatorio salvo el motivo. Permitir rechazo de una sesión `SOLICITADA` y cancelación antes de finalizar. Registrar actor, fecha, motivo y transición. Response: `200 OK`, `400 Bad Request`, `403 Forbidden` o `409 Conflict`. Probar permisos, estados incompatibles y motivo opcional.
- **[4.4.4] [Backend] Aplicar privacidad y efectos sobre la franja:** Integrar estas operaciones:
  ```http
  POST /api/v1/sessions/{sessionId}/confirm
  POST /api/v1/sessions/{sessionId}/cancel
  GET /api/v1/public/users/{userId}/availability
  ```
  `sessionId` y `userId` son `string` y viajan en el path. Request: `confirm` y `GET` sin body; `cancel` admite `reason: string` opcional. Response: `200 OK` para las transiciones y consulta válida, `403 Forbidden` por permisos insuficientes, `404 Not Found` si no existe el recurso o `409 Conflict` para una transición incompatible. Al confirmar, ocultar la franja comprometida de la vista pública; al cancelar, aplicar la liberación que corresponda sin exponer el acuerdo. Probar permisos de ambos participantes, consultas públicas posteriores y privacidad de los detalles.
- **[4.4.5] [Frontend] Gestionar acciones de sesión:** Crear acciones con confirmación, mostrar estados `SOLICITADA`/`CONFIRMADA`/`EN_CURSO`/`CANCELADA` y detalle visible solo a participantes. Mantener en esta subtarea los estados de carga, vacío, error, éxito y permisos que correspondan. Consultar y aplicar el skill `convenciones-frontend`.

### [4.5.0] — Finalizar una sesión

- **[4.5.1] [Backend] Finalizar sesión:** Implementar:
  ```http
  POST /api/v1/sessions/{sessionId}/complete
  ```
  Request: sin body; solo participantes autorizados. Marcar la sesión como `FINALIZADA` únicamente desde `EN_CURSO`. Response: `200 OK`, `400 Bad Request`, `403 Forbidden` o `409 Conflict`; impedir doble finalización.
- **[4.5.2] [Frontend] Completar sesión y habilitar acciones posteriores:** Mostrar completar solo cuando corresponda y habilitar historial, créditos y calificaciones después del éxito.

## [5.0.0] Créditos, historial y reputación

### [5.1.0] — Intercambiar con créditos

- **[5.1.1] [Backend] Gestionar saldo y libro de movimientos:** Implementar la consulta autenticada de saldo y movimientos internos:
  ```http
  GET /api/v1/me/credit-balance
  GET /api/v1/me/credit-movements?page={page}&pageSize={pageSize}
  ```
  Sin request body. `page` y `pageSize` son `integer`. Responder `200 OK` con saldo `integer` y movimientos `array<object>`, o `401 Unauthorized`. Probar privacidad y consistencia entre saldo y libro de movimientos.
- **[5.1.2] [Backend] Ejecutar transferencia idempotente:** Implementar:
  ```http
  POST /api/v1/sessions/{sessionId}/credit-transfer
  Idempotency-Key: {key}
  ```
  Request: sin body; derivar participantes y cantidad de la sesión. Response: `201 Created`, `400 Bad Request`, `409 Conflict` o `422 Unprocessable Entity`; impedir saldo negativo.

  Checklist técnica histórica:
  - [ ] [5.1.2.1] Validar saldo suficiente antes de transferir créditos.
  - [ ] [5.1.2.2] Registrar débito y crédito como una operación consistente e idempotente.
  - [ ] [5.1.2.3] Exponer el resultado de la transferencia sin tratar créditos como dinero.
- **[5.1.3] [Frontend] Mostrar créditos y resultado:** Mostrar costo, saldo y resultado de transferencia sin presentar créditos como dinero. Consultar y aplicar el skill `convenciones-frontend`.

### [5.2.0] — Consultar historial

- **[5.2.1] [Backend] Consultar historial de actividad:** Implementar:
  ```http
  GET /api/v1/me/history?type={type}&status={status}&from={from}&to={to}&page={page}&pageSize={pageSize}
  GET /api/v1/me/credit-movements
  ```
  Request: parámetros de filtro y paginación; sin body. Response: `200 OK`; restringir al usuario autenticado.

  Checklist técnica histórica:
  - [ ] [5.2.1.1] Consultar el saldo y los movimientos de créditos del usuario autenticado.
  - [ ] [5.2.1.2] Mantener separados historial de sesiones, intercambios, créditos y calificaciones.
  - [ ] [5.2.1.3] Aplicar paginación y filtros sin exponer información de otros usuarios.
- **[5.2.2] [Frontend] Crear historial de actividad:** Crear historial de sesiones, aprendizajes, intercambios, créditos y calificaciones con paginación, vacío y error.

### [5.3.0] — Calificarse mutuamente

- **[5.3.1] [Backend] Registrar calificación:** Implementar:
  ```http
  POST /api/v1/sessions/{sessionId}/ratings
  Content-Type: application/json
  ```
  Request body de calificación:
  ```json
  {
    "score": 5,
    "comment": "Muy clara y útil."
  }
  ```
  `sessionId` es `string`. Response: `201 Created`, `400 Bad Request`, `403 Forbidden` o `409 Conflict`; permitir una calificación por participante y solo después de una sesión `FINALIZADA`.
- **[5.3.2] [Backend] Consultar reputación pública actualizada:** Implementar:
  ```http
  GET /api/v1/public/users/{userId}/reputation
  ```
  `userId` es `string` y viaja en el path. Request: sin body. Response: `200 OK` con promedio y cantidad de calificaciones o `404 Not Found`; no exponer comentarios o datos privados fuera de lo definido.
- **[5.3.3] [Frontend] Calificar y consultar reputación:** Crear calificación posterior a la sesión, comentario opcional, confirmación y reputación pública.

## [6.0.0] Seguridad y administración

### [6.1.0] — Denunciar contenido o usuarios

- **[6.1.1] [Backend] Registrar denuncias:** Implementar:
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
- **[6.1.2] [Frontend] Crear flujo de denuncia:** Crear advertencias, denuncia de propuestas o usuarios, motivos y confirmación.

### [6.2.0] — Administrar seguridad

- **[6.2.1] [Backend] Consultar recursos administrativos:** Implementar:
  ```http
  GET /api/v1/admin/users
  GET /api/v1/admin/teaching-offers
  GET /api/v1/admin/reports
  ```
  Request: filtros administrativos sin body. Response: `200 OK`, `403 Forbidden` o `404 Not Found`. Restringir la información a permisos `ADMIN` y probar paginación y filtros.
- **[6.2.2] [Backend] Ocultar propuestas:** Implementar la acción protegida:
  ```http
  POST /api/v1/admin/teaching-offers/{offerId}/hide
  Content-Type: application/json
  ```
  `offerId` es `string`. Request body sugerido: `{ "reason": "Incumplimiento de las reglas" }`. Response: `200 OK`, `403 Forbidden`, `404 Not Found` o `409 Conflict`. Auditar actor, fecha, motivo y acción.
- **[6.2.3] [Backend] Suspender o reactivar cuentas:** Implementar acciones protegidas:
  ```http
  POST /api/v1/admin/users/{userId}/suspend
  POST /api/v1/admin/users/{userId}/reactivate
  Content-Type: application/json
  ```
  `userId` es `string`. Request body sugerido: `{ "reason": "Incumplimiento de las reglas" }`, donde `reason` es `string`. Responder `200 OK`, `403 Forbidden`, `404 Not Found` o `409 Conflict`. Auditar actor, fecha, motivo y acción; exigir revisión humana para sanciones definitivas.
- **[6.2.4] [Frontend] Crear panel administrativo:** Crear panel administrativo básico con revisión, filtros, detalle, confirmación y errores de autorización. Consultar y aplicar el skill `convenciones-frontend`.

## Tipos de datos de los contratos Backend/API REST

Además de los ejemplos JSON, las subtareas usan estos tipos para sus parámetros y respuestas:

| HU | Tipos relevantes |
|---|---|
| 1.1 | `offerId: string`; resultados públicos: `array<object>` |
| 1.2 | `userId: string`; `page/pageSize: integer`; rankings y trending: `array<object>` |
| 1.3 | `email: string(email)`; `password: string`; usuario creado: `object` sin credenciales |
| 1.4 | `email/password: string`; cookie de sesión segura |
| 2.1 | `name/description/generalLocation: string`; `teachingTopics/learningTopics: string[]` |
| 2.2 | campos descriptivos: `string`; `durationMinutes/creditCost: integer` |
| 2.3 | campos descriptivos: `string`; `needId: string` |
| 3.1 | `query/type: string`; `page/pageSize: integer`; resultados: `array<object>` |
| 3.2 | filtros textuales: `string`; `creditMax: number` |
| 3.3 | `page/pageSize: integer`; compatibilidades: `array<object>` |
| 4.1 | `availabilityId: string`; `date: date`; `startTime: time`; `durationMinutes: integer` |
| 4.2 | `userId: string`; `isPublic: boolean`; franjas: `array<object>` |
| 4.3 | IDs: `string`; `proposedDate: date`; `startTime: time`; duración y créditos: `integer` |
| 4.4 | `sessionId: string`; `reason: string` opcional; fechas de transición: `date-time` |
| 4.5 | `sessionId: string`; estado: `string` enumerado |
| 5.1 | IDs y `Idempotency-Key: string`; créditos: `integer` |
| 5.2 | filtros: `string/date`; paginación: `integer`; historial: `array<object>` |
| 5.3 | IDs: `string`; `score: integer` de 1 a 5; `comment: string` opcional |
| 6.1 | campos de denuncia: `string` |
| 6.2 | filtros, motivos e IDs: `string`; paginación: `integer` |

Los parámetros también deben documentarse con su propósito y un ejemplo concreto:

| HU | Ejemplos de parámetros |
|---|---|
| 1.1 | `offerId=of-123` identifica una propuesta pública |
| 1.2 | `userId=usr-123`; `page=1&pageSize=20` |
| 1.3 | `email=martin@example.com`; `password=Password123!` |
| 1.4 | `email=martin@example.com`; cookie segura de sesión |
| 2.1 | `teachingTopics=["Jira", "Gestión de proyectos"]`; `learningTopics=["Inglés"]` |
| 2.2 | `topic=Jira`; `durationMinutes=60`; `creditCost=1` |
| 2.3 | `topic=Inglés`; `objective=Conversar con fluidez` |
| 3.1 | `query=Ingles&type=offer&page=1&pageSize=20` |
| 3.2 | `date=2026-10-15`; `time=18:00`; `creditMax=2` |
| 3.3 | `page=1&pageSize=20` |
| 4.1 | `availabilityId=av-123`; `date=2026-10-15`; `startTime=18:00` |
| 4.2 | `userId=usr-123`; `isPublic=true` |
| 4.3 | `offerId=of-123`; `proposedDate=2026-10-15`; `startTime=18:00` |
| 4.4 | `sessionId=ses-123`; `reason=Imprevisto personal` |
| 4.5 | `sessionId=ses-123`; transición `EN_CURSO` → `FINALIZADA` |
| 5.1 | `sessionId=ses-123`; `Idempotency-Key=transfer-ses-123-001` |
| 5.2 | `type=session`; `from=2026-10-01`; `page=1&pageSize=20` |
| 5.3 | `sessionId=ses-123`; `score=5`; `comment=Muy clara y útil` |
| 6.1 | `targetType=OFFER`; `targetId=of-123`; `reasonCode=INAPPROPRIATE` |
| 6.2 | `status=ACTIVE`; `page=1&pageSize=20`; `reason=Incumplimiento` |

## Exclusiones técnicas

No se generan subtareas para comunidades, badges, IA avanzada, validación documental, recurrencias, clases grupales, equipos de enseñanza, sesiones con más de dos participantes, chat completo, videollamadas ni calendarios externos.
