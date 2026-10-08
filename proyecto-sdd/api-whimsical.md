# Definiciones de API extraídas de Whimsical

**Fuente:** carpeta `endpoints` del workspace `gdsi-workspace` en Whimsical.

**Estado:** especificación vigente para los flujos de registro e inicio de sesión. Las rutas incluidas en las secciones de módulos funcionales que todavía no tienen contrato detallado deben considerarse de alto nivel y no endpoints aprobados.

El tablero fuente contiene actualmente las páginas `Registro` e `Inicio de sesión`.

## 1. Entrada de la aplicación

### Cliente

- Frontend web.
- Rol técnico de la plataforma: `USER`. Una misma persona puede enseñar o aprender según la actividad, sin cambiar de rol técnico.
- Comunicación con la API mediante HTTPS y JSON.

### API REST

- Prefijo base: no definido en las páginas actuales de Whimsical.
- Responsabilidades visualizadas:
  - Autenticación.
  - Autorización.
  - Validación.
  - Errores HTTP.
- La API expone rutas hacia los módulos funcionales del producto.

## 2. Módulos y familias de rutas

### Endpoints confirmados: registro

El frontend conserva temporalmente los datos personales durante el primer paso del registro. No se envía una petición al backend al presionar `Siguiente`.

#### `GET /interests`

Devuelve las categorías principales de intereses disponibles para seleccionar.

Respuesta exitosa `200 OK`:

```json
[
  { "id": 1, "name": "Ciencias y Matemáticas" },
  { "id": 2, "name": "Tecnología e Informática" },
  { "id": 3, "name": "Idiomas" }
]
```

#### `GET /interests/{id}/subcategories`

Devuelve las subcategorías asociadas a una categoría de interés.

Respuesta exitosa `200 OK`:

```json
[
  { "id": 20, "name": "Fútbol" },
  { "id": 21, "name": "Natación" },
  { "id": 22, "name": "Yoga" }
]
```

Si la categoría no existe, devuelve `404 Not Found`:

```json
{
  "message": "Categoría no encontrada"
}
```

#### `POST /users`

Registra al usuario con sus datos personales y los intereses seleccionados.

Request:

```json
{
  "firstName": "Ana",
  "lastName": "Gómez",
  "username": "ana123",
  "email": "ana@example.com",
  "password": "********",
  "birthDate": "2000-05-15",
  "interests": [6, 20, 22, 24]
}
```

La especificación usa el array `interests` para enviar los IDs seleccionados de categorías y subcategorías. Esto debe mantenerse consistente en la implementación y validarse en el contrato definitivo.

Respuesta exitosa `201 Created`:

```json
{
  "message": "Usuario registrado correctamente"
}
```

Errores contemplados:

- `400 Bad Request`: datos inválidos.
- `409 Conflict`: el correo o nombre de usuario ya está registrado.

### Endpoints confirmados: inicio de sesión

#### `POST /auth/login`

Autentica al usuario mediante correo electrónico y contraseña.

Request:

```json
{
  "email": "ana@example.com",
  "password": "********"
}
```

Respuesta exitosa `200 OK`:

```json
{
  "isAuthenticated": true,
  "role": "USER"
}
```

Además, el backend envía una cookie de autenticación:

```text
Set-Cookie: access_token=JWT...; HttpOnly; Secure; SameSite=Strict
```

Errores contemplados:

- `400 Bad Request`: datos de inicio de sesión inválidos o incompletos.
- `401 Unauthorized`: correo o contraseña incorrectos.

El valor `USER` es el rol técnico vigente de la plataforma. La participación como persona que enseña o aprende se determina por cada actividad y no constituye un rol de cuenta separado.

### Acceso y perfiles

Familias visualizadas:

```text
/auth/*
/me/profile
/me/preferences
```

Responsabilidad: cuentas, autenticación, perfil y preferencias de participación.

### Propuestas y aprendizaje

Familias visualizadas:

```text
/teaching-offers
/learning-requests
```

Responsabilidad: propuestas de enseñanza y solicitudes de aprendizaje.

### Búsqueda y compatibilidad

Familias visualizadas:

```text
/search
/compatibilities
/recommendations
```

Responsabilidad: búsqueda, filtros, compatibilidad y recomendaciones.

### Solicitudes y sesiones

Familias visualizadas:

```text
/session-requests
/sessions/*
```

Responsabilidad: solicitudes de sesión, reservas, estados y operaciones sobre sesiones.

### Créditos e historial

Familias visualizadas:

```text
/me/history
/me/credit-movements
credit-transfer
```

Responsabilidad: historial de actividad, movimientos de créditos y transferencia asociada a sesiones.

> La ruta `credit-transfer` aparece en Whimsical sin prefijo ni verbo HTTP. Su forma definitiva queda pendiente.

### Calificaciones

Familias visualizadas:

```text
/ratings
/reputation
```

Responsabilidad: calificaciones y reputación.

### Seguridad y administración

Familias visualizadas:

```text
/content-validations
/reports
/admin/*
```

Responsabilidad: validación de contenidos, denuncias y operaciones administrativas protegidas.

## 3. Capa de aplicación y dominio

Todas las familias de rutas se conectan con una capa común de:

```text
Reglas de negocio y casos de uso
```

La vista de Whimsical explicita estas reglas:

- Estados.
- Permisos.
- Compatibilidad.
- Sesiones individuales 1 a 1.
- Créditos internos.

La API no debería contener directamente estas reglas: sus controllers o handlers deberían traducir HTTP y delegar los casos de uso.

## 4. Persistencia

La capa de dominio realiza lectura y escritura sobre una persistencia que contempla:

- Cuenta.
- Perfil.
- Propuesta.
- Solicitud.
- Sesión.
- Historial.
- Denuncia.
- Reputación.

## 5. Integración opcional con LLM

Whimsical incluye un LLM como integración opcional. La relación está descrita como:

1. El dominio realiza una consulta opcional al LLM.
2. El LLM sugiere recomendaciones.
3. El LLM sugiere un valor orientativo de créditos.
4. El dominio recibe la sugerencia, pero el LLM no decide.

La definición visual no especifica endpoint, proveedor, formato de request, formato de response ni política de errores.

## 6. Flujo representado

```text
Frontend web
    ↓ HTTPS / JSON
API REST
    ↓ rutas
Módulos funcionales de la API
    ↓ casos de uso
Reglas de negocio y dominio
    ├── lectura / escritura → Persistencia
    └── consulta opcional ↔ LLM
```

## 7. Elementos que no están definidos en Whimsical

El diagrama no define todavía:

- Métodos HTTP por ruta.
- Parámetros de path o query.
- Cuerpos de request.
- Esquemas de response.
- Códigos de error específicos.
- Mecanismo de autenticación y formato de tokens.
- Permisos concretos por endpoint.
- Paginación, ordenamiento o filtros detallados.
- Idempotencia y consistencia de la transferencia de créditos.
- Transiciones formales de estados.
- Contrato técnico de la integración con LLM.
- Especificación OpenAPI/Swagger.

## 8. Relación con la documentación existente

`proyecto-sdd/subtareas.md` contiene endpoints REST sugeridos con mayor detalle, por ejemplo métodos HTTP, parámetros y algunas acciones específicas. Este documento conserva la definición de alto nivel de Whimsical para compararla con esas propuestas antes de aprobar un contrato único.

