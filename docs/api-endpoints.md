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
| GET | `/api/v1/public/offers` | [BH95-166](https://martinporto.atlassian.net/browse/BH95-166) |
| GET | `/api/v1/public/learning-needs` | [BH95-167](https://martinporto.atlassian.net/browse/BH95-167) |
| GET | `/api/v1/public/users/{userId}/reputation` | [BH95-168](https://martinporto.atlassian.net/browse/BH95-168), [BH95-201](https://martinporto.atlassian.net/browse/BH95-201) |
| GET | `/api/v1/public/rankings` | [BH95-169](https://martinporto.atlassian.net/browse/BH95-169) |
| GET | `/api/v1/public/auth-requirement` | [BH95-170](https://martinporto.atlassian.net/browse/BH95-170) |
| POST | `/api/v1/users` | [BH95-170](https://martinporto.atlassian.net/browse/BH95-170) |
| POST | `/api/v1/auth/login` | [BH95-172](https://martinporto.atlassian.net/browse/BH95-172) |
| POST | `/api/v1/auth/logout` | [BH95-172](https://martinporto.atlassian.net/browse/BH95-172) |
| GET | `/api/v1/me/profile` | [BH95-174](https://martinporto.atlassian.net/browse/BH95-174) |
| PATCH | `/api/v1/me/profile` | [BH95-174](https://martinporto.atlassian.net/browse/BH95-174) |
| POST | `/api/v1/teaching-offers` | [BH95-176](https://martinporto.atlassian.net/browse/BH95-176) |
| GET | `/api/v1/teaching-offers/{offerId}` | [BH95-176](https://martinporto.atlassian.net/browse/BH95-176) |
| PATCH | `/api/v1/teaching-offers/{offerId}` | [BH95-176](https://martinporto.atlassian.net/browse/BH95-176) |
| POST | `/api/v1/learning-needs` | [BH95-178](https://martinporto.atlassian.net/browse/BH95-178) |
| GET | `/api/v1/learning-needs/{needId}` | [BH95-178](https://martinporto.atlassian.net/browse/BH95-178) |
| PATCH | `/api/v1/learning-needs/{needId}` | [BH95-178](https://martinporto.atlassian.net/browse/BH95-178) |
| GET | `/api/v1/public/search` | [BH95-180](https://martinporto.atlassian.net/browse/BH95-180), [BH95-182](https://martinporto.atlassian.net/browse/BH95-182) |
| GET | `/api/v1/me/compatibilities` | [BH95-184](https://martinporto.atlassian.net/browse/BH95-184) |
| GET | `/api/v1/me/availability` | [BH95-186](https://martinporto.atlassian.net/browse/BH95-186) |
| POST | `/api/v1/me/availability` | [BH95-186](https://martinporto.atlassian.net/browse/BH95-186) |
| PATCH | `/api/v1/me/availability/{availabilityId}` | [BH95-186](https://martinporto.atlassian.net/browse/BH95-186) |
| DELETE | `/api/v1/me/availability/{availabilityId}` | [BH95-186](https://martinporto.atlassian.net/browse/BH95-186) |
| GET | `/api/v1/public/users/{userId}/availability` | [BH95-188](https://martinporto.atlassian.net/browse/BH95-188), [BH95-216](https://martinporto.atlassian.net/browse/BH95-216) |
| PUT | `/api/v1/me/availability-visibility` | [BH95-189](https://martinporto.atlassian.net/browse/BH95-189) |
| POST | `/api/v1/sessions` | [BH95-190](https://martinporto.atlassian.net/browse/BH95-190), [BH95-207](https://martinporto.atlassian.net/browse/BH95-207) |
| POST | `/api/v1/sessions/{sessionId}/confirm` | [BH95-192](https://martinporto.atlassian.net/browse/BH95-192), [BH95-216](https://martinporto.atlassian.net/browse/BH95-216) |
| POST | `/api/v1/sessions/{sessionId}/cancel` | [BH95-193](https://martinporto.atlassian.net/browse/BH95-193), [BH95-216](https://martinporto.atlassian.net/browse/BH95-216) |
| POST | `/api/v1/sessions/{sessionId}/complete` | [BH95-194](https://martinporto.atlassian.net/browse/BH95-194) |
| POST | `/api/v1/sessions/{sessionId}/credit-transfer` | [BH95-196](https://martinporto.atlassian.net/browse/BH95-196) |
| GET | `/api/v1/me/history` | [BH95-198](https://martinporto.atlassian.net/browse/BH95-198) |
| GET | `/api/v1/me/credit-movements` | [BH95-198](https://martinporto.atlassian.net/browse/BH95-198), [BH95-208](https://martinporto.atlassian.net/browse/BH95-208) |
| POST | `/api/v1/sessions/{sessionId}/ratings` | [BH95-200](https://martinporto.atlassian.net/browse/BH95-200) |
| POST | `/api/v1/reports` | [BH95-202](https://martinporto.atlassian.net/browse/BH95-202) |
| GET | `/api/v1/admin/users` | [BH95-204](https://martinporto.atlassian.net/browse/BH95-204) |
| GET | `/api/v1/admin/teaching-offers` | [BH95-204](https://martinporto.atlassian.net/browse/BH95-204) |
| GET | `/api/v1/admin/reports` | [BH95-204](https://martinporto.atlassian.net/browse/BH95-204) |
| POST | `/api/v1/admin/users/{userId}/suspend` | [BH95-205](https://martinporto.atlassian.net/browse/BH95-205) |
| POST | `/api/v1/admin/users/{userId}/reactivate` | [BH95-205](https://martinporto.atlassian.net/browse/BH95-205) |
| POST | `/api/v1/me/availability/batch` | [BH95-206](https://martinporto.atlassian.net/browse/BH95-206) |
| GET | `/api/v1/me/credit-balance` | [BH95-208](https://martinporto.atlassian.net/browse/BH95-208) |
| POST | `/api/v1/admin/teaching-offers/{offerId}/hide` | [BH95-209](https://martinporto.atlassian.net/browse/BH95-209) |
| POST | `/api/v1/sessions/{sessionId}/start` | [BH95-210](https://martinporto.atlassian.net/browse/BH95-210) |
| GET | `/api/v1/public/offers/{offerId}` | [BH95-211](https://martinporto.atlassian.net/browse/BH95-211) |
| GET | `/api/v1/public/trending` | [BH95-213](https://martinporto.atlassian.net/browse/BH95-213) |

Los valores entre llaves son parámetros de ruta (por ejemplo, `{userId}`).
Las rutas compartidas por varios tickets aparecen una sola vez.

## Rutas auxiliares

| Verbo | Ruta | Respuesta |
| --- | --- | --- |
| GET | `/` | Nombre, versión, documentación y lista automática de endpoints. |
| GET | `/health` | Estado de salud de la API. |
| GET | `/api/hello` | Mensaje de ejemplo. |

## Actualizar este documento

Después de modificar el manifiesto, ejecutar desde la raíz del repositorio:

```powershell
python backend/generate_endpoint_docs.py
```

Incluir el documento regenerado en el mismo commit que el manifiesto.
