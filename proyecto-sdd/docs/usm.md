# User Story Map del MVP V3

**Fuente de verdad:** [`mvp-v3.md`](mvp-v3.md)

## Roles

- **`GUEST`:** descubre información pública en modo lectura.
- **`USER`:** ofrece aprendizajes, busca aprender, coordina sesiones y califica.
- **`ADMIN`:** protege el contenido y gestiona denuncias mediante permisos administrativos.

Un `USER` puede enseñar y aprender según la actividad.

## Backbone y flujo narrativo

`Descubrir → Registrarse cuando sea necesario → Ofrecer o buscar → Encontrar compatibilidad → Consultar disponibilidad → Acordar → Coordinar → Realizar → Calificarse`

## Mapa

### 1. Descubrir

- Explorar propuestas de enseñanza como `GUEST`.
- Explorar aprendizajes buscados.
- Consultar reputaciones, rankings y contenido trending.
- Consultar agendas públicas y horarios libres.

### 2. Acceder cuando sea necesario

- Crear una cuenta breve.
- Iniciar sesión.
- Convertir una intención de acción en una acción autenticada.
- Mantener la exploración pública sin exigir registro anticipado.

### 3. Ofrecer o buscar aprendizajes

- Completar un perfil básico.
- Publicar algo que el `USER` puede enseñar.
- Registrar algo que el `USER` desea aprender.
- Describir objetivos, niveles y modalidad.

### 4. Encontrar compatibilidades

- Buscar propuestas y aprendizajes buscados.
- Aplicar filtros básicos.
- Comparar temas, niveles, objetivos y modalidad.
- Comparar agendas públicas.
- Detectar intercambios recíprocos.

### 5. Consultar y gestionar disponibilidad

- Ver la propia agenda.
- Ver agendas públicas activadas.
- Cargar una disponibilidad concreta por fecha y hora.
- Cargar varias franjas mediante ayudas de interfaz.
- Activar o desactivar la publicación de la agenda.
- Ocultar una franja cuando queda comprometida.

### 6. Acordar y coordinar

- Crear una sesión en estado `SOLICITADA` desde una propuesta.
- Elegir intercambio recíproco o mediante créditos.
- Proponer fecha, hora, duración y modalidad.
- Aceptar o rechazar.
- Cancelar antes de realizar.

### 7. Realizar y registrar

- Gestionar la sesión: `SOLICITADA`, `CONFIRMADA`, `EN_CURSO` o `CANCELADA`.
- Marcar la sesión como `FINALIZADA`.
- Transferir créditos si corresponde.
- Registrar la actividad en el historial.
- Calificar al otro participante.
- Consultar reputación actualizada.

### 8. Proteger la comunidad

- Consultar reglas y advertencias.
- Denunciar usuarios o propuestas.
- Revisar denuncias como `ADMIN`.
- Ocultar propuestas o suspender cuentas cuando corresponda.

## Release slice del MVP V3

El release slice incluye descubrimiento público, registro breve, perfiles básicos, propuestas, necesidades de aprendizaje, búsqueda, compatibilidad, agenda explícita por fecha y hora, sesiones individuales entre dos `USER`, intercambios recíprocos o mediante créditos, historial, calificación mutua y seguridad mínima.

## Fuera del release slice

Quedan fuera comunidades, badges, IA avanzada, validación documental, recurrencias de agenda, clases grupales, equipos de enseñanza, sesiones con más de dos participantes, chat completo, videollamadas e integraciones externas de calendario.

## Trazabilidad

| Actividad | MVP V3 |
|---|---|
| Descubrir | Roles de acceso; Descubrir y comprender |
| Acceder cuando sea necesario | Crear una participación mínima |
| Ofrecer o buscar | Crear una participación mínima; Publicar y compatibilidades |
| Encontrar compatibilidades | Publicar y encontrar compatibilidades |
| Gestionar disponibilidad | Agenda pública de disponibilidad |
| Acordar y coordinar | Acordar y coordinar |
| Realizar y registrar | Créditos; Calificación; Soporte necesario |
| Proteger la comunidad | Seguridad y límites |

## Pendientes

- Definir qué acciones exactas disparan el registro.
- Definir el contenido público mínimo de una agenda.
- Definir cómo se presenta una franja tomada sin exponer el acuerdo.
- Definir el orden entre intercambio recíproco y créditos en la interfaz.
