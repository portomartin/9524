# Especificación Técnica de API (Mini-SDD) — Proyecto WBS Clásico

**Proyecto Jira:** `WBSO` — *WBS Original Histórico*  
**Fuente de verdad del alcance:** [`proyecto-wbs/wbs-original.md`](../wbs-original.md) y [`proyecto-wbs/jerarquia-jira.md`](../jerarquia-jira.md).  
**Propósito:** Definir los contratos HTTP, estructuras de datos y endpoints mock correspondientes a cada tarea y subtarea del tablero Jira WBS, permitiendo al frontend independiente interactuar con respuestas exitosas (200 OK) y datos de muestra sin requerir persistencia compleja.

---

## 1. Principios de Diseño de la API Mock

1. **Respuestas 200 OK garantizadas:** Todos los endpoints responden con estado HTTP 200 y estructuras JSON válidas para facilitar las pruebas del frontend.
2. **Tolerancia a payloads de entrada:** Los endpoints de mutación (`POST`, `PUT`, `PATCH`) aceptan cualquier payload sin fallar con errores de validación (`extra='allow'`).
3. **CORS universal:** Habilitado para cualquier origen (`*`), permitiendo conectar cualquier frontend local o desplegado sin bloqueos de navegador.
4. **Trazabilidad 1:1 con Jira:** Cada endpoint y ruta está etiquetado con su Historia de Usuario (`1.3` a `1.12`) y sus identificadores de Jira `WBSO-xxx`.

---

## 2. Mapa de Endpoints y Trazabilidad Jira

### HU [1.3] Sistema de Usuarios (`WBSO-7`)

| Verbo | Ruta | Tickets Jira | Descripción / Mock Response |
|---|---|---|---|
| `POST` | `/api/v1/auth/register` | `WBSO-33` [1.3.1] | Registro de usuario. Retorna usuario creado y token dummy. |
| `POST` | `/api/v1/auth/login` | `WBSO-34` [1.3.2] | Inicio de sesión con credenciales. Retorna token y perfil básico. |
| `POST` | `/api/v1/auth/logout` | `WBSO-34` [1.3.2] | Cierre de sesión. Retorna confirmación. |
| `POST` | `/api/v1/auth/recover-password` | `WBSO-35` [1.3.3] | Envío de email/código de recuperación. |
| `GET` | `/api/v1/users/me` | `WBSO-36` [1.3.4], `WBSO-38` [1.3.5], `WBSO-39` [1.3.6], `WBSO-42` [1.3.7], `WBSO-41` [1.3.8] | Perfil completo del usuario (nombre, temas para enseñar, temas para aprender, nivel, modalidad). |
| `PUT` | `/api/v1/users/me` | `WBSO-36` [1.3.4], `WBSO-38` [1.3.5], `WBSO-39` [1.3.6], `WBSO-42` [1.3.7], `WBSO-41` [1.3.8] | Actualización de perfil, temas, nivel y modalidad preferida. |
| `GET` | `/api/v1/users/me/availability` | `WBSO-37` [1.3.9] | Franjas horarias configuradas por el usuario. |
| `POST` | `/api/v1/users/me/availability` | `WBSO-37` [1.3.9] | Agregar franja de disponibilidad horaria. |
| `GET` | `/api/v1/users/me/credits` | `WBSO-40` [1.3.10] | Consulta de saldo de créditos virtuales actual. |

---

### HU [1.4] Sistema de Publicaciones (`WBSO-8`)

| Verbo | Ruta | Tickets Jira | Descripción / Mock Response |
|---|---|---|---|
| `GET` | `/api/v1/categories` | `WBSO-44` [1.4.2] | Catálogo de categorías disponibles (Tecnología, Idiomas, Arte, etc.). |
| `GET` | `/api/v1/publications` | `WBSO-43` [1.4.1], `WBSO-52` [1.4.8] | Listado de publicaciones activas con paginación dummy. |
| `POST` | `/api/v1/publications` | `WBSO-43` [1.4.1], `WBSO-45` [1.4.3], `WBSO-46` [1.4.4], `WBSO-47` [1.4.5], `WBSO-49` [1.4.6], `WBSO-50` [1.4.7], `WBSO-48` [1.4.9] | Crear nueva publicación (descripción, nivel, modalidad, duración, créditos). |
| `GET` | `/api/v1/publications/{id}` | `WBSO-45` [1.4.3], `WBSO-52` [1.4.8] | Detalle de publicación por identificador. |
| `PUT` | `/api/v1/publications/{id}` | `WBSO-52` [1.4.8] | Modificar publicación existente. |
| `DELETE` | `/api/v1/publications/{id}` | `WBSO-52` [1.4.8] | Eliminar o despublicar propuesta. |

