---
name: crear-wbs
description: Crear o actualizar una WBS orientada a entregables a partir de la especificación del MVP, usando una jerarquía numerada de proyecto, bloques principales, módulos y funcionalidades.
---

# WBS basada en entregables

Usar esta skill cuando el usuario solicite crear, revisar o reorganizar una WBS del proyecto.

Una WBS (*Work Breakdown Structure*, o estructura de desglose del trabajo) es una herramienta jerárquica que ordena y clasifica el trabajo de un proyecto. Descompone el trabajo en entregables y componentes progresivamente más pequeños, estimables y verificables.

## Fuente de información

Leer primero:

- `AGENTS.md` para las reglas del proyecto.
- La versión indicada del MVP (`docs/mvp-v1.md`, `docs/mvp-v2.md` o `docs/mvp-v3.md`) como única fuente de verdad del alcance y los requisitos.
- `references/directriz-wbs.md` para aplicar el formato de la captura de referencia.

Derivar el contenido únicamente del MVP. No leer el USM ni el backlog como entradas. Las reglas y referencias orientan el método y el formato, no agregan requisitos. Si existe `docs/wbs.md`, consultarlo solo para preservar identificadores y formato compatibles con el MVP; no usarlo como fuente de alcance.

## Estructura obligatoria

Organizar el trabajo según resultados o componentes entregables, no como una lista plana de tareas técnicas:

```text
0. Proyecto o producto
   1. Bloque principal o entregable
      1.1. Módulo, sistema o subentregable
         1.1.1. Funcionalidad concreta
```

La profundidad puede variar cuando el entregable sea suficientemente claro. No crear niveles artificiales solo para completar la numeración.

## Reglas

- Usar numeración jerárquica: `1`, `1.1`, `1.1.1`.
- Nombrar cada elemento con un resultado o capacidad comprensible.
- Mantener trazabilidad hacia secciones concretas del MVP.
- Distinguir `GUEST`, `USER` y `ADMIN` cuando corresponda.
- No mezclar en un mismo nivel funcionalidades, tareas técnicas y documentos de gestión.
- Incluir entregables académicos de gestión solo si están respaldados por el MVP; señalar los que requieran otra fuente como pendientes, sin incorporarlos automáticamente.
- Detectar elementos del MVP que no estén representados en la WBS.
- Señalar elementos de la WBS que no tengan respaldo explícito en el MVP.
- No usar el backlog para agregar alcance o decidir la estructura de la WBS.

## Resultado esperado

Presentar:

1. La WBS jerárquica en Markdown.
2. Una tabla de trazabilidad entre entregables y secciones del MVP.
3. Supuestos, ambigüedades y elementos pendientes de confirmar.

La WBS es una salida independiente del MVP; no es una entrada obligatoria del USM ni del backlog. No modificar ninguna versión del MVP, `docs/usm.md` ni `docs/backlog.md` automáticamente. Si la WBS se aprueba, guardarla en `docs/wbs.md` y registrar el cambio cuando corresponda.
