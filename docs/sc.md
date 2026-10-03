# SC (Scope Canvas) del MVP

## Usuarios

### Necesidades

- **USER:** enseñar conocimientos o habilidades y encontrar personas compatibles para aprender.
- **USER:** describir objetivos de aprendizaje, nivel, modalidad y disponibilidad según cada actividad.
- Encontrar intercambios recíprocos o alternativas mediante créditos virtuales.
- Coordinar sesiones individuales 1 a 1 y consultar el historial de actividad.
- Contar con señales de confianza mediante calificaciones, reputación y validación opcional de estudios.

**Trazabilidad:** `docs/mvp.md`, secciones “Descripción general”, “Perfiles de usuario”, “Sistema de compatibilidad”, “Solicitudes y reservas” y “Calificaciones y reputación”.

### Motivadores

- Aprender lo que se necesita.
- Enseñar lo que se sabe.
- Conseguir intercambios recíprocos.
- Usar créditos internos para aprender cuando no existe reciprocidad directa.
- Encontrar personas compatibles por temas, niveles, objetivos, horarios y modalidad.
- Participar en una comunidad educativa confiable.

Los créditos son internos de la plataforma: no son dinero ni pueden convertirse en dinero, productos o servicios.

**Trazabilidad:** `docs/mvp.md`, secciones “Descripción general”, “Intercambios recíprocos y créditos virtuales” y “Objetivo del MVP”.

## Negocio

### Propósito

Facilitar el intercambio de aprendizajes entre personas, permitiendo enseñar lo que se sabe y aprender lo que se necesita sin utilizar dinero.

**Trazabilidad:** `docs/mvp.md`, secciones “Descripción general” y “Objetivo del MVP”.

### Impacto

- Permitir que una comunidad organice intercambios de conocimiento entre sus integrantes.
- Facilitar el aprendizaje mediante intercambios directos o créditos virtuales.
- Aumentar la confianza en las propuestas educativas mediante reputación, denuncias y validaciones.

Los dos primeros puntos se desprenden del objetivo del MVP. El impacto de largo plazo y sus metas concretas quedan como propuesta pendiente de aprobación.

### Objetivos

- Validar una plataforma funcional de intercambio de aprendizajes.
- Permitir el registro, inicio de sesión y configuración de perfiles.
- Publicar conocimientos o habilidades para enseñar y registrar aprendizajes buscados.
- Encontrar propuestas y personas compatibles mediante búsqueda, filtros y reglas.
- Detectar intercambios recíprocos.
- Configurar disponibilidad horaria y modalidad.
- Solicitar, aceptar, rechazar, cancelar y completar sesiones.
- Transferir créditos cuando corresponda.
- Consultar historial, calificar participantes y calcular reputación.
- Denunciar usuarios o publicaciones y administrar el contenido denunciado.

**Trazabilidad:** `docs/mvp.md`, secciones “Funcionalidades principales del MVP”, “Contenidos no permitidos y seguridad”, “Panel de administración” y “Objetivo del MVP”.

## Comportamiento y medición

### Acciones

Se espera que los usuarios:

1. Se registren e inicien sesión.
2. Configuren su perfil como USER e indiquen qué pueden enseñar y qué desean aprender.
3. Indiquen qué pueden enseñar y qué desean aprender.
4. Definan nivel, objetivos, modalidad y disponibilidad.
5. Publiquen propuestas de enseñanza.
6. Busquen propuestas, solicitudes y personas compatibles.
7. Apliquen filtros.
8. Soliciten sesiones.
9. Acepten, rechacen o cancelen solicitudes.
10. Acuerden un intercambio recíproco o mediante créditos.
11. Realicen y confirmen sesiones completadas.
12. Transfieran créditos cuando corresponda.
13. Consulten el historial.
14. Se califiquen mutuamente después de una sesión completada.
15. Denuncien usuarios o publicaciones cuando sea necesario.

Los administradores revisan denuncias, gestionan publicaciones y cuentas, y administran categorías y expresiones prohibidas.

**Trazabilidad:** `docs/mvp.md`, secciones “Funcionalidades principales del MVP”, “Solicitudes y reservas”, “Historial de actividades”, “Contenidos no permitidos y seguridad” y “Panel de administración”.

### Métricas

El MVP no define metas numéricas. Se proponen los siguientes indicadores para validar sus objetivos:

- Usuarios registrados y perfiles completos.
- Propuestas publicadas.
- Solicitudes de sesión creadas y aceptadas.
- Coincidencias compatibles detectadas.
- Intercambios recíprocos acordados.
- Sesiones completadas.
- Transferencias de créditos realizadas.
- Calificaciones emitidas y calificación promedio.
- Denuncias recibidas y resueltas.
- Cuentas suspendidas o reactivadas.

Estas métricas son propuestas pendientes de aprobación; el MVP no define valores objetivo ni períodos de medición.

## Trazabilidad resumida

| Bloque del SC | Base en el MVP |
|---|---|
| Necesidades | Descripción general, perfiles y compatibilidad |
| Motivadores | Intercambios recíprocos, créditos y objetivo del MVP |
| Propósito | Descripción general y objetivo del MVP |
| Impacto | Objetivo del MVP y confianza en la plataforma |
| Objetivos | Funcionalidades principales del MVP |
| Acciones | Funcionalidades, solicitudes, historial y administración |
| Métricas | Propuestas derivadas de los objetivos; sin metas aprobadas |

## Pendientes de aprobación

- Definir metas cuantitativas y prioridades de las métricas.
- Definir el impacto de largo plazo esperado.
- Definir límites y reglas del cálculo orientativo de créditos mediante LLM.
- Definir documentos aceptados y procedimiento de validación.
- Confirmar el diseño final de las solicitudes de aprendizaje.
- Definir el canal de contacto sin convertirlo en una aplicación de chat completa.

## Coherencia del alcance

```text
Necesidades de aprendizaje e intercambio
        ↓
Publicar, buscar y encontrar compatibilidades
        ↓
Solicitar y coordinar sesiones
        ↓
Completar sesiones e intercambiar créditos
        ↓
Consultar historial y calificar
        ↓
Medir adopción, sesiones y resultados
```

El SC se mantiene dentro del MVP: aprendizaje entre personas, intercambios directos o mediante créditos internos y sesiones individuales 1 a 1. No incorpora storytelling, clases grupales ni sesiones con más de dos usuarios.
