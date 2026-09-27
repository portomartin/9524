# Graph de planificación: tres ramas desde el MVP

El grafo se declara en el bloque Mermaid y en las instrucciones del [skill coordinador `actualizar-planificacion`](../skills/actualizar-planificacion/SKILL.md). Ese archivo es la referencia del recorrido.

```text
             ┌→ Actualizar WBS ──────┐
Leer MVP ────┼→ Actualizar USM ──────┼→ Presentar resultados
             └→ Actualizar backlog ─┘
```

## Qué significa cada conexión

Las tres ramas reciben la misma versión de `docs/mvp.md`. No hay flechas entre WBS, USM y backlog: ninguna salida alimenta a otra. El último nodo reúne los resultados cuando las tres ramas terminaron o informaron un bloqueo.

| Rama | Skill | Fuente de requisitos | Destino al guardar |
|---|---|---|---|
| WBS | [wbs-por-entregables](../skills/wbs-por-entregables/SKILL.md) | MVP | `docs/wbs.md` |
| USM | [user-story-mapping](../skills/user-story-mapping/SKILL.md) | MVP | `docs/usm.md` |
| Backlog | [generar-backlog](../skills/generar-backlog/SKILL.md) | MVP | `docs/backlog.md` |

Cada rama puede consultar su propio documento anterior para conservar identificadores y formato, pero todo el contenido debe estar respaldado por el MVP. Las referencias metodológicas de los skills no agregan requisitos.

## Cómo se recorre

El agente lee las instrucciones del coordinador y aplica cada skill. Puede hacerlo uno después de otro: independencia de entradas no significa simultaneidad obligatoria. No hace falta Python ni varios agentes.

Cada salida se verifica contra el MVP. Si hay una duda, se informa en esa rama sin inventar una respuesta ni detener las otras. El cierre reúne los resultados; no hace que se copien requisitos entre documentos.

Este grafo no tiene ciclos. El [ejemplo de loop](loop-basico.md) muestra por separado cómo definir una repetición. Mermaid dibuja el recorrido, mientras que las instrucciones del skill indican qué hacer; el archivo no se ejecuta solo.

## Pedido para probarlo

> Usá skills/actualizar-planificacion/SKILL.md para preparar WBS, USM y backlog desde el mismo MVP. Mostrá cada rama y presentá los tres borradores con su trazabilidad y pendientes en el chat, sin editar archivos.

Esta versión reemplaza el ejemplo anterior en el que el mapa dependía de la WBS. El ejemplo Python en `ejemplos/graph-basico/` se conserva como ejercicio separado.