---

### HU [1.5] Sistema de Búsqueda y Compatibilidad (`WBSO-9`)

| Verbo | Ruta | Tickets Jira | Descripción / Mock Response |
|---|---|---|---|
| `GET` | `/api/v1/search` | `WBSO-51` [1.5.1], `WBSO-53` [1.5.2], `WBSO-54` [1.5.3] | Búsqueda con filtros (texto `q`, `category`, `level`, `modality`). |
| `GET` | `/api/v1/compatibilities` | `WBSO-55` [1.5.4], `WBSO-56` [1.5.5], `WBSO-57` [1.5.6], `WBSO-58` [1.5.7] | Perfiles compatibles calculados, detección de horarios comunes e intercambios recíprocos. |

---

### HU [1.6] Sistema de Solicitudes y Sesiones (`WBSO-10`)

| Verbo | Ruta | Tickets Jira | Descripción / Mock Response |
|---|---|---|---|
| `POST` | `/api/v1/requests` | `WBSO-59` [1.6.1] | Enviar solicitud de intercambio/sesión a otro usuario. |
| `GET` | `/api/v1/requests/received` | `WBSO-60` [1.6.2], `WBSO-62` [1.6.4] | Listado de solicitudes recibidas por el usuario. |
| `GET` | `/api/v1/requests/sent` | `WBSO-61` [1.6.3], `WBSO-62` [1.6.4] | Listado de solicitudes enviadas por el usuario. |
| `PATCH` | `/api/v1/requests/{id}/status` | `WBSO-62` [1.6.4] | Cambiar estado de solicitud (`ACEPTADA`, `RECHAZADA`, `CANCELADA`). |
| `GET` | `/api/v1/sessions` | `WBSO-63` [1.6.5], `WBSO-64` [1.6.6], `WBSO-65` [1.6.7] | Agenda de sesiones pactadas (fechas, horas, modalidad). |
| `POST` | `/api/v1/sessions/{id}/complete` | `WBSO-66` [1.6.8] | Confirmar que una sesión ha sido completada. |
| `GET` | `/api/v1/sessions/conflicts-check` | `WBSO-67` [1.6.9] | Validación de superposición de horarios. |

---

### HU [1.7] Sistema de Créditos Virtuales (`WBSO-11`)

| Verbo | Ruta | Tickets Jira | Descripción / Mock Response |
|---|---|---|---|
| `GET` | `/api/v1/credits/balance` | `WBSO-68` [1.7.1], `WBSO-69` [1.7.2] | Saldo total y desglose de créditos disponibles. |
| `POST` | `/api/v1/credits/reserve` | `WBSO-70` [1.7.3] | Bloqueo/reserva de crédito al iniciar solicitud. |
| `POST` | `/api/v1/credits/transfer` | `WBSO-71` [1.7.4], `WBSO-74` [1.7.7], `WBSO-75` [1.7.8] | Transferencia final de crédito tras completar sesión. |
| `POST` | `/api/v1/credits/cancel-hold` | `WBSO-72` [1.7.5] | Liberación de crédito por cancelación de sesión. |
| `GET` | `/api/v1/credits/movements` | `WBSO-73` [1.7.6] | Libro mayor/historial de movimientos de créditos. |

---

### HU [1.8] Sistema de Historial (`WBSO-12`)

