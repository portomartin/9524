# Backlog del MVP V3

**Proyecto:** Plataforma de intercambio de aprendizajes  
**Fuente de verdad:** [`mvp-v3.md`](mvp-v3.md)  
**Estado:** derivado del MVP V3; pendiente de revisión funcional.

Las historias se derivan exclusivamente del MVP V3. No se mezclan requisitos del backlog anterior ni se asignan prioridades o estimaciones no definidas por la especificación.

## Épica E1. Descubrimiento y acceso público

### Introducción

Esta épica permite que una persona entienda el valor de la plataforma y explore oportunidades de aprendizaje antes de registrarse. El acceso `GUEST` es de solo lectura; las acciones protegidas requieren autenticación.

### HU01 Explorar como `GUEST`

Como `GUEST`, quiero explorar propuestas de enseñanza y aprendizajes buscados, para descubrir rápidamente si la plataforma me interesa.

- **✅ Aceptación:** Se puede consultar contenido público sin crear una cuenta.

#### 🛠️ Refinamiento aplicado

- Mostrar qué se puede aprender.
- Mostrar qué conocimientos ofrecen otros usuarios.
- Permitir abrir el detalle público de una propuesta.

#### ❓ Pendientes de decisión

- Campos exactos visibles en el detalle público.
- Reglas de orden inicial del contenido.

### HU02 Consultar confianza pública

Como `GUEST`, quiero ver reputaciones, rankings y contenido trending, para evaluar si existen oportunidades valiosas.

- **✅ Aceptación:** La información pública se puede consultar sin exponer datos privados ni acuerdos.

#### 🛠️ Refinamiento aplicado

- Mostrar reputación promedio cuando exista.
- Separar rankings y trending de los datos privados.
- No mostrar agendas tomadas ni participantes de acuerdos.

#### ❓ Pendientes de decisión

- Definición exacta de ranking.
- Definición exacta de trending.

### HU03 Registrarse cuando sea necesario

Como `GUEST`, quiero registrarme solo cuando intento realizar una acción protegida, para no perder tiempo antes de entender el producto.

- **✅ Aceptación:** Una acción protegida ofrece iniciar sesión o registrarse y conserva el contexto cuando sea posible.

#### 🛠️ Refinamiento aplicado

- Mantener la exploración pública sin registro anticipado.
- Solicitar únicamente los datos necesarios.
- Diferenciar inicio de sesión de creación de cuenta.

#### ❓ Pendientes de decisión

- Campos mínimos del registro.
- Acciones exactas que requieren autenticación.

### HU04 Autenticarse

Como `USER`, quiero iniciar y cerrar sesión, para acceder a mis acciones y proteger mi cuenta.

- **✅ Aceptación:** El usuario puede iniciar sesión, mantener una sesión segura y cerrarla.

#### 🛠️ Refinamiento aplicado

- Mantener el rol técnico `USER`.
- No crear roles separados para enseñar y aprender.
- Proteger rutas y operaciones privadas.

#### ❓ Pendientes de decisión

- Duración y renovación de la sesión.
- Recuperación de contraseña.

## Épica E2. Perfil, propuestas y necesidades

### Introducción

Esta épica permite que un `USER` indique qué puede enseñar y qué desea aprender, y publique propuestas concretas para que otras personas las descubran.

### HU05 Completar el perfil

Como `USER`, quiero completar y editar mi perfil básico, para presentarme ante otras personas.

- **✅ Aceptación:** El perfil permite guardar y editar la información básica sin exigir completar todo el producto.

#### 🛠️ Refinamiento aplicado

- Permitir guardar información parcial.
- Informar conocimientos ofrecidos y aprendizajes buscados.
- Mantener separada la información pública de la privada.

#### ❓ Pendientes de decisión

- Campos obligatorios del perfil.
- Visibilidad de ubicación general.

### HU06 Publicar una propuesta

Como `USER`, quiero publicar algo que sé enseñar, para que otras personas puedan encontrarlo y crear una solicitud de sesión.

- **✅ Aceptación:** La propuesta incluye tema, categoría, descripción, nivel, modalidad, duración y condición de intercambio.

#### 🛠️ Refinamiento aplicado

- Permitir guardar borrador.
- Validar contenido antes de publicar.
- Mantener propuestas individuales.
- Mostrar una vista pública apta para `GUEST`.

#### ❓ Pendientes de decisión

- Campos obligatorios exactos.
- Revisión previa a la publicación.

### HU07 Registrar un aprendizaje buscado

Como `USER`, quiero indicar qué deseo aprender, para encontrar propuestas compatibles.

- **✅ Aceptación:** La necesidad permite describir objetivo, nivel, modalidad y disponibilidad.

