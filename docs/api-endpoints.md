# Endpoints de la API

Listado generado desde [`backend/backlog_endpoints.json`](../backend/backlog_endpoints.json).

Las 44 combinaciones de verbo y ruta del backlog son **stubs**:
devuelven `{}` con **200 OK**, sin lógica, autenticación ni persistencia.
Esto no implica que las tareas de Jira estén completadas.

- [API e índice actualizado](https://nine524-api.onrender.com/).
- [Documentación interactiva y parámetros](https://nine524-api.onrender.com/docs).
- [Contrato OpenAPI JSON](https://nine524-api.onrender.com/openapi.json).

## Rutas del backlog

| Verbo | Ruta | Tickets de Jira |
| --- | --- | --- |
| GET | [/api/v1/public/offers](https://nine524-api.onrender.com/api/v1/public/offers) | [BH95-166](https://martinporto.atlassian.net/browse/BH95-166) |
| GET | [/api/v1/public/learning-needs](https://nine524-api.onrender.com/api/v1/public/learning-needs) | [BH95-167](https://martinporto.atlassian.net/browse/BH95-167) |
| GET | [/api/v1/public/users/{userId}/reputation](https://nine524-api.onrender.com/api/v1/public/users/demo-id/reputation) | [BH95-168](https://martinporto.atlassian.net/browse/BH95-168), [BH95-201](https://martinporto.atlassian.net/browse/BH95-201) |
| GET | [/api/v1/public/rankings](https://nine524-api.onrender.com/api/v1/public/rankings) | [BH95-169](https://martinporto.atlassian.net/browse/BH95-169) |
| GET | [/api/v1/public/auth-requirement](https://nine524-api.onrender.com/api/v1/public/auth-requirement) | [BH95-170](https://martinporto.atlassian.net/browse/BH95-170) |
| POST | [/api/v1/users](https://nine524-api.onrender.com/docs#/Backlog%20%E2%80%94%20stubs/post__api_v1_users_api_v1_users_post) | [BH95-170](https://martinporto.atlassian.net/browse/BH95-170) |
| POST | [/api/v1/auth/login](https://nine524-api.onrender.com/docs#/Backlog%20%E2%80%94%20stubs/post__api_v1_auth_login_api_v1_auth_login_post) | [BH95-172](https://martinporto.atlassian.net/browse/BH95-172) |
| POST | [/api/v1/auth/logout](https://nine524-api.onrender.com/docs#/Backlog%20%E2%80%94%20stubs/post__api_v1_auth_logout_api_v1_auth_logout_post) | [BH95-172](https://martinporto.atlassian.net/browse/BH95-172) |
| GET | [/api/v1/me/profile](https://nine524-api.onrender.com/api/v1/me/profile) | [BH95-174](https://martinporto.atlassian.net/browse/BH95-174) |
| PATCH | [/api/v1/me/profile](https://nine524-api.onrender.com/docs#/Backlog%20%E2%80%94%20stubs/patch__api_v1_me_profile_api_v1_me_profile_patch) | [BH95-174](https://martinporto.atlassian.net/browse/BH95-174) |
| POST | [/api/v1/teaching-offers](https://nine524-api.onrender.com/docs#/Backlog%20%E2%80%94%20stubs/post__api_v1_teaching_offers_api_v1_teaching_offers_post) | [BH95-176](https://martinporto.atlassian.net/browse/BH95-176) |
| GET | [/api/v1/teaching-offers/{offerId}](https://nine524-api.onrender.com/api/v1/teaching-offers/demo-id) | [BH95-176](https://martinporto.atlassian.net/browse/BH95-176) |
| PATCH | [/api/v1/teaching-offers/{offerId}](https://nine524-api.onrender.com/docs#/Backlog%20%E2%80%94%20stubs/patch__api_v1_teaching_offers_offerId__api_v1_teaching_offers__offerId__patch) | [BH95-176](https://martinporto.atlassian.net/browse/BH95-176) |
| POST | [/api/v1/learning-needs](https://nine524-api.onrender.com/docs#/Backlog%20%E2%80%94%20stubs/post__api_v1_learning_needs_api_v1_learning_needs_post) | [BH95-178](https://martinporto.atlassian.net/browse/BH95-178) |
| GET | [/api/v1/learning-needs/{needId}](https://nine524-api.onrender.com/api/v1/learning-needs/demo-id) | [BH95-178](https://martinporto.atlassian.net/browse/BH95-178) |
| PATCH | [/api/v1/learning-needs/{needId}](https://nine524-api.onrender.com/docs#/Backlog%20%E2%80%94%20stubs/patch__api_v1_learning_needs_needId__api_v1_learning_needs__needId__patch) | [BH95-178](https://martinporto.atlassian.net/browse/BH95-178) |
| GET | [/api/v1/public/search](https://nine524-api.onrender.com/api/v1/public/search) | [BH95-180](https://martinporto.atlassian.net/browse/BH95-180), [BH95-182](https://martinporto.atlassian.net/browse/BH95-182) |
| GET | [/api/v1/me/compatibilities](https://nine524-api.onrender.com/api/v1/me/compatibilities) | [BH95-184](https://martinporto.atlassian.net/browse/BH95-184) |
| GET | [/api/v1/me/availability](https://nine524-api.onrender.com/api/v1/me/availability) | [BH95-186](https://martinporto.atlassian.net/browse/BH95-186) |
| POST | [/api/v1/me/availability](https://nine524-api.onrender.com/docs#/Backlog%20%E2%80%94%20stubs/post__api_v1_me_availability_api_v1_me_availability_post) | [BH95-186](https://martinporto.atlassian.net/browse/BH95-186) |
| PATCH | [/api/v1/me/availability/{availabilityId}](https://nine524-api.onrender.com/docs#/Backlog%20%E2%80%94%20stubs/patch__api_v1_me_availability_availabilityId__api_v1_me_availability__availabilityId__patch) | [BH95-186](https://martinporto.atlassian.net/browse/BH95-186) |
| DELETE | [/api/v1/me/availability/{availabilityId}](https://nine524-api.onrender.com/docs#/Backlog%20%E2%80%94%20stubs/delete__api_v1_me_availability_availabilityId__api_v1_me_availability__availabilityId__delete) | [BH95-186](https://martinporto.atlassian.net/browse/BH95-186) |
| GET | [/api/v1/public/users/{userId}/availability](https://nine524-api.onrender.com/api/v1/public/users/demo-id/availability) | [BH95-188](https://martinporto.atlassian.net/browse/BH95-188), [BH95-216](https://martinporto.atlassian.net/browse/BH95-216) |
| PUT | [/api/v1/me/availability-visibility](https://nine524-api.onrender.com/docs#/Backlog%20%E2%80%94%20stubs/put__api_v1_me_availability_visibility_api_v1_me_availability_visibility_put) | [BH95-189](https://martinporto.atlassian.net/browse/BH95-189) |
| POST | [/api/v1/sessions](https://nine524-api.onrender.com/docs#/Backlog%20%E2%80%94%20stubs/post__api_v1_sessions_api_v1_sessions_post) | [BH95-190](https://martinporto.atlassian.net/browse/BH95-190), [BH95-207](https://martinporto.atlassian.net/browse/BH95-207) |
| POST | [/api/v1/sessions/{sessionId}/confirm](https://nine524-api.onrender.com/docs#/Backlog%20%E2%80%94%20stubs/post__api_v1_sessions_sessionId_confirm_api_v1_sessions__sessionId__confirm_post) | [BH95-192](https://martinporto.atlassian.net/browse/BH95-192), [BH95-216](https://martinporto.atlassian.net/browse/BH95-216) |
| POST | [/api/v1/sessions/{sessionId}/cancel](https://nine524-api.onrender.com/docs#/Backlog%20%E2%80%94%20stubs/post__api_v1_sessions_sessionId_cancel_api_v1_sessions__sessionId__cancel_post) | [BH95-193](https://martinporto.atlassian.net/browse/BH95-193), [BH95-216](https://martinporto.atlassian.net/browse/BH95-216) |
| POST | [/api/v1/sessions/{sessionId}/complete](https://nine524-api.onrender.com/docs#/Backlog%20%E2%80%94%20stubs/post__api_v1_sessions_sessionId_complete_api_v1_sessions__sessionId__complete_post) | [BH95-194](https://martinporto.atlassian.net/browse/BH95-194) |
| POST | [/api/v1/sessions/{sessionId}/credit-transfer](https://nine524-api.onrender.com/docs#/Backlog%20%E2%80%94%20stubs/post__api_v1_sessions_sessionId_credit_transfer_api_v1_sessions__sessionId__credit_transfer_post) | [BH95-196](https://martinporto.atlassian.net/browse/BH95-196) |
| GET | [/api/v1/me/history](https://nine524-api.onrender.com/api/v1/me/history) | [BH95-198](https://martinporto.atlassian.net/browse/BH95-198) |
| GET | [/api/v1/me/credit-movements](https://nine524-api.onrender.com/api/v1/me/credit-movements) | [BH95-198](https://martinporto.atlassian.net/browse/BH95-198), [BH95-208](https://martinporto.atlassian.net/browse/BH95-208) |
| POST | [/api/v1/sessions/{sessionId}/ratings](https://nine524-api.onrender.com/docs#/Backlog%20%E2%80%94%20stubs/post__api_v1_sessions_sessionId_ratings_api_v1_sessions__sessionId__ratings_post) | [BH95-200](https://martinporto.atlassian.net/browse/BH95-200) |
| POST | [/api/v1/reports](https://nine524-api.onrender.com/docs#/Backlog%20%E2%80%94%20stubs/post__api_v1_reports_api_v1_reports_post) | [BH95-202](https://martinporto.atlassian.net/browse/BH95-202) |
| GET | [/api/v1/admin/users](https://nine524-api.onrender.com/api/v1/admin/users) | [BH95-204](https://martinporto.atlassian.net/browse/BH95-204) |
| GET | [/api/v1/admin/teaching-offers](https://nine524-api.onrender.com/api/v1/admin/teaching-offers) | [BH95-204](https://martinporto.atlassian.net/browse/BH95-204) |
| GET | [/api/v1/admin/reports](https://nine524-api.onrender.com/api/v1/admin/reports) | [BH95-204](https://martinporto.atlassian.net/browse/BH95-204) |
| POST | [/api/v1/admin/users/{userId}/suspend](https://nine524-api.onrender.com/docs#/Backlog%20%E2%80%94%20stubs/post__api_v1_admin_users_userId_suspend_api_v1_admin_users__userId__suspend_post) | [BH95-205](https://martinporto.atlassian.net/browse/BH95-205) |
| POST | [/api/v1/admin/users/{userId}/reactivate](https://nine524-api.onrender.com/docs#/Backlog%20%E2%80%94%20stubs/post__api_v1_admin_users_userId_reactivate_api_v1_admin_users__userId__reactivate_post) | [BH95-205](https://martinporto.atlassian.net/browse/BH95-205) |
| POST | [/api/v1/me/availability/batch](https://nine524-api.onrender.com/docs#/Backlog%20%E2%80%94%20stubs/post__api_v1_me_availability_batch_api_v1_me_availability_batch_post) | [BH95-206](https://martinporto.atlassian.net/browse/BH95-206) |
| GET | [/api/v1/me/credit-balance](https://nine524-api.onrender.com/api/v1/me/credit-balance) | [BH95-208](https://martinporto.atlassian.net/browse/BH95-208) |
| POST | [/api/v1/admin/teaching-offers/{offerId}/hide](https://nine524-api.onrender.com/docs#/Backlog%20%E2%80%94%20stubs/post__api_v1_admin_teaching_offers_offerId_hide_api_v1_admin_teaching_offers__offerId__hide_post) | [BH95-209](https://martinporto.atlassian.net/browse/BH95-209) |
| POST | [/api/v1/sessions/{sessionId}/start](https://nine524-api.onrender.com/docs#/Backlog%20%E2%80%94%20stubs/post__api_v1_sessions_sessionId_start_api_v1_sessions__sessionId__start_post) | [BH95-210](https://martinporto.atlassian.net/browse/BH95-210) |
| GET | [/api/v1/public/offers/{offerId}](https://nine524-api.onrender.com/api/v1/public/offers/demo-id) | [BH95-211](https://martinporto.atlassian.net/browse/BH95-211) |
| GET | [/api/v1/public/trending](https://nine524-api.onrender.com/api/v1/public/trending) | [BH95-213](https://martinporto.atlassian.net/browse/BH95-213) |

Los valores entre llaves son parámetros de ruta (por ejemplo, `{userId}`).
Los enlaces GET abren la API usando `demo-id` como identificador de ejemplo.
Los demás verbos abren su operación en `/docs`: usar Try it out y Execute.
Las rutas compartidas por varios tickets aparecen una sola vez.

## Rutas auxiliares

| Verbo | Ruta | Respuesta |
| --- | --- | --- |
| GET | [/](https://nine524-api.onrender.com/) | Nombre, versión, documentación y lista automática de endpoints. |
| GET | [/health](https://nine524-api.onrender.com/health) | Estado de salud de la API. |
| GET | [/api/hello](https://nine524-api.onrender.com/api/hello) | Mensaje de ejemplo. |

## Actualizar este documento

Después de modificar el manifiesto, ejecutar desde la raíz del repositorio:

```powershell
python backend/generate_endpoint_docs.py
```

Incluir el documento regenerado en el mismo commit que el manifiesto.
