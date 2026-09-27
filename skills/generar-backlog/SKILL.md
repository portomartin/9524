---
name: generar-backlog
description: Transformar la especificación vigente del MVP en épicas e historias de usuario trazables. Usar cuando se solicite crear o actualizar el backlog del proyecto.
---

# Generar backlog

Leer `AGENTS.md` y `docs/mvp.md` antes de proponer cambios.

Derivar el contenido únicamente del MVP, sin leer la WBS ni el USM como entradas. Si existe `docs/backlog.md`, consultarlo solo para preservar identificadores, épicas y formato compatibles con el MVP; no usarlo como fuente de alcance. El backlog puede prepararse aunque no existan WBS ni USM.

## Resultado

- Mantener las épicas existentes cuando sigan representando capacidades distintas.
- Crear historias de usuario con el formato: `Como [rol], quiero [acción], para [beneficio]`.
- Asignar cada historia a una épica y evitar historias duplicadas.
- No inventar funcionalidades que no estén respaldadas por el MVP.
- Separar claramente historias de Docente, Alumno y Administrador.
- Proponer criterios de aceptación breves para cada historia.
- Indicar la sección del MVP que respalda cada historia y señalar ambigüedades pendientes.
- No inventar prioridades, estimaciones ni decisiones técnicas; dejarlas pendientes si el MVP no las define.

Presentar el borrador en Markdown. Si se aprueba, guardarlo en `docs/backlog.md`, salvo que el usuario indique otra ubicación o formato. No modificar el MVP, la WBS ni el USM desde esta rama.
