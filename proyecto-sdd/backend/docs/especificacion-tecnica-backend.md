# Especificación Técnica de Backend — Intercambia (MVP V3)

**Estado:** Aprobada y vinculante para el desarrollo del backend.  
**Fuente funcional:** [`proyecto-sdd/docs/mvp-v3.md`](../../docs/mvp-v3.md)  
**Convenciones base:** [`proyecto-sdd/backend/skills/convenciones-backend/SKILL.md`](../skills/convenciones-backend/SKILL.md)  
**Catálogo de rutas del backlog:** [`proyecto-sdd/backend/backlog_endpoints.json`](../backlog_endpoints.json)

---

## 1. Stack Tecnológico y Persistencia Dual

| Componente | Tecnología | Justificación |
| :--- | :--- | :--- |
| **Framework Web** | **FastAPI** | Alto rendimiento, validación automática con tipos de Python y documentación OpenAPI/Swagger interactiva. |
| **ORM / Acceso a Datos** | **SQLModel** (SQLAlchemy + Pydantic) | Creado por el autor de FastAPI. Unifica la validación de esquemas HTTP con los modelos relacionales de BD en una sola clase. |
| **Entorno Local** | **SQLite** (`sqlite:///./app.db`) | Sin dependencias externas ni instalación de servidores de BD en local. |
| **Entorno Cloud (Render)** | **PostgreSQL** (`DATABASE_URL`) | Persistencia real en la nube sin pérdida de datos en el reinicio del contenedor efímero de Render. |
| **Gestión de Entorno** | `pydantic-settings` / `os.getenv` | Selección automática de motor: si existe `DATABASE_URL`, usa PostgreSQL; caso contrario, usa SQLite local. |

---

## 2. Patrón de Arquitectura: Layered Architecture (En Capas)

El código de `proyecto-sdd/backend/` se organiza en 4 capas estrictas para garantizar desacoplamiento y testeabilidad:

```text
proyecto-sdd/backend/
├── app/
│   ├── config.py           # Variables de entorno y configuración de conexión
│   ├── database.py         # Engine de SQLModel y dependency get_db()
│   ├── models/             # Tablas relacionales y esquemas SQLModel
│   │   ├── user.py
│   │   ├── offer.py
│   │   ├── need.py
│   │   ├── availability.py
│   │   ├── session.py
│   │   ├── credit.py
│   │   └── review.py
│   ├── repositories/       # Consultas directas a la base de datos (CRUD)
│   ├── services/           # Lógica de negocio, reglas de dominio y transacciones
│   ├── routers/            # Endpoints HTTP REST (/api/v1/...) delgados
│   └── security.py         # Hashing de passwords y generación/validación de tokens
├── main.py                 # Punto de entrada de la aplicación FastAPI
└── requirements.txt        # Dependencias de Python
```

### Reglas entre capas:
1. **Routers:** Solo reciben requests HTTP, validan parámetros de entrada con SQLModel/Pydantic, inyectan dependencias y devuelven respuestas JSON con los códigos de estado HTTP apropiados (`200`, `201`, `404`, etc.).
2. **Services:** Contienen toda la lógica de validación de negocio (ej. verificar si el usuario tiene crédito suficiente antes de pedir una sesión, compatibilidad, transición de estados).
3. **Repositories:** Solo ejecutan queries contra la sesión de base de datos (`session.exec(...)`, `session.add(...)`).
4. **Models:** Clases de SQLModel (`table=True` para tablas físicas y sin `table=True` para DTOs/schemas de request y response).

---

## 3. Modelo Físico de Base de Datos (SQLModel)

### 3.1 `User` (Usuarios y Perfiles)
* `id`: `str` (UUID o prefijo `usr-*`, Primary Key)
* `email`: `str` (Unique, Indexed)
* `password_hash`: `str` (Hash con bcrypt/argon2; nunca texto plano)
* `name`: `str`
* `description`: `str` (opcional)
* `role`: `str` (Default `'USER'`; reservado `'ADMIN'`)
* `general_location`: `str` (opcional)
* `teaching_topics`: `str` (JSON serializado con lista de strings)
* `learning_topics`: `str` (JSON serializado con lista de strings)
* `credit_balance`: `int` (Default `1`, balance inicial de cortesía)
* `is_active`: `bool` (Default `True`)
* `created_at`: `datetime`

