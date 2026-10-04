# WBS del MVP V3

**Fuente de verdad:** [`mvp-v3.md`](mvp-v3.md)

La WBS se deriva exclusivamente del MVP V3 activo.

## 0. Plataforma de intercambio de aprendizajes

### 1. Descubrimiento y acceso público

#### 1.1 Experiencia de `GUEST`

- **1.1.1. Explorar propuestas de enseñanza**
- **1.1.2. Explorar aprendizajes buscados**
- **1.1.3. Consultar reputaciones públicas**
- **1.1.4. Consultar rankings y contenido trending**
- **1.1.5. Consultar agendas públicas**

#### 1.2 Acceso de usuarios

- **1.2.1. Crear cuenta con registro breve**
- **1.2.2. Iniciar sesión**
- **1.2.3. Cerrar sesión**
- **1.2.4. Convertir una acción protegida de `GUEST` en acceso autenticado**

### 2. Participación y contenidos de aprendizaje

#### 2.1 Perfil de `USER`

- **2.1.1. Crear perfil básico**
- **2.1.2. Editar perfil**
- **2.1.3. Informar conocimientos que puede enseñar**
- **2.1.4. Informar aprendizajes que desea buscar**
- **2.1.5. Informar objetivos, niveles y modalidad**

#### 2.2 Propuestas y necesidades

- **2.2.1. Publicar propuesta de aprendizaje individual**
- **2.2.2. Editar propuesta**
- **2.2.3. Registrar necesidad de aprendizaje**
- **2.2.4. Aplicar validaciones básicas de contenido**

### 3. Búsqueda y compatibilidad

#### 3.1 Exploración

- **3.1.1. Buscar propuestas y aprendizajes buscados**
- **3.1.2. Filtrar por tema, categoría, nivel y modalidad**
- **3.1.3. Filtrar por disponibilidad y créditos**

#### 3.2 Compatibilidad

- **3.2.1. Comparar conocimientos ofrecidos y aprendizajes buscados**
- **3.2.2. Comparar niveles, objetivos y modalidad**
- **3.2.3. Comparar agendas públicas y franjas libres**
- **3.2.4. Detectar intercambios recíprocos**

### 4. Agenda y sesiones individuales

#### 4.1 Agenda de disponibilidad

- **4.1.1. Crear disponibilidad concreta por fecha y hora**
- **4.1.2. Editar y eliminar disponibilidades**
- **4.1.3. Activar o desactivar visibilidad pública**
- **4.1.4. Cargar múltiples franjas sin recurrencias persistidas**
- **4.1.5. Ocultar franjas comprometidas por acuerdos**

#### 4.2 Intercambio

- **4.2.1. Crear una sesión en estado solicitada desde una propuesta**
- **4.2.2. Elegir intercambio recíproco o mediante créditos**
- **4.2.3. Gestionar el estado de la sesión**
- **4.2.4. Confirmar la sesión y pasarla a en curso**
- **4.2.5. Cancelar la sesión antes de finalizarla**
- **4.2.6. Finalizar la sesión**

### 5. Créditos, historial y confianza

#### 5.1 Créditos internos

- **5.1.1. Asignar créditos a una propuesta**
- **5.1.2. Transferir créditos al completar una sesión**
- **5.1.3. Registrar movimientos de créditos**
- **5.1.4. Evitar saldos negativos y transferencias duplicadas**

#### 5.2 Historial y reputación

- **5.2.1. Consultar historial propio**
- **5.2.2. Calificar a otro participante**
- **5.2.3. Calcular reputación promedio**
- **5.2.4. Mostrar reputación pública**

### 6. Seguridad y administración

#### 6.1 Protección del contenido

- **6.1.1. Mostrar reglas y advertencias**
- **6.1.2. Recibir denuncias**
- **6.1.3. Revisar contenido denunciado**

#### 6.2 Administración

- **6.2.1. Consultar usuarios, propuestas y denuncias**
- **6.2.2. Ocultar propuestas**
- **6.2.3. Suspender o reactivar cuentas**

## Trazabilidad

| Bloque WBS | Secciones del MVP V3 |
|---|---|
| 1 | Roles de acceso; Principios; Descubrir y comprender |
| 2 | Crear una participación mínima; Publicar y encontrar compatibilidades |
| 3 | Publicar y encontrar compatibilidades |
| 4 | Agenda pública; Acordar y coordinar |
| 5 | Créditos internos; Calificación y confianza |
| 6 | Soporte necesario; Seguridad y límites |

## Exclusiones verificadas

Quedan fuera de esta WBS las recurrencias de agenda, las clases grupales, los equipos de enseñanza, las recomendaciones avanzadas mediante IA, la validación documental, el chat completo, las videollamadas integradas y las integraciones de calendario.

## Pendientes

- Definir los campos mínimos del registro breve.
- Definir qué información exacta de las propuestas es pública para `GUEST`.
- Definir la granularidad de duración de las sesiones.
- Definir reglas de saldo inicial y valor de los créditos.
- Definir filtros mínimos para la primera implementación.
