# MVP V3 — Plataforma de intercambio de aprendizajes

**Estado:** fuente de verdad activa del producto.

**Fuente de trabajo:** combina el MVP V2 con los refinamientos dictados posteriormente. Esta versión reemplaza a V1 y V2 como fuente activa, pero no modifica automáticamente sus artefactos derivados.

## 1. Idea central

La plataforma facilita el intercambio de aprendizajes entre personas.

Una persona puede ofrecer algo que sabe enseñar y otra puede encontrarlo porque desea aprenderlo. La plataforma acerca a ambas, ayuda a acordar y coordinar el intercambio, registra la sesión y permite que los participantes se califiquen.

El producto debe hacer especialmente fácil este recorrido:

```text
Descubrir → interesarse → encontrar compatibilidad → acordar intercambio
→ coordinar sesión → realizarla → calificarse
```

El valor principal es aprender sin utilizar dinero, ofreciendo a cambio un conocimiento o utilizando créditos internos cuando no existe reciprocidad directa.

## 2. Roles de acceso y forma de participación

La cuenta tiene un único rol técnico: `USER`.

Un `USER` puede enseñar, aprender o hacer ambas cosas según la actividad. Enseñar y aprender son formas de participación dentro de una propuesta, solicitud o sesión; no son tipos de cuenta separados.

La plataforma contempla además dos formas de acceso diferenciadas:

- `GUEST`: persona no autenticada, sin cuenta, con acceso público restringido y de solo lectura.
- `ADMIN`: usuario con permisos administrativos para proteger el servicio.

El `GUEST` puede explorar propuestas de enseñanza, aprendizajes buscados, reputaciones, rankings, contenido trending y agendas públicas. No puede publicar, solicitar, agendar, intercambiar mensajes, consultar acuerdos privados, utilizar créditos ni calificar.

Cuando un `GUEST` intenta realizar una acción protegida, debe iniciar sesión o registrarse.

La administración no forma parte del recorrido principal del usuario.

## 3. Principios de producto

- El usuario debe comprender el valor de la plataforma rápidamente.
- La exploración de oportunidades de aprendizaje y de agendas públicas debe ser posible antes de completar un registro extenso.
- El registro debe pedir únicamente lo necesario para avanzar y concretar un intercambio.
- La experiencia debe priorizar la acción de enseñar, aprender y encontrar compatibilidades.
- La agenda, los créditos, la reputación y la administración son medios para facilitar el intercambio.
- Las decisiones técnicas, de arquitectura y de API deben servir al flujo del producto, no desplazarlo.
- Toda funcionalidad debe justificar cómo ayuda a que un `USER` encuentre algo para aprender, ofrezca algo para enseñar o concrete un intercambio.

## 4. Alcance imprescindible del MVP

### 4.1 Descubrir y comprender

Una persona debe poder:

- acceder a la plataforma y entender que puede aprender enseñando;
- explorar propuestas de aprendizaje sin registrarse de inmediato;
- explorar propuestas de enseñanza y aprendizajes buscados como `GUEST`;
- buscar conocimientos o habilidades;
- consultar reputaciones, rankings y contenido trending público;
- consultar agendas públicas y sus horarios libres;
- consultar la información suficiente para decidir si una propuesta le interesa.

### 4.2 Crear una participación mínima

Un `USER` autenticado debe poder:

- crear una cuenta con un registro breve;
- completar un perfil básico;
- indicar qué conocimientos o habilidades puede enseñar;
- indicar qué desea aprender;
- describir objetivos de aprendizaje;
- informar nivel, modalidad y disponibilidad cuando sean necesarios para una compatibilidad.

No se debe exigir completar toda la información antes de permitir explorar el producto.

### 4.3 Agenda pública de disponibilidad

Cada `USER` tiene una agenda única de disponibilidad que puede utilizar tanto para enseñar como para aprender.

