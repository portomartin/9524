# Backlog del MVP

**Proyecto:** Plataforma de intercambio de aprendizajes  
**Versión:** 1.0 — derivada del MVP aprobado

Las historias se derivan exclusivamente de `docs/mvp.md`. No se asignan prioridades ni estimaciones porque el MVP no las define.

## Épica E1. Acceso y perfiles

### Introducción

Esta épica permite que una persona ingrese a la plataforma y configure la información necesaria para participar como Docente, Alumno o ambas cosas.

Construir una identidad básica y unas preferencias que permitan encontrar aprendizajes y personas compatibles.

La persona puede acceder a la plataforma y mantener un perfil completo y editable.

### HU01 Registrarse

Como usuario, quiero registrarme para crear una cuenta y utilizar la plataforma.

- **✅ Aceptación:** Se completan los datos básicos y se crea la cuenta.

#### 🛠️ Refinamiento aplicado

- Validar campos obligatorios y formato
- Mostrar errores junto al campo correspondiente
- Conservar los datos válidos después de un error
- Evitar almacenar contraseñas en texto plano
- Permitir contraseñas largas y no imponer combinaciones arbitrarias de caracteres.

#### ❓ Pendientes de decisión

- Confirmación de correo
- Longitud mínima
- Aceptación de términos
- Campos exactos del primer paso y política ante un correo ya registrado.

### HU02 Iniciar y cerrar sesión

Como usuario, quiero iniciar y cerrar sesión para acceder a mis actividades y proteger mi cuenta.

- **✅ Aceptación:** El usuario puede iniciar sesión con sus credenciales y cerrar la sesión activa.

#### 🛠️ Refinamiento aplicado

- Ofrecer mensajes de error claros sin revelar información sensible
- Invalidar la sesión al cerrar sesión
- Proteger los intentos repetidos y mantener una sesión segura en el navegador.

#### ❓ Pendientes de decisión

- Duración de la sesión
- Cierre de todas las sesiones
- Recuperación de contraseña
- Bloqueo temporal y autenticación multifactor.

### HU03 Completar el perfil

Como usuario, quiero completar mi nombre, descripción y ubicación general para presentarme ante la comunidad.

- **✅ Aceptación:** El perfil permite guardar esos datos y editarlos.

#### 🛠️ Refinamiento aplicado

- Permitir guardar parcialmente y editar el perfil
- Distinguir campos obligatorios de opcionales
- Mostrar una vista previa de la información visible para otros usuarios
- Validar textos y límites de longitud.

#### ❓ Pendientes de decisión

- Campos obligatorios
- Visibilidad de ubicación
- Posibilidad de ocultar el perfil y reglas para eliminar o cambiar información.

### HU04 Definir roles y preferencias

Como usuario, quiero indicar mis roles, niveles, objetivos, modalidad y disponibilidad para encontrar aprendizajes compatibles.

- **✅ Aceptación:** Se pueden configurar Docente y Alumno, niveles por tema, modalidad y franjas horarias.

#### 🛠️ Refinamiento aplicado

- Permitir que una persona actúe como Docente y Alumno
- Configurar nivel por tema
- Conservar las preferencias al editarlas
- Mostrar qué información falta para mejorar la compatibilidad.

#### ❓ Pendientes de decisión

- Si se exige al menos un tema para enseñar o aprender
- Valores permitidos para disponibilidad y si las preferencias pueden modificarse mientras existen solicitudes activas.

## Épica E2. Propuestas de enseñanza

### Introducción

Esta épica permite que un Docente publique un conocimiento o habilidad para que otras personas puedan encontrarlo y solicitar una sesión individual.

Convertir los conocimientos ofrecidos por la comunidad en propuestas claras, comparables y utilizables dentro del MVP.

Una propuesta publicada contiene la información necesaria para que un Alumno evalúe si desea solicitarla.

### HU05 Publicar una propuesta

Como Docente, quiero publicar un conocimiento o habilidad para que otros usuarios puedan encontrarlo.

- **✅ Aceptación:** La propuesta incluye nombre, categoría, descripción, niveles, modalidad, duración y créditos.

