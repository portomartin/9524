# User Story Map del MVP

**Proyecto:** Plataforma de intercambio de aprendizajes  
**Versión:** 1.1 — derivada del MVP aprobado

## Backbone y flujo narrativo

`Acceder → Configurar perfil → Ofrecer o buscar aprendizajes → Encontrar compatibilidades → Acordar intercambio → Coordinar sesión → Completar sesión → Consultar historial y calificar`

## Rol y participantes

- **USER:** puede ofrecer conocimientos, buscar aprendizajes y participar en sesiones.
- **Administrador:** revisa denuncias, contenidos y cuentas mediante permisos administrativos.

## Mapa de historias

### 1. Acceder

- Registrarse para crear una cuenta.
- Iniciar sesión para acceder al perfil y las actividades.
- Cerrar sesión para proteger la cuenta.

### 2. Configurar el perfil

- Completar nombre, descripción y ubicación general.
- Definir conocimientos que puede ofrecer y aprendizajes que desea buscar según la actividad.
- Indicar conocimientos ofrecidos y buscados.
- Informar nivel y objetivos por tema.
- Configurar disponibilidad y modalidad presencial o virtual.
- Consultar reputación y créditos disponibles.

### 3. Ofrecer o buscar aprendizajes

#### Persona que ofrece un aprendizaje

- Publicar una propuesta con conocimiento, categoría y descripción.
- Informar nivel requerido, nivel alcanzable, modalidad y duración.
- Definir créditos y publicar solo sesiones individuales.

#### Persona que busca un aprendizaje

- Indicar qué conocimiento desea aprender.
- Describir libremente su objetivo.
- Informar nivel actual, modalidad y disponibilidad.

### 4. Encontrar compatibilidades

- Buscar propuestas y solicitudes.
- Filtrar por conocimiento, categoría, nivel, modalidad, ubicación, disponibilidad, intercambio y créditos.
- Encontrar coincidencias por conocimientos, niveles, objetivos y horarios.
- Recibir recomendaciones mediante IA.

### 5. Acordar el intercambio

- Solicitar una sesión desde una propuesta.
- Elegir intercambio recíproco o mediante créditos.
- Incluir un mensaje opcional.
- Aceptar o rechazar la solicitud.

### 6. Coordinar la sesión

- Proponer fecha y horario dentro de la disponibilidad.
- Reservar una solicitud aceptada.
- Modificar o cancelar antes de realizarla.
- Gestionar estados pendiente, aceptada, rechazada, cancelada y completada.

### 7. Completar la sesión

- Realizar la sesión individual 1 a 1.
- Confirmar la finalización.
- Transferir créditos cuando corresponda.
- Registrar el movimiento en el historial.

### 8. Consultar resultados y calificar

- Consultar sesiones, temas enseñados y aprendidos.
- Consultar intercambios y créditos recibidos o utilizados.
- Calificar de 1 a 5 y agregar un comentario opcional.
- Actualizar la reputación promedio.

### Transversales

- Validar publicaciones y mostrar advertencias.
- Denunciar usuarios o publicaciones.
- Revisar denuncias y administrar cuentas.
- Cargar y revisar títulos, certificados o referencias.

## Release slice

El MVP incluye las historias anteriores para intercambios y sesiones individuales 1 a 1 entre dos usuarios.

Fuera del MVP quedan las clases grupales, los equipos de enseñanza, los intercambios 2×1 y cualquier sesión con más de dos usuarios.

## Trazabilidad

| Actividad | Secciones del MVP |
|---|---|
| Acceder | Funcionalidades principales del MVP |
| Configurar el perfil | Perfiles de usuario |
| Ofrecer o buscar aprendizajes | Publicación de propuestas; Descripción general; Perfiles de usuario |
| Encontrar compatibilidades | Sistema de compatibilidad; Búsqueda y filtros |
| Acordar el intercambio | Solicitudes y reservas; Intercambios recíprocos y créditos virtuales |
| Coordinar la sesión | Solicitudes y reservas; Disponibilidad horaria |
| Completar la sesión | Solicitudes y reservas; Intercambios recíprocos y créditos virtuales; Historial de actividades |
| Consultar resultados y calificar | Historial de actividades; Calificaciones y reputación |
| Transversales | Contenidos no permitidos y seguridad; Panel de administración |

## Pendientes

- Definir límites y reglas del cálculo orientativo de créditos mediante LLM.
- Definir documentos aceptados y procedimiento de validación.
- Confirmar el diseño final de las solicitudes de aprendizaje.
- Definir el canal de contacto sin convertirlo en una aplicación de chat completa.
