"""Genera el listado Markdown desde el manifiesto usado por la API."""

import json
import re
from pathlib import Path
from urllib.parse import quote


API_URL = "https://nine524-api.onrender.com"


def endpoint_url(endpoint: dict) -> str:
    method, path = endpoint["method"], endpoint["path"]
    name = method.lower() + "_" + re.sub(r"\W+", "_", path)
    operation_id = re.sub(r"\W", "_", name + path) + "_" + method.lower()
    return f"{API_URL}/docs#/{quote('Backlog — stubs', safe='')}/{operation_id}"


def markdown_label(text: str) -> str:
    return text.replace("\\", "\\\\").replace("[", "\\[").replace("]", "\\]").replace("|", "\\|")


def render_document(endpoints: list[dict], issue_titles: dict[str, str]) -> str:
    lines = [
        "# Endpoints de la API",
        "",
        "Listado generado desde [`backend/backlog_endpoints.json`](../backend/backlog_endpoints.json).",
        "",
        f"Las {len(endpoints)} combinaciones de verbo y ruta del backlog son **stubs**:",
        "devuelven `{}` con **200 OK**, sin lógica, autenticación ni persistencia.",
        "Esto no implica que las tareas de Jira estén completadas.",
        "",
        "- [API e índice actualizado](https://nine524-api.onrender.com/).",
        "- [Documentación interactiva y parámetros](https://nine524-api.onrender.com/docs).",
        "- [Contrato OpenAPI JSON](https://nine524-api.onrender.com/openapi.json).",
        "",
        "## Rutas del backlog",
        "",
        "| Verbo | Ruta | Tareas de Jira |",
        "| --- | --- | --- |",
    ]
    for endpoint in endpoints:
        tickets = "<br>".join(
            f"[{markdown_label(issue_titles[key])}](https://martinporto.atlassian.net/browse/{key})"
            for key in endpoint["issues"]
        )
        lines.append(
            f"| {endpoint['method']} | [{endpoint['path']}]({endpoint_url(endpoint)}) | {tickets} |"
        )
    lines += [
        "",
        "Los valores entre llaves son parámetros de ruta (por ejemplo, `{userId}`).",
        "Todos los verbos abren su operación en Swagger (`/docs`): usar Try it out y Execute.",
        "Las rutas compartidas por varios tickets aparecen una sola vez.",
        "",
        "## Rutas auxiliares",
        "",
        "| Verbo | Ruta | Respuesta |",
        "| --- | --- | --- |",
        f"| GET | [/]({API_URL}/docs#/default/root__get) | Nombre, versión, documentación y lista automática de endpoints. |",
        f"| GET | [/health]({API_URL}/docs#/default/health_health_get) | Estado de salud de la API. |",
        f"| GET | [/api/hello]({API_URL}/docs#/default/hello_api_hello_get) | Mensaje de ejemplo. |",
        "",
        "## Actualizar este documento",
        "",
        "Después de modificar el manifiesto, ejecutar desde la raíz del repositorio:",
        "",
        "```powershell",
        "python backend/generate_endpoint_docs.py",
        "```",
        "",
        "Incluir el documento regenerado en el mismo commit que el manifiesto.",
        "Los nombres de las tareas se conservan en `backend/backlog_issue_titles.json`.",
        "",
    ]
    return "\n".join(lines)


if __name__ == "__main__":
    backend_dir = Path(__file__).resolve().parent
    endpoints = json.loads((backend_dir / "backlog_endpoints.json").read_text(encoding="utf-8"))
    issue_titles = json.loads((backend_dir / "backlog_issue_titles.json").read_text(encoding="utf-8"))
    destination = backend_dir.parent / "docs" / "api-endpoints.md"
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(render_document(endpoints, issue_titles), encoding="utf-8")
    print(f"Generado: {destination} ({len(endpoints)} rutas del backlog)")
