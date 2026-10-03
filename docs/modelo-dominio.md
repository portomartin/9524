# Modelo de dominio

Este documento define los conceptos principales del producto y sus relaciones. Se deriva de `docs/mvp.md`; los detalles no resueltos por el MVP se mantienen como propuestas pendientes de aprobación.

## Cuenta

Identidad de una persona registrada en la plataforma.

- **Atributos:** correo, credencial y estado de acceso.
- **Relaciones:** tiene un Perfil, posee el rol técnico `USER` y posee un saldo de Créditos.
- **Reglas:** la capacidad de enseñar o aprender se determina por la actividad, no por roles de cuenta separados.

## Correo

Dirección utilizada para identificar y confirmar una Cuenta.

- **Relaciones:** pertenece a una Cuenta.
- **Pendiente:** política de confirmación y cambio de dirección.

## Credencial

Dato protegido utilizado para autenticar una Cuenta.

- **Relaciones:** pertenece a una Cuenta.
- **Reglas:** nunca se almacena en texto plano.

## Sesión de autenticación

Acceso temporal de una Cuenta autenticada a la plataforma.

- **Relaciones:** pertenece a una Cuenta y se valida mediante su Credencial.
- **Estados derivados:** activa o cerrada.
- **Pendiente:** duración, renovación y cierre simultáneo de todas las sesiones.

## Perfil

Información de una persona que la comunidad puede consultar según las reglas de visibilidad.

- **Atributos:** nombre, descripción personal, ubicación general, conocimientos, aprendizajes, niveles, objetivos, disponibilidad y modalidad.
- **Relaciones:** pertenece a una Cuenta y participa en Propuestas, Solicitudes, Sesiones y Calificaciones.
- **Pendiente:** campos obligatorios y visibilidad de cada dato.

## Tema

Conocimiento o habilidad que puede enseñarse o aprenderse.

- **Atributos:** nombre, categoría y nivel.
- **Relaciones:** aparece en Perfiles, Propuestas, Necesidades de aprendizaje y Compatibilidades.
- **Reglas:** los niveles del MVP son principiante, intermedio y avanzado.

## Categoría

Clasificación definida por la plataforma para organizar Temas y Propuestas.

- **Relaciones:** agrupa Temas y facilita la Búsqueda.
- **Pendiente:** catálogo inicial y reglas de administración.

## Disponibilidad

Franjas horarias en las que una persona puede participar.

- **Atributos derivados del MVP:** días y horarios.
- **Relaciones:** pertenece a un Perfil y se compara en una Compatibilidad.
- **Pendiente:** formato exacto, zona horaria y reglas de actualización.

## Propuesta

Oferta publicada por un USER sobre aquello que desea enseñar.

- **Atributos:** Tema, Categoría, descripción, nivel requerido, nivel alcanzable, modalidad, duración, créditos y tipo de clase.
- **Relaciones:** pertenece a un Perfil y puede recibir Solicitudes.
- **Estados derivados del MVP:** publicada u oculta.
- **Propuesta pendiente de aprobación:** estado borrador.

## Necesidad de aprendizaje

Declaración de aquello que un USER desea aprender.

- **Atributos:** Tema, nivel, objetivo, modalidad y Disponibilidad.
- **Relaciones:** pertenece a un Perfil y participa en una Compatibilidad.
- **Pendiente:** límite de necesidades activas y vencimiento.

## Búsqueda

Consulta realizada sobre Propuestas o Necesidades de aprendizaje.

- **Atributos derivados del MVP:** texto y filtros.
- **Relaciones:** produce Resultados.
- **Pendiente:** orden y paginación.

## Resultado

Propuesta o Necesidad de aprendizaje devuelta por una Búsqueda.

- **Relaciones:** puede mostrar un Perfil y explicar una Compatibilidad.

## Filtro

Condición aplicada a una Búsqueda para reducir sus Resultados.

- **Tipos:** Tema, nivel, modalidad, Disponibilidad y rango de Créditos.
- **Pendiente:** valores exactos y persistencia entre sesiones.

## Compatibilidad

Coincidencia entre lo que una persona puede enseñar y lo que otra desea aprender.

- **Criterios:** Tema, nivel, modalidad y Disponibilidad.
- **Relaciones:** vincula Perfiles, Propuestas y Necesidades de aprendizaje.
- **Pendiente:** ponderaciones, umbral y tratamiento de datos faltantes.

## Recomendación

Compatibilidad presentada al usuario como una opción especialmente relevante.

