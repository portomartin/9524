---
name: actualizar-jira
description: Sincronizar en Jira la planificación local aprobada del proyecto, comparando el backlog y las subtareas existentes para evitar duplicados o pérdida de decisiones.
---

# Actualizar Jira

Usar este skill únicamente cuando el usuario solicite crear, actualizar o sincronizar issues de Jira a partir de la documentación local aprobada.

## Fuente y alcance

- Leer `AGENTS.md` y confirmar qué versión del MVP está activa.
- Leer `docs/backlog.md` y `docs/subtareas.md`.
- Considerar la documentación local como fuente de la sincronización, no el contenido previo de Jira.
- No modificar el MVP, WBS, USM, backlog ni subtareas locales desde este skill.

## Flujo obligatorio

1. Resolver el proyecto y el sitio de Jira conectados.
2. Consultar las épicas, historias y subtareas existentes.
3. Comparar por claves, títulos, padres y contenido antes de crear o editar.
4. Proponer o ejecutar únicamente los cambios incluidos en la autorización del usuario.
5. Evitar duplicados y conservar estados, responsables, estimaciones y otros campos no solicitados.
6. Verificar al finalizar la cantidad de issues creadas o actualizadas y sus relaciones.

## Seguridad de la sincronización

- La derivación local no autoriza por sí sola cambios en Jira.
- Requiere una instrucción explícita como “sincronizar la derivación con Jira”.
- Si el usuario pide solo revisar o comparar, no crear ni editar issues.
- Si hay diferencias de alcance o decisiones ambiguas, detener la sincronización de esa parte y presentarlas.
- No eliminar issues automáticamente. Proponerlas como obsoletas o pedir autorización específica.

## Trazabilidad

Mantener la relación:

```text
MVP activo → Épica → Historia de usuario → Subtarea
```

Las descripciones deben conservar los criterios de aceptación y, en subtareas Backend/API REST, los bloques HTTP y JSON definidos en `docs/subtareas.md`.