#### 🛠️ Refinamiento aplicado

- Permitir objetivos escritos libremente.
- Permitir editar o pausar la necesidad.
- Usar la necesidad en la compatibilidad.

#### ❓ Pendientes de decisión

- Cantidad de necesidades simultáneas.
- Vencimiento de una necesidad inactiva.

## Épica E3. Búsqueda y compatibilidad

### Introducción

Esta épica conecta lo que un `USER` puede enseñar con lo que otro desea aprender, priorizando coincidencias comprensibles y accionables.

### HU08 Buscar aprendizajes

Como visitante o `USER`, quiero buscar propuestas y aprendizajes buscados, para encontrar oportunidades relevantes.

- **✅ Aceptación:** La búsqueda devuelve resultados públicos relacionados con el conocimiento consultado.

#### 🛠️ Refinamiento aplicado

- Permitir búsqueda a `GUEST`.
- Mostrar estado vacío y errores comprensibles.
- Diferenciar propuesta de aprendizaje buscado.

#### ❓ Pendientes de decisión

- Orden por relevancia.
- Búsqueda parcial y sin resultados.

### HU09 Filtrar resultados

Como visitante o `USER`, quiero filtrar resultados, para reducir rápidamente las opciones.

- **✅ Aceptación:** Los filtros se pueden combinar y limpiar.

#### 🛠️ Refinamiento aplicado

- Filtrar por tema, categoría, nivel y modalidad.
- Filtrar por disponibilidad pública.
- Filtrar por créditos cuando corresponda.

#### ❓ Pendientes de decisión

- Filtros mínimos de la primera interfaz.
- Paginación.

### HU10 Encontrar compatibilidades

Como `USER`, quiero conocer qué personas y propuestas son compatibles conmigo, para iniciar un intercambio posible.

- **✅ Aceptación:** La compatibilidad explica la coincidencia entre tema, nivel, objetivo, modalidad y disponibilidad.

#### 🛠️ Refinamiento aplicado

- Comparar conocimientos ofrecidos y aprendizajes buscados.
- Comparar agendas públicas libres.
- Destacar posibles intercambios recíprocos.
- No presentar la compatibilidad como garantía de éxito.

#### ❓ Pendientes de decisión

- Ponderación de criterios.
- Umbral mínimo de compatibilidad.

## Épica E4. Agenda y sesiones

### Introducción

Esta épica permite mostrar disponibilidad concreta, acordar una sesión individual y registrar su cumplimiento. La agenda es única para enseñar y aprender.

### HU11 Gestionar disponibilidad

Como `USER`, quiero cargar disponibilidades concretas, para que otras personas puedan encontrar horarios posibles.

- **✅ Aceptación:** Cada disponibilidad registra día, fecha y hora, y la unidad mínima es una hora.

#### 🛠️ Refinamiento aplicado

- Iniciar la agenda vacía.
- Permitir cargar una hora o muchas fechas.
- Permitir cargar disponibilidades de meses y años futuros.
- Ofrecer ayudas de carga masiva sin persistir recurrencias.

#### ❓ Pendientes de decisión

- Zona horaria.
- Duración de franjas mayores a una hora.

### HU12 Publicar la agenda

Como `USER`, quiero activar o desactivar la visibilidad de mi agenda, para decidir cuándo mostrar mis horarios libres.

- **✅ Aceptación:** Una agenda activada muestra solo franjas libres y una agenda desactivada no se muestra públicamente.

#### 🛠️ Refinamiento aplicado

- Permitir consultar siempre la propia agenda.
- Permitir que `GUEST` consulte agendas públicas.
- No mostrar datos de acuerdos privados.

#### ❓ Pendientes de decisión

- Vista exacta para una agenda vacía.
- Nivel de detalle de la disponibilidad pública.

### HU13 Crear una sesión solicitada

Como `USER`, quiero crear una sesión en estado `SOLICITADA` desde una propuesta, para iniciar el intercambio.

- **✅ Aceptación:** La sesión solicitada identifica participantes, tema, fecha, hora, duración, modalidad y tipo de intercambio, y comienza en estado `SOLICITADA`.

#### 🛠️ Refinamiento aplicado

- Impedir solicitudes sobre franjas tomadas.
- Mostrar resumen antes de confirmar.
- Mantener la sesión individual entre dos `USER`.

#### ❓ Pendientes de decisión

- Conflictos de horario.
- Vencimiento de solicitudes sin respuesta.

### HU14 Gestionar el estado de una sesión

Como `USER`, quiero aceptar, iniciar o cancelar una sesión solicitada, para llevarla al estado que corresponda durante el intercambio.

