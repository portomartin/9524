# Trabajo Práctico

## MVP: Plataforma de intercambio de aprendizajes

### Conceptos principales

Dentro de la plataforma existirá un único rol técnico:

- **USER:** usuario autenticado que puede ofrecer conocimientos o habilidades y solicitar o participar en sesiones de aprendizaje.

La participación como persona que enseña o aprende se determina por cada actividad y no constituye un tipo de cuenta separado.

### Descripción general
El MVP consistirá en una aplicación web que permita a las personas enseñar lo que saben y aprender de otros usuarios sin utilizar dinero.
Cada usuario indicará qué conocimientos o habilidades puede enseñar y cuáles desea aprender. A partir de esta información, la plataforma identificará personas compatibles considerando los temas ofrecidos y buscados, el nivel, los objetivos de aprendizaje, los horarios disponibles y la modalidad de las sesiones.

Cada usuario podrá describir libremente sus objetivos de aprendizaje, sin limitarse a opciones predeterminadas. Por ejemplo:

- Aprender inglés para mantener conversaciones.
- Aprender programación para crear una página web.
- Aprender fotografía para mejorar sus trabajos.
- Prepararse para rendir un examen.
- Alcanzar un nivel intermedio.

La plataforma utilizará esta información para mejorar la compatibilidad y generar recomendaciones personalizadas mediante inteligencia artificial.
El sistema priorizará los intercambios recíprocos, en los que dos personas puedan enseñarse mutuamente. También contará con créditos virtuales para permitir intercambios indirectos cuando esa coincidencia no exista.
La aplicación estará orientada exclusivamente al aprendizaje entre personas. No tendrá como finalidad contratar trabajadores, comprar o vender productos ni prestar servicios profesionales.
### Perfiles de usuario
Cada perfil incluirá:
- Nombre.
- Descripción personal.
- Ubicación general.
- Conocimientos o habilidades que la persona puede enseñar.
- Conocimientos o habilidades que desea aprender.
- Nivel en cada tema.
- Objetivos de aprendizaje.
- Disponibilidad horaria.
- Modalidad preferida: presencial o virtual.
- Calificación promedio obtenida en intercambios anteriores.
- Cantidad disponible de créditos virtuales.

El nivel de conocimiento se indicará para cada tema, tanto en las habilidades que la persona puede enseñar como en aquellas que desea aprender. Los niveles se clasificarán en principiante, intermedio y avanzado.
### Publicación de propuestas de enseñanza
Los usuarios podrán publicar aquello que desean enseñar. Cada publicación incluirá:
- Nombre del conocimiento o la habilidad.
- Categoría.
- Descripción de lo que se enseñará.
- Nivel requerido y nivel que se podrá alcanzar.
- Modalidad de la sesión.
- Duración estimada.
- Cantidad de créditos asignada a la sesión.
- Tipo de clase: individual.
Los temas se seleccionarán a partir de categorías definidas por la plataforma. Esto permitirá organizar las publicaciones, mejorar las búsquedas y reducir la aparición de contenido no permitido.
### Sistema de compatibilidad
La plataforma contará con un sistema basado en reglas para identificar usuarios compatibles.
Se considerará que existe compatibilidad cuando:
- Un usuario puede enseñar algo que otro desea aprender.
- Los niveles y objetivos de aprendizaje son compatibles.
- Coinciden en la modalidad seleccionada.
- Tienen al menos una franja horaria disponible en común.
El sistema destacará especialmente los intercambios recíprocos. Por ejemplo, una persona que sabe inglés y quiere aprender programación podrá coincidir con otra que sabe programación y quiere aprender inglés.
Los resultados mostrarán la información principal de cada usuario, los aprendizajes compatibles, su disponibilidad y su calificación promedio.
### Intercambios recíprocos y créditos virtuales
Cuando dos personas puedan enseñarse mutuamente, podrán acordar una sesión para cada aprendizaje sin necesidad de transferir créditos, siempre que ambas partes consideren equilibrado el intercambio.

Cuando el intercambio directo no sea posible, se utilizarán créditos virtuales:
- Cada usuario recibirá una cantidad inicial al registrarse.
- Quien participe como aprendiz entregará los créditos correspondientes al completar la sesión.
- Quien enseñe recibirá esos créditos y podrá utilizarlos para aprender con otro usuario.
- Cada movimiento quedará registrado en el historial de ambas personas.
Para definir una cantidad orientativa de créditos, se podrá utilizar un modelo de lenguaje (LLM) que compare cada propuesta con un estándar base de una sesión individual. El cálculo podrá considerar la duración, el nivel, la preparación necesaria y la modalidad. El LLM solo propondrá un valor; la plataforma aplicará reglas mínimas y máximas, y el usuario deberá confirmar la cantidad antes de publicar. Los administradores podrán revisar o corregir valores que resulten inadecuados.


