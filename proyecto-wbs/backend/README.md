# Backend Mock — Proyecto WBS Clásico

Backend ultra-rápido basado en **FastAPI** para soportar el frontend independiente desarrollado a partir de los tickets Jira del proyecto **WBSO** (`1.3` a `1.12`).

## Despliegue Público en Producción (Render)

- **URL Base:** `https://nine524.onrender.com`
- **Swagger UI:** [https://nine524.onrender.com/docs](https://nine524.onrender.com/docs)
- **OpenAPI JSON:** [https://nine524.onrender.com/openapi.json](https://nine524.onrender.com/openapi.json)
- **Healthcheck:** [https://nine524.onrender.com/health](https://nine524.onrender.com/health)

## Características

- **Respuestas 200 OK a todo:** Todos los endpoints responden con JSON representativo y status 200.
- **Tolerancia a esquemas:** Si el frontend envía propiedades extra o variaciones en el payload, las acepta sin error `422`.
- **CORS total:** Permite peticiones desde cualquier origen (`*`).
- **Ruta comodín:** Cualquier petición a `/api/...` no mapeada explícitamente es capturada y devuelta con 200 OK dummy.

## Cómo ejecutarlo

### 1. Requisitos previos
Tener Python 3.10+ instalado.

### 2. Instalar dependencias
```bash
cd c:\dev\95.24\proyecto-wbs\backend
pip install -r requirements.txt
```

*(Si ya estás usando el entorno virtual del repositorio: `..\..\proyecto-sdd\backend\.venv\Scripts\activate` y luego simplemente ejecutar).*

### 3. Iniciar el servidor
```bash
uvicorn main:app --reload --port 8000
```

### 4. Accesos directos
- **Swagger UI interactivo:** [http://localhost:8000/docs](http://localhost:8000/docs)
- **OpenAPI JSON:** [http://localhost:8000/openapi.json](http://localhost:8000/openapi.json)
- **Healthcheck:** [http://localhost:8000/health](http://localhost:8000/health)
