"""Genera el listado Markdown desde el manifiesto usado por la API."""

import json
from pathlib import Path


def render_document(endpoints: list[dict]) -> str:
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
        "| Verbo | Ruta | Tickets de Jira |",
        "| --- | --- | --- |",
    ]
    for endpoint in endpoints:
        tickets = ", ".join(
            f"[{key}](https://martinporto.atlassian.net/browse/{key})"
            for key in endpoint["issues"]
        )
        lines.append(f"| {endpoint['method']} | `{endpoint['path']}` | {tickets} |")
    lines += [
        "",
        "Los valores entre llaves son parámetros de ruta (por ejemplo, `{userId}`).",
        "Las rutas compartidas por varios tickets aparecen una sola vez.",
        "",
        "## Rutas auxiliares",
        "",
        "| Verbo | Ruta | Respuesta |",
        "| --- | --- | --- |",
        "| GET | `/` | Nombre, versión, documentación y lista automática de endpoints. |",
        "| GET | `/health` | Estado de salud de la API. |",
        "| GET | `/api/hello` | Mensaje de ejemplo. |",
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
        "",
    ]
    return "\n".join(lines)


if __name__ == "__main__":
    backend_dir = Path(__file__).resolve().parent
    endpoints = json.loads((backend_dir / "backlog_endpoints.json").read_text(encoding="utf-8"))
    destination = backend_dir.parent / "docs" / "api-endpoints.md"
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(render_document(endpoints), encoding="utf-8")
    print(f"Generado: {destination} ({len(endpoints)} rutas del backlog)")
