# Subtareas técnicas del MVP

**Proyecto:** Plataforma de intercambio de aprendizajes  
**Fuente de verdad:** [`mvp.md`](mvp.md)  
**Historias cubiertas:** HU01 a HU21  
**HU22:** no se descompone como trabajo comprometido porque permanece como candidata pendiente de confirmación.

## Criterio de descomposición

Cada historia de usuario se divide, como mínimo, en:

- **Backend/API REST:** modelo, reglas de negocio, endpoints, autorización y pruebas del servicio.
- **Frontend:** pantalla o pantallas, formularios, estados, validaciones de presentación, integración con la API y pruebas de interacción.

Las pruebas específicas forman parte de cada subtarea para evitar crear subtareas genéricas poco accionables. Las tareas transversales —autenticación, autorización, manejo de errores, auditoría y componentes compartidos— deben reutilizarse y no duplicarse en cada historia.

En cada subtarea de Backend se incluyen endpoints REST sugeridos con sus parámetros de path, query y body. Son una propuesta de diseño técnico y deben ajustarse al contrato final de la API. En cada subtarea de Frontend se debe consultar y aplicar el skill [`convenciones-frontend`](../skills/convenciones-frontend/SKILL.md), que centraliza las reglas de Vue, la librería de componentes y la prohibición de crear estilos propios.

## Épica E1. Acceso y perfiles

### HU01 — Registrarse

#### Backend/API REST — Implementar registro de usuario

- Crear el modelo y endpoint de registro.
- Endpoint sugerido: `POST /api/v1/auth/register`.
- Body sugerido: `{ email, password }`. Los campos adicionales del primer paso quedan sujetos a la decisión pendiente de HU01.
- Validar campos obligatorios, formato y correo no duplicado.
- Almacenar la contraseña con hash seguro; nunca guardar texto plano.
- Devolver errores de validación sin exponer información sensible.
- Probar creación exitosa, datos inválidos, correo existente y contraseña inválida.

#### Frontend — Crear pantalla de registro

- Construir formulario con los campos aprobados para el primer paso.
- Consultar y aplicar el skill `convenciones-frontend`.
- Mostrar errores junto al campo correspondiente y conservar datos válidos.
- Enviar el formulario a la API y mostrar estados de carga y error.
- Redirigir al flujo definido después del registro exitoso.
- Cubrir validación básica y respuesta de la API.

### HU02 — Iniciar y cerrar sesión

#### Backend/API REST — Implementar autenticación y cierre de sesión

- Crear endpoints de inicio y cierre de sesión.
- Endpoints sugeridos: `POST /api/v1/auth/login` y `POST /api/v1/auth/logout`.
- Body de login sugerido: `{ email, password }`. Logout sin body; la identidad se obtiene de la sesión o token autenticado.
- Validar credenciales sin revelar si existe una cuenta.
- Crear, invalidar y proteger la sesión según la política definida.
- Aplicar protección contra intentos repetidos.
- Probar credenciales válidas, inválidas, sesión vencida y cierre de sesión.

#### Frontend — Crear pantallas de inicio y cierre de sesión

- Crear formulario de inicio de sesión.
- Consultar y aplicar el skill `convenciones-frontend`.
- Mostrar errores claros y estados de carga.
- Mantener el estado de sesión en el navegador de forma segura.
- Proteger las rutas privadas y permitir cerrar sesión.
- Cubrir navegación de acceso, error y salida.

### HU03 — Completar el perfil

#### Backend/API REST — Implementar consulta y actualización del perfil

- Crear endpoints para consultar y actualizar nombre, descripción y ubicación general.
- Endpoints sugeridos: `GET /api/v1/me/profile` y `PATCH /api/v1/me/profile`.
- `GET` sin body. Body de `PATCH` sugerido: `{ name, description, generalLocation }`.
- Distinguir campos obligatorios y opcionales.
- Validar límites de longitud y contenido.
- Permitir guardar parcialmente y editar posteriormente.
- Restringir el acceso a la información según los permisos definidos.

#### Frontend — Crear pantalla de perfil editable

- Construir formulario de alta y edición del perfil.
- Consultar y aplicar el skill `convenciones-frontend`.
- Permitir guardar parcialmente y mostrar una vista previa.
- Mostrar validaciones, errores y confirmación de guardado.
- Diferenciar información visible para el propio usuario y para otros.
- Cubrir carga inicial, edición y error de guardado.

### HU04 — Definir roles y preferencias

