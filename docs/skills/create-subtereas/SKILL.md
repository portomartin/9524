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

### Granularidad y señales para dividir

Usar una granularidad que ayude a ejecutar, estimar y verificar el trabajo en Jira. No asumir que cada historia necesita dos subtareas ni fijar una cantidad objetivo.

- Un endpoint distinto es un indicio fuerte para evaluar una subtarea separada, pero no obliga a dividir si las operaciones forman una única unidad fuertemente acoplada, como una máquina de estados compartida.
- Una misma operación o endpoint puede dividirse cuando contiene responsabilidades independientes y verificables, por ejemplo validación, persistencia, disponibilidad, concurrencia, autorización o pruebas con resultados distintos.
- Mantener juntas las responsabilidades que comparten lógica, dependencias y resultado, cuando separarlas solo genere coordinación artificial.
- No crear una subtarea por cada campo, validación simple o detalle sin comportamiento propio. Incorporar esos elementos como checklist técnica dentro de la subtarea responsable.

Aplicar una granularidad asimétrica por especialidad:

- **Backend/API REST:** puede descomponerse con mayor detalle cuando hay endpoints, transiciones de estado, reglas de negocio, autorización, persistencia, concurrencia o pruebas independientes.
- **Frontend:** normalmente agrupar por pantalla o flujo completo. Dividir solo cuando existan pantallas, flujos, componentes compartidos o responsabilidades con ejecución y verificación independientes. Los estados de carga, vacío, error, éxito y permisos suelen quedar como checklist del flujo, salvo que constituyan una unidad claramente separable.

En el modelo de Jira, las subtareas son hijas directas de la historia y no se anidan entre sí. Los criterios de aceptación permanecen en la descripción de la historia; los contratos HTTP, reglas técnicas y checklists permanecen en la descripción de la subtarea correspondiente. La descomposición técnica debe conservar la trazabilidad al alcance y los criterios de la historia derivados del MVP, sin convertir una propuesta de endpoint en una nueva regla de producto.

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
2. Endpoints sugeridos, indicando cada verbo HTTP y su responsabilidad. Si varias subtareas usan la misma ruta, repetir la ruta dentro de cada subtarea y documentar explícitamente el verbo y la operación que le corresponden.
3. Parámetros de path y query.
4. Request body sugerido.
5. Response exitosa sugerida.
6. Response de error relevante cuando corresponda.
7. Criterios técnicos y pruebas.

Una subtarea `Backend/API REST` no se considera técnicamente completa mientras no tenga un contrato mínimo explícito: endpoint con verbo y propósito, request —incluyendo `sin body` cuando corresponda—, response exitosa y errores relevantes. Los parámetros de path, query y headers, sus tipos y ejemplos deben quedar documentados. Si el trabajo Backend es puramente interno y no tiene endpoint, declararlo explícitamente como excepción y describir su entrada, salida y pruebas.

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

Cuando una misma ruta tenga variantes por verbo, parámetros, body, respuesta o reglas de autorización, describir cada variante por separado dentro de la subtarea que la implementa. No agrupar contratos diferentes en una única descripción ambigua. Si dos variantes están fuertemente acopladas y se mantienen en una sola subtarea, documentar igualmente cada método y su contrato por separado.

## Formato para subtareas Frontend

Cada subtarea Frontend debe indicar:

```text
Consultar y aplicar el skill `convenciones-frontend`.
```

La implementación debe usar Vue y la librería de componentes adoptada por el proyecto. Las pantallas deben ser claras, consistentes, accesibles y responsive, con estados de carga, vacío, error y éxito cuando correspondan.

No crear estilos propios, CSS innecesario, objetos visuales ad hoc ni una identidad visual paralela. Reutilizar componentes, variantes, tokens y patrones de layout de la librería. Mantener la lógica de negocio en servicios o composables y validar en frontend sin reemplazar las validaciones del backend.

## Resultado local

Guardar la descomposición derivada en `docs/subtareas.md`, manteniendo la trazabilidad Épica → Historia → Subtarea y dejando explícitas las HU que no requieran subtareas. La sincronización con herramientas externas pertenece a un proceso separado.