- **✅ Aceptación:** La sesión registra cambios de estado válidos: `SOLICITADA`, `CONFIRMADA`, `EN_CURSO` o `CANCELADA`.

#### 🛠️ Refinamiento aplicado

- Aceptar una sesión solicitada y pasarla a `CONFIRMADA`.
- Rechazar una sesión solicitada implica cancelarla sin reservar la franja.
- Pasar una sesión confirmada a `EN_CURSO` cuando comience.
- Cancelar antes de realizar la sesión.
- Ocultar la franja reservada de la agenda pública.
- Mostrar detalles del acuerdo solo a los participantes.

#### ❓ Pendientes de decisión

- Motivos de rechazo.
- Política de cancelación.

### HU15 Finalizar una sesión

Como participante, quiero marcar una sesión en curso como `FINALIZADA`, para habilitar créditos, historial y calificaciones.

- **✅ Aceptación:** Una sesión en curso puede pasar a `FINALIZADA` y habilita las acciones posteriores.

#### 🛠️ Refinamiento aplicado

- Impedir completar dos veces.
- Registrar fecha y participantes.
- Mantener el detalle privado para los involucrados.

#### ❓ Pendientes de decisión

- Si se requiere confirmación de una o de ambas personas.
- Tratamiento de desacuerdos.

## Épica E5. Créditos, historial y reputación

### Introducción

Esta épica sostiene los intercambios no recíprocos, conserva la actividad y construye confianza mediante calificaciones mutuas.

### HU16 Intercambiar con créditos

Como `USER`, quiero usar créditos internos cuando no existe reciprocidad directa, para poder aprender de todas formas.

- **✅ Aceptación:** El participante que aprende entrega créditos y quien ofrece el aprendizaje los recibe al completar la sesión.

#### 🛠️ Refinamiento aplicado

- Mantener créditos internos.
- Evitar saldos negativos.
- Evitar transferencias duplicadas.
- Registrar origen, destino, cantidad y sesión.

#### ❓ Pendientes de decisión

- Saldo inicial.
- Valor de cada propuesta.
- Reversión por cancelación o disputa.

### HU17 Consultar historial

Como `USER`, quiero consultar mis sesiones, intercambios, créditos y calificaciones, para conocer mi actividad.

- **✅ Aceptación:** El historial muestra únicamente información propia y estados relevantes.

#### 🛠️ Refinamiento aplicado

- Separar sesiones, aprendizajes, intercambios y movimientos.
- Mostrar fechas y estados.
- Preparar paginación.

#### ❓ Pendientes de decisión

- Conservación del historial.
- Filtros del historial.

### HU18 Calificarse mutuamente

Como participante de una sesión completada, quiero calificar a la otra persona, para construir reputación y confianza.

- **✅ Aceptación:** Ambos participantes pueden emitir una calificación de 1 a 5 y un comentario opcional una sola vez.

#### 🛠️ Refinamiento aplicado

- Habilitar la calificación solo después de completar.
- Mostrar reputación promedio públicamente.
- Permitir consultar la reputación desde el acceso `GUEST`.

#### ❓ Pendientes de decisión

- Edición o eliminación de una calificación.
- Moderación de comentarios.

## Épica E6. Seguridad y administración

### Introducción

Esta épica protege el carácter educativo, lícito y seguro del intercambio sin desplazar el foco de la experiencia principal.

### HU19 Denunciar contenido o usuarios

Como `USER`, quiero denunciar contenido o usuarios, para ayudar a mantener un espacio seguro.

- **✅ Aceptación:** La denuncia queda registrada y puede ser revisada.

#### 🛠️ Refinamiento aplicado

- Mostrar reglas y advertencias antes de publicar.
- Pedir motivo de denuncia.
- No exponer información innecesaria.

#### ❓ Pendientes de decisión

- Catálogo inicial de motivos.
- Denuncias duplicadas.

### HU20 Administrar seguridad

Como `ADMIN`, quiero revisar usuarios, propuestas y denuncias, para proteger la plataforma.

- **✅ Aceptación:** `ADMIN` puede revisar, ocultar propuestas y suspender o reactivar cuentas según permisos.

#### 🛠️ Refinamiento aplicado

- Registrar acción, fecha y motivo.
- Requerir revisión humana para sanciones definitivas.
- Mantener las operaciones administrativas fuera del recorrido de `GUEST` y `USER`.

#### ❓ Pendientes de decisión

- Permisos administrativos exactos.
- Registro de auditoría.

## Exclusiones del MVP V3

Comunidades, badges, IA avanzada, validación documental, recurrencias de agenda, clases grupales, equipos de enseñanza, sesiones con más de dos participantes, chat completo, videollamadas e integraciones externas de calendario.
