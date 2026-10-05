# Planificación de sprints — MVP V3

**Fecha de derivación:** 2026-10-05.  
**Planificación base:** 2026-10-04.
**Estado:** distribución, estimaciones y descomposición variable aplicadas y verificadas en Jira el 2026-10-05; capacidad y refinamientos funcionales siguen siendo provisionales.
**Fuentes:** [MVP V3](mvp-v3.md), [WBS](wbs.md), [backlog](backlog.md), [subtareas](subtareas.md) y estimaciones acordadas en la conversación. Las claves Jira corresponden a las HU consultadas durante la sincronización registrada.

## Equipo y capacidad

| Dato | Valor | Base |
|---|---:|---|
| Integrantes | 6 | Informado por el usuario |
| Horas semanales por persona | 15 | Simulación solicitada |
| Duración | 2 semanas | Acordada |
| Horas brutas | 180 h | 6 × 15 × 2 semanas |
| Reserva | 45 h (25 %) | Coordinación e imprevistos |
| Horas planificables | 135 h | 180 × 0,75 |
| Compromiso horario orientativo | 130 h | Redondeo conservador |
| Capacidad de referencia | 20 SP/sprint | Hipótesis aceptada, no velocidad observada |

Se supone que no hay ausencias adicionales y que el equipo dispone de habilidades para frontend, backend y pruebas. Las 130 horas incluyen revisión, integración y correcciones. No existe una conversión de horas a puntos. La corrección de capacidad horaria no modifica automáticamente la hipótesis aceptada de 20 SP ni la distribución vigente. Recalibrar después de 2–3 sprints con historias realmente terminadas.

## Estimaciones conservadas

Son las nuevas estimaciones propuestas y aceptadas en esta conversación, no una recuperación de las estimaciones históricas perdidas. Incluyen la descomposición técnica necesaria de cada HU sin volver a sumar puntos por subtarea. `[2.1.0]` sirve como referencia de funcionalidad sencilla de 3 puntos.

| HU | Jira | Historia | SP | Motivo |
|---|---|---|---:|---|
| [1.1.0] | BH95-146 | Explorar como GUEST | 5 | Listados y detalle públicos con privacidad |
| [1.2.0] | BH95-147 | Consultar confianza pública | 8 | Reputación, rankings y trending por definir |
| [1.3.0] | BH95-148 | Registrarse cuando sea necesario | 5 | Registro y conservación del contexto |
| [1.4.0] | BH95-149 | Autenticarse | 5 | Sesiones seguras y rutas protegidas |
| [2.1.0] | BH95-150 | Completar el perfil | 3 | Edición básica y validación |
| [2.2.0] | BH95-151 | Publicar una propuesta | 8 | Publicación, borrador y validaciones |
| [2.3.0] | BH95-152 | Registrar un aprendizaje buscado | 3 | Alta, edición y pausa |
| [3.1.0] | BH95-153 | Buscar aprendizajes | 5 | Búsqueda pública y paginación |
| [3.2.0] | BH95-154 | Filtrar resultados | 5 | Filtros combinables y disponibilidad |
| [3.3.0] | BH95-155 | Encontrar compatibilidades | 8 | Reglas cruzadas y reciprocidad |
| [4.1.0] | BH95-156 | Gestionar disponibilidad | 8 | Franjas concretas y carga masiva |
| [4.2.0] | BH95-157 | Publicar la agenda | 3 | Visibilidad y privacidad |
| [4.3.0] | BH95-158 | Crear una sesión solicitada | 8 | Condiciones y conflictos de horario |
| [4.4.0] | BH95-159 | Gestionar el estado de una sesión | 8 | Transiciones y reserva de franjas |
| [4.5.0] | BH95-160 | Finalizar una sesión | 3 | Cierre válido sin duplicados |
| [5.1.0] | BH95-161 | Intercambiar con créditos | 8 | Consistencia de saldos e idempotencia |
| [5.2.0] | BH95-162 | Consultar historial | 5 | Actividad integrada y privacidad |
| [5.3.0] | BH95-163 | Calificarse mutuamente | 5 | Elegibilidad, unicidad y promedio |
| [6.1.0] | BH95-164 | Denunciar contenido o usuarios | 3 | Validaciones y registro |
| [6.2.0] | BH95-165 | Administrar seguridad | 8 | Moderación, permisos y auditoría |
| **Total** | | | **114** | |

Se supone autenticación con herramientas estándar y reutilización de componentes. La infraestructura inicial no está desglosada en estas 20 historias; comprobar su disponibilidad antes del primer compromiso. `[5.3.0]` implementa el cálculo y endpoint de reputación que reutiliza `[1.2.0]`; no implementarlo dos veces.

