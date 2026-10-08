# Plataforma de intercambio de aprendizajes

Este repositorio estudia dos enfoques independientes para planificar y desarrollar el mismo producto. El proyecto WBS representa el modelo de trabajo principal y vigente. El proyecto SDD ocupa un lugar alternativo y secundario dentro del repositorio, aunque explora un modelo de desarrollo más centrado en inteligencia artificial.

## Proyecto principal: desarrollo humano asistido por IA

[`proyecto-wbs/`](proyecto-wbs/README.md) representa un enfoque tradicional basado en el WBS original. El desarrollo sigue estando en manos de las personas y la IA funciona como una herramienta de asistencia.

1. Parte de una lista inicial de tareas que no fue derivada sistemáticamente del MVP mediante skills.
2. Cada integrante desarrolla una parte desde su propio entorno, con interpretaciones, criterios técnicos, ritmos y decisiones diferentes.
3. La responsabilidad principal de implementar, coordinar e integrar permanece distribuida entre las personas.
4. Los sprints concentran gran parte del esfuerzo en desarrollar tareas individuales y luego consolidarlas mediante ramas, pull requests, revisiones y merges.
5. Conserva una mayor intervención y creatividad individual, pero también introduce más variabilidad, bugs, retrabajo y demoras.
6. Es el enfoque vigente y tradicional, aunque se encuentra en vías de extinción frente a modelos de desarrollo centrados en especificaciones e IA.
7. Consolidar backend y frontend suele convertirse en un infierno: aunque ambas partes funcionen por separado, los errores humanos de comunicación e interpretación producen contratos, modelos, validaciones e interfaces incompatibles. Una parte importante de los sprints termina consumida en detectar diferencias, resolver conflictos y rehacer trabajo durante la integración.

Documentos:

- [MVP v1.0](proyecto-sdd/mvp-v1.md)
- [Historias de usuario (USM)](proyecto-wbs/historias-de-usuario.md)
- [Estructura de desglose del trabajo (WBS)](proyecto-wbs/wbs-original.md)
- [Scrum en Jira](https://martinporto.atlassian.net/jira/software/projects/WBSO/boards/35/backlog)

_[Proceso para crear y mantener Jira](proyecto-wbs/skills/crear-jira-desde-wbs-original/SKILL.md)_

## Proyecto alternativo: SDD centrado en IA

[`proyecto-sdd/`](proyecto-sdd/README.md) explora un modelo de *Spec-Driven Development*. El equipo humano concentra su trabajo en desarrollar y refinar la especificación, el MVP y los sprints. La creación del backend y del frontend se delega a agentes de IA que trabajan a partir de una fuente común y controlada.

En este enfoque, el trabajo humano consiste principalmente en:

- refinar la especificación y eliminar ambigüedades;
- controlar el alcance y la coherencia del MVP;
- revisar y validar lo producido por la IA;
- conducir los sprints desde la especificación;
- ocuparse de la integración final y del despliegue.

La diferencia central entre ambos enfoques es:

> En el proyecto WBS, las personas desarrollan con asistencia de IA. En el proyecto SDD, las personas dirigen y refinan mientras la IA implementa.

El proyecto SDD mantiene sus propios artefactos, código, skills y seguimiento. Sus tareas, estados, sprints e issues no deben mezclarse automáticamente con los del proyecto WBS principal.

Documentos:

- [MVP v3.0](proyecto-sdd/mvp-v3.md)
- [Proyecto SDD](proyecto-sdd/README.md)
- [Tablero Jira BH95](https://martinporto.atlassian.net/jira/software/projects/BH95/boards/2/backlog)

## Estructura

```text
proyecto-wbs/   Proyecto principal: desarrollo humano asistido por IA
proyecto-sdd/   Proyecto alternativo: desarrollo centrado en especificaciones e IA
```
