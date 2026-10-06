# Intercambia — 9524 Frontend

Frontend del MVP de **Intercambia**, una plataforma para conectar personas que quieren aprender y enseñar habilidades sin que el dinero sea un requisito. Los intercambios pueden ser recíprocos o utilizar créditos internos de la plataforma.

## Demo

La aplicación está publicada en GitHub Pages:

**[Abrir Intercambia](https://portomartin.github.io/9524-frontend/)**

> GitHub Pages puede tardar unos minutos en reflejar el último cambio publicado en `main`.

## API backend

API mínima en Python con FastAPI, publicada en Render:

- [API e índice automático de endpoints](https://nine524-api.onrender.com/).
- [Documentación interactiva para probar la API](https://nine524-api.onrender.com/docs).
- [Contrato OpenAPI en JSON](https://nine524-api.onrender.com/openapi.json).

El índice se actualiza automáticamente al agregar rutas. La API utiliza datos
de ejemplo, sin base de datos, y todavía no está conectada al frontend.
El plan gratuito puede tardar alrededor de un minuto en responder después de
un período de inactividad.

Para ejecutarla localmente o consultar la configuración de Render, ver
[`backend/README.md`](backend/README.md).

## Funcionalidades

- Exploración pública de propuestas y aprendizajes buscados.
- Búsqueda, filtros, reputaciones y contenido destacado.
- Registro, inicio de sesión y rutas protegidas.
- Edición de perfil y gestión de publicaciones.
- Compatibilidades explicadas entre intereses y propuestas.
- Agenda privada o pública con franjas concretas, sin recurrencias.
- Solicitud y gestión del ciclo de vida de sesiones.
- Créditos internos, historial y calificaciones.
- Denuncias de contenido o usuarios.
- Panel administrativo con revisión y control de acceso.

## Estado del proyecto

El frontend implementa las 20 subtareas frontend definidas para el MVP. Todavía utiliza datos mock persistidos en `localStorage` mediante una capa de servicios preparada para sustituirse por un adaptador HTTP; la API mínima publicada aún no está integrada.

No contiene credenciales reales ni realiza operaciones contra un backend.

## Credenciales de demostración

### Usuario

```text
Correo: demo@9524.test
Contraseña: demo1234
```

### Administración

```text
Correo: admin@9524.test
Contraseña: admin1234
```

## Stack

- Vue 3 y Composition API.
- Vite 6.
- Vue Router 4.
- PrimeVue 4 con un preset personalizado de Aura.
- PrimeFlex y PrimeIcons.
- API mock intercambiable y persistencia local.

## Ejecutar localmente

Requisitos: Node.js y npm.

```bash
npm install
npm run dev
```

Vite mostrará la URL local de desarrollo. En la configuración actual suele ser:

```text
http://localhost:5173/9524-frontend/
```

## Build de producción

```bash
npm run build
npm run preview
```

Los archivos optimizados se generan en `dist/`.

## Modos mock

La aplicación usa mocks de forma predeterminada:

```env
VITE_API_MODE=mock
```

También se pueden representar estados globales alternativos del catálogo público:

```env
VITE_MOCK_SCENARIO=empty
VITE_MOCK_SCENARIO=error
```

Para conectar una API real deberá incorporarse el adaptador HTTP manteniendo los contratos de los servicios existentes.

## Estructura principal

```text
src/
├── assets/       # Base visual mínima
├── components/   # Componentes compartidos
├── composables/  # Estado y carga reutilizable
├── mocks/        # Datos de demostración
├── router/       # Navegación y guards
├── services/     # Contratos y adaptadores de datos
├── stores/       # Estado persistente del MVP
├── views/        # Pantallas públicas, privadas y administrativas
└── theme.js      # Preset visual de PrimeVue
```

El progreso funcional está documentado en [`docs/frontend-progress.md`](docs/frontend-progress.md).

