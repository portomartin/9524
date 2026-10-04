# Planificación de sprints — MVP V3

**Fecha:** 2026-10-04.
**Estado:** distribución y estimaciones aplicadas y verificadas en Jira el 2026-10-04; capacidad y refinamientos funcionales siguen siendo provisionales.
**Fuentes:** [MVP V3](mvp-v3.md), [backlog](backlog.md), [subtareas](subtareas.md) y estimaciones acordadas en la conversación. Las claves Jira corresponden a las HU consultadas en esta sesión.

## Equipo y capacidad

| Dato | Valor | Base |
|---|---:|---|
| Integrantes | 6 | Informado por el usuario |
| Horas semanales por persona | 15 | Simulación solicitada |
| Duración | 1 semana | Acordada |
| Horas brutas | 90 h | 6 × 15 |
| Reserva | 22,5 h (25 %) | Coordinación e imprevistos |
| Horas planificables | 67,5 h | 90 × 0,75 |
| Compromiso horario orientativo | 65 h | Redondeo conservador |
| Capacidad de referencia | 20 SP/sprint | Hipótesis aceptada, no velocidad observada |

Se supone que no hay ausencias adicionales y que el equipo dispone de habilidades para frontend, backend y pruebas. Las 65 horas incluyen revisión, integración y correcciones. No existe una conversión de horas a puntos. Recalibrar después de 2–3 sprints con historias realmente terminadas.

## Estimaciones conservadas

Son las nuevas estimaciones propuestas y aceptadas en esta conversación, no una recuperación de las estimaciones históricas perdidas. Incluyen ambas subtareas técnicas sin volver a sumar sus puntos. HU05 sirve como referencia de funcionalidad sencilla de 3 puntos.

| HU | Jira | Historia | SP | Motivo |
|---|---|---|---:|---|
| HU01 | BH95-146 | Explorar como GUEST | 5 | Listados y detalle públicos con privacidad |
| HU02 | BH95-147 | Consultar confianza pública | 8 | Reputación, rankings y trending por definir |
| HU03 | BH95-148 | Registrarse cuando sea necesario | 5 | Registro y conservación del contexto |
| HU04 | BH95-149 | Autenticarse | 5 | Sesiones seguras y rutas protegidas |
| HU05 | BH95-150 | Completar el perfil | 3 | Edición básica y validación |
| HU06 | BH95-151 | Publicar una propuesta | 8 | Publicación, borrador y validaciones |
| HU07 | BH95-152 | Registrar un aprendizaje buscado | 3 | Alta, edición y pausa |
| HU08 | BH95-153 | Buscar aprendizajes | 5 | Búsqueda pública y paginación |
| HU09 | BH95-154 | Filtrar resultados | 5 | Filtros combinables y disponibilidad |
| HU10 | BH95-155 | Encontrar compatibilidades | 8 | Reglas cruzadas y reciprocidad |
| HU11 | BH95-156 | Gestionar disponibilidad | 8 | Franjas concretas y carga masiva |
| HU12 | BH95-157 | Publicar la agenda | 3 | Visibilidad y privacidad |
| HU13 | BH95-158 | Crear una sesión solicitada | 8 | Condiciones y conflictos de horario |
| HU14 | BH95-159 | Gestionar el estado de una sesión | 8 | Transiciones y reserva de franjas |
| HU15 | BH95-160 | Finalizar una sesión | 3 | Cierre válido sin duplicados |
| HU16 | BH95-161 | Intercambiar con créditos | 8 | Consistencia de saldos e idempotencia |
| HU17 | BH95-162 | Consultar historial | 5 | Actividad integrada y privacidad |
| HU18 | BH95-163 | Calificarse mutuamente | 5 | Elegibilidad, unicidad y promedio |
| HU19 | BH95-164 | Denunciar contenido o usuarios | 3 | Validaciones y registro |
| HU20 | BH95-165 | Administrar seguridad | 8 | Moderación, permisos y auditoría |
| **Total** | | | **114** | |

Se supone autenticación con herramientas estándar y reutilización de componentes. La infraestructura inicial no está desglosada en estas 20 HU; comprobar su disponibilidad antes del primer compromiso. HU18 implementa el cálculo y endpoint de reputación que reutiliza HU02; no implementarlo dos veces.

Rankings y trending sí aparecen en el MVP V3 vigente; se corrige la observación anterior basada en una versión local previa. Siguen pendientes sus reglas exactas. Los puntos de HU02 y de las demás historias con decisiones abiertas son provisionales hasta resolverlas.

## Distribución propuesta

Se propone una secuencia de **7 sprints de una semana**, sin fechas calendario nuevas. Se preservan los 114 puntos: seis sprints son solo el mínimo aritmético a 20 SP. Esta alternativa conservadora prioriza dependencias y entregas completas; no afirma que siete sea el mínimo posible.

