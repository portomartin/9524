# Relevamiento final de entrega WBS

Este documento organiza los pedidos de entrega, demo y reglas relevados para el proyecto WBSO. No crea ni modifica issues de Jira por sí mismo: sirve como matriz previa de ubicación y trazabilidad.

## Referencias de la estructura actual

- `WBSO-4` — Epic: Implementación, pruebas y entrega.
- `WBSO-10` — Historia: Sistema de solicitudes y sesiones.
- `WBSO-11` — Historia: Sistema de créditos virtuales.
- `WBSO-12` — Historia: Sistema de historial.
- `WBSO-19` — Historia: [1.15] Entrega del MVP.
- `WBSO-130` — Subtask: [1.15.7] Presentación y demostración del MVP.

## Matriz de ubicación

| ID | Elemento relevado | Tipo Jira propuesto | Padre / issue relacionado | Estado del relevamiento | Observaciones |
|---|---|---|---|---|---|
| RF-01 | Limpiar branches obsoletas | Subtask | `WBSO-19` | Por ubicar | Verificar branches antes de eliminar y conservar las activas. |
| RF-02 | Preparar entorno y datos creíbles para la demo | Subtask | `WBSO-19` | Por ubicar | Incluye cursos, nombres plausibles, dos computadoras e interacción Docente/Alumno. |
| RF-03 | Preparar escenarios y replay de la demo | Subtask | `WBSO-19` | Por ubicar | Reserva anticipada y cancelación; cancelación de clase; fecha ya pasada; filtro de clases cobradas/completadas. |
| RF-04 | Preparar presentación y listado de entregables | Subtask existente / actualización | `WBSO-130` | Revisar | Incorporar preguntas posibles de Ale y casos que se mostrarán. |
| RF-05 | Preparar retrospectiva del equipo | Subtask | `WBSO-19` | Por ubicar | Duración: 15 minutos. Incluir aprendizajes y dinámica del Barquito/Sailboat. |
| RF-06 | Fechas de finales | Contexto de planificación | `WBSO-19` | Registrado como contexto | Diciembre y febrero. No crear issue separado salvo que se necesite una fecha concreta. |
| RF-07 | Estados y cancelación de sesiones | Subtask | `WBSO-10` | Por ubicar | Pendiente, Aceptada, Completada y Cancelada; cancelación desde ambos lados. |
| RF-08 | Unidades de medida | Criterio transversal | `WBSO-10`, `WBSO-11` y documentación | Por definir | Indicar créditos, horas u otra unidad donde corresponda. |
| RF-09 | Créditos en custodia durante la sesión | Subtask | `WBSO-11` | Por ubicar | Freeze mientras la sesión está pactada; liberar al completar. |
| RF-10 | Recuperación de créditos ante cancelación | Subtask o criterio de RF-09 | `WBSO-11` | Decisión pendiente | Definir cancelación normal, tardía e inasistencia. |
| RF-11 | Filtro frontend de clases cobradas/completadas | Subtask | `WBSO-12` | Por ubicar | Validar nombres exactos de los estados visibles y resultado esperado. |

## Entregables de la materia a verificar

Estos entregables ya forman parte del relevamiento general. Hay que vincularlos con issues existentes o crear subtasks solo si no están cubiertos:

- WBS.
- User Story Mapping.
- Product Backlog.
- Detalle de User Stories.
- Sprints y Release Planning.
- Resultado de la retrospectiva.
- Estimaciones realizadas.
- Matriz de riesgos identificados.
- Diagrama de arquitectura elegida.
- Producto funcionando para evaluación.

## Criterio de cierre

El relevamiento queda completo cuando cada fila tiene una de estas resoluciones:

- issue existente identificado;
- nuevo Subtask propuesto con padre;
- criterio de aceptación agregado a un issue existente;
- contexto documentado sin issue;
- decisión pendiente explícita.

No se deben crear issues en Jira hasta revisar esta matriz y confirmar las decisiones pendientes.

## Tabla de trabajo con clasificación

Clasificación utilizada:

- **Funcionalidad del producto**
- **Técnico / infraestructura**
- **Entrega / documentación**

