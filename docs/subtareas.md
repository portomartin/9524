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

- **Backend/API REST:** Implementar `GET /api/v1/public/offers`, `GET /api/v1/public/learning-needs` y `GET /api/v1/public/offers/{offerId}`. Sin body. Responder `200 OK` con contenido público; `404 Not Found` si el recurso no existe o no es público. Validar que no se filtren datos privados.
- **Frontend:** Crear navegación pública, listados y detalle de propuestas. Incluir estados de carga, vacío y error; no exigir autenticación para explorar.

### HU02 — Consultar confianza pública

- **Backend/API REST:** Implementar `GET /api/v1/public/users/{userId}/reputation`, `GET /api/v1/public/rankings` y `GET /api/v1/public/trending`. Responder `200 OK`; aplicar paginación si corresponde; excluir acuerdos y datos privados.
- **Frontend:** Mostrar reputación, rankings y trending públicos con mensajes claros cuando no haya datos.

### HU03 — Registrarse cuando sea necesario

- **Backend/API REST:** Implementar `POST /api/v1/users` y `GET /api/v1/public/auth-requirement`. Body de usuario: `{ email, password }` más los campos mínimos aprobados. Responder `201 Created`, `400 Bad Request` o `409 Conflict`. No almacenar contraseñas en texto plano.
- **Frontend:** Interceptar acciones protegidas, conservar el contexto de navegación y ofrecer login o registro breve.

### HU04 — Autenticarse

- **Backend/API REST:** Implementar `POST /api/v1/auth/login` y `POST /api/v1/auth/logout`. Login recibe `{ email, password }`; responder `200 OK` y cookie segura o `401 Unauthorized`. Logout invalida la sesión.
- **Frontend:** Crear login, logout, protección de rutas y estados de error; mantener el estado `USER` de forma segura.

## E2. Perfil, propuestas y necesidades

### HU05 — Completar el perfil

- **Backend/API REST:** Implementar `GET /api/v1/me/profile` y `PATCH /api/v1/me/profile`. Body sugerido: `{ name, description, generalLocation, teachingTopics, learningTopics }`. Responder `200 OK`, `400` o `401`.
- **Frontend:** Crear perfil editable con guardado parcial, visibilidad diferenciada y estados de carga, éxito y error.

### HU06 — Publicar una propuesta

- **Backend/API REST:** Implementar `POST /api/v1/teaching-offers`, `GET /api/v1/teaching-offers/{offerId}` y `PATCH /api/v1/teaching-offers/{offerId}`. Body: `{ topic, categoryId, description, level, modality, durationMinutes, creditCost, status }`. Responder `201`, `200`, `400` o `422`.
- **Frontend:** Crear alta, borrador, edición, vista previa y publicación de propuesta individual; mostrar la vista pública apta para `GUEST`.

### HU07 — Registrar un aprendizaje buscado

- **Backend/API REST:** Implementar `POST /api/v1/learning-needs`, `GET /api/v1/learning-needs/{needId}` y `PATCH /api/v1/learning-needs/{needId}`. Body: `{ topic, objective, level, modality, availabilitySummary }`. Responder `201`, `200`, `400` o `404`.
- **Frontend:** Crear formulario de aprendizaje buscado, edición, pausa y eliminación lógica; validar objetivo y campos mínimos.

## E3. Búsqueda y compatibilidad

### HU08 — Buscar aprendizajes

- **Backend/API REST:** Implementar `GET /api/v1/public/search?query={query}&type={type}&page={page}&pageSize={pageSize}`. Responder `200 OK` con resultados públicos y `400` para filtros inválidos.
- **Frontend:** Crear buscador público con resultados diferenciados, estado vacío, paginación y error.

### HU09 — Filtrar resultados

- **Backend/API REST:** Extender búsqueda con `categoryId`, `level`, `modality`, `date`, `time` y `creditMax`. Validar combinaciones y responder `200 OK`.
- **Frontend:** Crear filtros combinables, filtros activos, limpiar filtros y conservarlos al paginar.

### HU10 — Encontrar compatibilidades

- **Backend/API REST:** Implementar `GET /api/v1/me/compatibilities?page={page}&pageSize={pageSize}`. Comparar temas, niveles, objetivos, modalidad y franjas libres. Responder `200 OK` o `401 Unauthorized`.
- **Frontend:** Mostrar coincidencias, criterios que las explican y acción para iniciar una solicitud; evitar presentarlas como garantía.

## E4. Agenda y sesiones

### HU11 — Gestionar disponibilidad

