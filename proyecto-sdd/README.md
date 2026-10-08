# Plataforma de intercambio de aprendizajes

Proyecto universitario para diseñar un MVP de una plataforma donde las personas puedan enseñar y aprender mediante intercambios directos, clases grupales y créditos virtuales.

## Documentación principal

- [Especificación del MVP V1](mvp-v1.md)
- [Especificación del MVP V2](mvp-v2.md)
- [Especificación del MVP V3](mvp-v3.md)
- [MVP resumido](mvp-resumido.md)
- [WBS del MVP](wbs.md)
- [USM del MVP](usm.md)
- [Backlog del MVP](backlog.md)
- [SC del MVP](sc.md)
- [SC visual del MVP](sc-visual.png)
- [Metodología de planificación](metodologia.md)
- [Índice de skills](indice-de-skills.md)
- [Alcance futuro](alcance-futuro.md)

La documentación está dividida en dos proyectos de planificación independientes:

- [`proyecto-sdd`](README.md): planificación vigente derivada de MVP V3.
- [`proyecto-wbs`](../proyecto-wbs/README.md): proyecto clásico basado exclusivamente en el WBS original.

## Enlaces externos

- [Cronograma Jira BH95](https://martinporto.atlassian.net/jira/software/projects/BH95/boards/2/timeline)
- [Repositorio GitHub](https://github.com/portomartin/9524)
- [Carpeta de Google Drive](https://drive.google.com/drive/folders/1yT3fRMZmn2E0MRizzJtzh7e1q5G1IJOz)

## Recursos

- Los diagramas vigentes están en `proyecto-sdd/assets/`.
- Los documentos y scripts heredados de la estructura anterior están en `old/` y se conservan como referencia histórica.

## Roles principales

- **USER:** puede ofrecer conocimientos o habilidades y también solicitar o participar en actividades de aprendizaje.

Una misma persona puede enseñar o aprender según la actividad, sin cambiar su rol técnico.

## Flujo de planificación

El flujo de planificación parte actualmente del **MVP V3** y produce WBS, USM, backlog y subtareas técnicas. Estos documentos ya fueron regenerados y mantienen trazabilidad con V3. [derivar-planificacion-mvp](skills/derivar-planificacion-mvp/SKILL.md) coordina la documentación local y su revisión. Al final, aplica [crear-sprints](skills/crear-sprints/SKILL.md) para estimar las HU, simular capacidad del equipo y proponer una distribución por objetivos y dependencias. Al ejecutar esa etapa, el resultado se guarda en `proyecto-sdd/sprints.md`. La sincronización externa se realiza por separado mediante `actualizar-jira`.

## Aplicación Intercambia

Frontend del MVP de **Intercambia**, una plataforma para conectar personas que quieren aprender y enseñar habilidades sin que el dinero sea un requisito. Los intercambios pueden ser recíprocos o utilizar créditos internos de la plataforma.

## Demo

La aplicación está publicada en GitHub Pages:

**[Abrir Intercambia](https://portomartin.github.io/9524/)**

> GitHub Pages puede tardar unos minutos en reflejar el último cambio publicado en `main`.

## API backend

API mínima en Python con FastAPI, publicada en Render:

- [Listado de endpoints: verbos, rutas y tickets de Jira](api-endpoints.md).
- [API e índice automático de endpoints](https://nine524-api-unificado.onrender.com/).
- [Documentación interactiva para probar la API](https://nine524-api-unificado.onrender.com/docs).
- [Contrato OpenAPI en JSON](https://nine524-api-unificado.onrender.com/openapi.json).

El índice se actualiza automáticamente al agregar rutas. De las 44 rutas y verbos
del backlog, `GET /api/v1/public/offers` devuelve propuestas de ejemplo y alimenta
el listado público del frontend. Las otras 43 devuelven `{}` con `200 OK`.
No hay autenticación ni base de datos en el backend.
El plan gratuito puede tardar alrededor de un minuto en responder después de
un período de inactividad.

Para ejecutarla localmente o consultar la configuración de Render, ver
[`proyecto-sdd/backend/README.md`](backend/README.md).

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

El frontend implementa las 20 subtareas frontend definidas para el MVP. Solo el listado de propuestas públicas consulta la API de Render. Los demás servicios, incluido el detalle de propuestas y la edición, utilizan mocks persistidos en `localStorage`.

No contiene credenciales reales. La única operación HTTP es la lectura del listado público de propuestas.

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
cd proyecto-sdd/frontend
npm install
npm run dev
```

Vite mostrará la URL local de desarrollo. En la configuración actual suele ser:

```text
http://localhost:5173/9524/
```

## Build de producción

Desde la carpeta `proyecto-sdd/frontend/`:

```bash
npm run build
npm run preview
```

Los archivos optimizados se generan en `proyecto-sdd/frontend/dist/`. GitHub Pages construye
y publica esta carpeta automáticamente.

## Modos mock

Los servicios usan mocks excepto el listado de propuestas, que consulta Render:

```env
VITE_API_MODE=mock
```

También se pueden representar estados globales alternativos del catálogo público:

```env
VITE_MOCK_SCENARIO=empty
VITE_MOCK_SCENARIO=error
```

El listado utiliza `VITE_API_URL` (por defecto `https://nine524-api-unificado.onrender.com`).
Para probar un backend local, configurar `VITE_API_URL=http://127.0.0.1:8000`
en `proyecto-sdd/frontend/.env.local` y reiniciar Vite. `VITE_MOCK_SCENARIO` solo afecta los mocks.
Las publicaciones creadas localmente no aparecen en el listado remoto de demostración.

## Estructura principal

```text
proyecto-sdd/frontend/src/
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

El progreso funcional está documentado en [`proyecto-sdd/frontend-progress.md`](frontend-progress.md).

La raíz contiene `proyecto-sdd/` (especificación, planificación, frontend Vue y backend FastAPI),
`proyecto-wbs/` (planificación clásica independiente), `.github/` (despliegue de Pages) y `render.yaml` (configuración del backend).