- **Relaciones:** se basa en Preferencias, Compatibilidades y actividad del usuario.
- **Pendiente:** cantidad, frecuencia, descarte y métricas de calidad.

## Solicitud

Pedido realizado por un USER a otro USER para coordinar una Sesión.

- **Atributos:** participantes, Propuesta, horario, modalidad, tipo de intercambio y Créditos.
- **Estados:** pendiente, aceptada, rechazada, cancelada y completada.
- **Relaciones:** una Solicitud aceptada puede originar una Sesión.

## Sesión

Encuentro de aprendizaje entre dos USER.

- **Atributos:** participantes, Tema, fecha, horario, modalidad, duración, tipo de intercambio y Créditos.
- **Estados derivados del MVP:** reservada, completada y cancelada.
- **Relaciones:** surge de una Solicitud aceptada y puede generar una Transferencia y Calificaciones.
- **Propuesta pendiente de aprobación:** estado disputada.
- **Pendiente:** confirmación de participantes y tratamiento de desacuerdos.

## Acuerdo de intercambio

Condiciones aceptadas por las partes para realizar una Sesión.

- **Atributos:** tipo recíproco o mediante Créditos, valor y confirmaciones.
- **Relaciones:** pertenece a una Solicitud y determina las condiciones de una Sesión.

## Reserva

Horario confirmado para realizar una Sesión.

- **Atributos:** fecha, horario, participantes y estado.
- **Relaciones:** pertenece a una Sesión y puede cancelarse antes de su realización.

## Crédito

Unidad interna de la plataforma para facilitar intercambios indirectos.

- **Reglas:** no es dinero y no puede convertirse en dinero, productos o servicios.
- **Relaciones:** se registra en Transferencias y pertenece al saldo de una Cuenta.

## Transferencia

Movimiento de Créditos entre participantes asociado a una Sesión completada.

- **Atributos:** origen, destino, cantidad, fecha, motivo y referencia de Sesión.
- **Regla derivada del MVP:** se realiza al completar una Sesión mediante Créditos y queda registrada para ambas personas.
- **Propuesta técnica pendiente de aprobación:** ejecutar la operación de forma atómica e idempotente e impedir saldos negativos.

## Historial

Conjunto de actividades registradas de una Cuenta.

- **Incluye:** Sesiones, Transferencias y Calificaciones.
- **Pendiente:** filtros, conservación y exportación.

## Calificación

Valoración de una experiencia completada.

- **Atributos:** puntuación de 1 a 5, comentario opcional, autor, destinatario y Sesión.
- **Reglas:** solo pueden calificarse participantes de una Sesión completada.
- **Pendiente:** edición, moderación y tratamiento de abuso.

## Denuncia

Reporte de contenido o conducta inapropiada.

- **Atributos:** autor, objeto denunciado, categoría, descripción, fecha y estado.
- **Estados:** recibida, en revisión, resuelta o descartada.

## Caso de moderación

Registro de la revisión y decisión asociada a una Denuncia.

- **Atributos:** responsable, acción, motivo, fecha y resultado.
- **Relaciones:** puede afectar una Cuenta o contenido publicado.
- **Pendiente:** roles administrativos, suspensiones y apelaciones.

## Documento de respaldo

Archivo presentado para validar conocimientos o estudios.

- **Estado de alcance:** concepto candidato; su incorporación a la primera versión requiere confirmación.

- **Atributos:** tipo, formato, tamaño, propietario y estado de revisión.
- **Estados:** pendiente, verificado o rechazado.
- **Relaciones:** pertenece a una Solicitud de verificación.
- **Regla:** el documento no se expone públicamente en el Perfil.

## Solicitud de verificación

Pedido para que un Documento de respaldo sea revisado.

- **Estado de alcance:** concepto candidato; su incorporación a la primera versión requiere confirmación.

- **Relaciones:** pertenece a una Cuenta y es atendida por un Revisor.
- **Estados:** pendiente, verificada o rechazada.

## Revisor

Persona autorizada para evaluar Solicitudes de verificación.

- **Estado de alcance:** concepto candidato; su incorporación a la primera versión requiere confirmación.

- **Relaciones:** revisa Documentos de respaldo y registra decisiones.
- **Pendiente:** permisos y responsabilidades exactas.

## Glosario de decisiones pendientes

Las definiciones marcadas como pendientes deben aprobarse antes de transformarse en reglas obligatorias. Si una decisión cambia el alcance o una regla del producto, primero debe actualizarse `docs/mvp.md`.