- **Backend/API REST:** Implementar `GET /api/v1/me/availability`, `POST /api/v1/me/availability`, `PATCH /api/v1/me/availability/{availabilityId}` y `DELETE /api/v1/me/availability/{availabilityId}`. Body: `{ date, startTime, durationMinutes }`. Responder `201`, `200`, `204`, `400` o `409`. Rechazar recurrencias.
- **Frontend:** Crear agenda inicialmente vacía, carga de una o múltiples franjas concretas y ayudas masivas sin crear reglas recurrentes.

### HU12 — Publicar la agenda

- **Backend/API REST:** Implementar `GET /api/v1/public/users/{userId}/availability` y `PUT /api/v1/me/availability-visibility`. Body: `{ isPublic }`. Responder solo franjas libres; ocultar franjas comprometidas.
- **Frontend:** Crear control activar/desactivar, agenda pública para `GUEST` y `USER`, vista privada propia y mensajes de privacidad.

### HU13 — Crear una sesión solicitada

- **Backend/API REST:** Implementar `POST /api/v1/sessions`. Body: `{ offerId, proposedDate, startTime, durationMinutes, modality, exchangeType, reciprocalOfferId, creditCost, message }`. Crear la sesión con estado `SOLICITADA`. Responder `201`, `400`, `409` o `401`.
- **Frontend:** Crear resumen de solicitud, validar franja libre y mostrar confirmación antes de enviar.

### HU14 — Gestionar el estado de una sesión

- **Backend/API REST:** Implementar acciones sobre `POST /api/v1/sessions/{sessionId}/confirm`, `/start` y `/cancel`. Registrar actor, fecha, motivo y transición; aceptar pasa a `CONFIRMADA`, iniciar pasa a `EN_CURSO` y cancelar pasa a `CANCELADA`. Responder `200`, `400`, `403` o `409`.
- **Frontend:** Crear acciones con confirmación, mostrar estados `SOLICITADA`/`CONFIRMADA`/`EN_CURSO`/`CANCELADA` y detalle visible solo a participantes.

### HU15 — Finalizar una sesión

- **Backend/API REST:** Implementar `POST /api/v1/sessions/{sessionId}/complete`. Marcar la sesión como `FINALIZADA` solo desde `EN_CURSO`. Responder `200`, `400`, `403` o `409`; impedir doble finalización.
- **Frontend:** Mostrar completar solo cuando corresponda y habilitar historial, créditos y calificaciones después del éxito.

## E5. Créditos, historial y reputación

### HU16 — Intercambiar con créditos

- **Backend/API REST:** Implementar `POST /api/v1/sessions/{sessionId}/credit-transfer` con `Idempotency-Key`. Derivar participantes y cantidad de la sesión. Responder `201`, `400`, `409` o `422`; impedir saldo negativo.
- **Frontend:** Mostrar costo, saldo y resultado de transferencia sin presentar créditos como dinero.

### HU17 — Consultar historial

- **Backend/API REST:** Implementar `GET /api/v1/me/history?type={type}&status={status}&from={from}&to={to}&page={page}&pageSize={pageSize}` y `GET /api/v1/me/credit-movements`. Responder `200 OK`; restringir al usuario autenticado.
- **Frontend:** Crear historial de sesiones, aprendizajes, intercambios, créditos y calificaciones con paginación, vacío y error.

### HU18 — Calificarse mutuamente

- **Backend/API REST:** Implementar `POST /api/v1/sessions/{sessionId}/ratings` y `GET /api/v1/public/users/{userId}/reputation`. Body: `{ score, comment }`. Responder `201`, `400`, `403` o `409`; permitir una calificación por participante.
- **Frontend:** Crear calificación posterior a la sesión, comentario opcional, confirmación y reputación pública.

## E6. Seguridad y administración

### HU19 — Denunciar contenido o usuarios

- **Backend/API REST:** Implementar `POST /api/v1/reports`. Body: `{ targetType, targetId, reasonCode, description }`. Responder `201`, `400` o `409`; no revelar datos innecesarios.
- **Frontend:** Crear advertencias, denuncia de propuestas o usuarios, motivos y confirmación.

### HU20 — Administrar seguridad

- **Backend/API REST:** Implementar consultas `GET /api/v1/admin/users`, `/admin/teaching-offers` y `/admin/reports`, y acciones protegidas para ocultar propuestas y suspender o reactivar cuentas. Responder `200`, `403` o `404`; auditar actor, fecha y motivo.
- **Frontend:** Crear panel administrativo básico con revisión, filtros, detalle, confirmación y errores de autorización.

## Exclusiones técnicas

No se generan subtareas para comunidades, badges, IA avanzada, validación documental, recurrencias, clases grupales, equipos de enseñanza, sesiones con más de dos participantes, chat completo, videollamadas ni calendarios externos.