| Nº | Punto | Notas | Clasificación de cada nota |
|---|---|---|---|
| 1 | Planificación, Entrega y Demo | - Limpieza previa: borrar branches viejas en Git.<br>- Estructura: Demo en vivo + Retrospectiva (15 min).<br>- Fechas de Finales: Diciembre y Febrero.<br>- Presentación en PPT con listado de entregables.<br>- Ale va a hacer preguntas durante la defensa.<br>- Listar aprendizajes del equipo.<br>- Usar templates de Ale (dinámica del Barquito / Sailboat). | - Técnico / infraestructura<br>- Entrega / documentación<br>- Entrega / documentación<br>- Entrega / documentación<br>- Entrega / documentación<br>- Entrega / documentación<br>- Entrega / documentación |
| 2 | Pautas para la Demo | - Datos reales: nada de "asdf", usar cursos y nombres creíbles.<br>- Setup: llevar 2 computadoras para mostrar la interacción en vivo entre Docente y Alumno.<br>- Usuario que reservó con anticipación y cancelación (tener armado el replay).<br>- Qué pasa si se cancela la clase o si ya pasó la fecha.<br>- Filtro en frontend para clases cobradas / completadas. | - Entrega / documentación<br>- Técnico / infraestructura + Entrega / documentación<br>- Funcionalidad del producto + Entrega / documentación<br>- Funcionalidad del producto<br>- Funcionalidad del producto |
| 3 | Reglas de Negocio, Estados y Jira | - Jira: subir todo esto como issues.<br>- Unidad: indicar siempre la unidad (créditos, horas, etc.).<br>- Pendiente.<br>- Aceptada.<br>- Completada.<br>- Cancelada (se puede cancelar de ambos lados).<br>- Créditos: quedan en freeze (en custodia, tipo plazo fijo) mientras la sesión está pactada.<br>- Aclarar qué recupera el comprador si la clase se cancela. | - Entrega / documentación<br>- Funcionalidad del producto<br>- Funcionalidad del producto<br>- Funcionalidad del producto<br>- Funcionalidad del producto<br>- Funcionalidad del producto<br>- Funcionalidad del producto<br>- Funcionalidad del producto |
| 4 | Entrega final de trabajo | - Presentación en la fecha de coloquio (incluye exposición oral).<br>- Informe con los componentes detallados a continuación.<br>- App construida.<br>- Narrativa de la iniciativa.<br>- Diagrama de causa efecto / template de análisis del problema.<br>- Storytelling.<br>- Scope Canvas.<br>- User Research: entrevistas / Perfiles Persona / Mapas de empatía.<br>- Benchmarking.<br>- User Interface + Wireframing.<br>- Workflows de la aplicación.<br>- WBS.<br>- USM.<br>- Product Backlog.<br>- Detalle de User Stories.<br>- Sprints y Release Planning.<br>- Resultado de una Retro ideada por el grupo.<br>- Estimaciones realizadas.<br>- Matriz de riesgos identificados.<br>- Diagrama de la arquitectura elegida.<br>- Producto funcionando para su evaluación.<br>- Diagramas para la entrega. | - Entrega / documentación<br>- Entrega / documentación<br>- Funcionalidad del producto<br>- Entrega / documentación<br>- Entrega / documentación<br>- Entrega / documentación<br>- Entrega / documentación<br>- Entrega / documentación<br>- Entrega / documentación<br>- Entrega / documentación<br>- Entrega / documentación<br>- Entrega / documentación<br>- Entrega / documentación<br>- Entrega / documentación<br>- Entrega / documentación<br>- Entrega / documentación<br>- Entrega / documentación<br>- Entrega / documentación<br>- Entrega / documentación<br>- Entrega / documentación<br>- Técnico / infraestructura<br>- Funcionalidad del producto<br>- Entrega / documentación |

## Tabla expandida con procedencia

Cada fila repite el punto y el agrupador original para conservar el contexto si después se reorganiza la tabla.