#### Backend/API REST — Implementar preferencias de participación

- Crear modelo y endpoints para roles Docente y Alumno.
- Endpoints sugeridos: `GET /api/v1/me/preferences` y `PUT /api/v1/me/preferences`.
- Body de `PUT` sugerido: `{ roles, teachingTopics[{ topicId, level }], learningTopics[{ topicId, level, objective }], preferredModality, availability[{ dayOfWeek, startTime, endTime }] }`.
- Persistir conocimientos ofrecidos y buscados, nivel, objetivos, modalidad y disponibilidad.
- Validar valores permitidos y consistencia por tema.
- Permitir modificar preferencias sin perder datos existentes.
- Exponer la información faltante para mejorar la compatibilidad.

#### Frontend — Crear pantalla de roles y preferencias

- Permitir seleccionar uno o ambos roles.
- Consultar y aplicar el skill `convenciones-frontend`.
- Crear formularios para temas, niveles, objetivos, modalidad y franjas horarias.
- Mostrar qué información está incompleta.
- Permitir editar y conservar la configuración.
- Cubrir combinaciones de Docente, Alumno y ambos roles.

## Épica E2. Propuestas de enseñanza

### HU05 — Publicar una propuesta

#### Backend/API REST — Implementar alta y edición de propuestas

- Crear modelo y endpoints para propuestas en borrador y publicadas.
- Endpoints sugeridos: `POST /api/v1/teaching-offers`, `GET /api/v1/teaching-offers/{offerId}`, `PATCH /api/v1/teaching-offers/{offerId}` y `POST /api/v1/teaching-offers/{offerId}/publish`.
- Path: `offerId`. Body de `POST` sugerido: `{ topicId, name, categoryId, description, requiredLevel, reachableLevel, modality, estimatedDurationMinutes, credits, status }`. Body de `PATCH`: los campos editables de creación. `publish` sin body o con `{ confirmWarnings }`.
- Validar nombre, categoría, descripción, niveles, modalidad, duración y créditos.
- Impedir publicar sin los campos obligatorios y categoría.
- Permitir guardar borrador y editar según el estado de la propuesta.
- Probar validaciones, transición de estado y control de propiedad.

#### Frontend — Crear pantalla de publicación de propuesta

- Construir formulario con los datos de la propuesta.
- Consultar y aplicar el skill `convenciones-frontend`.
- Permitir guardar borrador y mostrar resumen previo.
- Mostrar advertencias, errores y datos faltantes antes de publicar.
- Mostrar el estado de la propuesta y permitir editarla cuando corresponda.
- Cubrir creación, borrador, publicación y error de validación.

### HU06 — Publicar una sesión individual

#### Backend/API REST — Aplicar regla de sesión individual

- Garantizar que una propuesta tenga un solo Docente y un solo Alumno.
- Endpoint sugerido: `GET /api/v1/teaching-offers/{offerId}/session-configuration`.
- Path: `offerId`; sin body. Devuelve la configuración individual de la propuesta.
- Rechazar configuraciones grupales o con múltiples participantes.
- Validar la restricción al crear y actualizar la propuesta.
- Probar intentos de configuración grupal y respuestas de error.

#### Frontend — Mostrar y validar modalidad individual

- Presentar la sesión individual como única modalidad de participantes del MVP.
- Consultar y aplicar el skill `convenciones-frontend`.
- No ofrecer controles para clases grupales.
- Informar la restricción antes de guardar.
- Mostrar correctamente la configuración en el resumen de la propuesta.

## Épica E3. Solicitudes de aprendizaje

### HU07 — Indicar qué aprender

#### Backend/API REST — Implementar solicitudes de aprendizaje

- Crear modelo y endpoints para registrar conocimiento, objetivo libre, nivel, modalidad y disponibilidad.
- Endpoints sugeridos: `POST /api/v1/learning-requests`, `GET /api/v1/learning-requests/{requestId}` y `PATCH /api/v1/learning-requests/{requestId}`.
- Path: `requestId` en `GET` y `PATCH`. Body de `POST` sugerido: `{ topicId, objective, currentLevel, preferredModality, availability[{ dayOfWeek, startTime, endTime }], status }`. Body de `PATCH`: campos editables y `status` para pausar o reactivar.
- Permitir editar, pausar y eliminar solicitudes.
- Validar datos obligatorios y estado de la solicitud.
- Evitar inconsistencias en solicitudes activas.
- Probar alta, edición, pausa, reactivación y eliminación.

