---
name: generar-backlog
description: Transformar la especificación vigente del MVP en épicas e historias de usuario trazables. Usar cuando se solicite crear o actualizar el backlog del proyecto.
---

# Generar backlog

Leer `AGENTS.md` y `docs/mvp.md` antes de proponer cambios.

Derivar el contenido únicamente del MVP, sin leer la WBS ni el USM como entradas. Si existe `docs/backlog.md`, consultarlo solo para preservar identificadores, épicas y formato compatibles con el MVP; no usarlo como fuente de alcance. El backlog puede prepararse aunque no existan WBS ni USM.

El backlog es un documento vivo: las correcciones humanas aprobadas deben conservarse. Antes de regenerar, comparar el backlog existente y no eliminar introducciones, aclaraciones, criterios o decisiones agregadas manualmente. Si hay un conflicto con el MVP, señalarlo en vez de sobrescribirlo.

Las decisiones aprobadas deben quedar registradas en el backlog, dentro de la HU correspondiente o en una sección claramente identificada como `Decisiones aprobadas`. Antes de volver a formular una pregunta, consultar esas decisiones y tratarlas como restricciones vigentes. Una decisión aprobada debe dejar de aparecer como pendiente.

## Resultado

- Mantener las épicas existentes cuando sigan representando capacidades distintas.
- Incluir debajo de cada título de épica una introducción breve que explique su propósito y alcance, derivada exclusivamente del MVP.
- Enriquecer cada épica con objetivo, valor para el usuario, alcance, fuera de alcance cuando corresponda, resultado esperado y trazabilidad al MVP.
- Incluir un storytelling visual breve por épica, preferentemente un diagrama Mermaid simple del recorrido del usuario o del resultado que la épica habilita. Debe ser comprensible y no representar arquitectura técnica.
- Construir cada storytelling únicamente con la introducción, el alcance y las historias de su propia épica. El último nodo debe representar un resultado alcanzado dentro de esa épica, sin adelantar capacidades de otras épicas.
- Crear historias de usuario con el formato: `Como [rol], quiero [acción], para [beneficio]`.
- Asignar cada historia a una épica y evitar historias duplicadas.
- No inventar funcionalidades que no estén respaldadas por el MVP.
- Separar claramente historias de Docente, Alumno y Administrador.
- Proponer criterios de aceptación breves para cada historia.
- Indicar la sección del MVP que respalda cada historia y señalar ambigüedades pendientes.
- No inventar prioridades, estimaciones ni decisiones técnicas; dejarlas pendientes si el MVP no las define.

## Propuestas de refinamiento

La IA puede enriquecer el backlog, pero debe distinguir el origen y el estado de cada aporte:

- **Derivado del MVP:** requisito respaldado directamente por `docs/mvp.md`.
- **Corrección humana:** contenido aprobado por el equipo y conservado del backlog existente.
- **Propuesta de refinamiento:** mejora sugerida por la IA para aclarar una HU, detectar un caso límite o facilitar el desarrollo.
- **Pendiente de decisión:** definición necesaria que el MVP todavía no resuelve.
- **Fuera de alcance:** funcionalidad o regla que no debe incorporarse al MVP.

Los refinamientos y pendientes específicos deben quedar dentro de la HU correspondiente, después de sus criterios de aceptación y trazabilidad. Solo las decisiones o recomendaciones transversales pueden quedar en una sección general.

Cada pendiente de decisión debe incluir, cuando sea posible, una `Recomendación de IA` basada en prácticas actuales, junto con su motivo, alternativas, impacto y estado `pendiente de aprobación`. La recomendación no se considera una decisión aprobada hasta que el usuario la confirme.

La recomendación debe ser concreta y accionable: debe responder cada punto planteado en el pendiente, no limitarse a describir una buena práctica general. Cuando el pendiente solicite campos, valores permitidos, estados, límites, condiciones o reglas, enumerar una propuesta específica para cada uno. Distinguir explícitamente qué parte se deriva del MVP y qué parte es una sugerencia nueva de la IA; no incorporar la sugerencia como requisito aprobado.

El contenido de `Refinamiento aplicado`, `Pendientes de decisión` y `Recomendación de IA` debe escribirse siempre como listas Markdown con viñetas atómicas. Cada viñeta debe expresar una sola acción, decisión, campo, valor, estado, límite o regla; no agrupar varias ideas con comas, punto y coma o frases coordinadas. No usar párrafos corridos en esas secciones. En `Recomendación de IA`, usar una viñeta rotulada para `Recomendación`, `Motivo`, `Alternativas`, `Impacto` y `Estado`, con subviñetas atómicas cuando haya varios elementos.

Para facilitar la lectura, usar emojis semánticos relacionados con el contenido de cada subviñeta, no repetir automáticamente el mismo emoji en todas. Por ejemplo: `✉️` para correo, `🔐` para contraseñas o seguridad, `📍` para ubicación, `👤` para perfil, `📚` para temas de aprendizaje, `🗓️` para disponibilidad, `🪙` para créditos, `🔎` para búsqueda, `🤝` para compatibilidad, `⭐` para calificaciones y `🛡️` para moderación. Las etiquetas principales (`Recomendación`, `Motivo`, `Alternativas`, `Impacto` y `Estado`) no deben llevar emoji; usar emojis solo en las viñetas de contenido debajo de ellas.