| Punto original | Agrupador original | Ítem / nota | Clasificación |
|---|---|---|---|
| 1. Planificación, Entrega y Demo | 1.1 Limpieza previa | Borrar branches viejas en Git. | Técnico / infraestructura |
| 1. Planificación, Entrega y Demo | 1.2 Estructura | Demo en vivo + Retrospectiva (15 min). | Entrega / documentación |
| 1. Planificación, Entrega y Demo | 1.3 Fechas de Finales | Diciembre y Febrero. | Entrega / documentación |
| 1. Planificación, Entrega y Demo | 1.4 Entregables | Presentación en PPT con listado de entregables. | Entrega / documentación |
| 1. Planificación, Entrega y Demo | 1.4 Entregables | Ale va a hacer preguntas durante la defensa. | Entrega / documentación |
| 1. Planificación, Entrega y Demo | 1.5 Retrospectiva | Listar aprendizajes del equipo. | Entrega / documentación |
| 1. Planificación, Entrega y Demo | 1.5 Retrospectiva | Usar templates de Ale (dinámica del Barquito / Sailboat). | Entrega / documentación |
| 2. Pautas para la Demo | 2.1 Datos reales | Nada de "asdf", usar cursos y nombres creíbles. | Entrega / documentación |
| 2. Pautas para la Demo | 2.2 Setup | Llevar 2 computadoras para mostrar la interacción en vivo entre Docente y Alumno. | Técnico / infraestructura + Entrega / documentación |
| 2. Pautas para la Demo | 2.3 Casos a mostrar | Usuario que reservó con anticipación y cancelación (tener armado el replay). | Funcionalidad del producto + Entrega / documentación |
| 2. Pautas para la Demo | 2.3 Casos a mostrar | Qué pasa si se cancela la clase o si ya pasó la fecha. | Funcionalidad del producto |
| 2. Pautas para la Demo | 2.3 Casos a mostrar | Filtro en frontend para clases cobradas / completadas. | Funcionalidad del producto |
| 3. Reglas de Negocio, Estados y Jira | 3.1 Jira | Subir todo esto como issues. | Entrega / documentación |
| 3. Reglas de Negocio, Estados y Jira | 3.2 Unidad | Indicar siempre la unidad (créditos, horas, etc.). | Funcionalidad del producto |
| 3. Reglas de Negocio, Estados y Jira | 3.3 Los 4 estados de sesión | Pendiente. | Funcionalidad del producto |
| 3. Reglas de Negocio, Estados y Jira | 3.3 Los 4 estados de sesión | Aceptada. | Funcionalidad del producto |
| 3. Reglas de Negocio, Estados y Jira | 3.3 Los 4 estados de sesión | Completada. | Funcionalidad del producto |
| 3. Reglas de Negocio, Estados y Jira | 3.3 Los 4 estados de sesión | Cancelada (se puede cancelar de ambos lados). | Funcionalidad del producto |
| 3. Reglas de Negocio, Estados y Jira | 3.4 Créditos | Quedan en freeze (en custodia, tipo plazo fijo) mientras la sesión está pactada. | Funcionalidad del producto |
| 3. Reglas de Negocio, Estados y Jira | 3.4 Créditos | Aclarar qué recupera el comprador si la clase se cancela. | Funcionalidad del producto |
| 4. Entrega final de trabajo | 4.1 Entrega final | Presentación en la fecha de coloquio (incluye exposición oral). | Entrega / documentación |
| 4. Entrega final de trabajo | 4.1 Entrega final | Informe con los componentes detallados a continuación. | Entrega / documentación |
| 4. Entrega final de trabajo | 4.1 Entrega final | App construida. | Funcionalidad del producto |
| 4. Entrega final de trabajo | 4.2 Primero: Introducción a la iniciativa | Describir en formato texto la iniciativa (Narrativa de la iniciativa). | Entrega / documentación |
| 4. Entrega final de trabajo | 4.2 Primero: Introducción a la iniciativa | Usar el diagrama de causa efecto / template de análisis del problema para comprender la necesidad / el problema bajo estudio. | Entrega / documentación |
| 4. Entrega final de trabajo | 4.2 Primero: Introducción a la iniciativa | Ilustrar la idea con un Storytelling. | Entrega / documentación |
| 4. Entrega final de trabajo | 4.2 Primero: Introducción a la iniciativa | Componer un Scope Canvas de la iniciativa. | Entrega / documentación |
| 4. Entrega final de trabajo | 4.3 Segundo: Design Thinking de la iniciativa | User Research: entrevistas / Perfiles Persona / Mapas de empatía. | Entrega / documentación |
| 4. Entrega final de trabajo | 4.3 Segundo: Design Thinking de la iniciativa | Benchmarking. | Entrega / documentación |
| 4. Entrega final de trabajo | 4.3 Segundo: Design Thinking de la iniciativa | UX: user Interface + Wireframing. | Entrega / documentación |
| 4. Entrega final de trabajo | 4.3 Segundo: Design Thinking de la iniciativa | Workflows de la aplicación. | Entrega / documentación |
| 4. Entrega final de trabajo | 4.4 Tercero: Construcción de la iniciativa – App funcionando | WBS: Work Breakdown Structure. | Entrega / documentación |
| 4. Entrega final de trabajo | 4.4 Tercero: Construcción de la iniciativa – App funcionando | USM: User Story Mapping. | Entrega / documentación |
| 4. Entrega final de trabajo | 4.4 Tercero: Construcción de la iniciativa – App funcionando | Product Backlog. | Entrega / documentación |
| 4. Entrega final de trabajo | 4.4 Tercero: Construcción de la iniciativa – App funcionando | Detalle de User Stories. | Entrega / documentación |
| 4. Entrega final de trabajo | 4.4 Tercero: Construcción de la iniciativa – App funcionando | Detalle los Sprints y Realease planning. | Entrega / documentación |
| 4. Entrega final de trabajo | 4.4 Tercero: Construcción de la iniciativa – App funcionando | Resultado de una Retro ideada por el grupo. | Entrega / documentación |
| 4. Entrega final de trabajo | 4.4 Tercero: Construcción de la iniciativa – App funcionando | Estimaciones realizadas. | Entrega / documentación |
| 4. Entrega final de trabajo | 4.4 Tercero: Construcción de la iniciativa – App funcionando | Matriz de riesgos identificados. | Entrega / documentación |
| 4. Entrega final de trabajo | 4.4 Tercero: Construcción de la iniciativa – App funcionando | Diagrama de la arquitectura elegida. | Técnico / infraestructura |
| 4. Entrega final de trabajo | 4.4 Tercero: Construcción de la iniciativa – App funcionando | Producto funcionando (Permitiendo el uso para su evaluación). | Funcionalidad del producto |
| 4. Entrega final de trabajo | 4.5 Agregado a la fila 4 | Diagramas para la entrega. | Entrega / documentación |