### 3.2 `TeachingOffer` (Propuestas de Enseñanza)
* `id`: `str` (Primary Key, prefijo `offer-*`)
* `user_id`: `str` (Foreign Key -> `User.id`)
* `title`: `str`
* `description`: `str`
* `category`: `str`
* `level`: `str` (`Inicial`, `Intermedio`, `Avanzado`)
* `modality`: `str` (`Virtual`, `Presencial`)
* `duration_minutes`: `int` (Default `60`)
* `status`: `str` (`ACTIVE`, `PAUSED`, `ARCHIVED`)
* `created_at`: `datetime`

### 3.3 `LearningNeed` (Aprendizajes Buscados)
* `id`: `str` (Primary Key, prefijo `need-*`)
* `user_id`: `str` (Foreign Key -> `User.id`)
* `title`: `str`
* `description`: `str`
* `category`: `str`
* `level`: `str`
* `modality`: `str`
* `status`: `str` (`ACTIVE`, `PAUSED`, `ARCHIVED`)
* `created_at`: `datetime`

### 3.4 `AvailabilitySlot` (Agenda de Disponibilidad)
* `id`: `str` (Primary Key, prefijo `slot-*`)
* `user_id`: `str` (Foreign Key -> `User.id`)
* `date`: `str` (`YYYY-MM-DD`)
* `start_time`: `str` (`HH:MM`)
* `duration_minutes`: `int` (Mínimo 60 min según MVP V3)
* `is_booked`: `bool` (Default `False`)
* `is_public`: `bool` (Default `True`)
* `created_at`: `datetime`

### 3.5 `ExchangeSession` (Sesiones de Intercambio)
* `id`: `str` (Primary Key, prefijo `ses-*`)
* `offer_id`: `str` (Foreign Key -> `TeachingOffer.id`, opcional si es necesidad directa)
* `teacher_id`: `str` (Foreign Key -> `User.id`)
* `student_id`: `str` (Foreign Key -> `User.id`)
* `date`: `str` (`YYYY-MM-DD`)
* `start_time`: `str` (`HH:MM`)
* `duration_minutes`: `int`
* `modality`: `str`
* `exchange_type`: `str` (`RECIPROCAL` o `CREDITS`)
* `credit_cost`: `int` (1 si es por créditos, 0 si es recíproco)
* `status`: `str` (`SOLICITADA`, `ACEPTADA`, `FINALIZADA`, `CANCELADA`)
* `rated`: `bool` (Default `False`)
* `created_at`: `datetime`

### 3.6 `CreditMovement` (Libro Mayor de Créditos)
* `id`: `str` (Primary Key, prefijo `mov-*`)
* `user_id`: `str` (Foreign Key -> `User.id`)
* `session_id`: `str` (Foreign Key -> `ExchangeSession.id`, opcional)
* `amount`: `int` (Positivo o negativo: +1, -1)
* `balance_after`: `int`
* `reason`: `str` (`INITIAL_GRANT`, `SESSION_PAYMENT`, `SESSION_EARNING`, `REFUND`)
* `created_at`: `datetime`

### 3.7 `Review` (Calificaciones y Reputación)
* `id`: `str` (Primary Key, prefijo `rev-*`)
* `session_id`: `str` (Foreign Key -> `ExchangeSession.id`)
* `reviewer_id`: `str` (Foreign Key -> `User.id`)
* `reviewee_id`: `str` (Foreign Key -> `User.id`)
* `rating`: `int` (1 a 5 estrellas)
* `comment`: `str` (opcional)
* `created_at`: `datetime`

---

## 4. Reglas Críticas de Negocio e Integridad Transaccional

1. **Unicidad del Rol:** No existen tablas separadas de Profesores y Alumnos. El usuario siempre es `USER`.
2. **Ciclo de Estados de Sesión:**
   ```text
   [SOLICITADA] ──(Aceptar)──> [ACEPTADA] ──(Completar)──> [FINALIZADA]
        │                           │
        └──(Rechazar/Cancelar)──────┴──(Cancelar)────────> [CANCELADA]
   ```