#### 🛠️ Refinamiento aplicado

- Validar campos antes de publicar
- Permitir guardar un borrador
- Mostrar un resumen previo
- Impedir publicar sin categoría
- Modalidad
- Nivel
- Duración y créditos cuando sean obligatorios.

#### ❓ Pendientes de decisión

- Moderación previa obligatoria
- Límites de duración y créditos
- Edición posterior a una solicitud y estados de borrador/publicada/oculta.

### HU06 Publicar una sesión individual

Como Docente, quiero indicar que mi propuesta es individual para mantener el alcance del MVP.

- **✅ Aceptación:** La propuesta no permite configurar más de un Docente o Alumno en la misma sesión.

#### 🛠️ Refinamiento aplicado

- Validar que cada sesión tenga un solo Docente y un solo Alumno
- Rechazar configuraciones grupales
- Comunicar la restricción antes de guardar.

#### ❓ Pendientes de decisión

- Si una propuesta puede tener múltiples horarios disponibles y si el Docente puede publicar varias propuestas sobre el mismo tema.

## Épica E3. Solicitudes de aprendizaje

### Introducción

Esta épica permite que un Alumno exprese qué desea aprender y con qué objetivo, sin limitarse a opciones predeterminadas.

Representar necesidades de aprendizaje reales para mejorar la búsqueda y la compatibilidad entre personas.

El sistema dispone de una solicitud de aprendizaje suficientemente clara para buscar propuestas adecuadas.

### HU07 Indicar qué aprender

Como Alumno, quiero indicar qué conocimiento deseo aprender para encontrar propuestas adecuadas.

- **✅ Aceptación:** La solicitud permite describir el objetivo libremente, indicar nivel, modalidad y disponibilidad.

#### 🛠️ Refinamiento aplicado

- Permitir objetivo libre y datos estructurados de apoyo
- Permitir editar
- Pausar o eliminar la solicitud
- Mostrar un estado claro de la solicitud.

#### ❓ Pendientes de decisión

- Si una persona puede tener varias solicitudes simultáneas
- Cuándo una solicitud deja de estar activa y qué datos son obligatorios.

## Épica E4. Búsqueda y compatibilidad

### Introducción

Esta épica ayuda a las personas a encontrar propuestas, solicitudes y usuarios compatibles según sus conocimientos y objetivos.

Reducir el esfuerzo de encontrar oportunidades relevantes y favorecer los intercambios recíprocos.

Los resultados muestran oportunidades y personas compatibles con información suficiente para decidir el siguiente paso.

### HU08 Buscar propuestas y solicitudes

Como usuario, quiero buscar conocimientos, propuestas y solicitudes para encontrar oportunidades relevantes.

- **✅ Aceptación:** Se muestran resultados relacionados con el conocimiento o habilidad buscada.

#### 🛠️ Refinamiento aplicado

- Mostrar estado vacío cuando no existan resultados
- Permitir consultar resultados en páginas
- Presentar información suficiente para distinguir una propuesta de una solicitud.

#### ❓ Pendientes de decisión

- Orden por relevancia
- Fecha o compatibilidad
- Búsqueda parcial y comportamiento ante errores del servicio.

### HU09 Aplicar filtros

Como usuario, quiero filtrar resultados por conocimiento, categoría, nivel, modalidad, ubicación, disponibilidad, intercambio y créditos.

- **✅ Aceptación:** Cada filtro puede aplicarse a los resultados y combinarse con otros.

#### 🛠️ Refinamiento aplicado

- Permitir combinar filtros
- Mostrar filtros activos
- Ofrecer limpiar uno o todos
- Conservar los filtros al cambiar de página
- Informar cuando la combinación no produce resultados.

#### ❓ Pendientes de decisión

- Valores exactos de cada filtro
- Si se puede filtrar por rangos de créditos y si los filtros se guardan entre sesiones.

### HU10 Encontrar compatibilidades

Como usuario, quiero encontrar personas compatibles según conocimientos, niveles, objetivos, modalidad y horarios.

