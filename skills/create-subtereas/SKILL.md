---
name: create-subtereas
description: Derivar las subtareas técnicas que realmente necesita cada historia de usuario, con contratos HTTP legibles y convenciones Vue cuando correspondan.
---

# Create subtareas

Usar este skill cuando el usuario solicite crear, actualizar o refinar subtareas técnicas para las historias de usuario del proyecto Plataforma de intercambio de aprendizajes.

## Fuentes y alcance

1. Leer `AGENTS.md`, la versión indicada del MVP (`docs/mvp-v1.md`, `docs/mvp-v2.md` o `docs/mvp-v3.md`) y `docs/backlog.md` antes de generar subtareas.
2. Mantener la trazabilidad: Épica → Historia de usuario → Subtarea.
3. No incorporar funcionalidades fuera del MVP ni resolver unilateralmente pendientes de decisión.
4. No crear subtareas para historias candidatas o pendientes de confirmación, salvo aprobación explícita.

## Decidir la descomposición

Determinar la cantidad y el tipo de subtareas a partir del trabajo necesario para cumplir la historia y sus criterios de aceptación. No crear subtareas para alcanzar una cantidad mínima ni dividir trabajo que resulte más claro y verificable como una sola unidad.

Una historia puede requerir ninguna subtarea, una o varias. Usar, según corresponda:

- **Backend/API REST:** cuando haya modelo, persistencia, reglas de negocio, endpoints, autorización, validaciones o pruebas del servicio.
- **Frontend:** cuando haya pantalla o flujo de usuario, integración con la API, estados visuales, validaciones de presentación o pruebas de interacción.
- **Otras especialidades:** únicamente cuando exista trabajo independiente y verificable de infraestructura, migración, seguridad, datos, diseño o pruebas que no quede cubierto razonablemente dentro de Backend o Frontend.

Crear más de una subtarea de una misma especialidad cuando represente unidades de trabajo con resultados distintos, dependencias diferentes o posibilidad real de ejecución independiente. Mantenerlas juntas cuando separarlas solo produzca coordinación artificial o títulos genéricos.

Antes de finalizar la descomposición, comprobar que todas las partes necesarias de la HU estén cubiertas y que ninguna subtarea replique trabajo transversal ya asignado a otra historia. Si la HU es suficientemente pequeña para ejecutarse directamente, conservarla sin subtareas y explicar brevemente esa decisión en el resultado local.

Usar títulos trazables con numeración WBS, conservando por ahora el tipo técnico:

```text
[1.1.1] [Backend] Implementar registro de usuario
[1.1.2] [Frontend] Crear pantalla de registro
```

Cada subtarea creada debe usar el tercer nivel derivado de su épica e historia entre corchetes: `[1.1.1]`, `[1.1.2]`, etc. Numerarlas consecutivamente según la descomposición resultante; el sufijo no implica una especialidad fija. No usar `HUxx` en el título visible.

Agregar subtareas transversales solo cuando una pieza técnica no pertenezca claramente a una historia específica. No duplicar autenticación, componentes compartidos, manejo común de errores o auditoría en todas las historias.

## Formato para subtareas Backend

Cada subtarea Backend debe incluir, en este orden:

1. Objetivo breve.
2. Endpoints sugeridos.
3. Parámetros de path y query.
4. Request body sugerido.
5. Response exitosa sugerida.
6. Response de error relevante cuando corresponda.
7. Criterios técnicos y pruebas.

Los endpoints y payloads deben aparecer en bloques de código Markdown para que Jira los muestre de forma legible:

```http
POST /api/v1/recurso
Content-Type: application/json
```

```json
{
  "field": "value"
}
```

Las responses deben ser ejemplos JSON plausibles, con códigos HTTP explícitos. Los cuerpos son propuestas técnicas: no convertir sus campos en reglas de negocio aprobadas si el MVP o el backlog los dejan pendientes.

Usar convenciones consistentes:

- Prefijo sugerido: `/api/v1`.
- Identificadores en path como `{id}`.
- Filtros y paginación como query parameters.
- Datos de creación o actualización en JSON.
- Fechas y horas en un formato acordado, preferentemente ISO 8601.
- Usuario autenticado obtenido de la sesión o token, no de un `userId` enviado por el cliente cuando no sea necesario.
- Errores con forma común, por ejemplo:

```json
{
  "code": "VALIDATION_ERROR",
  "message": "Hay campos inválidos",
  "fields": {}
}
```

Incluir validaciones, autorización, idempotencia y auditoría cuando sean necesarias por la historia. Las transferencias de créditos deben derivar cantidad y participantes de la sesión y evitar duplicados.

## Formato para subtareas Frontend

Cada subtarea Frontend debe indicar:

```text
Consultar y aplicar el skill `convenciones-frontend`.
```

La implementación debe usar Vue y la librería de componentes adoptada por el proyecto. Las pantallas deben ser claras, consistentes, accesibles y responsive, con estados de carga, vacío, error y éxito cuando correspondan.

No crear estilos propios, CSS innecesario, objetos visuales ad hoc ni una identidad visual paralela. Reutilizar componentes, variantes, tokens y patrones de layout de la librería. Mantener la lógica de negocio en servicios o composables y validar en frontend sin reemplazar las validaciones del backend.

## Resultado local

Guardar la descomposición derivada en `docs/subtareas.md`, manteniendo la trazabilidad Épica → Historia → Subtarea y dejando explícitas las HU que no requieran subtareas. La sincronización con herramientas externas pertenece a un proceso separado.
