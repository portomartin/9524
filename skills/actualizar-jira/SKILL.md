---
name: actualizar-jira
description: Sincronizar en Jira la planificación local aprobada y publicar siempre el MVP activo y su resumen en la sección Documentos de Confluence, evitando duplicados o pérdida de decisiones.
---

# Actualizar Jira

Usar este skill únicamente cuando el usuario solicite crear, actualizar o sincronizar issues de Jira a partir de la documentación local aprobada. La sincronización autorizada incluye siempre la actualización documental del MVP activo y del MVP resumido en la sección Documentos asociada al proyecto.

## Fuente y alcance

- Leer `AGENTS.md` y confirmar qué versión del MVP está activa.
- Leer el archivo de la versión activa, por defecto `docs/mvp-v3.md`.
- Leer `docs/mvp-resumido.md`.
- Leer `docs/backlog.md` y `docs/subtareas.md`.
- Considerar la documentación local como fuente de la sincronización, no el contenido previo de Jira.
- No modificar el MVP, WBS, USM, backlog ni subtareas locales desde este skill.

## Política de versionado en Jira

- Toda épica, historia y subtarea nueva derivada del MVP activo debe recibir la etiqueta `mvp-v3` cuando la fuente activa sea `docs/mvp-v3.md`.
- Si cambia la versión activa, usar una etiqueta equivalente y explícita, por ejemplo `mvp-v4`.
- Las épicas deben conservar en el resumen su identificador de WBS: `E1`, `E2`, `E3`, etc., seguido del nombre de la épica.
- Las historias deben conservar su identificador `HUxx`.
- Las subtareas deben incluir `HUxx` y su tipo técnico (`Backend` o `Frontend`) en un resumen breve y legible. Los endpoints, cuerpos HTTP, respuestas y detalles de implementación deben quedar en la descripción, nunca en el título.
- En las subtareas `Backend/API REST`, la descripción debe separar claramente la especificación técnica: usar bloques de código `http` para endpoints, headers y parámetros, bloques `json` para request/response bodies cuando corresponda, y texto separado para reglas, estados y códigos HTTP. No dejar contratos técnicos extensos como texto inline.
- Cuando una subtarea incluya varios endpoints, explicar la responsabilidad de cada método (por ejemplo, `GET` consulta y `PATCH` modifica parcialmente), indicando para cada uno si recibe body y qué response espera.
- Las issues históricas no deben modificarse ni recibir etiquetas retroactivamente, salvo autorización explícita.
- La etiqueta debe aplicarse a todos los niveles para que los filtros, tableros, dashboards y reportes incluyan el conjunto completo de la versión.

## Flujo obligatorio

1. Resolver el proyecto, el sitio de Jira y el espacio de Confluence conectados.
2. Buscar en la sección Documentos las páginas correspondientes al MVP activo y a `MVP resumido`.
3. Actualizar esas páginas con el contenido local vigente; si no existen, crearlas allí. No crear duplicados por cambios de nombre o ejecuciones repetidas.
4. Consultar las épicas, historias y subtareas existentes.
5. Comparar por claves, títulos, padres y contenido antes de crear o editar.
6. Proponer o ejecutar únicamente los cambios incluidos en la autorización del usuario.
7. Aplicar la etiqueta de versión a cada issue nueva: épica, historia y subtarea.
8. Evitar duplicados y conservar estados, responsables, estimaciones y otros campos no solicitados.
9. Verificar al finalizar la publicación documental, la cantidad de issues creadas o actualizadas, sus etiquetas y sus relaciones.

## Seguridad de la sincronización

- La derivación local no autoriza por sí sola cambios en Jira.
- Requiere una instrucción explícita como “sincronizar la derivación con Jira”.
- Cuando se autoriza la sincronización, la actualización del MVP activo y de `MVP resumido` en Documentos forma parte obligatoria de la operación.
- Si no se puede resolver la sección Documentos o una página existente, detener esa publicación y reportarlo; no crear páginas fuera del espacio del proyecto sin autorización.
- Si el usuario pide solo revisar o comparar, no crear ni editar issues.
- Si hay diferencias de alcance o decisiones ambiguas, detener la sincronización de esa parte y presentarlas.
- No eliminar issues automáticamente. Proponerlas como obsoletas o pedir autorización específica.

## Trazabilidad

Mantener la relación:

```text
MVP activo → Épica → Historia de usuario → Subtarea
```

Las descripciones deben conservar los criterios de aceptación y, en subtareas Backend/API REST, los bloques HTTP y JSON definidos en `docs/subtareas.md`, manteniendo separados endpoints, request, response y reglas de negocio.
