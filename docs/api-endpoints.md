# Endpoints de la API

Listado generado desde [`backend/backlog_endpoints.json`](../backend/backlog_endpoints.json).

Hay 44 combinaciones de verbo y ruta del backlog.
`GET /api/v1/public/offers` devuelve un array con una propuesta de ejemplo y alimenta el listado del frontend.
Las demás rutas son **stubs**: devuelven `{}` con **200 OK**.
No hay autenticación ni persistencia.
Esto no implica que las tareas de Jira estén completadas.

- [API e índice actualizado](https://nine524-api-unificado.onrender.com/).
- [Documentación interactiva y parámetros](https://nine524-api-unificado.onrender.com/docs).
- [Contrato OpenAPI JSON](https://nine524-api-unificado.onrender.com/openapi.json).

## Rutas del backlog

| Verbo | Ruta | Tareas de Jira |
| --- | --- | --- |
| GET | [/api/v1/public/offers](https://nine524-api-unificado.onrender.com/docs#/Backlog%20%E2%80%94%20stubs/get__api_v1_public_offers_api_v1_public_offers_get) | [\[1.1.1\] \[Backend\] Listar propuestas de enseñanza públicas](https://martinporto.atlassian.net/browse/BH95-166) |
| GET | [/api/v1/public/learning-needs](https://nine524-api-unificado.onrender.com/docs#/Backlog%20%E2%80%94%20stubs/get__api_v1_public_learning_needs_api_v1_public_learning_needs_get) | [\[1.1.2\] \[Backend\] Listar aprendizajes buscados públicos](https://martinporto.atlassian.net/browse/BH95-167) |
| GET | [/api/v1/public/users/{userId}/reputation](https://nine524-api-unificado.onrender.com/docs#/Backlog%20%E2%80%94%20stubs/get__api_v1_public_users_userId_reputation_api_v1_public_users__userId__reputation_get) | [\[1.2.1\] \[Backend\] Consultar reputación pública](https://martinporto.atlassian.net/browse/BH95-168)<br>[\[5.3.2\] \[Backend\] Consultar reputación pública actualizada](https://martinporto.atlassian.net/browse/BH95-201) |
| GET | [/api/v1/public/rankings](https://nine524-api-unificado.onrender.com/docs#/Backlog%20%E2%80%94%20stubs/get__api_v1_public_rankings_api_v1_public_rankings_get) | [\[1.2.2\] \[Backend\] Consultar rankings públicos](https://martinporto.atlassian.net/browse/BH95-169) |
| GET | [/api/v1/public/auth-requirement](https://nine524-api-unificado.onrender.com/docs#/Backlog%20%E2%80%94%20stubs/get__api_v1_public_auth_requirement_api_v1_public_auth_requirement_get) | [\[1.3.1\] \[Backend\] Registrar usuario y resolver requisito de autenticación](https://martinporto.atlassian.net/browse/BH95-170) |
| POST | [/api/v1/users](https://nine524-api-unificado.onrender.com/docs#/Backlog%20%E2%80%94%20stubs/post__api_v1_users_api_v1_users_post) | [\[1.3.1\] \[Backend\] Registrar usuario y resolver requisito de autenticación](https://martinporto.atlassian.net/browse/BH95-170) |
| POST | [/api/v1/auth/login](https://nine524-api-unificado.onrender.com/docs#/Backlog%20%E2%80%94%20stubs/post__api_v1_auth_login_api_v1_auth_login_post) | [\[1.4.1\] \[Backend\] Gestionar autenticación de usuario](https://martinporto.atlassian.net/browse/BH95-172) |
| POST | [/api/v1/auth/logout](https://nine524-api-unificado.onrender.com/docs#/Backlog%20%E2%80%94%20stubs/post__api_v1_auth_logout_api_v1_auth_logout_post) | [\[1.4.1\] \[Backend\] Gestionar autenticación de usuario](https://martinporto.atlassian.net/browse/BH95-172) |
| GET | [/api/v1/me/profile](https://nine524-api-unificado.onrender.com/docs#/Backlog%20%E2%80%94%20stubs/get__api_v1_me_profile_api_v1_me_profile_get) | [\[2.1.1\] \[Backend\] Consultar y actualizar perfil](https://martinporto.atlassian.net/browse/BH95-174) |
| PATCH | [/api/v1/me/profile](https://nine524-api-unificado.onrender.com/docs#/Backlog%20%E2%80%94%20stubs/patch__api_v1_me_profile_api_v1_me_profile_patch) | [\[2.1.1\] \[Backend\] Consultar y actualizar perfil](https://martinporto.atlassian.net/browse/BH95-174) |
| POST | [/api/v1/teaching-offers](https://nine524-api-unificado.onrender.com/docs#/Backlog%20%E2%80%94%20stubs/post__api_v1_teaching_offers_api_v1_teaching_offers_post) | [\[2.2.1\] \[Backend\] Gestionar propuestas de enseñanza](https://martinporto.atlassian.net/browse/BH95-176) |
| GET | [/api/v1/teaching-offers/{offerId}](https://nine524-api-unificado.onrender.com/docs#/Backlog%20%E2%80%94%20stubs/get__api_v1_teaching_offers_offerId__api_v1_teaching_offers__offerId__get) | [\[2.2.1\] \[Backend\] Gestionar propuestas de enseñanza](https://martinporto.atlassian.net/browse/BH95-176) |
| PATCH | [/api/v1/teaching-offers/{offerId}](https://nine524-api-unificado.onrender.com/docs#/Backlog%20%E2%80%94%20stubs/patch__api_v1_teaching_offers_offerId__api_v1_teaching_offers__offerId__patch) | [\[2.2.1\] \[Backend\] Gestionar propuestas de enseñanza](https://martinporto.atlassian.net/browse/BH95-176) |
| POST | [/api/v1/learning-needs](https://nine524-api-unificado.onrender.com/docs#/Backlog%20%E2%80%94%20stubs/post__api_v1_learning_needs_api_v1_learning_needs_post) | [\[2.3.1\] \[Backend\] Gestionar aprendizajes buscados](https://martinporto.atlassian.net/browse/BH95-178) |
| GET | [/api/v1/learning-needs/{needId}](https://nine524-api-unificado.onrender.com/docs#/Backlog%20%E2%80%94%20stubs/get__api_v1_learning_needs_needId__api_v1_learning_needs__needId__get) | [\[2.3.1\] \[Backend\] Gestionar aprendizajes buscados](https://martinporto.atlassian.net/browse/BH95-178) |
| PATCH | [/api/v1/learning-needs/{needId}](https://nine524-api-unificado.onrender.com/docs#/Backlog%20%E2%80%94%20stubs/patch__api_v1_learning_needs_needId__api_v1_learning_needs__needId__patch) | [\[2.3.1\] \[Backend\] Gestionar aprendizajes buscados](https://martinporto.atlassian.net/browse/BH95-178) |
| GET | [/api/v1/public/search](https://nine524-api-unificado.onrender.com/docs#/Backlog%20%E2%80%94%20stubs/get__api_v1_public_search_api_v1_public_search_get) | [\[3.1.1\] \[Backend\] Buscar contenido público](https://martinporto.atlassian.net/browse/BH95-180)<br>[\[3.2.1\] \[Backend\] Aplicar filtros a la búsqueda](https://martinporto.atlassian.net/browse/BH95-182) |
| GET | [/api/v1/me/compatibilities](https://nine524-api-unificado.onrender.com/docs#/Backlog%20%E2%80%94%20stubs/get__api_v1_me_compatibilities_api_v1_me_compatibilities_get) | [\[3.3.1\] \[Backend\] Calcular compatibilidades](https://martinporto.atlassian.net/browse/BH95-184) |
| GET | [/api/v1/me/availability](https://nine524-api-unificado.onrender.com/docs#/Backlog%20%E2%80%94%20stubs/get__api_v1_me_availability_api_v1_me_availability_get) | [\[4.1.1\] \[Backend\] Gestionar franjas](https://martinporto.atlassian.net/browse/BH95-186) |
| POST | [/api/v1/me/availability](https://nine524-api-unificado.onrender.com/docs#/Backlog%20%E2%80%94%20stubs/post__api_v1_me_availability_api_v1_me_availability_post) | [\[4.1.1\] \[Backend\] Gestionar franjas](https://martinporto.atlassian.net/browse/BH95-186) |
| PATCH | [/api/v1/me/availability/{availabilityId}](https://nine524-api-unificado.onrender.com/docs#/Backlog%20%E2%80%94%20stubs/patch__api_v1_me_availability_availabilityId__api_v1_me_availability__availabilityId__patch) | [\[4.1.1\] \[Backend\] Gestionar franjas](https://martinporto.atlassian.net/browse/BH95-186) |
| DELETE | [/api/v1/me/availability/{availabilityId}](https://nine524-api-unificado.onrender.com/docs#/Backlog%20%E2%80%94%20stubs/delete__api_v1_me_availability_availabilityId__api_v1_me_availability__availabilityId__delete) | [\[4.1.1\] \[Backend\] Gestionar franjas](https://martinporto.atlassian.net/browse/BH95-186) |
| GET | [/api/v1/public/users/{userId}/availability](https://nine524-api-unificado.onrender.com/docs#/Backlog%20%E2%80%94%20stubs/get__api_v1_public_users_userId_availability_api_v1_public_users__userId__availability_get) | [\[4.2.1\] \[Backend\] Consultar agenda pública](https://martinporto.atlassian.net/browse/BH95-188)<br>[\[4.4.4\] \[Backend\] Aplicar privacidad y efectos sobre la franja](https://martinporto.atlassian.net/browse/BH95-216) |
| PUT | [/api/v1/me/availability-visibility](https://nine524-api-unificado.onrender.com/docs#/Backlog%20%E2%80%94%20stubs/put__api_v1_me_availability_visibility_api_v1_me_availability_visibility_put) | [\[4.2.2\] \[Backend\] Modificar visibilidad de la agenda](https://martinporto.atlassian.net/browse/BH95-189) |
| POST | [/api/v1/sessions](https://nine524-api-unificado.onrender.com/docs#/Backlog%20%E2%80%94%20stubs/post__api_v1_sessions_api_v1_sessions_post) | [\[4.3.1\] \[Backend\] Crear sesión solicitada](https://martinporto.atlassian.net/browse/BH95-190)<br>[\[4.3.2\] \[Backend\] Controlar disponibilidad y concurrencia](https://martinporto.atlassian.net/browse/BH95-207) |
| POST | [/api/v1/sessions/{sessionId}/confirm](https://nine524-api-unificado.onrender.com/docs#/Backlog%20%E2%80%94%20stubs/post__api_v1_sessions_sessionId_confirm_api_v1_sessions__sessionId__confirm_post) | [\[4.4.1\] \[Backend\] Aceptar sesión solicitada](https://martinporto.atlassian.net/browse/BH95-192)<br>[\[4.4.4\] \[Backend\] Aplicar privacidad y efectos sobre la franja](https://martinporto.atlassian.net/browse/BH95-216) |
| POST | [/api/v1/sessions/{sessionId}/cancel](https://nine524-api-unificado.onrender.com/docs#/Backlog%20%E2%80%94%20stubs/post__api_v1_sessions_sessionId_cancel_api_v1_sessions__sessionId__cancel_post) | [\[4.4.3\] \[Backend\] Cancelar sesión de intercambio](https://martinporto.atlassian.net/browse/BH95-193)<br>[\[4.4.4\] \[Backend\] Aplicar privacidad y efectos sobre la franja](https://martinporto.atlassian.net/browse/BH95-216) |
| POST | [/api/v1/sessions/{sessionId}/complete](https://nine524-api-unificado.onrender.com/docs#/Backlog%20%E2%80%94%20stubs/post__api_v1_sessions_sessionId_complete_api_v1_sessions__sessionId__complete_post) | [\[4.5.1\] \[Backend\] Finalizar sesión](https://martinporto.atlassian.net/browse/BH95-194) |
| POST | [/api/v1/sessions/{sessionId}/credit-transfer](https://nine524-api-unificado.onrender.com/docs#/Backlog%20%E2%80%94%20stubs/post__api_v1_sessions_sessionId_credit_transfer_api_v1_sessions__sessionId__credit_transfer_post) | [\[5.1.2\] \[Backend\] Ejecutar transferencia idempotente](https://martinporto.atlassian.net/browse/BH95-196) |
| GET | [/api/v1/me/history](https://nine524-api-unificado.onrender.com/docs#/Backlog%20%E2%80%94%20stubs/get__api_v1_me_history_api_v1_me_history_get) | [\[5.2.1\] \[Backend\] Consultar historial de actividad](https://martinporto.atlassian.net/browse/BH95-198) |
| GET | [/api/v1/me/credit-movements](https://nine524-api-unificado.onrender.com/docs#/Backlog%20%E2%80%94%20stubs/get__api_v1_me_credit_movements_api_v1_me_credit_movements_get) | [\[5.2.1\] \[Backend\] Consultar historial de actividad](https://martinporto.atlassian.net/browse/BH95-198)<br>[\[5.1.1\] \[Backend\] Gestionar saldo y libro de movimientos](https://martinporto.atlassian.net/browse/BH95-208) |
| POST | [/api/v1/sessions/{sessionId}/ratings](https://nine524-api-unificado.onrender.com/docs#/Backlog%20%E2%80%94%20stubs/post__api_v1_sessions_sessionId_ratings_api_v1_sessions__sessionId__ratings_post) | [\[5.3.1\] \[Backend\] Registrar calificación](https://martinporto.atlassian.net/browse/BH95-200) |
| POST | [/api/v1/reports](https://nine524-api-unificado.onrender.com/docs#/Backlog%20%E2%80%94%20stubs/post__api_v1_reports_api_v1_reports_post) | [\[6.1.1\] \[Backend\] Registrar denuncias](https://martinporto.atlassian.net/browse/BH95-202) |
| GET | [/api/v1/admin/users](https://nine524-api-unificado.onrender.com/docs#/Backlog%20%E2%80%94%20stubs/get__api_v1_admin_users_api_v1_admin_users_get) | [\[6.2.1\] \[Backend\] Consultar recursos administrativos](https://martinporto.atlassian.net/browse/BH95-204) |
| GET | [/api/v1/admin/teaching-offers](https://nine524-api-unificado.onrender.com/docs#/Backlog%20%E2%80%94%20stubs/get__api_v1_admin_teaching_offers_api_v1_admin_teaching_offers_get) | [\[6.2.1\] \[Backend\] Consultar recursos administrativos](https://martinporto.atlassian.net/browse/BH95-204) |
| GET | [/api/v1/admin/reports](https://nine524-api-unificado.onrender.com/docs#/Backlog%20%E2%80%94%20stubs/get__api_v1_admin_reports_api_v1_admin_reports_get) | [\[6.2.1\] \[Backend\] Consultar recursos administrativos](https://martinporto.atlassian.net/browse/BH95-204) |
| POST | [/api/v1/admin/users/{userId}/suspend](https://nine524-api-unificado.onrender.com/docs#/Backlog%20%E2%80%94%20stubs/post__api_v1_admin_users_userId_suspend_api_v1_admin_users__userId__suspend_post) | [\[6.2.3\] \[Backend\] Suspender o reactivar cuentas](https://martinporto.atlassian.net/browse/BH95-205) |
| POST | [/api/v1/admin/users/{userId}/reactivate](https://nine524-api-unificado.onrender.com/docs#/Backlog%20%E2%80%94%20stubs/post__api_v1_admin_users_userId_reactivate_api_v1_admin_users__userId__reactivate_post) | [\[6.2.3\] \[Backend\] Suspender o reactivar cuentas](https://martinporto.atlassian.net/browse/BH95-205) |
| POST | [/api/v1/me/availability/batch](https://nine524-api-unificado.onrender.com/docs#/Backlog%20%E2%80%94%20stubs/post__api_v1_me_availability_batch_api_v1_me_availability_batch_post) | [\[4.1.2\] \[Backend\] Procesar carga múltiple sin recurrencia](https://martinporto.atlassian.net/browse/BH95-206) |
| GET | [/api/v1/me/credit-balance](https://nine524-api-unificado.onrender.com/docs#/Backlog%20%E2%80%94%20stubs/get__api_v1_me_credit_balance_api_v1_me_credit_balance_get) | [\[5.1.1\] \[Backend\] Gestionar saldo y libro de movimientos](https://martinporto.atlassian.net/browse/BH95-208) |
| POST | [/api/v1/admin/teaching-offers/{offerId}/hide](https://nine524-api-unificado.onrender.com/docs#/Backlog%20%E2%80%94%20stubs/post__api_v1_admin_teaching_offers_offerId_hide_api_v1_admin_teaching_offers__offerId__hide_post) | [\[6.2.2\] \[Backend\] Ocultar propuestas](https://martinporto.atlassian.net/browse/BH95-209) |
| POST | [/api/v1/sessions/{sessionId}/start](https://nine524-api-unificado.onrender.com/docs#/Backlog%20%E2%80%94%20stubs/post__api_v1_sessions_sessionId_start_api_v1_sessions__sessionId__start_post) | [\[4.4.2\] \[Backend\] Pasar sesión confirmada a `EN_CURSO`](https://martinporto.atlassian.net/browse/BH95-210) |
| GET | [/api/v1/public/offers/{offerId}](https://nine524-api-unificado.onrender.com/docs#/Backlog%20%E2%80%94%20stubs/get__api_v1_public_offers_offerId__api_v1_public_offers__offerId__get) | [\[1.1.3\] \[Backend\] Consultar detalle público de una propuesta](https://martinporto.atlassian.net/browse/BH95-211) |
| GET | [/api/v1/public/trending](https://nine524-api-unificado.onrender.com/docs#/Backlog%20%E2%80%94%20stubs/get__api_v1_public_trending_api_v1_public_trending_get) | [\[1.2.3\] \[Backend\] Consultar contenido trending](https://martinporto.atlassian.net/browse/BH95-213) |

Los valores entre llaves son parámetros de ruta (por ejemplo, `{userId}`).
Todos los verbos abren su operación en Swagger (`/docs`): usar Try it out y Execute.
Las rutas compartidas por varios tickets aparecen una sola vez.

## Rutas auxiliares

| Verbo | Ruta | Respuesta |
| --- | --- | --- |
| GET | [/](https://nine524-api-unificado.onrender.com/docs#/default/root__get) | Nombre, versión, documentación y lista automática de endpoints. |
| GET | [/health](https://nine524-api-unificado.onrender.com/docs#/default/health_health_get) | Estado de salud de la API. |
| GET | [/api/hello](https://nine524-api-unificado.onrender.com/docs#/default/hello_api_hello_get) | Mensaje de ejemplo. |

## Actualizar este documento

Después de modificar el manifiesto, ejecutar desde la raíz del repositorio:

```powershell
python backend/generate_endpoint_docs.py
```

Incluir el documento regenerado en el mismo commit que el manifiesto.
Los nombres de las tareas se conservan en `backend/backlog_issue_titles.json`.