#### Frontend — Crear pantalla de solicitud de aprendizaje

- Construir formulario con objetivo libre y datos estructurados de apoyo.
- Consultar y aplicar el skill `convenciones-frontend`.
- Mostrar y editar el estado de la solicitud.
- Permitir pausar o eliminar con confirmación.
- Mostrar errores y conservar los datos válidos.
- Cubrir solicitud activa, pausada y eliminada.

## Épica E4. Búsqueda y compatibilidad

### HU08 — Buscar propuestas y solicitudes

#### Backend/API REST — Implementar búsqueda paginada

- Crear endpoint de búsqueda de propuestas y solicitudes.
- Endpoint sugerido: `GET /api/v1/search?query={query}&type={type}&page={page}`.
- Query sugerida: `query`, `type`, `category`, `level`, `modality`, `location`, `availability`, `exchangeType`, `creditsMin`, `creditsMax`, `page` y `pageSize`. Sin body.
- Buscar por conocimiento o habilidad y distinguir el tipo de resultado.
- Implementar paginación y estado sin resultados.
- Respetar visibilidad, estados y permisos.
- Probar coincidencias, ausencia de resultados, paginación y errores.

#### Frontend — Crear pantalla de búsqueda

- Crear campo de búsqueda y listado de resultados.
- Consultar y aplicar el skill `convenciones-frontend`.
- Distinguir visualmente propuestas y solicitudes.
- Implementar paginación y estado vacío.
- Mostrar la información mínima para decidir el siguiente paso.
- Cubrir carga, resultados, ausencia de resultados y error.

### HU09 — Aplicar filtros

#### Backend/API REST — Implementar filtros combinables

- Agregar filtros por conocimiento, categoría, nivel, modalidad, ubicación, disponibilidad, tipo de intercambio y créditos.
- Endpoint sugerido: `GET /api/v1/search?query={query}&category={category}&level={level}&modality={modality}&location={location}&availability={availability}&exchangeType={exchangeType}&creditsMin={creditsMin}&creditsMax={creditsMax}&page={page}`.
- Todos los filtros se envían como query parameters; no usar body en una búsqueda `GET`.
- Permitir combinar filtros y conservarlos durante la paginación.
- Validar valores y rangos permitidos.
- Devolver filtros aplicados y cantidad de resultados.
- Probar filtros individuales, combinados y sin coincidencias.

#### Frontend — Crear controles de filtros

- Construir controles para los filtros aprobados.
- Consultar y aplicar el skill `convenciones-frontend`.
- Mostrar filtros activos y permitir limpiar uno o todos.
- Conservar filtros al cambiar de página.
- Informar cuando la combinación no produce resultados.
- Cubrir aplicación, modificación, limpieza y error.

### HU10 — Encontrar compatibilidades

#### Backend/API REST — Implementar compatibilidad basada en reglas

- Implementar reglas de coincidencia de conocimientos, niveles, objetivos, modalidad y horarios.
- Endpoint sugerido: `GET /api/v1/compatibilities?page={page}`.
- Query sugerida: `page`, `pageSize`, `type` y opcionalmente `topicId`. El usuario y sus preferencias se obtienen de la sesión autenticada.
- Detectar y priorizar intercambios recíprocos.
- Devolver los criterios que explican cada coincidencia.
- Diferenciar coincidencia parcial de coincidencia fuerte sin presentarla como garantía.
- Probar datos completos, faltantes y combinaciones incompatibles.

#### Frontend — Crear pantalla de compatibilidades

- Mostrar personas compatibles y los aprendizajes relacionados.
- Consultar y aplicar el skill `convenciones-frontend`.
- Indicar los criterios que generaron cada coincidencia.
- Diferenciar coincidencias parciales, fuertes y recíprocas.
- Permitir revisar la información que sustenta el resultado.
- Cubrir resultados, estado vacío y error.

### HU11 — Recibir recomendaciones

#### Backend/API REST — Implementar recomendaciones

- Crear servicio y endpoint de recomendaciones basado en objetivos, nivel, modalidad y disponibilidad.
- Endpoint sugerido: `GET /api/v1/recommendations`.
- Query sugerida: `page`, `pageSize` y `type`. Los objetivos, nivel, modalidad y disponibilidad se obtienen del perfil autenticado.
- Integrar el mecanismo de IA/LLM solo con el alcance y las reglas aprobadas.
- Explicar el motivo de cada recomendación.
- Permitir descartar recomendaciones y evitar repetirlas indefinidamente.
- Probar actualización ante cambios de preferencias y fallas del servicio.

