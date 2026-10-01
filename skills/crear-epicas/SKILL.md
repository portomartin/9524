---
name: crear-epicas
description: Crear o actualizar las épicas del backlog a partir del MVP aprobado, manteniendo alcance y compatibilidad con Jira.
---

# Crear épicas del backlog

Usar esta skill cuando se solicite identificar, crear, revisar o reorganizar épicas del proyecto.

## Fuente de verdad

Leer primero `AGENTS.md` y el contenido completo de `docs/mvp.md`. El MVP es la única fuente de alcance.

Si existe `docs/backlog.md`, consultarlo únicamente para conservar IDs, nombres y formato compatibles. No usar la WBS ni el User Story Map para agregar alcance a las épicas.

## Reglas

- Crear épicas como capacidades o resultados amplios del producto, no como tareas técnicas.
- Mantener cada épica enfocada en una capacidad distinta y evitar solapamientos.
- Derivar las épicas únicamente de funcionalidades explícitas del MVP.
- Mantener separados, cuando corresponda, los comportamientos de Docente, Alumno y Administrador.
- No convertir roles en épicas si el MVP no los trata como capacidades independientes.
- No inventar prioridades, estimaciones, responsables, estados ni decisiones técnicas.
- Mantener explícito que los créditos son internos de la plataforma y no son dinero.
- Mantener fuera del MVP las clases grupales, equipos docentes, intercambios 2×1 y sesiones con más de un Docente o Alumno.
- Señalar ambigüedades y pendientes en lugar de resolverlos inventando reglas.

## Identificación y formato

Usar identificadores estables con el formato `E1`, `E2`, `E3`.

Para cada épica presentar:

- ID y nombre.
- Objetivo o capacidad que agrupa.
- Historias incluidas, si ya existen.
- Pendientes o límites relevantes.

Ejemplo de estructura:

```markdown
## E4. Búsqueda y compatibilidad

**Objetivo:** permitir encontrar propuestas, solicitudes y personas compatibles.

**Historias:** HU08, HU09, HU10, HU11.
```

## Conservación del backlog

- Si una épica existente sigue representando una capacidad del MVP, conservar su ID y nombre salvo que el usuario pida renombrarla.
- Si una épica deja de tener respaldo en el MVP, marcarla como obsoleta y explicar el motivo; no eliminarla silenciosamente.
- Si una nueva capacidad del MVP no tiene épica, proponer una nueva épica con el siguiente ID disponible.
- No modificar historias, criterios de aceptación ni el MVP desde esta skill, salvo que el usuario solicite explícitamente esa operación.

## Salida

Presentar primero el borrador de épicas. Incluir un apartado de duplicados, cambios y pendientes.

Por defecto, no guardar archivos ni crear issues externos. Para guardar el resultado, requerir aprobación explícita y escribir en `docs/backlog.md` sin sobrescribir historias no relacionadas.

Si el usuario solicita Jira y existe un conector disponible, preparar la correspondencia `épica → historias` y pedir confirmación antes de crear o modificar issues externos. Si no hay conector, entregar un formato importable o una tabla de mapeo, sin simular la sincronización.