## Tabla jerárquica identificada

| ID | Nivel | Elemento | Clasificación |
|---|---|---|---|
| 1 | Punto | Planificación, Entrega y Demo | Entrega / documentación |
| 1.1 | Agrupador | Limpieza previa | Técnico / infraestructura |
| 1.1.1 | Ítem | Borrar branches viejas en Git. | Técnico / infraestructura |
| 1.2 | Agrupador | Estructura | Entrega / documentación |
| 1.2.1 | Ítem | Demo en vivo. | Entrega / documentación |
| 1.2.2 | Ítem | Retrospectiva (15 min). | Entrega / documentación |
| 1.3 | Agrupador | Fechas de Finales | Entrega / documentación |
| 1.3.1 | Ítem | Diciembre. | Entrega / documentación |
| 1.3.2 | Ítem | Febrero. | Entrega / documentación |
| 1.4 | Agrupador | Entregables | Entrega / documentación |
| 1.4.1 | Ítem | Presentación en PPT con listado de entregables. | Entrega / documentación |
| 1.4.2 | Ítem | Ale va a hacer preguntas durante la defensa. | Entrega / documentación |
| 1.5 | Agrupador | Retrospectiva | Entrega / documentación |
| 1.5.1 | Ítem | Listar aprendizajes del equipo. | Entrega / documentación |
| 1.5.2 | Ítem | Usar templates de Ale (dinámica del Barquito / Sailboat). | Entrega / documentación |
| 2 | Punto | Pautas para la Demo | Entrega / documentación |
| 2.1 | Agrupador | Datos reales | Entrega / documentación |
| 2.1.1 | Ítem | Nada de "asdf", usar cursos y nombres creíbles. | Entrega / documentación |
| 2.2 | Agrupador | Setup | Técnico / infraestructura + Entrega / documentación |
| 2.2.1 | Ítem | Llevar 2 computadoras para mostrar la interacción en vivo entre Docente y Alumno. | Técnico / infraestructura + Entrega / documentación |
| 2.3 | Agrupador | Casos a mostrar | Funcionalidad del producto + Entrega / documentación |
| 2.3.1 | Ítem | Usuario que reservó con anticipación y cancelación (tener armado el replay). | Funcionalidad del producto + Entrega / documentación |
| 2.3.2 | Ítem | Qué pasa si se cancela la clase o si ya pasó la fecha. | Funcionalidad del producto |
| 2.3.3 | Ítem | Filtro en frontend para clases cobradas / completadas. | Funcionalidad del producto |
| 3 | Punto | Reglas de Negocio, Estados y Jira | Entrega / documentación |
| 3.1 | Agrupador | Jira | Entrega / documentación |
| 3.1.1 | Ítem | Subir todo esto como issues. | Entrega / documentación |
| 3.2 | Agrupador | Unidad | Funcionalidad del producto |
| 3.2.1 | Ítem | Indicar siempre la unidad (créditos, horas, etc.). | Funcionalidad del producto |
| 3.3 | Agrupador | Los 4 estados de sesión | Funcionalidad del producto |
| 3.3.1 | Ítem | Pendiente. | Funcionalidad del producto |
| 3.3.2 | Ítem | Aceptada. | Funcionalidad del producto |
| 3.3.3 | Ítem | Completada. | Funcionalidad del producto |
| 3.3.4 | Ítem | Cancelada (se puede cancelar de ambos lados). | Funcionalidad del producto |
| 3.4 | Agrupador | Créditos | Funcionalidad del producto |
| 3.4.1 | Ítem | Quedan en freeze (en custodia, tipo plazo fijo) mientras la sesión está pactada. | Funcionalidad del producto |
| 3.4.2 | Ítem | Aclarar qué recupera el comprador si la clase se cancela. | Funcionalidad del producto |
| 4 | Punto | Entrega final de trabajo | Entrega / documentación |
| 4.1 | Agrupador | La entrega final de trabajo consistirá de tres elementos | Entrega / documentación |
| 4.1.1 | Ítem | Presentación en la fecha de coloquio (incluye exposición oral). | Entrega / documentación |
| 4.1.2 | Ítem | Informe con los componentes detallados a continuación. | Entrega / documentación |
| 4.1.3 | Ítem | App construida. | Funcionalidad del producto |
| 4.2 | Agrupador | Primero: Introducción a la iniciativa | Entrega / documentación |
| 4.2.1 | Ítem | Describir en formato texto la iniciativa (Narrativa de la iniciativa). | Entrega / documentación |
| 4.2.2 | Ítem | Usar el diagrama de causa efecto / template de análisis del problema para comprender la necesidad / el problema bajo estudio. | Entrega / documentación |
| 4.2.3 | Ítem | Ilustrar la idea con un Storytelling. | Entrega / documentación |
| 4.2.4 | Ítem | Componer un Scope Canvas de la iniciativa. | Entrega / documentación |
| 4.3 | Agrupador | Segundo: Design Thinking de la iniciativa | Entrega / documentación |
| 4.3.1 | Ítem | User Research: entrevistas / Perfiles Persona / Mapas de empatía. | Entrega / documentación |
| 4.3.2 | Ítem | Benchmarking. | Entrega / documentación |
| 4.3.3 | Ítem | UX: user Interface + Wireframing. | Entrega / documentación |
| 4.3.4 | Ítem | Workflows de la aplicación. | Entrega / documentación |
| 4.4 | Agrupador | Tercero: Construcción de la iniciativa – App funcionando | Entrega / documentación |
| 4.4.1 | Ítem | WBS: Work Breakdown Structure. | Entrega / documentación |
| 4.4.2 | Ítem | USM: User Story Mapping. | Entrega / documentación |
| 4.4.3 | Ítem | Product Backlog. | Entrega / documentación |
| 4.4.4 | Ítem | Detalle de User Stories. | Entrega / documentación |
| 4.4.5 | Ítem | Detalle los Sprints y Realease planning. | Entrega / documentación |
| 4.4.6 | Ítem | Resultado de una Retro ideada por el grupo. | Entrega / documentación |
| 4.4.7 | Ítem | Estimaciones realizadas. | Entrega / documentación |
| 4.4.8 | Ítem | Matriz de riesgos identificados. | Entrega / documentación |
| 4.4.9 | Ítem | Diagrama de la arquitectura elegida. | Técnico / infraestructura |
| 4.4.10 | Ítem | Producto funcionando (Permitiendo el uso para su evaluación). | Funcionalidad del producto |
| 4.5 | Agrupador | Agregado a la fila 4 | Entrega / documentación |
| 4.5.1 | Ítem | Diagramas para la entrega. | Entrega / documentación |