Rankings y trending sí aparecen en el MVP V3 vigente; se corrige la observación anterior basada en una versión local previa. Siguen pendientes sus reglas exactas. Los puntos de `[1.2.0]` y de las demás historias con decisiones abiertas son provisionales hasta resolverlas.

## Distribución propuesta

Se establece un límite de **4 sprints de dos semanas**. El calendario confirmado es: Sprint 1, 24-sept–8-oct; Sprint 2, 8-oct–22-oct; Sprint 3, 22-oct–5-nov; Sprint 4, 5-nov–19-nov. Se preservan las estimaciones de las 20 historias. La capacidad de 20 SP por sprint se adopta como límite blando: sirve como referencia de carga, pero no bloquea la asignación.

| Sprint | Período | Objetivo | HU asignadas (SP) | Total SP | Capacidad SP | Dependencias o riesgos |
|---|---|---|---|---:|---:|---|
| Sprint 1 | 24-sept–8-oct | Acceder y crear un perfil | [1.3.0] (5), [1.4.0] (5), [2.1.0] (3) | 13 | 20 | Integrar registro y autenticación antes de cerrar perfil |
| Sprint 2 | 8-oct–22-oct | Publicar, explorar y encontrar compatibilidades | [2.2.0] (8), [2.3.0] (3), [1.1.0] (5), [1.2.0] (8), [3.3.0] (8) | 32 | 20 | Requiere acceso y contenido publicado; sobrecupo visible de 12 SP |
| Sprint 3 | 22-oct–5-nov | Consultar horarios y completar el ciclo de sesión | [4.1.0] (8), [4.2.0] (3), [3.1.0] (5), [4.3.0] (8), [4.4.0] (8), [4.5.0] (3) | 35 | 20 | La agenda y la propuesta habilitan solicitud, gestión y finalización; sobrecupo visible de 15 SP |
| Sprint 4 | 5-nov–19-nov | Créditos, historial, reputación y seguridad | [3.2.0] (5), [6.1.0] (3), [5.1.0] (8), [5.2.0] (5), [5.3.0] (5), [6.2.0] (8) | 34 | 20 | Se completa el valor posterior a la sesión y la operación segura; sobrecupo visible de 14 SP |
| **Total** | — | **20 historias asignadas** | — | **114** | **80** | **Límite blando: 34 SP por encima de la capacidad de referencia; no quedan HU sin sprint** |

La búsqueda manual permite solicitar sesiones antes del recomendador de compatibilidad. Esto ordena la implementación sin retirar compatibilidad del MVP. Las entregas intermedias son incrementos de desarrollo, no una autorización para operar públicamente sin la administración y seguridad completas.

Las reglas de franjas libres y privacidad se implementan en [4.1.0]/[4.2.0]. [3.3.0] se ubica después de publicar y buscar contenido; [4.4.0] y [4.5.0] completan el ciclo de la sesión en Sprint 3; [5.1.0], [5.2.0], [5.3.0] y [6.2.0] quedan en Sprint 4 como capacidades posteriores a la sesión. [1.2.0] se mantiene en Sprint 2 por decisión confirmada.

### Capacidad y límite blando

No quedan historias sin asignar. La brecha entre las 114 SP estimadas y las 80 SP de capacidad de referencia es de **34 SP**. Los puntos sirven para visualizar la carga, pero no bloquean la asignación de HU; los sobrecupos quedan visibles y se revisarán contra la velocidad real del equipo.

## Relación con los sprints existentes en Jira

En la consulta realizada durante esta sesión existen Sprint 1–4, IDs 1–4, en el tablero BH95 (ID 2), con trabajo asignado. El calendario local confirmado es Sprint 1: **24 de septiembre–8 de octubre de 2026**; Sprint 2: **8–22 de octubre**; Sprint 3: **22 de octubre–5 de noviembre**; Sprint 4: **5–19 de noviembre**. Releer Jira antes de aplicar cambios posteriores.

Se propone reutilizar únicamente Sprint 1–4. No crear Sprint 5–7 ni asignar historias adicionales fuera de este horizonte. Los objetivos y fechas aquí propuestos sustituyen los anteriores solo dentro de esa sincronización autorizada. No iniciar ni cerrar sprints automáticamente.

## Refinamiento previo al compromiso

- Confirmar campos públicos, mínimos de registro, sesión y perfil.
- Definir ranking/trending y criterios de compatibilidad antes de [1.2.0]/[3.3.0].
- Resolver zona horaria, conflictos de agenda y reserva antes de [4.1.0]/[4.3.0]/[4.4.0].
- Acordar quién confirma la finalización y las reglas de créditos antes de [4.5.0]/[5.1.0].
- Resolver permisos administrativos, auditoría y reglas de denuncias antes de [6.1.0]/[6.2.0].
- Validar habilidades, ausencias, infraestructura y experiencia del equipo. No se dispone de velocidad histórica ni de estimaciones horarias por tarea que prueben el encaje en 130 h.

