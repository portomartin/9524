---
name: contexto-wbs
description: Mantener y aplicar el contexto del proyecto WBS de entrega, sus notas, decisiones y trabajo en Jira WBSO. Usar cuando el usuario comparta notas crudas, pida organizarlas, preparar la demo/defensa o crear y actualizar issues del WBS.
metadata:
  short-description: Contexto persistente y trabajo del proyecto WBS
---

# Contexto del proyecto WBS

Este skill corresponde exclusivamente al proyecto de entrega WBS y al proyecto Jira `WBSO`.

## Separación obligatoria

- No mezclar este trabajo con el proyecto SDD.
- No usar `BH95` para estas notas, decisiones o tareas.
- No usar `proyecto-sdd/` como fuente de requisitos para este proyecto.
- No modificar el alcance, la documentación ni los issues del proyecto SDD como consecuencia de trabajar aquí.

## Contexto persistente

Antes de analizar o transformar notas del WBS, leer, si existen:

1. [`contexto/README.md`](../../contexto/README.md)
2. [`contexto/notas.md`](../../contexto/notas.md)
3. [`contexto/decisiones.md`](../../contexto/decisiones.md)
4. La WBS histórica y los skills de `proyecto-wbs` relevantes para la tarea.

El contexto persistente es una memoria versionada del proyecto. No se considera entrenamiento del modelo: cada nueva instancia debe leer estos archivos.

## Cómo trabajar con notas nuevas

- Conservar primero el sentido y el texto original de las notas.
- Separar contexto, decisiones, requisitos, historias, tareas, bugs y pendientes.
- No convertir automáticamente cada nota en un issue.
- Para Jira, usar `WBSO` como destino y diferenciar épicas, HU, criterios de aceptación y tareas técnicas.
- Mantener trazabilidad desde el issue hacia la nota o decisión de origen.
- Antes de una escritura externa en Jira, mostrar la propuesta y pedir confirmación si la autorización no está explícita en el pedido actual.

## Actualización de la memoria

Cuando el usuario pida guardar contexto o entregue notas para conservar:

- agregar las notas a `contexto/notas.md` sin borrar notas anteriores;
- registrar acuerdos confirmados en `contexto/decisiones.md`;
- actualizar `contexto/README.md` solo si cambia la navegación o el estado general;
- conservar los cambios en archivos Markdown para que puedan recuperarse desde otra computadora mediante Git.

Escribir en español claro, mantener el alcance de WBS explícito y no inventar decisiones que el usuario no haya confirmado.