## Bolsa completa de información relevada

Esta sección conserva el detalle original sin resumir.

### 1. Planificación, entrega y demo

| ID | Nota original completa | Ubicación propuesta |
|---|---|---|
| D-01 | Limpieza previa: borrar branches viejas en Git. | Subtask bajo `WBSO-19`. |
| D-02 | Estructura: demo en vivo + retrospectiva de 15 minutos. | Demo: `WBSO-130`; retrospectiva: nuevo Subtask bajo `WBSO-19`. |
| D-03 | Fechas de finales: diciembre y febrero. | Contexto de planificación; no issue separado por ahora. |
| D-04 | Entregable: presentación en PPT con listado de entregables. | Actualizar `WBSO-130`. |
| D-05 | Ale va a hacer preguntas durante la defensa. | Criterio de preparación de `WBSO-130`. |
| D-06 | Retrospectiva: listar aprendizajes del equipo. | Nuevo Subtask de retrospectiva bajo `WBSO-19`. |
| D-07 | Retrospectiva: usar templates de Ale, dinámica del Barquito / Sailboat. | Criterio del Subtask de retrospectiva. |

### 2. Pautas para la demo

| ID | Nota original completa | Ubicación propuesta |
|---|---|---|
| D-08 | Datos reales: nada de `asdf`; usar cursos y nombres creíbles. | Criterio de un nuevo Subtask de entorno y datos de demo. |
| D-09 | Setup: llevar 2 computadoras para mostrar la interacción en vivo entre Docente y Alumno. | Criterio del Subtask de entorno y datos de demo. |
| D-10 | Caso a mostrar: usuario que reservó con anticipación y cancelación; tener armado el replay. | Subtask de escenarios y replay de demo. |
| D-11 | Caso a mostrar: qué pasa si se cancela la clase. | Criterio del Subtask de escenarios y replay. También relacionado con `WBSO-10`. |
| D-12 | Caso a mostrar: qué pasa si ya pasó la fecha. | Criterio del Subtask de escenarios y replay. |
| D-13 | Caso a mostrar: filtro en frontend para clases cobradas / completadas. | Subtask relacionado con `WBSO-12`. |