- La agenda existe desde la creación de la cuenta, pero comienza vacía.
- El `USER` agrega disponibilidades concretas indicando día, fecha y hora.
- La unidad mínima de disponibilidad es una hora.
- Cada franja se carga para una fecha y hora específicas.
- No existe disponibilidad recurrente como concepto del dominio.
- El `USER` puede cargar una sola hora, varios días, meses completos o fechas de uno o más años.
- La interfaz puede ofrecer ayudas para cargar muchas franjas rápidamente, sin convertirlas en recurrencias persistidas.
- El `USER` puede activar o desactivar la visibilidad pública de su agenda.
- Una agenda desactivada no se muestra públicamente.
- Una agenda pública muestra únicamente horarios libres, sin datos de acuerdos privados.
- Cuando una franja queda comprometida por un acuerdo, deja de aparecer como disponible.
- El `USER` puede consultar su propia agenda completa.
- Los detalles del acuerdo, la fecha tomada y sus participantes solo son visibles para los `USER` involucrados.

Las agendas públicas pueden ser consultadas por `USER` y `GUEST`.

### 4.4 Publicar y encontrar compatibilidades

Un `USER` debe poder:

- publicar una propuesta de aprendizaje individual;
- describir el tema, la categoría, el contenido, el nivel, la modalidad y la duración;
- buscar propuestas y aprendizajes buscados;
- aplicar filtros básicos;
- ver compatibilidades entre lo que puede enseñar y lo que otra persona desea aprender;
- identificar posibles intercambios recíprocos.

La compatibilidad inicial se resolverá mediante reglas claras: tema, nivel, objetivo, modalidad y disponibilidad.

### 4.5 Acordar y coordinar

La entidad central del intercambio es la **Sesión**. La plataforma busca que existan sesiones de aprendizaje entre dos `USER`; la solicitud no es una entidad separada del objetivo, sino el estado inicial de una sesión.

Una Sesión debe poder transitar por estos estados:

- `SOLICITADA`: una persona inició el pedido y espera respuesta;
- `CONFIRMADA`: ambas partes aceptaron las condiciones y la fecha quedó acordada;
- `EN_CURSO`: llegó el momento acordado y la sesión comenzó;
- `FINALIZADA`: la sesión fue realizada y puede habilitar créditos, historial y calificaciones;
- `CANCELADA`: la sesión no se realizará o fue cancelada antes de finalizar.

Dos `USER` deben poder:

- crear una Sesión en estado `SOLICITADA` desde una propuesta;
- acordar un intercambio recíproco o mediante créditos;
- indicar fecha, horario, duración y modalidad;
- aceptar la Sesión y pasarla a `CONFIRMADA`;
- iniciar la Sesión cuando corresponda y pasarla a `EN_CURSO`;
- cancelar la Sesión antes de finalizarla;
- marcar la Sesión como `FINALIZADA` cuando se haya realizado.

El MVP contempla sesiones individuales entre dos `USER`.

### 4.6 Créditos internos

Cuando no exista reciprocidad directa, un `USER` podrá aprender utilizando créditos internos.

- Los créditos se obtienen y utilizan dentro de la plataforma.
- No son dinero y no pueden convertirse en dinero, productos ni servicios.
- El `USER` que aprende entrega los créditos correspondientes.
- El `USER` que ofrece el aprendizaje recibe los créditos.
- Cada movimiento queda registrado.
- La transferencia debe ejecutarse de forma consistente y evitar duplicaciones.

La cantidad de créditos puede definirse al publicar una propuesta, con reglas simples y comprensibles. La estimación mediante LLM no es necesaria para validar el núcleo del MVP y queda fuera de esta versión.

### 4.7 Calificación y confianza

Después de una sesión completada, ambas personas deben poder calificarse mutuamente mediante:

- puntuación de 1 a 5;
- comentario opcional;
- cálculo de una reputación promedio.

La calificación solo estará disponible para participantes de una sesión completada.

## 5. Soporte necesario para operar

Estas capacidades son necesarias, pero deben mantenerse simples:

- autenticación y cierre de sesión;
- perfil básico y edición posterior;
- agenda de disponibilidad explícita administrada dentro de la aplicación;
- historial de sesiones, intercambios, créditos y calificaciones;
- validaciones básicas de contenido;
- denuncias de usuarios o publicaciones;
- revisión administrativa mínima y suspensión de cuentas cuando sea necesario.

No se debe convertir ninguna de estas áreas en el centro de la experiencia.

## 6. Seguridad y límites del producto

La plataforma se limita al aprendizaje entre personas con fines educativos, lícitos y seguros.

No tiene como finalidad:

- contratar trabajadores;
- comprar o vender productos;
- prestar servicios profesionales;
- reemplazar una matrícula o habilitación legal;
- funcionar como una red social generalista;
- funcionar como una aplicación de videollamadas o chat completa.

La plataforma puede mostrar advertencias, validar publicaciones, recibir denuncias y permitir revisión administrativa. Las sanciones definitivas requieren revisión humana.

## 7. Fuera del MVP V3

Quedan para etapas posteriores:

- comunidades y círculos especializados;
- badges, premios y reconocimientos;
- recomendaciones avanzadas mediante IA o LLM;
- validación documental de títulos y certificados;
- clases grupales y equipos de enseñanza;
- intercambios con más de dos participantes;
- integraciones con calendarios externos;
- chat completo o videollamadas integradas;
- automatizaciones e integraciones no necesarias para concretar el intercambio.

Estas capacidades pueden enriquecer el producto después de validar el núcleo, pero no deben distraer del recorrido principal.

## 8. Criterio de priorización

Una funcionalidad pertenece al MVP V3 si ayuda directamente a que un `USER` pueda:

1. descubrir algo que desea aprender;
2. ofrecer algo que sabe enseñar;
3. encontrar una compatibilidad;
4. acordar y coordinar un intercambio;
5. completar la sesión;
6. registrar créditos o reputación cuando corresponda.

Si no cumple ninguno de estos objetivos, debe quedar fuera del MVP o pasar a una etapa posterior.

## 9. Reglas específicas de la agenda

La agenda del MVP V3 no admite reglas de recurrencia. Las ayudas de carga masiva son únicamente una facilidad de interfaz para crear disponibilidades concretas.

La visibilidad pública nunca expone acuerdos, participantes ni información privada. Solo expone franjas libres cuando el `USER` decidió publicar su agenda.

## 10. Objetivo del MVP V3

Validar que una plataforma puede facilitar, de forma simple y sin dinero, intercambios reales de aprendizaje entre personas.

La primera versión refinada no busca demostrar una arquitectura amplia ni acumular funcionalidades satelitales. Busca demostrar que una persona puede llegar como `GUEST`, descubrir una oportunidad y una disponibilidad, registrarse solo cuando necesite accionar, ofrecer o buscar un aprendizaje, encontrar a otra persona compatible, coordinar una sesión, realizarla y construir confianza mediante la calificación mutua.

## 11. Impactos para la derivación

Al adoptar el MVP V3 como fuente de verdad, hay que revisar especialmente:

- actores y permisos de acceso público;
- navegación sin autenticación y transición de `GUEST` a `USER`;
- visibilidad pública de propuestas, reputaciones, rankings y agendas;
- modelo de disponibilidad por fecha y hora concreta;
- ausencia de recurrencias en dominio y API;
- ocultamiento de franjas tomadas;
- privacidad de acuerdos y participantes;
- búsqueda y compatibilidad;
- épicas, historias, criterios de aceptación y subtareas;
- contrato de API, WBS, USM, SC y backlog de Jira.

## 12. Derivación posterior

Para alinear el proyecto con el MVP V3, hay que derivar nuevamente:

- épicas;
- historias de usuario;
- criterios de aceptación;
- tareas técnicas;
- modelo de dominio;
- contrato de API;
- backlog de Jira;
- WBS, USM y SC.

La implementación debe comenzar después de completar esa derivación y validar que todos los artefactos reflejan el mismo núcleo.