## Verificación

20 HU consideradas, asignadas una vez cada una; 114 SP en historias y 114 SP distribuidos en los cuatro sprints. Los sprints contienen 13, 32, 35 y 34 SP frente a una referencia de 20 SP; no quedan HU sin sprint.

## Registro de sincronización — 2026-10-05

- Pedido de aplicación: «actualizar jira».
- Reutilizados Sprint 1–4 (IDs 1–4), con objetivos actualizados y calendario de dos semanas aplicado.
- Sprint 5 (ID 35), Sprint 6 (ID 36) y Sprint 7 (ID 37) quedaron vacíos y futuros; no forman parte de la planificación activa de cuatro sprints.
- La planificación local queda limitada a Sprint 1–4: 20 historias asignadas, 114 SP distribuidos en 13, 32, 35 y 34 SP; no quedan historias pendientes. Se adopta un límite blando y los sobrecupos quedan explícitos.
- Verificadas las 40 subtareas en el mismo sprint que sus respectivas HU, sin puntos adicionales.
- MVP V3 y MVP resumido en Confluence coinciden con los archivos locales; no se generaron versiones idénticas innecesarias.
- El calendario local confirmado establece únicamente cuatro sprints de dos semanas: Sprint 1, 24 de septiembre–8 de octubre; Sprint 2, 8–22 de octubre; Sprint 3, 22 de octubre–5 de noviembre; Sprint 4, 5–19 de noviembre. Jira quedó alineado en fechas y asignaciones; Sprint 5–7 permanecen vacíos porque Jira no permite eliminar sprints futuros mediante el conector.
- [Tablero Jira BH95](https://martinporto.atlassian.net/jira/software/projects/BH95/boards/2).

## Registro de sincronización — 2026-10-05 (ajuste de [1.2.0])

- Pedido de aplicación: «actualizar jira» luego de confirmar la incorporación de [1.2.0].
- [1.2.0] (BH95-147) y sus subtareas BH95-168/BH95-169 quedaron asignadas al Sprint 2.
- Sprint 2 queda con 4 HU y 24 SP; se mantiene el sobrecupo explícitamente confirmado.
- Se verificó que MVP V3 y MVP resumido en Documentos ya coinciden con los archivos locales; no se generaron versiones idénticas innecesarias.

## Registro de sincronización — 2026-10-05 (límite blando)

- Confirmado que las 20 HU deben quedar distribuidas en los cuatro sprints.
- Se adopta un límite blando de 20 SP por sprint como referencia, no como bloqueo.
- Distribución aplicada: Sprint 1 = 13 SP, Sprint 2 = 32 SP, Sprint 3 = 35 SP y Sprint 4 = 34 SP.
- Se movieron 24 issues entre HU y subtareas; las 20 HU quedaron asignadas a Sprint 1–4.
- Sprint 5–7 permanecen vacíos y futuros.

## Registro de sincronización — 2026-10-05 (reconciliación de planificación)

- Se verificaron 6 épicas, 20 historias y 40 subtareas etiquetadas para MVP V3.
- Se corrigieron las descripciones de BH95-149, BH95-152, BH95-155, BH95-160 y BH95-163 para eliminar encabezados de la épica siguiente incorporados accidentalmente.
- Se normalizó el rol de BH95-153 y BH95-154 de “visitante” a `GUEST` o `USER` según el backlog vigente.
- Se actualizaron los objetivos de Sprint 2–4 para que coincidan con la planificación local, conservando nombres, estados y fechas.
- Se verificó la distribución: Sprint 1 = 13 SP, Sprint 2 = 32 SP, Sprint 3 = 35 SP y Sprint 4 = 34 SP; total = 114 SP.
- Las páginas `MVP V3` y `MVP resumido` de Confluence coinciden exactamente con los archivos locales; no se crearon versiones duplicadas.

## Revisión local — 2026-10-05 (WBS y descomposición variable)

- En una revisión intermedia, la WBS se reorganizó en 6 bloques y 20 módulos para estructurar directamente las 6 épicas y 20 HU; esta decisión fue posteriormente reemplazada por el modelo de derivación independiente registrado más abajo.
- La validación WBS–backlog quedó completa, sin paquetes ni historias huérfanas; no se generó una nueva matriz permanente.
- La descomposición local pasó de una plantilla fija de 40 subtareas a 45 subtareas decididas por responsabilidad: 15 HU con dos y 5 HU con tres.
- Las estimaciones se conservan porque los story points corresponden a la HU completa y el alcance funcional no cambió.
- Jira conserva la descomposición previamente sincronizada hasta que el usuario solicite una nueva actualización externa.

## Registro de sincronización — 2026-10-05 (45 subtareas)

- Se actualizaron 10 subtareas existentes de [4.1.0], [4.3.0], [4.4.0], [5.1.0] y [6.2.0] para reflejar responsabilidades y numeración nuevas.
- Se crearon BH95-206, BH95-207, BH95-208, BH95-209 y BH95-210 como nuevas subtareas Backend.
- Las cinco HU afectadas quedaron con tres subtareas cada una; las restantes conservan dos.
- Se verificaron 6 épicas, 20 HU y 45 subtareas, sin identificadores de subtarea duplicados.
- Las nuevas subtareas quedaron en el mismo sprint que su HU: [4.1.0], [4.3.0] y [4.4.0] en Sprint 3; [5.1.0] y [6.2.0] en Sprint 4.
- Se conservaron estados, responsables, fechas y 114 SP distribuidos en 13, 32, 35 y 34 SP.
- `MVP V3` y `MVP resumido` ya coincidían exactamente con Confluence; no se crearon versiones documentales duplicadas.

## Revisión local — 2026-10-05 (derivación independiente)

- Se restableció al MVP V3 como única entrada de requisitos para WBS, backlog y USM.
- La WBS y el backlog vuelven a derivarse en ramas independientes; ninguno estructura ni agrega alcance al otro.
- La relación WBS–backlog queda limitada a una validación posterior opcional de cobertura, sin matriz permanente obligatoria.
- La WBS recuperó su jerarquía orientada a entregables; la numeración del backlog continúa como convención propia y no expresa dependencia jerárquica.
- Las 45 subtareas, los 114 SP y la distribución en cuatro sprints se conservan porque este ajuste conceptual no cambia el alcance funcional ni la descomposición técnica aprobada.
- Jira no fue modificado por esta revisión conceptual.

## Registro de verificación Jira — 2026-10-05 (modelo independiente)

- Se comparó la planificación local posterior al restablecimiento de la derivación independiente con el proyecto BH95.
- Jira ya contenía 6 épicas, 20 HU y 45 subtareas con etiqueta `mvp-v3`; no fue necesario crear ni editar issues.
- No se detectaron identificadores de subtarea duplicados.
- Se verificaron 114 SP distribuidos en Sprint 1 = 13, Sprint 2 = 32, Sprint 3 = 35 y Sprint 4 = 34.
- Se conservaron objetivos, estados y fechas de Sprint 1–4.
- `MVP V3` y `MVP resumido` coinciden exactamente con Confluence; no se crearon versiones nuevas.
- El ajuste WBS–backlog permanece exclusivamente documental y no modifica la planificación ejecutable en Jira.

## Revisión local — 2026-10-05 (reconciliación histórica integrada)

- Se ejecutó nuevamente la derivación completa desde el MVP V3 como única fuente de requisitos.
- Se conservaron 6 épicas, 20 HU y 45 subtareas: 15 HU con dos subtareas y 5 HU con tres, según responsabilidades técnicas verificables y sin una cantidad mínima obligatoria.
- Después de derivar las subtareas se aplicó la reconciliación histórica obligatoria; las checklists vigentes permanecen dentro de sus subtareas Backend y no se crearon HU ni subtareas adicionales para forzar el mapeo.
- La matriz histórica continúa como entrada exclusiva del parche de migración y no interviene en la generación del backlog.
- Se conservaron las estimaciones y la distribución aprobadas: 114 SP en Sprint 1–4, con 13, 32, 35 y 34 SP respectivamente.
- Esta revisión local queda preparada para su comparación y sincronización con Jira y Confluence.

## Registro de sincronización — 2026-10-05 (parche histórico preservado)

- Se comparó la derivación completa con Jira después de incorporar la reconciliación histórica al flujo obligatorio.
- Se actualizaron BH95-186 (`[4.1.1] Gestionar franjas`) y BH95-196 (`[5.1.2] Ejecutar transferencia idempotente`) para incorporar las checklists históricas que faltaban.
- Se preservó el avance registrado en Jira para `[1.4.1.1]` y `[1.4.1.2]`, ambos completados, y se reflejó ese estado en `docs/subtareas.md`.
- Jira conserva 6 épicas, 20 HU y 45 subtareas con etiqueta `mvp-v3`; no se crearon issues ni se alteraron estados o responsables.
- Se verificaron 114 SP distribuidos en Sprint 1 = 13, Sprint 2 = 32, Sprint 3 = 35 y Sprint 4 = 34; se conservaron objetivos, fechas y estados de los cuatro sprints.
- `MVP V3` y `MVP resumido` coinciden exactamente con Confluence; no se generaron versiones documentales nuevas.
