# Índice de skills del proyecto

Los skills se organizan por área: `docs/skills/` para documentación y planificación,
`frontend/skills/` para la interfaz y su publicación, y `backend/skills/` para la API.
Las rutas de archivos citadas en las instrucciones se resuelven desde la raíz del repositorio.

Este documento orienta qué skill usar, cuándo aplicarlo y cómo se relaciona con los demás. La fuente de requisitos del producto es `docs/mvp-v3.md`.

## Flujo principal

```text
MVP V3
  → SC, épicas, WBS y USM
  → backlog
  → subtareas técnicas
  → revisión y refinamiento
  → estimaciones y sprints
  → sincronización con Jira y Confluence
  → push del repositorio
```

La derivación local ocurre antes de Jira. Jira y Confluence son destinos externos, no fuentes de alcance.

## Planificación y producto

| Skill | Uso principal | Momento recomendado |
|---|---|---|
| [`derivar-planificacion-mvp`](skills/derivar-planificacion-mvp/SKILL.md) | Coordinar la derivación completa desde el MVP, revisar el resultado y proponer sprints. | Cuando se solicita derivar o actualizar la planificación completa. |
| [`crear-sc`](skills/crear-sc/SKILL.md) | Crear o revisar el Scope Canvas. | Al definir o revisar el foco del producto. |
| [`crear-epicas`](skills/crear-epicas/SKILL.md) | Identificar capacidades amplias del producto. | Antes del backlog, si las épicas faltan o cambiaron. |
| [`crear-wbs`](skills/crear-wbs/SKILL.md) | Organizar entregables y capacidades en una estructura jerárquica. | Como rama independiente de la derivación. |
| [`crear-usm`](skills/crear-usm/SKILL.md) | Representar el recorrido del usuario y el release slice. | Como rama independiente de la derivación. |
| [`crear-backlog`](skills/crear-backlog/SKILL.md) | Crear épicas, historias, criterios, refinamientos y pendientes. | Después de leer el MVP activo. |
| [`create-subtereas`](skills/create-subtereas/SKILL.md) | Descomponer cada HU en subtareas técnicas trazables. | Después de validar el backlog. |
| [`ampliar-backlog-con-mapeo`](skills/ampliar-backlog-con-mapeo/SKILL.md) | Reconciliar detalle técnico histórico con subtareas actuales. | Después de generar subtareas y solo mientras exista el mapeo histórico. |
| [`crear-sprints`](skills/crear-sprints/SKILL.md) | Estimar HU, calcular capacidad y proponer sprints. | Después de revisar backlog y subtareas. |

## Calidad y cambios

| Skill | Uso principal | Momento recomendado |
|---|---|---|
| [`analizar-cambios`](skills/analizar-cambios/SKILL.md) | Comparar una propuesta con la versión activa del MVP. | Antes de aprobar cambios de alcance o reglas. |
| [`convenciones-backend`](../backend/skills/convenciones-backend/SKILL.md) | Revisar endpoints, seguridad, reglas, persistencia y pruebas Backend. | En cada subtarea o revisión Backend. |
| [`convenciones-frontend`](../frontend/skills/convenciones-frontend/SKILL.md) | Revisar pantallas, flujos, estados, accesibilidad y pruebas Frontend. | En cada subtarea o revisión Frontend. |
| [`implementar-frontend-mvp`](../frontend/skills/implementar-frontend-mvp/SKILL.md) | Implementar y continuar las subtareas frontend del MVP. | Cuando se solicita construir o continuar la interfaz. |

## Publicación y mantenimiento

| Skill | Uso principal | Momento recomendado |
|---|---|---|
| [`actualizar-jira`](skills/actualizar-jira/SKILL.md) | Sincronizar la planificación local con Jira y publicar MVP V3 en Confluence. | Solo con autorización explícita. |
| [`publicar-frontend`](../frontend/skills/publicar-frontend/SKILL.md) | Preparar y publicar el frontend estático en GitHub Pages mediante GitHub Actions. | Cuando se solicita desplegar la interfaz. |
| [`push`](skills/push/SKILL.md) | Revisar, commitear y publicar cambios del repositorio. | Solo cuando se solicita publicar cambios Git. |
| [`readme`](skills/readme/SKILL.md) | Mantener la entrada principal de documentación del repositorio. | Cuando cambien los enlaces o la orientación del proyecto. |

## Loops y grafos

- `derivar-planificacion-mvp` tiene un loop de refinamiento local de máximo tres pasadas y una condición de corte explícita.
- `actualizar-jira` tiene un loop corto de sincronización: leer, comparar, escribir, releer y corregir una diferencia concreta como máximo.
- Ambos skills contienen diagramas Mermaid porque tienen decisiones y ciclos.
- Las convenciones Backend y Frontend, `crear-sprints`, `push` y la reconciliación histórica tienen validaciones, aunque no todos necesitan un loop formal.

## Reglas de orientación

1. Usar `docs/mvp-v3.md` como fuente activa de alcance.
2. No usar Jira para decidir qué debe contener el producto.
3. Refinar los documentos locales antes de sincronizar destinos externos.
4. No modificar automáticamente el MVP por una propuesta técnica.
5. Registrar pendientes cuando falte una decisión de producto.
