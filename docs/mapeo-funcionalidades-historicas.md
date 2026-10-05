# Mapeo de funcionalidades históricas

**Estado:** documento auxiliar de análisis.

**No es fuente de verdad:** no modifica el MVP V3, el backlog, la WBS ni Jira. Sirve para conservar la trazabilidad de funcionalidades encontradas en documentación histórica y decidir posteriormente si requieren criterios, endpoints o nuevas subtareas.

**Decisión vigente:** este mapeo se aplica como reconciliación obligatoria al final de `derivar-planificacion-mvp` mientras dure la migración del trabajo inicial. No participa en la derivación del backlog y dejará de aplicarse cuando el equipo confirme que la migración terminó.

## Criterio de mapeo

La relación puede ser uno a uno, uno a varios o varios a uno:

```text
funcionalidad histórica → tarea Backend actual → decisión futura
```

No se crea automáticamente una subtarea por cada campo. Una separación futura debería justificarse por una responsabilidad independiente, endpoint, recurso, regla de negocio o validación relevante.

## Tabla de equivalencias Backend

| Funcionalidad histórica | Tarea Backend actual | Relación / observación |
|---|---|---|
| 1.3.1 Módulo de registro | `[1.3.1] [Backend]` Implementar registro breve | Directa |
| 1.3.2 Módulo de inicio y cierre de sesión | `[1.4.1] [Backend]` Implementar autenticación | Directa |
| 1.3.3 Recuperación de contraseña | Sin tarea Backend específica | Pendiente de decisión dentro de autenticación |
| 1.3.4 Perfil de usuario | `[2.1.1] [Backend]` Gestionar perfil de usuario | Directa |
| 1.3.5 Registro de conocimientos que puede enseñar | `[2.1.1] [Backend]` Gestionar perfil de usuario; `[2.2.1] [Backend]` Gestionar propuestas | Una funcionalidad histórica se divide en perfil y publicación |
| 1.3.6 Registro de conocimientos que desea aprender | `[2.1.1] [Backend]` Gestionar perfil de usuario; `[2.3.1] [Backend]` Gestionar aprendizajes buscados | Una funcionalidad histórica se divide en perfil y necesidad concreta |
| 1.3.7 Configuración de nivel | `[2.2.1] [Backend]` Gestionar propuestas; `[2.3.1] [Backend]` Gestionar aprendizajes buscados | Campo usado en más de un contexto |
| 1.3.8 Configuración de modalidad | `[2.2.1] [Backend]` Gestionar propuestas; `[2.3.1] [Backend]` Gestionar aprendizajes buscados | Campo usado en más de un contexto |
| 1.3.9 Configuración de disponibilidad horaria | `[4.1.1] [Backend]` Gestionar disponibilidad; `[4.2.1] [Backend]` Publicar disponibilidad | Gestión privada y visibilidad pública separadas |
| 1.3.10 Visualización del saldo de créditos | `[5.1.1] [Backend]` Transferir créditos; `[5.2.1] [Backend]` Consultar historial | Saldo y movimientos tienen responsabilidades distintas |
| 1.4.1 Formulario de publicación | `[2.2.1] [Backend]` Gestionar propuestas | El formulario consume el contrato de propuestas |
| 1.4.2 Catálogo de categorías | `[2.2.1] [Backend]` Gestionar propuestas | Verificar posteriormente si requiere recurso independiente |
| 1.4.3 Descripción del aprendizaje ofrecido | `[2.2.1] [Backend]` Gestionar propuestas | Campo de la propuesta |
| 1.4.4 Selección del nivel | `[2.2.1] [Backend]` Gestionar propuestas | Campo de la propuesta |
| 1.4.5 Selección de modalidad | `[2.2.1] [Backend]` Gestionar propuestas | Campo de la propuesta |
| 1.4.6 Duración estimada | `[2.2.1] [Backend]` Gestionar propuestas | Campo con validación de duración |
| 1.4.7 Valor en créditos | `[2.2.1] [Backend]` Gestionar propuestas | Campo con reglas de créditos |
| 1.4.8 Gestión de publicaciones | `[2.2.1] [Backend]` Gestionar propuestas | Alta, edición, borrador, publicación y pausa |
| 1.4.9 Validación de contenido | `[2.2.1] [Backend]` Gestionar propuestas | Verificar posteriormente si requiere módulo de moderación separado |

## Decisiones pendientes

- Definir si recuperación de contraseña pertenece al alcance del MVP V3.
- Definir si el catálogo de categorías requiere endpoints y subtarea propia.
- Definir si la validación de contenido es una regla de propuestas o una capacidad transversal de moderación.
- Definir si el saldo de créditos necesita una consulta Backend específica además de transferencia e historial.