- **✅ Aceptación:** Los resultados muestran coincidencias y la información principal de cada usuario.

#### 🛠️ Refinamiento aplicado

- Mostrar qué criterios generaron cada coincidencia
- Diferenciar coincidencia parcial de coincidencia fuerte
- Evitar presentar el resultado como garantía de éxito
- Permitir revisar la información que sustenta la coincidencia.

#### ❓ Pendientes de decisión

- Ponderación de criterios
- Mínimo de compatibilidad
- Desempate y tratamiento de datos faltantes.

### HU11 Recibir recomendaciones

Como usuario, quiero recibir recomendaciones de clases y personas compatibles según mis intereses y objetivos.

- **✅ Aceptación:** Las recomendaciones consideran objetivos libres, nivel, modalidad y disponibilidad.

#### 🛠️ Refinamiento aplicado

- Explicar por qué se recomienda una persona o propuesta
- Permitir descartar una recomendación
- Evitar repetir indefinidamente contenido descartado
- Actualizar recomendaciones cuando cambien las preferencias.

#### ❓ Pendientes de decisión

- Frecuencia de actualización
- Cantidad de recomendaciones
- Uso de IA/LLM y métricas para evaluar la calidad.

## Épica E5. Intercambios y sesiones

### Introducción

Esta épica organiza el paso desde una propuesta encontrada hasta la realización y confirmación de una sesión de aprendizaje.

Permitir que Docentes y Alumnos coordinen intercambios claros, con estados y reglas visibles para ambas partes.

Una sesión pasa por estados claros y, al completarse, queda disponible para historial, créditos y calificaciones.

### HU12 Solicitar una sesión

Como Alumno, quiero solicitar una sesión desde una propuesta para comenzar el intercambio.

- **✅ Aceptación:** La solicitud identifica participantes, tema, fecha, horario, duración, modalidad y tipo de intercambio.

#### 🛠️ Refinamiento aplicado

- Validar disponibilidad y datos obligatorios
- Impedir solicitudes duplicadas para la misma propuesta y franja
- Mostrar un resumen antes de enviar
- Registrar el estado inicial como pendiente.

#### ❓ Pendientes de decisión

- Conflictos con otras reservas
- Modificación de una solicitud pendiente y vencimiento de solicitudes sin respuesta.

### HU13 Elegir el tipo de intercambio

Como Docente y Alumno, quiero acordar si el intercambio será recíproco o mediante créditos.

- **✅ Aceptación:** Se registra el tipo elegido y, si corresponde, el conocimiento ofrecido o la cantidad de créditos.

#### 🛠️ Refinamiento aplicado

- Mostrar claramente las dos alternativas
- Pedir confirmación del tipo elegido
- Registrar el conocimiento ofrecido cuando sea recíproco y los créditos cuando corresponda
- Impedir valores negativos o inconsistentes.

#### ❓ Pendientes de decisión

- Si ambas partes deben confirmar
- Si pueden cambiar el tipo después de aceptar y cómo se resuelven diferencias sobre el valor del intercambio.

### HU14 Gestionar una solicitud

Como Docente, quiero aceptar o rechazar una solicitud para confirmar si realizaré la sesión.

- **✅ Aceptación:** La solicitud cambia a aceptada o rechazada y conserva su estado.

#### 🛠️ Refinamiento aplicado

- Mostrar toda la información antes de aceptar o rechazar
- Registrar quién y cuándo realizó la acción
- Impedir aceptar una solicitud incompatible con la disponibilidad actual
- Comunicar el cambio de estado.

#### ❓ Pendientes de decisión

- Motivos obligatorios de rechazo
- Vencimiento automático y posibilidad de volver a abrir una solicitud rechazada.

### HU15 Reservar o cancelar

Como participante, quiero reservar o cancelar una sesión antes de realizarla para mantener actualizada la coordinación del encuentro.

- **✅ Aceptación:** Una solicitud aceptada conserva la fecha acordada y cualquiera de los participantes puede cancelarla antes de realizarse, dejando registrado el estado cancelado.

#### 🛠️ Refinamiento aplicado

