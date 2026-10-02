---
name: convenciones-backend
description: Definir y validar convenciones de Backend para el MVP usando una API REST segura, consistente y testeable.
---

# Convenciones y validación de Backend

Aplicar este skill en todas las subtareas de Backend/API REST del proyecto Plataforma de intercambio de aprendizajes. También usarlo como checklist para revisar endpoints, servicios y reglas de negocio existentes.

## API REST

- Usar el prefijo `/api/v1`.
- Nombrar recursos con sustantivos y rutas consistentes.
- Usar métodos HTTP según la intención: `GET` consulta, `POST` creación o acción, `PUT` reemplazo e `PATCH` actualización parcial.
- Enviar identificadores en path parameters como `{id}`.
- Enviar filtros, búsqueda y paginación como query parameters.
- Enviar datos de creación o actualización en JSON.
- Documentar endpoint, autenticación, parámetros, request body, response exitosa y errores.
- Usar fechas y horas en un formato único, preferentemente ISO 8601.

## Capas y responsabilidades

- Mantener los controllers delgados: traducen HTTP y delegan la operación.
- Mantener las reglas de negocio en services o casos de uso.
- Mantener el acceso a datos en repositories o una capa equivalente.
- Evitar consultas a la base de datos directamente desde controllers.
- Evitar duplicar reglas de negocio entre endpoints.
- Separar DTOs de entrada y salida de los modelos internos cuando sea necesario.

## Validación y errores

- Validar body, path y query parameters antes de ejecutar la lógica de negocio.
- No confiar en validaciones del frontend.
- Devolver códigos HTTP coherentes: `400`, `401`, `403`, `404`, `409`, `422` y `500` según corresponda.
- Usar un formato de error común:

```json
{
  "code": "VALIDATION_ERROR",
  "message": "Hay campos inválidos",
  "fields": {}
}
```

- No exponer contraseñas, tokens, información interna, stack traces ni datos sensibles.
- Diferenciar errores de validación, autorización, conflicto de estado y error inesperado.

## Autenticación y autorización

- Obtener el usuario autenticado desde la sesión o token, no desde un `userId` enviado por el cliente cuando no sea necesario.
- Verificar autenticación en todos los endpoints privados.
- Verificar autorización sobre el recurso y la acción, no solo sobre la existencia del usuario.
- Aplicar permisos administrativos únicamente a endpoints de administración.
- No revelar si una cuenta existe al responder credenciales inválidas.
- Almacenar contraseñas únicamente con hash seguro.

## Consistencia e idempotencia

- Usar transacciones para operaciones que modifiquen varios registros.
- Garantizar idempotencia en transferencias de créditos y acciones que puedan repetirse.
- Aceptar `Idempotency-Key` cuando una operación pueda duplicarse por reintentos.
- Derivar cantidad y participantes de créditos desde la sesión persistida; no confiar en valores sensibles enviados por el cliente.
- Controlar transiciones válidas de estados.
- Evitar completar, calificar o transferir dos veces la misma operación.

## Paginación y filtros

- Usar parámetros coherentes como `page` y `pageSize`.
- Devolver metadatos de paginación junto con los elementos:

```json
{
  "items": [],
  "pagination": {
    "page": 1,
    "pageSize": 20,
    "totalItems": 0,
    "totalPages": 0
  }
}
```

- Validar límites de `pageSize`.
- Mantener los filtros aplicados en la response cuando ayude a la interfaz.
- Definir un orden estable para resultados paginados.

## Seguridad, auditoría y datos

- Validar y normalizar entradas antes de persistirlas.
- Aplicar las categorías permitidas y expresiones prohibidas según las reglas vigentes.
- Registrar acciones administrativas con actor, fecha, motivo y recurso afectado.
- No convertir créditos internos en dinero, productos o servicios.
- Proteger el acceso a información personal, historial, documentos y denuncias.
- No aplicar sanciones definitivas automáticamente cuando el MVP exige revisión humana.

## Pruebas y documentación

- Cubrir casos exitosos, validaciones, permisos, conflictos, estados inválidos y errores inesperados.
- Crear pruebas unitarias para reglas de negocio.
- Crear pruebas de integración para endpoints y persistencia.
- Probar idempotencia y transacciones en operaciones críticas.
- Mantener actualizado el contrato REST y, cuando corresponda, la documentación OpenAPI/Swagger.

## Modo de validación

Cuando el usuario solicite validar una implementación Backend, revisar explícitamente:

- [ ] La ruta y el método HTTP son coherentes.
- [ ] Los parámetros de path, query y body están documentados y validados.
- [ ] La response exitosa y los errores tienen formato consistente.
- [ ] El controller delega la lógica y no contiene reglas de negocio complejas.
- [ ] La autenticación y autorización están aplicadas correctamente.
- [ ] No se exponen datos sensibles.
- [ ] Las transacciones e idempotencia están cubiertas cuando corresponden.
- [ ] Las transiciones de estado son válidas y no permiten duplicados.
- [ ] La paginación, filtros y ordenamiento son consistentes.
- [ ] Existen pruebas para éxito, validación, permisos y errores.
- [ ] La implementación respeta `docs/mvp.md` y no incorpora alcance no aprobado.

El resultado de la validación debe separar hallazgos bloqueantes, observaciones y aspectos conformes. Si algo no puede verificarse con la evidencia disponible, indicarlo como “no verificable” en lugar de asumir que se cumple.
