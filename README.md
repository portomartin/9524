# Plataforma de intercambio de aprendizajes

Proyecto universitario para diseñar un MVP de una plataforma donde las personas puedan enseñar y aprender mediante intercambios directos, clases grupales y créditos virtuales.

## Documentación principal

- [Especificación del MVP](docs/mvp.md)
- [WBS del MVP](docs/wbs.md)
- [USM del MVP](docs/usm.md)
- [Backlog del MVP](docs/backlog.md)
- [Metodología de planificación](docs/metodologia.md)
- [Ejemplo básico de graph de skills](docs/graph-de-skills.md)
- [Ejemplo básico de loop](docs/loop-basico.md)
- [Alcance futuro](docs/alcance-futuro.md)
- [Registro de cambios](docs/cambios.md)
- [Skill para crear WBS](skills/crear-wbs/SKILL.md)
- [Skill para crear USM](skills/crear-usm/SKILL.md)
- [Skill para crear épicas](skills/crear-epicas/SKILL.md)
- [Skill coordinador del grafo de planificación](skills/coordinar-planificacion/SKILL.md)

## Recursos

- Los diagramas vigentes están en `docs/assets/`.
- Los documentos y scripts heredados de la estructura anterior están en `old/` y se conservan como referencia histórica.

## Roles principales

- **Docente:** ofrece conocimientos o habilidades.
- **Alumno:** solicita o participa en actividades de aprendizaje.

Una misma persona puede desempeñar ambos roles.

## Skills del proyecto

Las skills de la carpeta `skills/` ayudan a transformar la especificación en backlog, historias de usuario y documentación revisable.

El flujo de planificación parte de `docs/mvp.md` y tiene tres ramas independientes: WBS, USM y backlog. Cada una deriva su contenido directamente del mismo MVP. El skill `coordinar-planificacion` coordina las tres y presenta sus resultados; el backlog se guardará cuando se ejecute y apruebe su generación.