- Controlar transiciones válidas de estado
- Impedir cancelar una sesión ya completada
- Pedir confirmación antes de cancelar
- Conservar el historial de cambios.

#### ❓ Pendientes de decisión

- Plazo máximo de cancelación
- Modificación de horario
- Motivo de cancelación
- Penalizaciones y tratamiento de créditos cancelados.

### HU16 Completar una sesión

Como participante, quiero marcar la sesión como completada para registrar el resultado del encuentro.

- **✅ Aceptación:** Una sesión finalizada queda disponible para historial, créditos y calificación.

#### 🛠️ Refinamiento aplicado

- Permitir completar solo una sesión aceptada y pasada
- Registrar fecha y participante que la completó
- Impedir completar dos veces la misma sesión
- Habilitar historial y calificación después de completarla.

#### ❓ Pendientes de decisión

- Si deben confirmar ambas partes
- Cómo se gestionan disputas y cuánto tiempo se permite informar que una sesión no ocurrió.

## Épica E6. Créditos e historial

### Introducción

Esta épica registra el valor interno de los intercambios mediante créditos y conserva la actividad realizada por cada usuario.

Hacer transparente el movimiento de créditos y permitir que cada persona consulte su recorrido dentro de la plataforma.

Los créditos y las actividades quedan registrados de forma consultable para ambas partes.

### Restricciones

Los créditos son internos de la plataforma y no son dinero ni pueden convertirse en dinero, productos o servicios.

### HU17 Transferir créditos

Como plataforma, quiero transferir créditos al Docente cuando una sesión mediante créditos se complete.

- **✅ Aceptación:** El Alumno entrega los créditos, el Docente los recibe y el movimiento queda registrado.

#### 🛠️ Refinamiento aplicado

- Ejecutar la transferencia como una operación consistente
- Impedir saldos negativos
- Registrar origen
- Destino
- Cantidad
- Sesión y fecha
- Evitar transferencias duplicadas.

#### 📌 Reglas vigentes

- Los créditos son internos de la plataforma
- Los créditos no son dinero
- Los créditos no pueden convertirse en dinero, productos ni servicios.

#### ❓ Pendientes de decisión

- Saldo inicial
- Límites
- Reversión por cancelación o disputa y reglas para cuentas suspendidas.

### HU18 Consultar historial

Como usuario, quiero consultar mis sesiones, aprendizajes, intercambios y movimientos para hacer seguimiento de mi actividad.

- **✅ Aceptación:** Se muestran sesiones solicitadas, aceptadas, canceladas y completadas, además de créditos y temas.

#### 🛠️ Refinamiento aplicado

- Separar sesiones
- Aprendizajes
- Intercambios y movimientos
- Mostrar estados y fechas
- Permitir consultar el detalle
- Controlar el acceso para que cada usuario vea solo su información autorizada.

#### ❓ Pendientes de decisión

- Filtros
- Exportación
- Paginación y tiempo de conservación del historial.

## Épica E7. Calificaciones y reputación

### Introducción

Esta épica permite que las personas valoren sus experiencias de aprendizaje una vez finalizada la sesión.

Generar señales de confianza para ayudar a la comunidad a evaluar futuras propuestas y participantes.

Cada perfil puede mostrar una reputación basada en experiencias reales y completadas.

### Restricciones

Solo pueden calificarse participantes de una sesión marcada como completada.

### HU19 Calificar una experiencia

Como participante, quiero calificar a la otra persona después de completar una sesión para aportar información a la comunidad.

- **✅ Aceptación:** Solo se puede calificar una sesión completada, con puntuación de 1 a 5 y comentario opcional.

#### 🛠️ Refinamiento aplicado

- Habilitar la calificación solo después de completar
- Permitir una puntuación de 1 a 5 y comentario opcional
- Evitar calificaciones duplicadas
- Mostrar el promedio y conservar las calificaciones que lo componen.

#### ❓ Pendientes de decisión

- Plazo para calificar
- Posibilidad de editar
- Moderación de comentarios
- Respuesta del calificado y tratamiento de calificaciones abusivas.

