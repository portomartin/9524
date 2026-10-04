---
name: crear-sprints
description: Estimar historias de usuario en story points, simular capacidad según integrantes y dedicación, y organizar sprints por objetivos, dependencias y velocidad. Usar al planificar sprints o reconstruir una distribución perdida; permite trabajar con backlog local o Jira.
---

# Crear sprints

Preparar una planificación trazable en español, separando capacidad horaria, estimaciones relativas y velocidad observada. Puede ejecutarse solo la estimación, la simulación o la distribución que solicite el usuario; no exigir todo el flujo.

## Entradas y fuentes

- Leer las instrucciones del proyecto y la especificación que declaren vigente. No fijar una versión o ruta de MVP para todos los proyectos.
- Obtener las HU actuales con identificador, descripción, criterios de aceptación, subtareas, estimación existente y dependencias. Si la fuente es Jira, consultar todas las páginas y descubrir los campos de puntos y sprint del sitio; no asumir sus identificadores.
- Recuperar del contexto: integrantes, horas semanales por persona, duración del sprint, ausencias, margen de coordinación e imprevistos, fechas y restricciones de entrega. Preguntar solo los datos necesarios que falten. Para una simulación, se pueden proponer supuestos explícitos.
- Conservar estimaciones acordadas salvo que el usuario pida reestimar. Distinguir estimación recuperada, nueva estimación y supuesto. Una HU recreada no conserva necesariamente el historial de la eliminada: no afirmar que se recuperaron puntos sin evidencia.
- Señalar diferencias entre Jira y el MVP; no resolverlas agregando requisitos ni cambiando la especificación. Se puede estimar condicionalmente la variante solicitada, identificándola.

## Capacidad horaria

Calcular por persona, permitiendo dedicaciones distintas:

`horas brutas = suma(horas semanales por persona × semanas del sprint − ausencias dentro de esa dedicación)`

`horas planificables = horas brutas × (1 − reserva)`

No descontar dos veces reuniones o ausencias ya excluidas de las horas informadas. Usar una reserva del 25 % solo como supuesto inicial cuando el usuario no haya fijado otra. Mostrar el cálculo exacto y cualquier redondeo conservador. La capacidad planificable incluye desarrollo, revisión, pruebas, integración y correcciones necesarias para terminar las HU; no volver a descontar estas actividades como reserva.

La suma es un techo orientativo: indicar restricciones relevantes de habilidades o disponibilidad compartida. No suponer que duplicar integrantes duplica automáticamente la entrega.

## Estimar las historias

- Usar la escala relativa 1, 2, 3, 5, 8, 13, salvo que el equipo use otra. Comparar con una historia de referencia del mismo backlog; valorar complejidad, trabajo e incertidumbre.
- Estimar la HU completa: frontend, backend, permisos, validaciones, integración, pruebas y criterios de aceptación. Sus subtareas explican el trabajo; no sumar otra vez sus puntos al total de la HU. Tampoco sumar puntos de épicas junto a sus historias.
- Como orientación inicial: 1–2 para cambios pequeños y claros; 3 para una funcionalidad sencilla con patrones conocidos; 5 para varias validaciones o integraciones moderadas; 8 para reglas cruzadas, concurrencia o incertidumbre significativa; 13 para historias grandes que conviene dividir antes de comprometer.
- Expresar supuestos que cambien materialmente la estimación. Las dependencias condicionan el orden; no equivalen por sí solas a más esfuerzo. Contar trabajo compartido una sola vez e indicar dónde queda cubierto.
- No agregar funcionalidades pendientes como si ya estuvieran aprobadas. Si una definición faltante impide estimar razonablemente, marcar la HU como pendiente o dar una estimación condicional, sin falsa precisión.
- No rebajar puntos para cumplir una fecha. No asignar puntos según cantidad de personas, horas disponibles ni un reparto uniforme entre historias.

## Capacidad en puntos y escenarios

Las horas no determinan los story points. No establecer equivalencias como un punto igual a cierta cantidad de horas.

Con historial comparable, calcular la velocidad a partir de los puntos de HU realmente terminadas por sprint y presentar su variación. No contar trabajo parcial ni cambiar puntos retrospectivamente para ajustar la velocidad. Revisar comparabilidad si cambió el equipo, su dedicación o la escala.