#### Frontend — Crear pantalla de recomendaciones

- Mostrar recomendaciones de clases y personas.
- Consultar y aplicar el skill `convenciones-frontend`.
- Explicar por qué se recomienda cada resultado.
- Permitir descartar una recomendación.
- Mostrar estados de carga, ausencia de recomendaciones y error.
- Actualizar la vista cuando cambien las preferencias.

## Épica E5. Intercambios y sesiones

### HU12 — Solicitar una sesión

#### Backend/API REST — Implementar creación de solicitudes de sesión

- Crear modelo y endpoint con participantes, tema, fecha, horario, duración, modalidad y tipo de intercambio.
- Endpoint sugerido: `POST /api/v1/session-requests`.
- Body sugerido: `{ teachingOfferId, topicId, proposedDateTime, durationMinutes, modality, exchangeType, offeredKnowledgeTopicId, credits, message }`.
- Validar disponibilidad y datos obligatorios.
- Impedir solicitudes duplicadas para la misma propuesta y franja.
- Registrar el estado inicial como pendiente.
- Probar conflictos, duplicados y creación exitosa.

#### Frontend — Crear flujo de solicitud de sesión

- Construir formulario o modal desde una propuesta.
- Consultar y aplicar el skill `convenciones-frontend`.
- Permitir seleccionar fecha, horario, duración, modalidad y tipo de intercambio.
- Mostrar resumen antes de enviar.
- Informar conflictos, duplicados y resultado de la operación.
- Cubrir carga, validación y envío.

### HU13 — Elegir el tipo de intercambio

#### Backend/API REST — Implementar reglas de intercambio recíproco y por créditos

- Persistir el tipo de intercambio elegido.
- Endpoint sugerido: `PATCH /api/v1/session-requests/{requestId}/exchange`.
- Path: `requestId`. Body sugerido: `{ exchangeType, offeredKnowledgeTopicId, credits }`; usar el conocimiento ofrecido para intercambio recíproco y créditos para intercambio mediante créditos.
- Validar conocimiento ofrecido cuando sea recíproco.
- Validar cantidad de créditos cuando corresponda.
- Impedir valores negativos o combinaciones inconsistentes.
- Probar ambas alternativas y sus errores de validación.

#### Frontend — Crear selector de tipo de intercambio

- Mostrar claramente intercambio recíproco y mediante créditos.
- Consultar y aplicar el skill `convenciones-frontend`.
- Mostrar campos condicionales según la alternativa seleccionada.
- Pedir confirmación antes de enviar.
- Mostrar el conocimiento ofrecido o la cantidad de créditos en el resumen.
- Cubrir cambio de alternativa y validación.

### HU14 — Gestionar una solicitud

#### Backend/API REST — Implementar aceptación y rechazo

- Crear endpoints para aceptar o rechazar solicitudes.
- Endpoints sugeridos: `POST /api/v1/session-requests/{requestId}/accept` y `POST /api/v1/session-requests/{requestId}/reject`.
- Path: `requestId`. `accept` sin body o con `note` opcional. `reject` puede recibir `{ reason, message }`, sujeto a la decisión sobre motivos obligatorios.
- Controlar transiciones válidas y disponibilidad vigente.
- Registrar quién y cuándo realizó la acción.
- Mantener el estado y el historial de cambios.
- Probar aceptar, rechazar, repetir acciones y solicitud incompatible.

#### Frontend — Crear pantalla de gestión de solicitudes

- Mostrar toda la información antes de aceptar o rechazar.
- Consultar y aplicar el skill `convenciones-frontend`.
- Permitir ejecutar ambas acciones con confirmación.
- Informar el nuevo estado y el resultado de la operación.
- Mostrar solicitudes pendientes, aceptadas y rechazadas.
- Cubrir permisos y errores.

### HU15 — Reservar o cancelar

#### Backend/API REST — Implementar reserva, cancelación y transiciones

- Persistir la fecha acordada y las transiciones de estado.
- Endpoints sugeridos: `POST /api/v1/sessions/{sessionId}/cancel` y `PATCH /api/v1/sessions/{sessionId}/schedule`.
- Path: `sessionId`. Body de `schedule`: `{ proposedDateTime, durationMinutes, modality }`. Body de `cancel`: `{ reason, message }`.
- Permitir cancelar antes de realizar la sesión.
- Impedir cancelar sesiones completadas.
- Registrar participante, fecha y motivo cuando esté definido.
- Probar reserva, cancelación, repetición y estados inválidos.

