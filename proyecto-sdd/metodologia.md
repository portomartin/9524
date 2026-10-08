# Metodología de planificación

## Importancia de la WBS y la USM

La WBS y la USM permiten definir y organizar el alcance del MVP. A partir de estas herramientas se pueden identificar los entregables, las actividades, las tareas y las historias de usuario necesarias para construir el producto.

En este proyecto, WBS, USM, backlog y subtareas se elaboran de manera independiente a partir de una versión explícita del MVP. Actualmente reflejan el **MVP V3**, en `proyecto-sdd/mvp-v3.md`. V1 y V2 se conservan como referencias históricas. Ninguno de los documentos derivados usa a los otros como fuente de requisitos. Las reglas y referencias de los skills orientan el formato y el método; cada salida mantiene trazabilidad directa al MVP seleccionado.

El [skill de derivación](skills/derivar-planificacion-mvp/SKILL.md) declara el grafo: leer MVP, preparar las salidas, generar subtareas y revisar la derivación. Las ramas iniciales pueden ejecutarse en cualquier orden y no requieren ejecución simultánea.

Al final, [crear-sprints](skills/crear-sprints/SKILL.md) utiliza el backlog revisado, sus subtareas y los datos del equipo para estimar historias, simular capacidad y proponer sprints. Esta etapa sí depende de los documentos anteriores. Su resultado se guarda en `proyecto-sdd/sprints.md`, identificando los supuestos y decisiones pendientes. La capacidad horaria se calcula según dedicación y disponibilidad; la velocidad en story points se obtiene del historial o se declara como hipótesis, sin convertir horas a puntos. La propuesta local no modifica Jira.

La WBS organiza el trabajo según entregables y resultados verificables. La USM representa el recorrido de los usuarios y permite visualizar cómo interactúan con el producto. Ambas herramientas ayudan a mantener un alcance claro y evitar la incorporación de funcionalidades que no forman parte del MVP.

Estas herramientas orientan principalmente el alcance y la organización del trabajo. Las decisiones técnicas, las estimaciones precisas y las fechas definitivas requieren además analizar dependencias, recursos y esfuerzo.