Sin historial, declarar una hipótesis de velocidad negociable. Si el usuario ya adoptó una, reutilizarla. Los 20 puntos semanales del ejemplo son una hipótesis de ese equipo, no un valor por defecto universal. Contrastar el conjunto de HU con la disponibilidad y dependencias; si se dispone de horas estimadas por tarea, sirven como control de viabilidad, no como fórmula para producir puntos.

Cuando ayude, comparar escenarios con distintas dedicaciones, reservas o velocidades, etiquetando cada variable como dato o supuesto. No recalcular velocidad automáticamente en proporción a las horas. Recalibrar después de 2–3 sprints con datos reales.

## Distribuir en sprints

Cuando el usuario pida crear o planificar sprints, entregar la asignación concreta de HU a cada sprint; no terminar únicamente con estimaciones, capacidad o una cantidad sugerida de sprints. Si pide solo estimar, respetar ese alcance. Reutilizar los sprints existentes cuando corresponda y distinguir una distribución propuesta de una aplicada en Jira.

1. Definir un objetivo concreto por sprint y ordenar dependencias. Priorizar entregas utilizables; evitar separar sistemáticamente frontend y backend en sprints diferentes.
2. Seleccionar HU completas dentro de la capacidad provisional. Considerar bloqueos, especialidades y trabajo compartido. Si una dependencia se implementa en el mismo sprint, explicar el orden y el riesgo.
3. Dejar visibles las HU que no caben y las que necesitan refinamiento. Una historia de 13 puntos puede requerir descomposición, pero no crear historias nuevas ni cambiar alcance silenciosamente.
4. Mostrar puntos por sprint y total pendiente. `techo(total de puntos / velocidad)` es una referencia aritmética, no un calendario garantizado: las HU indivisibles y dependencias pueden requerir más sprints.
5. Si hay una fecha o cantidad fija de sprints insuficiente, exponer la brecha y opciones de priorización, plazo o capacidad. No modificar estos compromisos automáticamente.

Presentar la distribución con estas columnas:

| Sprint | Objetivo | HU asignadas (ID y puntos) | Total SP | Capacidad SP | Dependencias o riesgos |
|---|---|---|---:|---:|---|

Agregar una lista separada de HU sin asignar con sus puntos y el motivo (falta de capacidad, bloqueo o refinamiento pendiente). Si no hay un límite de sprints, proponer los necesarios; si hay un límite, conservarlo y mostrar el remanente. Una HU no debe aparecer comprometida en más de un sprint. Las subtareas acompañan a su historia sin consumir puntos adicionales.

Antes de presentar, comprobar que cada HU considerada esté asignada una sola vez o figure como pendiente, que las sumas por sprint coincidan con sus historias y que la suma de asignadas y pendientes coincida con el total estimado. No superar la capacidad declarada sin señalarlo como una excepción que requiere una decisión del equipo. Las dependencias deben resolverse antes de sus consumidoras o tener un orden viable explícito dentro del mismo sprint.

## Resultado y aplicación

Entregar, según el pedido:

- Supuestos del equipo y cálculo de capacidad horaria.
- Tabla de HU con identificador, título, puntos, motivo y dudas relevantes.
- Velocidad observada o hipotética, claramente diferenciadas.
- Tabla de sprints con objetivo, HU, puntos, dependencias y remanente.
- Fuentes y límites de la estimación. Distinguir documento propuesto de cambios efectivamente guardados.

Estimar o simular no implica autorización para modificar Jira. Si el usuario pide cargar estimaciones o crear/distribuir sprints, ejecutar lo autorizado sin una confirmación redundante; en caso contrario, presentar la propuesta. No cambiar estados, fechas, alcance o responsables por el solo hecho de planificar.

Al aplicar en Jira: leer el estado actual, reutilizar sprints existentes adecuados, escribir únicamente los campos autorizados y verificar por lectura los puntos y pertenencia finales. Conservar subtareas vinculadas a su HU. Antes de reintentar una creación o una respuesta ambigua, comprobar qué se guardó para evitar duplicados. Detener las escrituras ante un conflicto persistente y reportar cambios realizados y pendientes. No cerrar ni iniciar sprints sin que el pedido lo incluya.

Cuando se guarde documentación, registrar la fecha, entradas, supuestos, estimaciones y asignaciones en el destino acordado, conservando trazabilidad por clave de HU. No modificar el MVP para justificar la planificación.

## Ejemplo de calibración

Leer [el ejemplo](references/ejemplo-capacidad.md) cuando se necesite reproducir el escenario de seis integrantes de esta conversación o explicar la diferencia entre horas y puntos.
