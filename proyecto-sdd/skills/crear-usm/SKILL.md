---
name: crear-usm
description: Crear o actualizar un User Story Map directamente desde una versión indicada del MVP, independiente de la WBS y del backlog.
---

# User Story Mapping

Usar esta skill cuando el usuario solicite crear, revisar o reorganizar el User Story Map del proyecto.

## Fuentes de información

Leer primero:

- `AGENTS.md` para las reglas generales del proyecto.
- La versión indicada del MVP (`proyecto-sdd/mvp-v1.md`, `proyecto-sdd/mvp-v2.md` o `proyecto-sdd/mvp-v3.md`) como única fuente de verdad del alcance de la ejecución.
- `references/directriz-usm.md` para aplicar la estructura conceptual del mapa.

Derivar el contenido únicamente del MVP. No leer la WBS ni el backlog como entradas. Las reglas y referencias orientan el método y el formato, no agregan requisitos. Si existe `proyecto-sdd/usm.md`, consultarlo solo para preservar identificadores y formato compatibles con el MVP; no usarlo como fuente de alcance.

## Modelo del mapa

Organizar el mapa siguiendo un recorrido de izquierda a derecha y una descomposición de arriba hacia abajo:

1. **Backbone:** estructura superior que contiene las actividades principales.
2. **Actividades:** grandes momentos del recorrido del usuario.
3. **Flujo narrativo:** orden lógico en que el usuario atraviesa las actividades.
4. **Tareas del usuario:** acciones que una persona realiza dentro de cada actividad.
5. **Detalles o historias:** necesidades concretas que describen valor para un rol.
6. **Release slice:** corte horizontal que identifica qué conjunto de historias forma el MVP.

Cuando se organice el mapa, considerar estos niveles conceptuales:

1. **Rol:** identifica al usuario que recorre el mapa.
2. **Actividades o backbone:** agrupa los grandes momentos del recorrido.
3. **Tareas del usuario:** expresa las acciones principales dentro de cada actividad.
4. **Detalles:** descompone cada tarea en historias o comportamientos concretos.

El `release slice` puede representarse como una marca de alcance o una separación entre historias incluidas y posteriores. No copiar los colores, nombres ni el dominio de la captura de referencia. El resultado puede presentarse como tabla, lista jerárquica, diagrama u otro formato que facilite la lectura.

El mapa debe representar los recorridos de `GUEST`, `USER` y `ADMIN` cuando corresponda:

- `GUEST`: descubre propuestas, reputaciones, rankings, trending y agendas públicas en modo lectura.
- `USER`: ofrece aprendizajes, busca aprender, coordina sesiones y califica.
- `ADMIN`: revisa contenido y denuncias mediante permisos administrativos.

Un `USER` puede enseñar y aprender según la actividad.

## Reglas del proyecto

- Basar el mapa en la versión indicada del MVP, no en ideas no aprobadas.
- Mantener el MVP limitado a intercambios y sesiones individuales 1 a 1.
- No proponer funcionalidades futuras que no estén descritas como tales en el MVP; señalar exclusiones sin inventar historias para otros cortes.
- No convertir el mapa en una lista de tareas técnicas.
- Cada historia debe expresar una acción y un beneficio para un rol.
- Evitar duplicar historias cuando una misma acción pueda ser realizada por cualquier `USER`.
- Mantener el flujo narrativo de la experiencia, desde el ingreso hasta la finalización y evaluación de una sesión.
- Usar el release slice para separar el MVP del alcance futuro, no para crear una lista independiente de prioridades.
- Mantener trazabilidad directa hacia secciones del MVP.
- Señalar ambigüedades, dependencias y funcionalidades que no tengan respaldo en la especificación.

## Resultado esperado

Presentar:

1. El User Story Map en Markdown, usando el formato más claro para el proyecto.
2. La identificación del backbone, actividades, tareas, detalles e historias.
3. El flujo narrativo del usuario.
4. El release slice del MVP y los elementos posteriores.
5. Una tabla de trazabilidad hacia secciones de la versión indicada del MVP.
6. Supuestos y puntos pendientes de confirmar.

No modificar ninguna versión del MVP ni `proyecto-sdd/wbs.md` automáticamente. Si el mapa se aprueba, guardarlo en `proyecto-sdd/usm.md` y registrar el cambio cuando corresponda.
