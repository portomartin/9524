---
name: ampliar-backlog-con-mapeo
description: Ampliar el detalle técnico de las subtareas Backend usando una matriz de funcionalidades históricas, sin cambiar la jerarquía de Jira ni modificar automáticamente el alcance del MVP.
---

# Ampliar backlog con mapeo histórico

Usar este skill cuando se necesite recuperar granularidad técnica de documentación histórica y expresarla dentro de las subtareas Backend existentes.

## Fuentes

Leer, en este orden:

1. `AGENTS.md`.
2. `proyecto-sdd/mvp-v3.md` para verificar el alcance vigente.
3. `proyecto-sdd/mapeo-funcionalidades-historicas.md` para obtener las funcionalidades a rastrear.
4. `proyecto-sdd/backlog.md` y `proyecto-sdd/subtareas.md` para resolver las HU y tareas actuales.

La fuente de verdad sigue siendo `proyecto-sdd/mvp-v3.md`. La matriz histórica es auxiliar y no puede introducir funcionalidades fuera del MVP.

## Resultado por defecto

- Ampliar las descripciones de las subtareas Backend existentes en `proyecto-sdd/subtareas.md`.
- Incorporar checklists técnicas con identificadores documentales de cuarto nivel, por ejemplo `[2.2.1.1]`, `[2.2.1.2]` y `[2.2.1.3]`.
- Mantener las subtareas Backend actuales como unidades Jira.
- No crear subtareas Jira anidadas: Jira no admite una subtarea hija de otra subtarea.
- No modificar automáticamente `proyecto-sdd/backlog.md`, `proyecto-sdd/mvp-v3.md` ni Jira.

## Regla de decisión

Agregar un ítem de checklist cuando la funcionalidad histórica represente una responsabilidad Backend concreta, como:

- endpoint o recurso independiente;
- regla de negocio relevante;
- validación con comportamiento propio;
- operación de persistencia o transición diferenciada.

No crear un ítem separado para cada campo simple si no tiene comportamiento propio. Agrupar campos relacionados dentro de un único ítem.

## Numeración

La numeración de checklist extiende la WBS documental de la subtarea:

```text
[épica] → [historia] → [subtarea] → [detalle técnico]
[2.0.0] → [2.2.0] → [2.2.1] → [2.2.1.1]
```

Estos identificadores sirven para documentación y trazabilidad. No son claves Jira ni implican una nueva jerarquía de issues.

## Protección del alcance

- Si una funcionalidad histórica no está cubierta por el MVP V3, marcarla como `pendiente` o `fuera de alcance`; no agregarla a la checklist como trabajo aprobado.
- Si el mapeo revela una nueva capacidad funcional, registrar la observación y detener esa parte para revisión; no cambiar el backlog automáticamente.
- `proyecto-sdd/backlog.md` solo se modifica con autorización explícita cuando cambian una historia, sus criterios de aceptación o el alcance funcional. Agregar detalle técnico no alcanza para modificarlo.
- Preservar endpoints, ejemplos HTTP/JSON, tipos, parámetros, respuestas y reglas existentes en `proyecto-sdd/subtareas.md`.
- Evitar duplicar ítems ya documentados; comparar por identificador y responsabilidad.

## Modos de uso

### Propuesta

Por defecto, producir una propuesta de ampliación y señalar qué subtareas Backend serían enriquecidas, sin escribir archivos.

### Aplicación local

Solo cuando el usuario lo autorice explícitamente, actualizar `proyecto-sdd/subtareas.md` con las checklists técnicas. Verificar que cada ítem tenga una única subtarea Backend responsable.

### Sincronización externa

La aplicación local no autoriza Jira. Para reflejar los cambios en Jira se requiere una solicitud separada de sincronización y se debe respetar el skill `actualizar-jira`.

## Verificación

Al finalizar una aplicación local:

- cada funcionalidad mapeada tiene estado `cubierta`, `pendiente` o `fuera de alcance`;
- no se crearon subtareas Jira ni se alteró la jerarquía;
- los identificadores de cuarto nivel son únicos dentro de su subtarea;
- no se modificó el alcance del MVP sin autorización;
- la documentación conserva los contratos técnicos existentes.