3. **Transacción Atómica de Créditos (Unit of Work):**
   Al transicionar una sesión a `FINALIZADA` con `exchange_type == 'CREDITS'`:
   * Se ejecuta en un único bloque transaccional (`session.begin()`):
     1. Actualizar `ExchangeSession.status = 'FINALIZADA'`.
     2. `Student.credit_balance -= 1`.
     3. `Teacher.credit_balance += 1`.
     4. Insertar 2 registros en `CreditMovement` (uno de egreso para el alumno y uno de ingreso para el profesor).
   * Si cualquiera falla, se hace rollback total.
4. **Idempotencia:**
   El endpoint `/api/v1/sessions/{sessionId}/credit-transfer` no debe permitir transferir dos veces sobre una sesión ya finalizada.

---

## 5. Formato Estándar de Respuesta de Errores

En caso de validación fallida o conflicto de negocio, se devuelve la estructura requerida por el skill de convenciones:
```json
{
  "code": "INSUFFICIENT_CREDITS",
  "message": "No cuentas con créditos suficientes para solicitar esta sesión.",
  "fields": {}
}
```

---

## 6. Fases de Implementación Incremental Equilibradas (~20% cada una)

* **Fase 1: Infraestructura y Datos Semilla (~20%)**  
  * Conexión dual de BD con SQLModel (SQLite local `sqlite:///./app.db` y PostgreSQL `DATABASE_URL` en Render).
  * Creación física de tablas relacionales.
  * Script `seed.py` para cargar los datos iniciales de prueba (idénticos a `mockData.js`).
  * Integración inicial de `get_db` en FastAPI sin alterar stubs.

* **Fase 2: Catálogo y Búsqueda Pública (~20%)**  
  * Reemplazo de stubs de lectura pública por queries reales de base de datos:
    * `GET /api/v1/public/offers` y detalle `GET /api/v1/teaching-offers/{offerId}`
    * `GET /api/v1/public/learning-needs` y detalle `GET /api/v1/learning-needs/{needId}`
    * `GET /api/v1/public/search` (búsqueda y filtros por categoría/modalidad)
    * `GET /api/v1/public/rankings` y reputación `GET /api/v1/public/users/{userId}/reputation`

* **Fase 3: Cuentas, Autenticación y Gestión de Propuestas (~20%)**  
  * Hashing seguro de passwords y generación/validación de tokens JWT.
  * Endpoints de registro y login: `POST /api/v1/users`, `POST /api/v1/auth/login`, `POST /api/v1/auth/logout`.
  * Perfil autenticado: `GET /api/v1/me/profile`, `PATCH /api/v1/me/profile`.
  * Publicación y edición de propuestas propias:
    * `POST /api/v1/teaching-offers` y `PATCH /api/v1/teaching-offers/{offerId}`
    * `POST /api/v1/learning-needs` y `PATCH /api/v1/learning-needs/{needId}`

* **Fase 4: Agenda y Franjas de Disponibilidad (~20%)**  
  * Gestión de franjas horarias privadas del usuario:
    * `GET /api/v1/me/availability`
    * `POST /api/v1/me/availability` (mínimo 1 hora por franja según MVP V3)
    * `PATCH /api/v1/me/availability/{availabilityId}`
    * `DELETE /api/v1/me/availability/{availabilityId}`
  * Agenda pública y privacidad:
    * `GET /api/v1/public/users/{userId}/availability` (solo franjas libres no comprometidas)
    * `PUT /api/v1/me/availability-visibility` (activar/desactivar visibilidad pública)

* **Fase 5: Sesiones, Transacción de Créditos y Calificaciones (~20%)**  
  * Ciclo de vida y máquina de estados de sesiones:
    * `POST /api/v1/sessions` (crear sesión solicitada y comprometer horario)
    * `POST /api/v1/sessions/{sessionId}/confirm` (aceptar sesión)
    * `POST /api/v1/sessions/{sessionId}/cancel` (cancelar y liberar franja)
    * `POST /api/v1/sessions/{sessionId}/complete` (finalizar sesión)
  * Transacción atómica de créditos (Unit of Work + Idempotencia):
    * `POST /api/v1/sessions/{sessionId}/credit-transfer`
    * `GET /api/v1/me/credit-movements` y `GET /api/v1/me/history`
  * Calificaciones y reputación:
    * `POST /api/v1/sessions/{sessionId}/ratings` (1 a 5 estrellas + recalcular promedio)

