# Especificación Técnica y Convenciones: Búsqueda y Compatibilidad (Épica 1.5)

**Proyecto:** GDSI 2026 — Plataforma de Intercambio de Aprendizajes  
**Proyecto Jira:** `WBSO` (`WBSO-9`)  
**Fuente de verdad del alcance:** [`wbs-original.md`](../wbs-original.md) y [`jerarquia-jira.md`](../jerarquia-jira.md).  
**Repositorio de implementación backend:** `9524-backend`  

---

## 1. Trazabilidad con Jira y WBS (Épica 1.5)

Esta especificación cubre la funcionalidad acordada con el equipo de Frontend para la búsqueda, filtrado y exploración de ofertas de clase:

| Requisito / Parámetro | Ticket Jira | Tarea WBS |
|---|---|---|
| `query` (búsqueda insensible sobre título y descripción) | `WBSO-51` | **[1.5.1] Buscador de aprendizajes** |
| `category_id`, `subcategory_id`, `level`, `modality` | `WBSO-53` | **[1.5.2] Filtros de búsqueda** |
| Response paginado (`total`, `page`, `page_size`, `items`) | `WBSO-54` | **[1.5.3] Resultados de búsqueda** |
| Objeto `teacher` (`user_id`, `first_name`, `last_name`, `image_url`) | `WBSO-55` | **[1.5.4] Vista de perfiles compatibles** |
| Solo activas, excluir al propio usuario, `compatible_with_me` | `WBSO-56` | **[1.5.5] Motor de compatibilidad basado en reglas** |
| `days` (CSV), `time_from`, `time_to` con cálculo de solape | `WBSO-57` | **[1.5.6] Detección de coincidencias horarias** |
| `reciprocal_with_me` (bool calculado o default false) | `WBSO-58` | **[1.5.7] Detección de intercambios recíprocos** |

---

## 2. Contrato de la API

### Endpoint
- **Método y Ruta:** `GET /publications`
- **Autenticación:** Requiere sesión obligatoria mediante cookie HttpOnly de sesión (o header `X-User-Id` en entorno de test/desarrollo).
  - Sin cookie ni sesión activa → **`401 Unauthorized`**.

### Query Parameters (todos opcionales salvo defaults de paginación)
| Parámetro | Tipo | Descripción y Validación |
|---|---|---|
| `query` | `string` | Búsqueda parcial *case-insensitive* sobre `title` y `description`. |
| `category_id` | `int` | ID de la categoría principal (equivalente a `interest_id` del catálogo). Si no existe devuelve lista vacía `[]`. |
| `subcategory_id` | `int` | ID de la subcategoría (equivalente a `subinterest_id`). Si no existe devuelve lista vacía `[]`. |
| `level` | `string` | Nivel de la clase (`Principiante`, `Intermedio`, `Avanzado`, `Experto`). Si el valor no está en catálogo → `422`. |
| `modality` | `string` | Modalidad (`online`, `in_person`). Si el valor no está en catálogo → `422`. |
| `days` | `string` (CSV) | Días en formato CSV (ej. `days=mon,wed`). Si algún día no es válido → `422`. |
| `time_from` | `string` | Horario inicio en formato `HH:mm` (ej. `18:00`). |
| `time_to` | `string` | Horario fin en formato `HH:mm` (ej. `20:00`). |
| `compatible_with_me` | `boolean` | Cruza con la agenda del usuario (fase 2: requiere agenda en perfil). |
| `page` | `int` | Número de página (default: `1`, mínimo `1`). Si `page < 1` → `422`. |
| `page_size` | `int` | Tamaño de página (default: `10`, rango permitido `1` a `50`). Si está fuera de rango → `422`. |

---

## 3. Semántica de Filtros y Reglas de Negocio

1. **Acumulación de filtros:** Todos los filtros se combinan con lógica **`AND`** entre grupos.
2. **Disponibilidad horaria:**
   - **`days`:** La publicación debe tener al menos una franja de disponibilidad en alguno de los días indicados.
   - **`time_from` / `time_to`:** Al menos una franja de la publicación debe solaparse con la ventana horaria solicitada:
     $$\text{slot.start} < \text{time\_to} \quad \text{AND} \quad \text{slot.end} > \text{time\_from}$$
   - **`days` + franja juntos:** El solape debe producirse en un día incluido en `days`.
3. **Estado de publicación:**
   - Solo se devuelven publicaciones con `status == "active"` y `moderation_status == "active"`.
4. **Exclusión del usuario propio:**
   - El buscador está diseñado para explorar clases de otros profesores, por lo que **se excluyen las publicaciones del usuario en sesión** (`user_id != current_user.id`).
5. **Orden por defecto:**
   - Relevancia / orden por defecto más recientes (`id` descendente).

---

## 4. Estructura de Respuesta (HTTP 200 OK)