#### Frontend — Crear gestión de reserva y cancelación

- Mostrar la fecha y el estado de la sesión.
- Consultar y aplicar el skill `convenciones-frontend`.
- Permitir cancelar con confirmación.
- Actualizar el historial de cambios visible.
- Mostrar mensajes claros para acciones no permitidas.
- Cubrir sesión aceptada, cancelada y completada.

### HU16 — Completar una sesión

#### Backend/API REST — Implementar confirmación de sesión completada

- Crear endpoint para completar sesiones aceptadas y ya realizadas.
- Endpoint sugerido: `POST /api/v1/sessions/{sessionId}/complete`.
- Path: `sessionId`; sin body o con `{ confirmed: true }`. El backend debe verificar estado aceptado, fecha pasada y permisos.
- Validar fecha, estado y permisos del participante.
- Impedir completar dos veces la misma sesión.
- Emitir los eventos necesarios para historial, créditos y calificaciones.
- Probar estados inválidos y repetición de la operación.

#### Frontend — Crear acción de completar sesión

- Mostrar la acción solo cuando corresponda.
- Consultar y aplicar el skill `convenciones-frontend`.
- Pedir confirmación y mostrar el resultado.
- Actualizar el estado de la sesión y habilitar historial y calificación.
- Informar por qué la acción no está disponible cuando aplique.

## Épica E6. Créditos e historial

### HU17 — Transferir créditos

#### Backend/API REST — Implementar transferencia consistente de créditos

- Crear operación transaccional de débito al Alumno y crédito al Docente.
- Endpoint sugerido: `POST /api/v1/sessions/{sessionId}/credit-transfer`.
- Path: `sessionId`; la cantidad y los participantes deben derivarse de la sesión. Body opcional: `{ confirmed: true }`. Aceptar header `Idempotency-Key` para evitar duplicados.
- Validar saldo suficiente y evitar saldos negativos.
- Registrar origen, destino, cantidad, sesión y fecha.
- Garantizar idempotencia y evitar transferencias duplicadas.
- Probar transferencia exitosa, saldo insuficiente y repetición.

#### Frontend — Mostrar saldo y resultado de transferencia

- Mostrar el saldo de créditos disponible.
- Consultar y aplicar el skill `convenciones-frontend`.
- Informar cuándo se realizará la transferencia.
- Actualizar saldos y movimientos después de completar una sesión.
- Mostrar errores sin presentar los créditos como dinero.
- Cubrir operación exitosa, pendiente y fallida.

### HU18 — Consultar historial

#### Backend/API REST — Implementar historial de actividad

- Crear endpoints para sesiones, aprendizajes, intercambios y movimientos.
- Endpoints sugeridos: `GET /api/v1/me/history` y `GET /api/v1/me/credit-movements`.
- Query de historial: `type`, `status`, `from`, `to`, `page`, `pageSize`. Query de movimientos: `from`, `to`, `direction`, `page`, `pageSize`. Sin body.
- Devolver estados, fechas y detalle relacionado.
- Restringir el acceso a la información autorizada del usuario.
- Preparar paginación si el volumen lo requiere.
- Probar separación de datos entre usuarios y estados principales.

#### Frontend — Crear pantalla de historial

- Separar sesiones, aprendizajes, intercambios y movimientos.
- Consultar y aplicar el skill `convenciones-frontend`.
- Mostrar estados, fechas y detalle.
- Permitir consultar el detalle de una actividad.
- Mostrar estados de carga, vacío y error.
- Cubrir acceso únicamente a la información propia.

## Épica E7. Calificaciones y reputación

### HU19 — Calificar una experiencia

#### Backend/API REST — Implementar calificaciones y promedio

- Crear modelo y endpoints de calificación.
- Endpoints sugeridos: `POST /api/v1/sessions/{sessionId}/ratings` y `GET /api/v1/users/{userId}/reputation`.
- Path: `sessionId` o `userId`. Body de calificación: `{ ratedUserId, score, comment }`, con `score` entre 1 y 5. Reputación sin body; query opcional `page`, `pageSize`, `includeRatings`.
- Permitir calificar solo a participantes de una sesión completada.
- Validar puntuación entre 1 y 5 y comentario opcional.
- Impedir calificaciones duplicadas.
- Calcular y exponer el promedio junto con sus calificaciones.

