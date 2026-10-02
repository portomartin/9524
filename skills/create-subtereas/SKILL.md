---
name: create-subtereas
description: Crear subtareas técnicas de Jira debajo de historias de usuario, separando Backend/API REST y Frontend, con contratos HTTP legibles y convenciones Vue.
---

# Create subtareas

Usar este skill cuando el usuario solicite crear, actualizar o refinar subtareas técnicas para las historias de usuario del proyecto Plataforma de intercambio de aprendizajes.

## Fuentes y alcance

1. Leer `AGENTS.md`, `docs/mvp.md` y `docs/backlog.md` antes de generar subtareas.
2. Mantener la trazabilidad: Épica → Historia de usuario → Subtarea.
3. No incorporar funcionalidades fuera del MVP ni resolver unilateralmente pendientes de decisión.
4. No crear subtareas para historias candidatas o pendientes de confirmación, como HU22, salvo aprobación explícita.
5. Si se actualiza Jira, verificar primero el proyecto, las historias existentes, el tipo de issue `Subtask` y las subtareas ya creadas para evitar duplicados.

## Descomposición estándar

Cada historia aprobada debe tener, como mínimo, dos subtareas:

- **Backend/API REST:** modelo, reglas de negocio, endpoints, autorización, validaciones y pruebas del servicio.
- **Frontend:** pantalla o flujo de usuario, integración con la API, estados visuales, validaciones de presentación y pruebas de interacción.

Usar títulos trazables, por ejemplo:

```text
HU01 [Backend] Implementar registro de usuario
HU01 [Frontend] Crear pantalla de registro
```

Agregar subtareas transversales solo cuando una pieza técnica no pertenezca claramente a una historia específica. No duplicar autenticación, componentes compartidos, manejo común de errores o auditoría en todas las historias.

## Formato obligatorio para Backend

Cada subtarea Backend debe incluir, en este orden:

1. Objetivo breve.
2. Endpoints sugeridos.
3. Parámetros de path y query.
4. Request body sugerido.
5. Response exitosa sugerida.
6. Response de error relevante cuando corresponda.
7. Criterios técnicos y pruebas.

Los endpoints y payloads deben aparecer en bloques de código Markdown para que Jira los muestre de forma legible:

```http
POST /api/v1/recurso
Content-Type: application/json
```

```json
{
  "field": "value"
}
```

Las responses deben ser ejemplos JSON plausibles, con códigos HTTP explícitos. Los cuerpos son propuestas técnicas: no convertir sus campos en reglas de negocio aprobadas si el MVP o el backlog los dejan pendientes.

Usar convenciones consistentes:

- Prefijo sugerido: `/api/v1`.
- Identificadores en path como `{id}`.
- Filtros y paginación como query parameters.
- Datos de creación o actualización en JSON.
- Fechas y horas en un formato acordado, preferentemente ISO 8601.
- Usuario autenticado obtenido de la sesión o token, no de un `userId` enviado por el cliente cuando no sea necesario.
- Errores con forma común, por ejemplo:

```json
{
  "code": "VALIDATION_ERROR",
  "message": "Hay campos inválidos",
  "fields": {}
}
```

Incluir validaciones, autorización, idempotencia y auditoría cuando sean necesarias por la historia. Las transferencias de créditos deben derivar cantidad y participantes de la sesión y evitar duplicados.

## Formato obligatorio para Frontend

Cada subtarea Frontend debe indicar:

```text
Consultar y aplicar el skill `convenciones-frontend`.
```

La implementación debe usar Vue y la librería de componentes adoptada por el proyecto. Las pantallas deben ser claras, consistentes, accesibles y responsive, con estados de carga, vacío, error y éxito cuando correspondan.

No crear estilos propios, CSS innecesario, objetos visuales ad hoc ni una identidad visual paralela. Reutilizar componentes, variantes, tokens y patrones de layout de la librería. Mantener la lógica de negocio en servicios o composables y validar en frontend sin reemplazar las validaciones del backend.

## Creación en Jira

Cuando el usuario autorice actualizar Jira:

1. Resolver el proyecto y las historias existentes.
2. Confirmar que no existan subtareas equivalentes.
3. Crear cada issue como tipo `Subtask` con el campo `parent` apuntando a la historia.
4. Usar labels coherentes, por ejemplo `mvp`, `subtask`, `backend` o `frontend`.
5. Mantener el estado inicial del flujo del proyecto, salvo instrucción expresa.
6. Verificar al finalizar la cantidad creada, los padres y que las descripciones conserven los bloques `http` y `json`.

La creación de subtareas en Jira es una mutación externa: requiere autorización explícita del usuario para ejecutarse.