```json
{
  "total": 37,
  "page": 1,
  "page_size": 10,
  "items": [
    {
      "id": 1,
      "user_id": 12,
      "title": "Introducción a Python y Lógica de Programación",
      "description": "Aprenderás variables, bucles y funciones paso a paso.",
      "image_url": "https://.../imagen.webp",
      "interest_id": 2,
      "subinterest_id": 201,
      "level_taught": "Principiante",
      "language": "Español",
      "max_students": 5,
      "modality": "online",
      "location": null,
      "credits_cost": 2,
      "duration_minutes": 60,
      "time_zone": "America/Argentina/Buenos_Aires",
      "availability": [
        { "day": "mon", "start_time": "18:00", "end_time": "19:00" },
        { "day": "wed", "start_time": "18:00", "end_time": "19:00" }
      ],
      "status": "active",
      "is_active": true,
      "created_at": "2026-03-10T12:00:00Z",
      "updated_at": "2026-03-10T12:00:00Z",
      "moderation_status": "active",
      "moderation_reason": null,
      "teacher": {
        "user_id": 12,
        "first_name": "Juan",
        "last_name": "Perez",
        "image_url": null
      },
      "reciprocal_with_me": false
    }
  ]
}
```

### Campos enriquecidos:
- **`teacher`**:
  - `user_id`: ID del docente.
  - `first_name`: Nombre.
  - `last_name`: Apellido.
  - `image_url`: URL de avatar o `null` (el frontend renderiza iniciales si es null).
- **`reciprocal_with_me`**: `true` si el docente enseña lo que el usuario busca y viceversa; si no está calculado todavía se retorna `false`.
- **`credits_cost`**: Costo de la clase en créditos.

---

## 5. Convenciones de Desarrollo y Filosofía del Repositorio `9524-backend`

1. **Aislamiento de artefactos y documentación:**
   - Toda la documentación, especificaciones, trazabilidad Jira y decisiones de arquitectura residen en `95.24/proyecto-wbs/docs/`.
   - En `9524-backend` **no se agregan archivos Markdown, notas ni documentos extra**. Únicamente se realizan los cambios de código fuente (`.py`) estrictamente requeridos para que los commits y PRs del equipo queden limpios y enfocados.
2. **Determinismo y cero Inteligencia Artificial:**
   - La búsqueda, filtrado y compatibilidad de la Épica 1.5 se implementan de forma puramente determinista (Python + SQLAlchemy). No se incorporan llamadas a LLM ni dependencias de IA para este flujo.

---

## 6. Guía de Estilo y Patrones de Código en `9524-backend`

Para que el nuevo código parezca escrito por el mismo equipo y no desentone:

1. **Arquitectura funcional y "delgada" en routers:**
   - En `app/routers/publications.py` la lógica de preparación, filtrado y paginación se organiza mediante **helpers privados con prefijo `_`** (`_to_dict`, `_is_public`, `_page`, `_sorted`, etc.). Evitar crear capas abstractas innecesarias (*Service*, *Repository*) si el módulo no las usa.
2. **Inyección de dependencias de autenticación:**
   - Se utiliza `user: dict = Depends(current_user)` desde `app.deps`.
   - Este dependency gestiona transparentemente la cookie HttpOnly en producción y el header `X-User-Id` durante la ejecución de tests automatizados (`ALLOW_DEV_USER_HEADER=True`).
3. **Manejo de errores:**
   - Se lanzan directamente excepciones estándar `HTTPException(status_code=401, detail="...")`, `HTTPException(status_code=404, detail="...")` y `HTTPException(status_code=422, detail="...")`.
4. **Comentarios inline con trazabilidad WBS:**
   - Mantener comentarios concisos en español que identifiquen la tarea correspondiente (ej. `# 1.5.1: buscador por texto`, `# 1.5.6: filtro de solapamiento horario`).

---

## 7. Estrategia de Testing y Mantenimiento de Suites

1. **Aprovechar las fixtures existentes:**
   - Usar las fixtures ya definidas en los tests (`sofia`, `lucas`, `anon`), las cuales proporcionan instancias de `TestClient` configuradas como usuarios autenticados o anónimos.
2. **Actualización de tests de contratos que evolucionaron:**
   - `test_public_list_needs_no_login(anon)` en `tests/publications/test_publications_management.py` reflejaba el comportamiento de 1.4.8 (acceso público sin login). Al evolucionar la HU hacia 1.5 con sesión obligatoria, debe actualizarse para esperar **`401`** cuando la petición es anónima.
   - Las pruebas de filtrado existentes deben pasar a utilizar un cliente autenticado (`lucas` o `sofia`).
3. **Incorporación de nuevos casos de prueba de 1.5 sin crear archivos extra:**
   - Para no dispersar la suite de tests ni agregar nuevos archivos al repositorio, los nuevos tests de 1.5 se añaden directamente al final de `tests/publications/test_publications_management.py`:
     - Exclusión de publicaciones del propio usuario logueado.
     - Filtrado por `days` (CSV) y combinación con solape horario `time_from`/`time_to`.
     - Presencia y tipado del objeto `teacher` y `reciprocal_with_me`.
     - Validaciones `422` ante parámetros fuera de rango (`page < 1`, `page_size > 50`) o formatos horarios inválidos.