La cantidad de créditos se definirá al publicar la propuesta y representará el tiempo y la dedicación de la sesión. Los créditos solo podrán utilizarse dentro de la plataforma y no podrán convertirse en dinero, productos o servicios.
### Solicitudes y reservas
Un usuario podrá solicitar una sesión desde la publicación de un aprendizaje. La solicitud incluirá:
- Usuario que realiza la solicitud.
- Usuario que la recibe.
- Tema seleccionado.
- Fecha y horario propuestos.
- Duración.
- Modalidad.
- Tipo de intercambio: recíproco o mediante créditos.
- Conocimiento ofrecido a cambio, si corresponde.
- Cantidad de créditos, si corresponde.
- Mensaje opcional.
Las solicitudes podrán tener los siguientes estados: pendiente, aceptada, rechazada, cancelada o completada.
El usuario que recibe la solicitud podrá aceptarla o rechazarla. Cualquiera de los participantes podrá cancelarla antes de que se realice. Una vez finalizado el encuentro, la sesión se marcará como completada y, si corresponde, se transferirán los créditos.
### Disponibilidad horaria
Cada usuario podrá configurar sus días y horarios disponibles. La plataforma utilizará esta información para mostrar coincidencias y facilitar la elección de una fecha.
No se incluirá una integración con calendarios externos. La disponibilidad y las reservas se administrarán únicamente dentro de la aplicación.
### Historial de actividades
Los usuarios podrán consultar un historial con:
- Sesiones solicitadas, aceptadas, canceladas y completadas.
- Temas enseñados y aprendidos.
- Intercambios recíprocos realizados.
- Créditos recibidos y utilizados.
- Calificaciones realizadas y recibidas.
### Calificaciones y reputación
Después de completar una sesión, los participantes podrán calificarse mutuamente mediante una puntuación de 1 a 5 y un comentario opcional.
La plataforma calculará la calificación promedio de cada usuario y la mostrará en su perfil. Solo podrán calificarse personas que hayan participado en una sesión marcada como completada.
### Búsqueda y filtros
Los usuarios podrán buscar propuestas y aplicar filtros por:
- Conocimiento o habilidad.
- Categoría.
- Nivel.
- Modalidad.
- Ubicación general.
- Disponibilidad.
- Tipo de intercambio.
- Cantidad de créditos.
Los filtros permitirán encontrar oportunidades relevantes aunque no exista un intercambio recíproco entre los usuarios.
### Funcionalidades principales del MVP
La primera versión incluirá:
- Registro e inicio de sesión.
- Creación y edición de perfiles.
- Publicación de conocimientos o habilidades que se pueden enseñar.
- Registro de lo que cada usuario desea aprender.
- Búsqueda y filtros básicos.
- Compatibilidad basada en reglas.
- Detección de intercambios recíprocos.
- Configuración de disponibilidad horaria.
- Solicitudes de sesiones.
- Aceptación, rechazo y cancelación de solicitudes.
- Confirmación de sesiones completadas.
- Transferencia de créditos virtuales cuando corresponda.
- Historial de sesiones y movimientos.
- Calificaciones y reputación.
- Denuncia de usuarios o publicaciones.
- Administración básica del contenido denunciado.
### Contenidos no permitidos y seguridad
La plataforma permitirá únicamente publicaciones y sesiones de aprendizaje con fines educativos, lícitos y seguros.
La plataforma incorporará:
- Categorías de aprendizaje permitidas.
- Lista de palabras y expresiones prohibidas.
- Validación de publicaciones antes de guardarlas.
- Botón para denunciar usuarios o publicaciones.
- Registro de denuncias.
- Revisión administrativa del contenido denunciado.
- Suspensión de cuentas.
- Términos y condiciones de uso.
- Mensajes de advertencia antes de publicar.
Las denuncias y sanciones serán revisadas por un administrador. La plataforma no aplicará sanciones definitivas de manera automática.
Para las clases que requieran formación académica o habilitación específica, el usuario podrá informar sus títulos, certificados o estudios relacionados. La plataforma podrá implementar un sistema de validación de títulos y estudios mediante la carga de documentación, la revisión administrativa y distintos niveles de verificación visibles en el perfil.

La validación no implicará que la persona pueda ofrecer servicios profesionales ni reemplazará una matrícula o habilitación legal cuando estas sean obligatorias. Su finalidad será aumentar la confianza en las propuestas educativas y distinguir entre conocimientos adquiridos por experiencia, formación acreditada y certificaciones verificadas.


### Panel de administración
La aplicación contará con un panel administrativo básico que permitirá:
- Consultar usuarios registrados.
- Consultar publicaciones.
- Revisar denuncias.
- Ocultar publicaciones.
- Suspender o reactivar cuentas.
- Administrar categorías de aprendizaje.
- Administrar palabras o expresiones prohibidas.
### Objetivo del MVP
El objetivo del MVP es demostrar el funcionamiento completo de una plataforma de intercambio de aprendizajes: desde el registro y la publicación de aquello que una persona puede enseñar hasta la búsqueda de alguien compatible, la coordinación de las sesiones y la calificación de los participantes.
La propuesta busca validar que una comunidad puede organizarse para que sus integrantes enseñen lo que saben y aprendan lo que necesitan. Los intercambios podrán realizarse directamente entre dos personas o mediante créditos virtuales cuando no exista una coincidencia recíproca.
De esta manera, el proyecto mantendrá un alcance adecuado para una primera versión funcional y, al mismo tiempo, expresará con claridad su idea central: aprender enseñando y enseñar para poder seguir aprendiendo.

