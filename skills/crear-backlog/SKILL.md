---
name: crear-backlog
description: Transformar la especificación vigente del MVP en épicas e historias de usuario. Usar cuando se solicite crear o actualizar el backlog del proyecto.
---

# Generar backlog

Leer `AGENTS.md` y la versión indicada del MVP (`docs/mvp-v1.md`, `docs/mvp-v2.md` o `docs/mvp-v3.md`) antes de proponer cambios.

Derivar el contenido únicamente del MVP, sin leer la WBS ni el USM como entradas. Si existe `docs/backlog.md`, consultarlo solo para preservar identificadores, épicas y formato compatibles con el MVP; no usarlo como fuente de alcance. El backlog puede prepararse aunque no existan WBS ni USM.

El backlog es un documento vivo: las correcciones humanas aprobadas deben conservarse. Antes de regenerar, comparar el backlog existente y no eliminar introducciones, aclaraciones, criterios o decisiones agregadas manualmente. Si hay un conflicto con el MVP, señalarlo en vez de sobrescribirlo.

Las decisiones aprobadas deben quedar registradas en el backlog, dentro de la HU correspondiente o en una sección claramente identificada como `Decisiones aprobadas`. Antes de volver a formular una pregunta, consultar esas decisiones y tratarlas como restricciones vigentes. Una decisión aprobada debe dejar de aparecer como pendiente.

## Resultado

- Mantener las épicas existentes cuando sigan representando capacidades distintas.
- Incluir debajo de cada título de épica una única sección `Introducción`, derivada exclusivamente del MVP, que integre en párrafos breves el propósito de la épica, su objetivo, el valor para el usuario y el resultado esperado. No crear secciones separadas para esos conceptos.
- Crear historias de usuario con el formato: `Como [rol], quiero [acción], para [beneficio]`.
- Titular cada historia con el formato `HU01 Nombre de la historia`, sin guion dentro del identificador ni raya entre el identificador y el nombre.
- Colocar la formulación `Como...` inmediatamente debajo del título de cada historia. Es el contenido principal de la HU y debe aparecer antes de refinamientos, pendientes o criterios de aceptación.
- Asignar cada historia a una épica y evitar historias duplicadas.
- No inventar funcionalidades que no estén respaldadas por el MVP.
- Separar claramente las historias de `GUEST`, `USER` y `ADMIN` cuando sus permisos o beneficios sean diferentes.
- Proponer un criterio de aceptación breve para cada historia, presentado como una viñeta con la etiqueta `**✅ Aceptación:**` y texto iniciado con mayúscula.
- Señalar las ambigüedades como pendientes dentro de la HU correspondiente.
- No inventar prioridades, estimaciones ni decisiones técnicas; dejarlas pendientes si el MVP no las define.

## Propuestas de refinamiento

La IA puede enriquecer el backlog, pero debe distinguir el origen y el estado de cada aporte:

- **Derivado del MVP:** requisito respaldado directamente por la versión indicada del MVP.
- **Corrección humana:** contenido aprobado por el equipo y conservado del backlog existente.
- **Propuesta de refinamiento:** mejora sugerida por la IA para aclarar una HU, detectar un caso límite o facilitar el desarrollo.
- **Pendiente de decisión:** definición necesaria que el MVP todavía no resuelve.
- **Fuera de alcance:** funcionalidad o regla que no debe incorporarse al MVP.

Los refinamientos y pendientes específicos deben quedar dentro de la HU correspondiente, después de sus criterios de aceptación. Solo las decisiones o recomendaciones transversales pueden quedar en una sección general.

El contenido de `🛠️ Refinamiento aplicado` y `❓ Pendientes de decisión` debe escribirse siempre como listas Markdown con viñetas atómicas. Cada viñeta debe comenzar con mayúscula y expresar una sola acción, decisión, campo, valor, estado, límite o regla; no agrupar varias ideas con comas, punto y coma o frases coordinadas. No usar párrafos corridos en esas secciones.

Para facilitar la lectura, concentrar los emojis en los títulos de sección y no usarlos en las viñetas. Usar `🛠️ Refinamiento aplicado`, `❓ Pendientes de decisión`, `📌 Reglas vigentes` y `⚠️ Estado de alcance` cuando correspondan.

## Refinamiento informado por prácticas actuales

Cuando el usuario solicite más profundidad o cuando una definición pendiente afecte de forma importante la calidad del producto, la IA puede proponer alternativas basadas en prácticas actuales, productos comparables, estándares y patrones habituales del mercado.

Para cada propuesta informada debe indicar, cuando corresponda:

- La práctica o patrón observado.
- El problema que ayuda a resolver.
- Alternativas posibles.
- Impacto en alcance, experiencia de usuario, seguridad, operación o desarrollo.
- Estado: propuesta, pendiente de aprobación o fuera de alcance.
- Fuentes consultadas o aclaración de que se trata de una inferencia.

Si la propuesta depende de información que puede cambiar con el tiempo, investigar fuentes actuales antes de presentarla. Priorizar documentación oficial, estándares reconocidos y referencias primarias; no presentar una práctica de mercado como requisito del producto sin aprobación humana.

Las propuestas que agreguen alcance, modifiquen una regla de negocio o cambien una exclusión no deben incorporarse como requisitos aprobados. Deben presentarse separadas y esperar confirmación humana. Las propuestas de redacción o detalle que no cambien el alcance pueden incorporarse como refinamiento, identificándolas como tales cuando corresponda.

Cuando una definición pendiente sea necesaria para implementar una HU, documentarla como pendiente en lugar de inventar una respuesta. Si el equipo aprueba una propuesta que cambia el alcance o una regla del producto, solicitar primero la actualización de la versión activa del MVP y luego sincronizar el backlog.

Cuando una decisión aprobada modifique el alcance o una regla de negocio del MVP, registrar también el cambio en la versión activa del MVP y en el registro de cambios del proyecto antes de actualizar los documentos derivados. Si la decisión solo aclara o refina una HU sin cambiar el alcance, conservarla en el backlog sin modificar el MVP.

Las historias de usuario deben aparecer después del contenido introductorio de su épica. No crear una sección redundante llamada “Subítems”: cuando el backlog se traslade a una herramienta de gestión, las historias podrán representarse como subítems de la épica.

Presentar el borrador en Markdown. Si se aprueba, guardarlo en `docs/backlog.md`, salvo que el usuario indique otra ubicación o formato. No modificar el MVP, la WBS ni el USM desde esta rama.
