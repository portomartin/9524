# Grafo de planificación: tres ramas desde el MVP y refinamiento opcional

El grafo se declara en el bloque Mermaid y en las instrucciones del [skill coordinador `coordinar-planificacion`](../skills/coordinar-planificacion/SKILL.md). Ese archivo es la referencia del recorrido.

```text
             ┌→ Crear WBS ──────────┐
Leer MVP ────┼→ Crear USM ──────────┼→ Presentar resultados
             └→ Crear backlog ──────┘
                         │
                         └╌→ Refinar backlog (opcional)
```

## Qué significa cada conexión

Las tres ramas reciben la misma versión de `docs/mvp.md`. No hay flechas entre WBS, USM y backlog: ninguna salida alimenta a otra. Después de crear el backlog, puede ejecutarse opcionalmente `refinar-backlog` para revisarlo antes de una nueva presentación.

| Rama | Skill | Fuente de requisitos | Destino al guardar |
|---|---|---|---|
| WBS | [crear-wbs](../skills/crear-wbs/SKILL.md) | MVP | `docs/wbs.md` |
| USM | [crear-usm](../skills/crear-usm/SKILL.md) | MVP | `docs/usm.md` |
| Backlog | [crear-backlog](../skills/crear-backlog/SKILL.md) | MVP | `docs/backlog.md` |
| Refinamiento opcional | [refinar-backlog](../skills/refinar-backlog/SKILL.md) | Backlog creado + MVP | Propuestas de revisión |

Cada rama puede consultar su propio documento anterior para conservar identificadores y formato, pero todo el contenido debe estar respaldado por el MVP. Las referencias metodológicas de los skills no agregan requisitos.

## Cómo se recorre

El agente lee las instrucciones del coordinador y aplica cada skill. Puede hacerlo uno después de otro: independencia de entradas no significa simultaneidad obligatoria. No hace falta Python ni varios agentes.

Cada salida se verifica contra el MVP. Si hay una duda, se informa en esa rama sin inventar una respuesta ni detener las otras. El refinamiento revisa el backlog ya creado, propone cambios y espera confirmación antes de reescribirlo. El cierre reúne los resultados; no hace que se copien requisitos entre documentos.

Este grafo no tiene ciclos. El [ejemplo de loop](loop-basico.md) muestra por separado cómo definir una repetición. Mermaid dibuja el recorrido, mientras que las instrucciones del skill indican qué hacer; el archivo no se ejecuta solo.

## Pedido para probarlo

> Usá skills/coordinar-planificacion/SKILL.md para preparar WBS, USM y backlog desde el mismo MVP. Mostrá cada rama y presentá los tres borradores con su trazabilidad y pendientes en el chat. Si corresponde, ejecutá después `refinar-backlog` sobre el backlog, sin editarlo hasta recibir aprobación.

Esta versión reemplaza el ejemplo anterior en el que el mapa dependía de la WBS. El ejemplo Python anterior fue eliminado; este documento y el skill coordinador son la referencia vigente.
