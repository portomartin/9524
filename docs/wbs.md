# WBS del MVP

**Proyecto:** Plataforma de intercambio de aprendizajes  
**Versión:** 1.1 — derivada del MVP aprobado

La WBS descompone el producto en entregables y capacidades verificables. Se deriva exclusivamente de `docs/mvp.md`.

## 0. Plataforma de intercambio de aprendizajes

### 1. Cuentas y perfiles

#### 1.1. Acceso a la plataforma

- **1.1.1. Registro de usuario**
- **1.1.2. Inicio de sesión**
- **1.1.3. Cierre de sesión**

#### 1.2. Perfil y participación

- **1.2.1. Información personal y ubicación general**
- **1.2.2. Participación como persona que enseña**
- **1.2.3. Participación como persona que aprende**
- **1.2.4. Conocimientos ofrecidos y buscados**
- **1.2.5. Nivel y objetivos por tema**
- **1.2.6. Disponibilidad y modalidad preferida**
- **1.2.7. Reputación y créditos disponibles**

### 2. Propuestas y solicitudes de aprendizaje

#### 2.1. Propuestas de enseñanza

- **2.1.1. Nombre, categoría y descripción**
- **2.1.2. Nivel requerido y nivel alcanzable**
- **2.1.3. Modalidad y duración estimada**
- **2.1.4. Cantidad de créditos**
- **2.1.5. Configuración de sesión individual**
- **2.1.6. Validación y advertencia antes de publicar**

#### 2.2. Solicitudes de aprendizaje

- **2.2.1. Conocimiento que se desea aprender**
- **2.2.2. Objetivo de aprendizaje libre**
- **2.2.3. Nivel actual**
- **2.2.4. Modalidad y disponibilidad**

### 3. Búsqueda, compatibilidad y recomendaciones

#### 3.1. Búsqueda y filtros

- **3.1.1. Búsqueda por conocimiento o habilidad**
- **3.1.2. Filtros por categoría y nivel**
- **3.1.3. Filtros por modalidad y ubicación**
- **3.1.4. Filtros por disponibilidad**
- **3.1.5. Filtros por tipo de intercambio y créditos**

#### 3.2. Compatibilidad basada en reglas

- **3.2.1. Coincidencia de conocimientos**
- **3.2.2. Compatibilidad de niveles y objetivos**
- **3.2.3. Compatibilidad de modalidad y horarios**
- **3.2.4. Presentación de resultados compatibles**
- **3.2.5. Detección de intercambios recíprocos**

#### 3.3. Recomendaciones mediante IA

- **3.3.1. Interpretación de intereses y objetivos**
- **3.3.2. Recomendación de clases y personas**
- **3.3.3. Priorización por nivel, modalidad y disponibilidad**

### 4. Intercambios y sesiones

#### 4.1. Solicitudes y reservas

- **4.1.1. Solicitud de sesión individual**
- **4.1.2. Datos de la solicitud**
- **4.1.3. Aceptación o rechazo**
- **4.1.4. Propuesta de fecha y horario**
- **4.1.5. Reserva de sesión**
- **4.1.6. Modificación o cancelación**
- **4.1.7. Estados pendiente, aceptada, rechazada, cancelada y completada**

#### 4.2. Intercambio recíproco y créditos

- **4.2.1. Acuerdo de intercambio recíproco**
- **4.2.2. Créditos iniciales**
- **4.2.3. Transferencia de créditos al completar**
- **4.2.4. Uso y consulta de créditos**
- **4.2.5. Registro de movimientos**
- **4.2.6. Estimación orientativa de créditos mediante LLM**

#### 4.3. Finalización e historial

- **4.3.1. Confirmación de sesión completada**
- **4.3.2. Historial de sesiones**
- **4.3.3. Historial de temas enseñados y aprendidos**
- **4.3.4. Historial de intercambios y créditos**

### 5. Reputación, seguridad y administración

#### 5.1. Calificaciones

- **5.1.1. Puntuación de 1 a 5**
- **5.1.2. Comentario opcional**
- **5.1.3. Cálculo y visualización del promedio**

#### 5.2. Contenidos y denuncias

- **5.2.1. Categorías permitidas**
- **5.2.2. Lista de palabras y expresiones prohibidas**
- **5.2.3. Validación de publicaciones**
- **5.2.4. Advertencias antes de publicar**
- **5.2.5. Denuncia de usuarios o publicaciones**

#### 5.3. Panel de administración

- **5.3.1. Consulta de usuarios y publicaciones**
- **5.3.2. Revisión de denuncias**
- **5.3.3. Ocultamiento de publicaciones**
- **5.3.4. Suspensión o reactivación de cuentas**
- **5.3.5. Administración de categorías y expresiones prohibidas**
- **5.3.6. Revisión humana de sanciones definitivas**

#### 5.4. Validación de conocimientos y estudios

- **5.4.1. Carga de títulos, certificados o referencias**
- **5.4.2. Revisión administrativa**
- **5.4.3. Nivel de verificación visible en el perfil**

## Trazabilidad con el MVP

| Entregable WBS | Secciones del MVP |
|---|---|
| 1. Cuentas y perfiles | Conceptos principales; Perfiles de usuario |
| 2. Propuestas y solicitudes | Publicación de propuestas; Descripción general; Perfiles de usuario |
| 3. Búsqueda, compatibilidad y recomendaciones | Sistema de compatibilidad; Búsqueda y filtros; Descripción general |
| 4. Intercambios y sesiones | Intercambios recíprocos y créditos virtuales; Solicitudes y reservas; Disponibilidad horaria; Historial de actividades |
| 5. Reputación, seguridad y administración | Calificaciones y reputación; Contenidos no permitidos y seguridad; Panel de administración |

## Supuestos y pendientes

- El MVP mantiene sesiones individuales 1 a 1.
- Los límites y reglas del cálculo de créditos mediante LLM están pendientes de definición.
- Deben definirse los documentos aceptados para validar conocimientos y estudios.
- La WBS no incorpora documentación académica ni tareas técnicas sin respaldo explícito en el MVP.
- Clases grupales, equipos de enseñanza e intercambios no 1 a 1 quedan fuera del MVP.