## Refinamiento informado por prácticas actuales

Cuando el usuario solicite más profundidad o cuando una definición pendiente afecte de forma importante la calidad del producto, la IA puede proponer alternativas basadas en prácticas actuales, productos comparables, estándares y patrones habituales del mercado.

Para cada propuesta informada debe indicar, cuando corresponda:

- La práctica o patrón observado.
- El problema que ayuda a resolver.
- Alternativas posibles.
- Recomendación de la IA.
- Impacto en alcance, experiencia de usuario, seguridad, operación o desarrollo.
- Estado: propuesta, pendiente de aprobación o fuera de alcance.
- Fuentes consultadas o aclaración de que se trata de una inferencia.

Si la propuesta depende de información que puede cambiar con el tiempo, investigar fuentes actuales antes de presentarla. Priorizar documentación oficial, estándares reconocidos y referencias primarias; no presentar una práctica de mercado como requisito del producto sin aprobación humana.

Las propuestas que agreguen alcance, modifiquen una regla de negocio o cambien una exclusión no deben incorporarse como requisitos aprobados. Deben presentarse separadas y esperar confirmación humana. Las propuestas de redacción o detalle que no cambien el alcance pueden incorporarse como refinamiento, identificándolas como tales cuando corresponda.

Cuando una definición pendiente sea necesaria para implementar una HU, documentarla como pendiente en lugar de inventar una respuesta. Si el equipo aprueba una propuesta que cambia el alcance o una regla del producto, solicitar primero la actualización de `docs/mvp.md` y luego sincronizar el backlog.

Cuando una decisión aprobada modifique el alcance o una regla de negocio del MVP, registrar también el cambio en `docs/mvp.md` y en el registro de cambios del proyecto antes de actualizar los documentos derivados. Si la decisión solo aclara o refina una HU sin cambiar el alcance, conservarla en el backlog sin modificar el MVP.

Las historias de usuario deben aparecer después del contenido introductorio de su épica para conservar la trazabilidad del documento. No crear una sección redundante llamada “Subítems”: cuando el backlog se traslade a una herramienta de gestión, las historias podrán representarse como subítems de la épica.

Cuando una HU use conceptos relevantes del negocio, agregar una sección `#### Objetos de dominio involucrados`. Identificar cada objeto con nombre, definición breve, atributos o relaciones relevantes y, cuando aplique, sus estados principales. No inventar objetos ajenos al MVP: si el concepto es ambiguo, presentarlo como propuesta pendiente de validación humana. Diferenciar objetos de dominio —por ejemplo, Sesión, Solicitud, Propuesta, Crédito o Calificación— de pantallas, botones o tareas técnicas.

El detalle completo de los objetos debe mantenerse en `docs/modelo-dominio.md`. Cada objeto mencionado en el backlog debe enlazar a su definición mediante un enlace relativo, por ejemplo `[Sesión](modelo-dominio.md#sesión)`. El modelo de dominio debe derivarse del MVP, documentar definición, atributos, relaciones, estados y reglas, y marcar como `Propuesta pendiente de aprobación` cualquier detalle que el MVP no resuelva. No duplicar definiciones extensas dentro del backlog.

Al ejecutar `generar-backlog`, esta revisión de dominio es obligatoria: leer o crear `docs/modelo-dominio.md`, detectar los objetos de negocio relevantes de cada HU, agregar en la HU una referencia breve enlazada y sincronizar en el modelo de dominio su definición completa. La ejecución debe preservar las definiciones y decisiones humanas existentes, actualizar solo lo que se derive del MVP o esté marcado como propuesta, y verificar que cada enlace del backlog apunte a una definición existente.

Para documentar profesionalmente cada objeto en `docs/modelo-dominio.md`, usar cuando corresponda esta estructura:

- `Definición`: qué representa el objeto dentro del negocio.
- `Identidad`: identificador o criterio que lo distingue.
- `Atributos`: tabla con nombre, descripción, tipo conceptual y obligatoriedad cuando esté definido.
- `Relaciones`: vínculos con otros objetos y cardinalidad cuando pueda determinarse.
- `Estados propuestos`: ciclo de vida y transiciones válidas.
- `Reglas de negocio`: invariantes y comportamientos que debe respetar.
- `Decisiones pendientes`: aspectos que requieren aprobación humana.

No definir un objeto circularmente. Diferenciar relaciones —por ejemplo, “una Reserva corresponde a una Sesión”— de reglas de negocio —por ejemplo, “una Reserva confirmada puede cancelarse antes del inicio”—. No inventar tipos técnicos, cardinalidades o estados como hechos aprobados: marcarlos como propuestas cuando el MVP no los establezca.

Antes de conservar un storytelling, verificar que cada nodo pertenezca al alcance de la épica, que el resultado final no requiera otra épica y que no aparezcan términos o acciones propios de capacidades posteriores. Si el flujo conduce a otra épica, terminar con un resultado neutral como “Perfil listo”, “Propuesta publicada” o “Sesión completada”.

Presentar el borrador en Markdown. Si se aprueba, guardarlo en `docs/backlog.md`, salvo que el usuario indique otra ubicación o formato. No modificar el MVP, la WBS ni el USM desde esta rama.