| Sprint | Objetivo | HU asignadas (SP) | Total SP | Capacidad SP | Dependencias o riesgos |
|---|---|---|---:|---:|---|
| Sprint 1 | Acceder y crear un perfil | HU03 (5), HU04 (5), HU05 (3) | 13 | 20 | Integrar registro y autenticación antes de cerrar perfil |
| Sprint 2 | Publicar y explorar oportunidades | HU06 (8), HU07 (3), HU01 (5) | 16 | 20 | Requiere acceso; publicar propuestas y necesidades antes de validar exploración con datos reales |
| Sprint 3 | Consultar horarios y buscar aprendizajes | HU11 (8), HU12 (3), HU08 (5) | 16 | 20 | HU11 antes de HU12; HU08 utiliza el contenido del sprint 2 |
| Sprint 4 | Encontrar opciones y solicitar una sesión | HU09 (5), HU13 (8), HU19 (3) | 16 | 20 | Filtros usan búsqueda y agenda; solicitudes usan propuestas y franjas; denuncias usan contenido existente |
| Sprint 5 | Completar un intercambio y transferir créditos | HU14 (8), HU15 (3), HU16 (8) | 19 | 20 | Secuencia HU14 → HU15 → HU16; riesgo alto de integración y concurrencia |
| Sprint 6 | Recomendar coincidencias y registrar resultados | HU10 (8), HU18 (5), HU17 (5) | 18 | 20 | Compatibilidad reutiliza agenda y solicitud; HU18 antes del cierre del historial con calificaciones |
| Sprint 7 | Mostrar confianza y administrar seguridad | HU02 (8), HU20 (8) | 16 | 20 | HU02 reutiliza HU18; HU20 usa usuarios, propuestas y denuncias |
| **Total** | | **20 HU** | **114** | **140** | **26 SP de margen agregado, no transferible automáticamente entre semanas** |

La búsqueda manual permite solicitar sesiones antes del recomendador de compatibilidad. Esto ordena la implementación sin retirar compatibilidad del MVP. Las entregas intermedias son incrementos de desarrollo, no una autorización para operar públicamente sin la administración y seguridad completas.

Las reglas de franjas libres y privacidad se implementan en HU11/HU12 y se integran con la reserva real en HU14; el sprint 5 debe incluir pruebas de regresión de agendas, filtros y solicitudes. HU15 cubre el cierre y los puntos de integración; HU16, HU18 y HU17 cubren las funciones consumidoras, sin contarlas dos veces.

### HU sin asignar

Ninguna en el horizonte propuesto de siete sprints. La asignación es provisional y no declara resueltos los pendientes funcionales.

Si se limita la entrega a los primeros cuatro sprints de esta propuesta, se asignan 61 SP y quedan **53 SP**: HU02, HU10, HU14, HU15, HU16, HU17, HU18 y HU20. La brecha aritmética mínima de 114 frente a 80 es 34 SP, pero esta distribución concreta conserva más margen por dependencias y secuencia.

## Relación con los sprints existentes en Jira

En la consulta realizada durante esta sesión existían Sprint 1–4, IDs 1–4, en el tablero BH95 (ID 2), sin issues. Sprint 1 estaba activo con fin previsto el 1 de octubre; los demás tenían fechas futuras y objetivos anteriores. Releer Jira antes de aplicar: este documento no cambia ese estado ni acredita disponibilidad actual.

Se propone reutilizar los nombres Sprint 1–4 y agregar Sprint 5–7 únicamente cuando se autorice sincronizar esta propuesta. Los objetivos aquí propuestos sustituyen los anteriores solo dentro de esa sincronización autorizada. Mantener fechas y estados existentes; acordar aparte la reprogramación del Sprint 1 y la calendarización de la secuencia semanal. No iniciar ni cerrar sprints automáticamente.

## Refinamiento previo al compromiso

- Confirmar campos públicos, mínimos de registro, sesión y perfil.
- Definir ranking/trending y criterios de compatibilidad antes de HU02/HU10.
- Resolver zona horaria, conflictos de agenda y reserva antes de HU11/HU13/HU14.
- Acordar quién confirma la finalización y las reglas de créditos antes de HU15/HU16.
- Resolver permisos administrativos, auditoría y reglas de denuncias antes de HU19/HU20.
- Validar habilidades, ausencias, infraestructura y experiencia del equipo. No se dispone de velocidad histórica ni de estimaciones horarias por tarea que prueben el encaje en 65 h.

## Verificación

20 HU consideradas, asignadas una vez cada una; 114 SP en historias y 114 SP en sprints. Ningún sprint supera 20 SP. Los criterios, reglas del producto, responsables y estados de Jira no se modificaron.

## Registro de sincronización — 2026-10-04

- Pedido de aplicación: «actualizar jira».
- Reutilizados Sprint 1–4 (IDs 1–4), con objetivos actualizados y fechas/estados conservados.
- Creados Sprint 5 (ID 35), Sprint 6 (ID 36) y Sprint 7 (ID 37), futuros y sin fechas.
- Cargados y verificados los puntos y asignaciones de las 20 HU: 114 SP, distribuidos en 13, 16, 16, 16, 19, 18 y 16 SP.
- Verificadas las 40 subtareas en el mismo sprint que sus respectivas HU, sin puntos adicionales.
- MVP V3 y MVP resumido en Confluence coinciden con los archivos locales; no se generaron versiones idénticas innecesarias.
- Sigue pendiente acordar el calendario: el Sprint 1 conserva su fecha vencida y los sprints nuevos no están calendarizados.
- [Tablero Jira BH95](https://martinporto.atlassian.net/jira/software/projects/BH95/boards/2).
