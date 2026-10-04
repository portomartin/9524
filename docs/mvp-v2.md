# MVP V2 — Plataforma de intercambio de aprendizajes

**Estado:** versión refinada del MVP.

**Fuente de trabajo:** combina el MVP V1 con el refinamiento de producto dictado el 2026-10-03. Esta versión no reemplaza automáticamente los artefactos derivados del MVP V1.

## 1. Idea central

La plataforma facilita el intercambio de aprendizajes entre personas.

Una persona puede ofrecer algo que sabe enseñar y otra puede encontrarlo porque desea aprenderlo. La plataforma acerca a ambas, ayuda a acordar y coordinar el intercambio, registra la sesión y permite que los participantes se califiquen.

El producto debe hacer especialmente fácil este recorrido:

```text
Descubrir → interesarse → encontrar compatibilidad → acordar intercambio
→ coordinar sesión → realizarla → calificarse
```

El valor principal es aprender sin utilizar dinero, ofreciendo a cambio un conocimiento o utilizando créditos internos cuando no existe reciprocidad directa.

## 2. Rol y forma de participación

La cuenta tiene un único rol técnico: `USER`.

Un `USER` puede enseñar, aprender o hacer ambas cosas según la actividad. Enseñar y aprender son formas de participación dentro de una propuesta, solicitud o sesión; no son tipos de cuenta separados.

La plataforma puede contar con permisos administrativos para proteger el servicio, pero la administración no forma parte del recorrido principal del usuario.

## 3. Principios de producto

- El usuario debe comprender el valor de la plataforma rápidamente.
- La exploración de oportunidades de aprendizaje debe ser posible antes de completar un registro extenso.
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
- buscar conocimientos o habilidades;
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

### 4.3 Publicar y encontrar compatibilidades

Un `USER` debe poder:

- publicar una propuesta de aprendizaje individual;
- describir el tema, la categoría, el contenido, el nivel, la modalidad y la duración;
- buscar propuestas y aprendizajes buscados;
- aplicar filtros básicos;
- ver compatibilidades entre lo que puede enseñar y lo que otra persona desea aprender;
- identificar posibles intercambios recíprocos.

La compatibilidad inicial se resolverá mediante reglas claras: tema, nivel, objetivo, modalidad y disponibilidad.

### 4.4 Acordar y coordinar

Dos `USER` deben poder:

- iniciar una solicitud desde una propuesta;
- acordar un intercambio recíproco o mediante créditos;
- indicar fecha, horario, duración y modalidad;
- aceptar o rechazar la solicitud;
- cancelar antes de realizar la sesión;
- confirmar que la sesión fue completada.

El MVP contempla sesiones individuales entre dos `USER`.

### 4.5 Créditos internos

Cuando no exista reciprocidad directa, un `USER` podrá aprender utilizando créditos internos.

- Los créditos se obtienen y utilizan dentro de la plataforma.
- No son dinero y no pueden convertirse en dinero, productos ni servicios.
- El `USER` que aprende entrega los créditos correspondientes.
- El `USER` que ofrece el aprendizaje recibe los créditos.
- Cada movimiento queda registrado.
- La transferencia debe ejecutarse de forma consistente y evitar duplicaciones.

La cantidad de créditos puede definirse al publicar una propuesta, con reglas simples y comprensibles. La estimación mediante LLM no es necesaria para validar el núcleo del MVP y queda fuera de esta versión.

### 4.6 Calificación y confianza

Después de una sesión completada, ambas personas deben poder calificarse mutuamente mediante:

- puntuación de 1 a 5;
- comentario opcional;
- cálculo de una reputación promedio.

La calificación solo estará disponible para participantes de una sesión completada.

## 5. Soporte necesario para operar

Estas capacidades son necesarias, pero deben mantenerse simples:

- autenticación y cierre de sesión;
- perfil básico y edición posterior;
- disponibilidad horaria administrada dentro de la aplicación;
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

## 7. Fuera del MVP V2

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

Una funcionalidad pertenece al MVP V2 si ayuda directamente a que un `USER` pueda:

1. descubrir algo que desea aprender;
2. ofrecer algo que sabe enseñar;
3. encontrar una compatibilidad;
4. acordar y coordinar un intercambio;
5. completar la sesión;
6. registrar créditos o reputación cuando corresponda.

Si no cumple ninguno de estos objetivos, debe quedar fuera del MVP o pasar a una etapa posterior.

## 9. Objetivo del MVP V2

Validar que una plataforma puede facilitar, de forma simple y sin dinero, intercambios reales de aprendizaje entre personas.

La primera versión refinada no busca demostrar una arquitectura amplia ni acumular funcionalidades satelitales. Busca demostrar que una persona puede llegar, descubrir una oportunidad, ofrecer o buscar un aprendizaje, encontrar a otra persona compatible, coordinar una sesión, realizarla y construir confianza mediante la calificación mutua.

## 10. Derivación posterior

Si se selecciona el MVP V2 como fuente de verdad activa, habrá que derivar nuevamente:

- épicas;
- historias de usuario;
- criterios de aceptación;
- tareas técnicas;
- modelo de dominio;
- contrato de API;
- backlog de Jira;
- WBS, USM y SC.

La implementación debe comenzar después de completar esa derivación y validar que todos los artefactos reflejan el mismo núcleo.