## Épica E8. Seguridad y administración

### Introducción

Esta épica protege el carácter educativo, lícito y seguro de la plataforma y brinda herramientas básicas de revisión administrativa.

Prevenir contenidos inadecuados y permitir que las denuncias y sanciones sean revisadas por una persona administradora.

La plataforma puede detectar, recibir, revisar y gestionar contenidos o cuentas que incumplan las reglas del MVP.

### Restricciones

Las sanciones definitivas requieren revisión administrativa y la plataforma no permite ofrecer servicios profesionales.

### HU20 Validar y denunciar contenidos

Como plataforma, quiero validar publicaciones y permitir denuncias para limitar contenidos ilegales, riesgosos o ajenos al aprendizaje.

- **✅ Aceptación:** Se aplican categorías y expresiones prohibidas, se muestran advertencias y se pueden denunciar publicaciones o cuentas.

#### 🛠️ Refinamiento aplicado

- Mostrar reglas antes de publicar
- Validar categorías y expresiones prohibidas
- Ofrecer motivos de denuncia claros
- Confirmar la recepción de la denuncia sin revelar información innecesaria.

#### ❓ Pendientes de decisión

- Lista exacta de categorías y expresiones
- Revisión automática o manual inicial
- Anonimato de la denuncia y límite contra denuncias abusivas.

### HU21 Administrar denuncias y cuentas

Como Administrador, quiero revisar denuncias, ocultar publicaciones y suspender o reactivar cuentas cuando corresponda.

- **✅ Aceptación:** Las sanciones definitivas requieren revisión humana y quedan registradas.

#### 🛠️ Refinamiento aplicado

- Separar permisos administrativos
- Registrar acciones y motivos
- Mostrar el estado de cada denuncia
- Permitir ocultar y restaurar publicaciones
- Conservar un registro de suspensiones y reactivaciones.

- **Regla vigente:** las sanciones definitivas requieren revisión humana y no se aplican de manera automática.

#### ❓ Pendientes de decisión

- Roles administrativos
- Duración de suspensiones
- Notificación al usuario
- Apelaciones y retención del registro de auditoría.

### HU22 Validar conocimientos y estudios

Como Docente, quiero cargar títulos, certificados o referencias para aumentar la confianza en mis propuestas.

- **✅ Aceptación:** La documentación puede revisarse y el perfil muestra un nivel de verificación.

#### ⚠️ Estado de alcance

- Historia candidata pendiente de confirmación para la primera versión
- El MVP permite implementar validación documental, pero no la incluye expresamente entre sus funcionalidades principales.

#### 🛠️ Refinamiento aplicado

- Informar qué documentación puede cargarse
- Mostrar estado de revisión
- Restringir el acceso a documentos
- Diferenciar experiencia
- Formación acreditada y certificación verificada
- Permitir rechazar o solicitar correcciones.

#### 📌 Reglas vigentes

- La validación no habilita servicios profesionales
- La validación no reemplaza una matrícula ni una habilitación legal.

#### ❓ Pendientes de decisión

- Documentos aceptados
- Tamaño y formato
- Conservación y eliminación
- Responsables de revisión
- Niveles de verificación y visibilidad en el perfil.

### Fuentes de refinamiento

- [OWASP Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)
- [OWASP Email Validation and Verification Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Email_Validation_and_Verification_Cheat_Sheet.html)
- [OWASP Input Validation Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html)
- [NIST SP 800-63B](https://pages.nist.gov/800-63-4/sp800-63b.html)
- [W3C WCAG 2.2 — Error Identification](https://www.w3.org/WAI/WCAG22/Understanding/error-identification)

## Pendientes sin decisión aprobada

- Límites, reglas y revisión del cálculo orientativo de créditos mediante LLM.
- Documentos aceptados y procedimiento de validación de estudios.
- Diseño final de las solicitudes de aprendizaje.
- Canal de contacto entre participantes.

## Exclusiones del MVP

- Clases grupales.
- Equipos docentes.
- Intercambios 2×1 u otras equivalencias.
- Sesiones con más de un Docente o más de un Alumno.
