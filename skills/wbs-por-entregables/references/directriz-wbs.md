# Directriz de contenido para la WBS

La captura de referencia se utiliza únicamente para identificar el tipo de nombres y el nivel de detalle esperado en los elementos de la WBS. No define colores, distribución gráfica ni una herramienta específica para representar el resultado.

## Definición de referencia

WBS significa **Work Breakdown Structure** —estructura de desglose del trabajo—. Es un gráfico o herramienta que permite ordenar y clasificar las tareas de un proyecto bajo una jerarquía. Descompone el trabajo en entregables más pequeños y estimables.

En esta skill se prioriza la descomposición por entregables y resultados verificables. Las tareas pueden aparecer en los niveles inferiores solo cuando ayudan a producir o completar un entregable.

## Niveles de desglose de referencia

### Nivel 0: producto o sistema

Representa el proyecto completo, por ejemplo `Airbnb`.

### Nivel 1: bloques principales

Son grandes áreas de resultado o gestión. En la captura aparecen, por ejemplo:

- Gestión de usuarios.
- Gestión de hospedaje.
- Gestión de experiencias.
- Administración y control de proyectos.

### Nivel 2: módulos o subentregables

Descomponen cada bloque principal en capacidades relacionadas, por ejemplo:

- Sistema de registro.
- Sistema de inicio de sesión.
- Perfil de usuario.
- Reserva de hospedaje.
- Búsquedas de hospedaje.

### Nivel 3: funcionalidades concretas

Representan resultados específicos que pueden describirse y verificarse, por ejemplo:

- Registrarse con mail.
- Iniciar sesión con mail.
- Cerrar sesión.
- Crear hospedaje.
- Modificar hospedaje.
- Eliminar hospedaje.

## Convenciones de numeración

- Bloque principal: `1`, `2`, `3`.
- Módulo: `1.1`, `1.2`, `2.1`.
- Funcionalidad: `1.1.1`, `1.2.1`, `2.1.1`.
- La numeración debe reflejar la relación padre-hijo.
- No reutilizar un identificador para dos elementos distintos.

## Aplicación al proyecto

Para la plataforma de intercambio de aprendizajes, los bloques principales pueden organizarse alrededor de entregables como cuentas y perfiles, enseñanza y aprendizaje, clases e intercambios, créditos y sesiones, seguridad y administración, e inteligencia artificial. Los nombres definitivos deben surgir del MVP vigente.

Si el MVP los incluye, el bloque de administración y control puede contener directamente entregables de gestión, como documentación, backlog, informes de avance e informes de riesgos, aunque no tengan un nivel intermedio de módulo. Estos ejemplos no agregan alcance al MVP.
