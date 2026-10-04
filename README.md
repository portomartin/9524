# Plataforma de intercambio de aprendizajes

Proyecto universitario para diseñar un MVP de una plataforma donde las personas puedan enseñar y aprender mediante intercambios directos, clases grupales y créditos virtuales.

## Documentación principal

- [Especificación del MVP V1](docs/mvp-v1.md)
- [Especificación del MVP V2](docs/mvp-v2.md)
- [Especificación del MVP V3](docs/mvp-v3.md)
- [MVP resumido](docs/mvp-resumido.md)
- [WBS del MVP](docs/wbs.md)
- [USM del MVP](docs/usm.md)
- [Backlog del MVP](docs/backlog.md)
- [SC del MVP](docs/sc.md)
- [SC visual del MVP](docs/sc-visual.png)
- [Metodología de planificación](docs/metodologia.md)
- [Alcance futuro](docs/alcance-futuro.md)

## Enlaces externos

- [Cronograma Jira BH95](https://martinporto.atlassian.net/jira/software/projects/BH95/boards/2/timeline)
- [Repositorio GitHub](https://github.com/portomartin/9524)
- [Carpeta de Google Drive](https://drive.google.com/drive/folders/1yT3fRMZmn2E0MRizzJtzh7e1q5G1IJOz)

## Recursos

- Los diagramas vigentes están en `docs/assets/`.
- Los documentos y scripts heredados de la estructura anterior están en `old/` y se conservan como referencia histórica.

## Roles principales

- **USER:** puede ofrecer conocimientos o habilidades y también solicitar o participar en actividades de aprendizaje.

Una misma persona puede enseñar o aprender según la actividad, sin cambiar su rol técnico.

## Flujo de planificación

El flujo de planificación parte actualmente del **MVP V3** y produce WBS, USM, backlog y subtareas técnicas. Estos documentos ya fueron regenerados y mantienen trazabilidad con V3. [derivar-planificacion-mvp](skills/derivar-planificacion-mvp/SKILL.md) coordina la documentación local y su revisión. Al final, aplica [crear-sprints](skills/crear-sprints/SKILL.md) para estimar las HU, simular capacidad del equipo y proponer una distribución por objetivos y dependencias. Al ejecutar esa etapa, el resultado se guarda en `docs/sprints.md`. La sincronización externa se realiza por separado mediante `actualizar-jira`.
