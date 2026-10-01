---
name: readme
description: Generar o actualizar el README principal del proyecto con la documentación vigente, los enlaces externos y una descripción breve del producto.
---

# README del proyecto

Usar esta skill cuando el usuario solicite crear, actualizar, ordenar o regenerar el `README.md` del repositorio.

## Fuente y alcance

- Leer `AGENTS.md` y verificar los archivos existentes antes de escribir enlaces.
- Mantener la especificación de `docs/mvp.md` como fuente de verdad del producto.
- No modificar `docs/mvp.md`, el backlog, la WBS, la USM ni Jira desde esta skill.
- No hacer commit ni push automáticamente.

## Estructura vigente

El README debe contener estas secciones, en este orden:

1. Título y descripción breve del proyecto.
2. `## Documentación principal`, con únicamente estos documentos:
   - `docs/mvp.md` — Especificación del MVP.
   - `docs/wbs.md` — WBS del MVP.
   - `docs/usm.md` — USM del MVP.
   - `docs/backlog.md` — Backlog del MVP.
   - `docs/sc.md` — SC del MVP.
   - `docs/metodologia.md` — Metodología de planificación.
   - `docs/alcance-futuro.md` — Alcance futuro.
3. `## Enlaces externos`, con:
   - el tablero Jira del proyecto, si puede verificarse;
   - el repositorio GitHub canónico, obtenido del remoto o de una redirección verificada.
   - la carpeta de Google Drive del proyecto: `https://drive.google.com/drive/folders/1yT3fRMZmn2E0MRizzJtzh7e1q5G1IJOz`.
4. `## Recursos`, solo si existen recursos vigentes que el usuario quiera destacar.
5. `## Roles principales`, usando la terminología Docente, Alumno y Administrador cuando corresponda.
6. Una sección breve sobre el flujo de planificación, indicando que WBS, USM y backlog parten del MVP.

## Reglas de contenido

- Usar las convenciones `WBS`, `USM` y `backlog`.
- No volver a incluir `docs/graph-de-skills.md` ni `docs/loop-basico.md`.
- No listar todas las skills en el README; solo mencionar el flujo si aporta contexto.
- No inventar URLs, nombres de proyectos, roles ni funcionalidades.
- Comprobar que cada enlace local apunta a un archivo existente.
- Mantener el README breve: funciona como índice del proyecto, no como copia de la documentación.

## Resultado

Presentar o guardar el README según lo que solicite el usuario. Después de actualizarlo, informar qué enlaces o secciones se agregaron, eliminaron o conservaron.
