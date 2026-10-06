# 9524 API

API mínima con FastAPI, sin base de datos ni autenticación.

## Ejecutar localmente (PowerShell)

Desde la raíz del repositorio:

```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m uvicorn main:app --reload
```

La API queda en http://127.0.0.1:8000 y la documentación interactiva en
http://127.0.0.1:8000/docs.

Endpoints GET:

- `/`: nombre, versión, enlaces a documentación y OpenAPI, y lista automática de endpoints (`method`, `path`). Las nuevas rutas se agregan al listado automáticamente.
- `/health`: devuelve `{"status":"ok"}`.
- `/api/hello`: devuelve un mensaje de ejemplo.
- `/api/v1/public/offers`: lista pública de propuestas de enseñanza (datos de ejemplo).

Este último endpoint inicia la subtarea `[1.1.1]` del backlog MVP V3 de 95.24.
Devuelve `200 OK` con un array de propuestas, sin autenticación ni datos privados.
Es una demo sin persistencia; la subtarea completa sigue pendiente de integrar
el almacenamiento y las reglas de publicación. Se puede probar desde `/docs`.

## Desplegar en Render

Subir estos archivos a GitHub y crear un **Blueprint** en Render seleccionando
este repositorio. El archivo `render.yaml` configura el servicio gratis.
Cuando Render pida `CORS_ORIGINS`, indicar el origen del frontend, por ejemplo
`https://tu-usuario.github.io` (sin ruta ni barra final).

También se puede crear un **Web Service** manualmente con:

- Language: Python 3.
- Root Directory: `backend`.
- Build Command: `pip install -r requirements.txt`.
- Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`.
- Health Check Path: `/health`.
- Instance Type: Free.
- Variable `CORS_ORIGINS`: origen del frontend.

Para permitir varios frontends, separar sus orígenes con comas. En local,
los valores predeterminados permiten Vite en `localhost:5173` y `127.0.0.1:5173`.
Esta variable configura CORS; no restringe el acceso directo ni autentica usuarios.

La URL pública asignada por Render será del tipo
`https://9524-api-xxxx.onrender.com`. Probar `/health`, `/api/hello` y `/docs`.
El frontend todavía no consume esta API.

El servicio gratis se suspende después de 15 minutos sin tráfico y tarda
aproximadamente un minuto en reactivarse. No usar archivos locales para
persistir datos en ese plan.

Guía oficial: https://render.com/docs/deploy-fastapi