#### Frontend — Crear pantalla de calificación

- Mostrar la acción solo después de completar una sesión.
- Consultar y aplicar el skill `convenciones-frontend`.
- Crear selector de puntuación y campo de comentario opcional.
- Mostrar errores y confirmación de envío.
- Mostrar promedio y reputación en el perfil.
- Cubrir sesión no completada, calificación enviada y duplicada.

## Épica E8. Seguridad y administración

### HU20 — Validar y denunciar contenidos

#### Backend/API REST — Implementar validación y denuncias

- Mantener categorías permitidas y expresiones prohibidas configurables.
- Endpoints sugeridos: `POST /api/v1/content-validations` y `POST /api/v1/reports`.
- Body de validación: `{ contentType, contentId, text, categoryId }`. Body de denuncia: `{ targetType, targetId, reasonCode, description }`.
- Validar publicaciones antes de guardarlas o publicarlas.
- Crear endpoints para denunciar usuarios o publicaciones.
- Registrar motivo, autor, fecha, contenido denunciado y estado.
- Probar contenido válido, bloqueado, advertencias y denuncias duplicadas o abusivas.

#### Frontend — Crear advertencias y flujo de denuncia

- Mostrar reglas y advertencias antes de publicar.
- Consultar y aplicar el skill `convenciones-frontend`.
- Informar por qué un contenido no puede publicarse cuando corresponda.
- Agregar acción de denuncia para usuarios y publicaciones.
- Mostrar motivos claros y confirmación de recepción.
- Evitar revelar información innecesaria sobre la denuncia.

### HU21 — Administrar denuncias y cuentas

#### Backend/API REST — Implementar operaciones administrativas

- Crear endpoints protegidos para consultar usuarios, publicaciones y denuncias.
- Endpoints sugeridos: `GET /api/v1/admin/users`, `GET /api/v1/admin/teaching-offers` y `GET /api/v1/admin/reports`.
- Query de usuarios: `status`, `query`, `page`, `pageSize`. Query de propuestas: `status`, `categoryId`, `query`, `page`, `pageSize`. Query de denuncias: `status`, `targetType`, `from`, `to`, `page`, `pageSize`.
- Para acciones administrativas, sugerir endpoints protegidos como `POST /api/v1/admin/teaching-offers/{offerId}/hide`, `POST /api/v1/admin/teaching-offers/{offerId}/restore`, `POST /api/v1/admin/users/{userId}/suspend` y `POST /api/v1/admin/users/{userId}/reactivate`, con body `{ reason }` cuando corresponda.
- Permitir ocultar/restaurar publicaciones y suspender/reactivar cuentas.
- Separar permisos administrativos de los permisos comunes.
- Registrar acción, administrador, fecha y motivo.
- Garantizar revisión humana antes de sanciones definitivas.
- Probar autorización, auditoría y transiciones administrativas.

#### Frontend — Crear panel administrativo básico

- Crear vistas de usuarios, publicaciones y denuncias.
- Consultar y aplicar el skill `convenciones-frontend`.
- Mostrar estado y detalle de cada denuncia.
- Permitir ocultar/restaurar publicaciones y suspender/reactivar cuentas.
- Solicitar motivo y confirmación para acciones sensibles.
- Mostrar el registro de acciones y errores de autorización.

## Historia candidata no comprometida

### HU22 — Validar conocimientos y estudios

No se generan subtareas para cargar en Jira hasta que se confirme que esta historia pertenece a la primera versión. Si se aprueba, se puede aplicar la misma estructura:

- Backend/API REST: carga segura, revisión administrativa, niveles de verificación y permisos sobre documentos.
- Frontend: carga de documentación, estado de revisión y nivel visible en el perfil.

## Tareas transversales recomendadas

Estas tareas no deben repetirse debajo de todas las historias:

1. **Backend — Definir autenticación, autorización y formato común de errores.**
2. **Backend — Configurar persistencia, migraciones y estrategia de pruebas.**
3. **Frontend — Crear componentes compartidos de formularios, estados, mensajes y paginación.**
4. **Backend/Frontend — Configurar observabilidad mínima, auditoría y manejo de errores.**
5. **Backend/Frontend — Documentar el contrato de la API REST y el flujo de ejecución local.**

Estas tareas deben colgar de una épica técnica o de la historia técnica que el equipo utilice como habilitadora, no duplicarse en cada HU.