| Verbo | Ruta | Tickets Jira | Descripción / Mock Response |
|---|---|---|---|
| `GET` | `/api/v1/history/summary` | `WBSO-76` [1.8.1] a `WBSO-81` [1.8.6] | Vista consolidada de historial de solicitudes, sesiones, enseñanzas y créditos. |
| `GET` | `/api/v1/history/sessions` | `WBSO-77` [1.8.2], `WBSO-78` [1.8.3], `WBSO-79` [1.8.4] | Historial detallado de sesiones enseñadas y aprendidas. |

---

### HU [1.9] Sistema de Calificaciones y Reputación (`WBSO-13`)

| Verbo | Ruta | Tickets Jira | Descripción / Mock Response |
|---|---|---|---|
| `POST` | `/api/v1/ratings` | `WBSO-82` [1.9.1], `WBSO-83` [1.9.2], `WBSO-84` [1.9.3], `WBSO-87` [1.9.6], `WBSO-88` [1.9.7] | Registrar calificación (1 a 5 estrellas) y comentario para una sesión. |
| `GET` | `/api/v1/users/{userId}/reputation` | `WBSO-85` [1.9.4], `WBSO-86` [1.9.5] | Consulta de puntaje promedio y reseñas públicas del usuario. |

---

### HU [1.10] Sistema de Notificaciones (`WBSO-14`)

| Verbo | Ruta | Tickets Jira | Descripción / Mock Response |
|---|---|---|---|
| `GET` | `/api/v1/notifications` | `WBSO-89` [1.10.1] a `WBSO-95` [1.10.7] | Lista de alertas (solicitudes, cancelaciones, cambios de horario, créditos, etc.). |
| `PATCH` | `/api/v1/notifications/{id}/read` | `WBSO-89` [1.10.1] a `WBSO-95` [1.10.7] | Marcar notificación como leída. |

---

### HU [1.11] Sistema de Seguridad y Moderación (`WBSO-17`)

| Verbo | Ruta | Tickets Jira | Descripción / Mock Response |
|---|---|---|---|
| `GET` | `/api/v1/security/categories` | `WBSO-96` [1.11.1] | Categorías formales admitidas por la política del sistema. |
| `GET` | `/api/v1/security/prohibited-words` | `WBSO-97` [1.11.2], `WBSO-98` [1.11.3] | Diccionario de términos no admitidos para validación de contenido. |
| `POST` | `/api/v1/reports` | `WBSO-99` [1.11.4], `WBSO-100` [1.11.5] | Crear denuncia sobre una publicación o conducta de usuario. |
| `GET` | `/api/v1/legal/terms` | `WBSO-101` [1.11.6], `WBSO-103` [1.11.8] | Términos y condiciones y política de datos personales. |

---

### HU [1.12] Panel de Administración (`WBSO-15`)

| Verbo | Ruta | Tickets Jira | Descripción / Mock Response |
|---|---|---|---|
| `GET` | `/api/v1/admin/users` | `WBSO-104` [1.12.1] | Listado de usuarios del sistema con estado administrativo. |
| `GET` | `/api/v1/admin/publications` | `WBSO-106` [1.12.2] | Listado general de publicaciones para moderación. |
| `GET` | `/api/v1/admin/reports` | `WBSO-105` [1.12.3] | Registro de denuncias pendientes de resolución. |
| `PATCH` | `/api/v1/admin/users/{userId}/status` | `WBSO-107` [1.12.4] | Suspender o reactivar cuentas de usuario. |
| `POST` | `/api/v1/admin/categories` | `WBSO-108` [1.12.5] | Crear o modificar categorías administradas. |
| `POST` | `/api/v1/admin/prohibited-words` | `WBSO-109` [1.12.6] | Administrar lista de palabras prohibidas. |
| `GET` | `/api/v1/admin/audit-log` | `WBSO-110` [1.12.7] | Registro de auditoría de decisiones tomadas por moderadores. |

---

## 3. Ejecución del Servidor Mock

El servidor mock está implementado en `proyecto-wbs/backend/main.py`.

```bash
# Desde la carpeta proyecto-wbs/backend/
pip install -r requirements.txt
uvicorn main:app --port 8000 --reload
```

- **Documentación Swagger UI:** `http://localhost:8000/docs`
- **Especificación OpenAPI JSON:** `http://localhost:8000/openapi.json`
- **Endpoint Healthcheck:** `http://localhost:8000/health`
