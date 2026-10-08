---
name: crear-jira-desde-wbs-original
description: Construir y mantener un proyecto Jira separado a partir del WBS original, usando ese WBS como única fuente de verdad y sin mezclarlo con el proyecto activo del MVP V3.
---

# Proyecto Jira basado en el WBS original

Usar este skill únicamente para armar el proyecto Jira independiente basado en el WBS original del proyecto. No usarlo para sincronizar el backlog vigente ni para actualizar el proyecto Jira del MVP V3.

## Aislamiento obligatorio

Este flujo no puede contaminar el trabajo existente. Bajo ninguna circunstancia debe modificar, mover, etiquetar, borrar o sincronizar elementos de:

- el proyecto Jira actual del MVP V3;
- `proyecto-sdd/mvp-v3.md`, `proyecto-sdd/backlog.md`, `proyecto-sdd/wbs.md` o `proyecto-sdd/subtareas.md`;
- `proyecto-sdd/mapeo-funcionalidades-historicas.md`;
- `proyecto-sdd/sprints.md`;
- los skills o documentos usados para derivar y ejecutar el MVP V3.

Si una operación pudiera afectar alguno de esos elementos, detenerla y tratarla como fuera de alcance.

## Fuente de verdad

- Usar exclusivamente `proyecto-wbs/wbs-original.md` como fuente del WBS original histórico.
- No usar `proyecto-sdd/mvp-v3.md`, `proyecto-sdd/backlog.md`, `proyecto-sdd/wbs.md` ni `proyecto-sdd/subtareas.md` para agregar, quitar o reorganizar alcance en este proyecto.
- Si el WBS original no está disponible o hay más de una versión, detener la construcción y pedir que se indique cuál usar.
- Mantener la numeración y los nombres del WBS original, aunque difieran del MVP V3 o del backlog actual.

## Separación de proyectos

- Este proyecto Jira debe ser independiente del proyecto actual del MVP V3.
- La sincronización Jira de este skill debe operar sobre un proyecto Jira nuevo y un tablero Jira nuevo asociados a ese proyecto.
- El proyecto Jira es el contenedor de épicas, HU y tareas; el tablero es únicamente la vista de trabajo del proyecto y su filtro.
- No reutilizar el proyecto ni el tablero del MVP V3.
- No mezclar épicas, historias, subtareas, sprints, estimaciones, estados ni responsables entre ambos proyectos.
- Las funcionalidades coincidentes pueden existir en los dos proyectos: pertenecen a fuentes de verdad distintas.
- Identificar el proyecto como basado en el WBS original para evitar confundirlo con la ejecución del MVP V3.

### Destino Jira vigente

- Proyecto: `WBSO` — `WBS Original Histórico`.
- Tablero: `WBSO board` — tablero Scrum del proyecto.
- URL del tablero: `https://martinporto.atlassian.net/jira/software/projects/WBSO/boards/35/backlog`.
- Si el proyecto o el tablero ya existen, reutilizarlos y no crear duplicados.

## Sincronización de la jerarquía

Cuando el usuario autorice la carga en Jira:

1. Crear o reutilizar las épicas técnicas agrupadoras.
2. Crear cada HU `1.x` como issue tipo `Historia` dentro de su épica.
3. Crear cada tarea `1.x.x` como `Subtask` de la HU correspondiente.
4. Mantener el identificador WBS al comienzo del resumen y aplicar las etiquetas `wbs-original`, `hu-wbs` o `tarea-wbs` según el nivel.
5. Verificar que cada issue quede en `WBSO` y que sus padres pertenezcan al mismo proyecto.

La carga actual contempla cuatro épicas, quince HU y las tareas del archivo `proyecto-wbs/wbs-original.md`. No copiar issues ni relaciones desde `BH95`.

## Estructura Jira

Representar la jerarquía del WBS sin cambiar su numeración:

```text
Proyecto Jira → Épica técnica → HU 1.x → Tarea 1.x.x
```

- Crear épicas únicamente como contenedores técnicos de Jira; las épicas no forman parte del WBS original y no deben recibir numeración WBS. La agrupación inicial es:
  - `Producto y diseño`: HU `1.1` y `1.2`.
  - `Funcionalidad de la plataforma`: HU `1.3` a `1.10`.
  - `Seguridad y administración`: HU `1.11` y `1.12`.
  - `Implementación, pruebas y entrega`: HU `1.13` a `1.15`.
- No inventar épicas funcionales ni usar las épicas para alterar la jerarquía del WBS.
- Forzar cada bloque `1.x` del WBS a una HU Jira, aunque semánticamente el WBS lo nombre como sistema, módulo o bloque principal.
- Representar cada elemento `1.x.x` como tarea funcional hija de la HU `1.x`.
- La estructura del WBS original termina en `1.x.x`; no crear ni asumir niveles adicionales.
- Si Jira exige un contenedor superior, usarlo solo como estructura técnica del proyecto y no asignarle un identificador WBS ni tratarlo como parte del alcance.
- Usar los niveles Jira disponibles de forma consistente con la profundidad real del WBS.
- Conservar el identificador WBS en el resumen visible, por ejemplo `[1.4.1] Formulario de publicación`.
- No reemplazar un elemento por otro más resumido solo porque exista una funcionalidad parecida en el MVP V3.
- No crear tareas técnicas que no estén respaldadas por el WBS original, salvo pedido explícito.
- Mantener duplicados funcionales si aparecen en el WBS; la correspondencia se define por el identificador WBS, no por similitud de nombre.

## Construcción progresiva

El proyecto puede armarse por partes. En cada incorporación:

1. Leer el tramo correspondiente del WBS original.
2. Identificar su nivel jerárquico y su padre.
3. Crear o actualizar únicamente los issues de ese tramo en el proyecto separado.
4. Mantener el identificador WBS y el nombre original.
5. Registrar los issues creados y sus padres para continuar después sin duplicarlos.

No asumir que una ejecución anterior completó otros tramos. No reconstruir ni modificar automáticamente el proyecto MVP V3.

## Autorización y límites

- La lectura y el mapeo pueden prepararse localmente.
- Crear o modificar el proyecto, issues o sprints de Jira requiere una solicitud explícita del usuario.
- La solicitud de sincronización debe identificar o aprobar el nuevo proyecto y tablero destino antes de crear issues.
- Una solicitud para trabajar sobre este proyecto no autoriza cambios en el proyecto MVP V3.
- La sincronización de este proyecto no publica ni actualiza el MVP V3, el backlog vigente ni Confluence.
- No publicar el MVP, el backlog ni documentación de Confluence como parte de este skill.
- No eliminar issues automáticamente. Si el WBS cambia, informar diferencias y pedir autorización antes de desactivar o borrar elementos.

## Resultado esperado

Entregar, según lo solicitado:

- el mapeo del tramo WBS trabajado;
- la jerarquía Jira creada o propuesta;
- las claves Jira y sus padres;
- los elementos pendientes o ambiguos;
- una separación explícita respecto del proyecto MVP V3.

Este skill no define agentes, subskills, loops de verificación ni automatizaciones recurrentes. Es un único flujo de construcción progresiva guiado por el usuario.