### 3. Reglas de negocio, estados y Jira

| ID | Nota original completa | Ubicación propuesta |
|---|---|---|
| D-14 | Jira: subir todo esto como issues. | Regla de trabajo del relevamiento; destino `WBSO`. |
| D-15 | Unidad: indicar siempre la unidad: créditos, horas, etc. | Criterio transversal en los issues correspondientes. |
| D-16 | Estado de sesión 1: Pendiente. | Subtask de estados bajo `WBSO-10`. |
| D-17 | Estado de sesión 2: Aceptada. | Subtask de estados bajo `WBSO-10`. |
| D-18 | Estado de sesión 3: Completada. | Subtask de estados bajo `WBSO-10`. |
| D-19 | Estado de sesión 4: Cancelada. | Subtask de estados bajo `WBSO-10`. |
| D-20 | Una sesión cancelada se puede cancelar de ambos lados. | Criterio del Subtask de estados y cancelación bajo `WBSO-10`. |
| D-21 | Los créditos quedan en freeze, en custodia tipo plazo fijo, mientras la sesión está pactada. | Subtask de créditos bajo `WBSO-11`. |
| D-22 | Aclarar qué recupera el comprador si la clase se cancela. | Decisión pendiente y criterio del Subtask de créditos bajo `WBSO-11`. |

### 4. Entregables solicitados por la materia

| ID | Entregable | Ubicación inicial |
|---|---|---|
| E-01 | WBS: Work Breakdown Structure. | Ya representado por `WBSO-21`; revisar contenido final. |
| E-02 | USM: User Story Mapping. | Ya representado por `WBSO-22`; revisar contenido final. |
| E-03 | Product Backlog. | Ya representado por `WBSO-23`; revisar contenido final. |
| E-04 | Detalle de User Stories. | Revisar si está cubierto por los issues existentes; crear Subtask solo si falta. |
| E-05 | Detalle de los Sprints y Release Planning. | Verificar cobertura; crear Subtask si falta. |
| E-06 | Resultado de una retrospectiva ideada por el grupo. | Relacionar con el Subtask nuevo de retrospectiva. |
| E-07 | Estimaciones realizadas. | Verificar cobertura; crear Subtask si falta. |
| E-08 | Matriz de riesgos identificados. | Verificar cobertura; crear Subtask si falta. |
| E-09 | Diagrama de la arquitectura elegida. | Incorporar a `WBSO-129` o crear Subtask específico si se necesita seguimiento propio. |
| E-10 | Producto funcionando, permitiendo el uso para su evaluación. | Relacionar con `WBSO-124`, `WBSO-126` y `WBSO-130`. |
| E-11 | Diagramas para la entrega. | Pendiente de definir cuáles y cómo se presentarán. |
