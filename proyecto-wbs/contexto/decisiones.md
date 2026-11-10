# Decisiones del proyecto WBS

## Confirmadas

### Destino del trabajo

- Las notas de entrega, demo, defensa, retrospectiva, planificación y reglas asociadas se gestionan en el proyecto Jira `WBSO`.
- `BH95` queda fuera de este flujo: corresponde al proyecto técnico SDD.
- El contexto de este proyecto se conserva también en archivos Markdown versionados dentro de `proyecto-wbs/contexto/`.

### Organización de las épicas en Jira — 2026-11-09

| Épica | Título en Jira | Alcance acordado |
| --- | --- | --- |
| [WBSO-1](https://martinporto.atlassian.net/browse/WBSO-1) | Producto y diseño | Investigación, planificación y definición del MVP. Incluye la gestión del hosting, el despliegue del frontend y del backend y su integración con el código fuente. |
| [WBSO-2](https://martinporto.atlassian.net/browse/WBSO-2) | Funcionalidad de la plataforma | Desarrollo de las funcionalidades de la plataforma. |
| [WBSO-3](https://martinporto.atlassian.net/browse/WBSO-3) | Seguridad y administración | Desarrollo de seguridad y administración. |
| [WBSO-4](https://martinporto.atlassian.net/browse/WBSO-4) | Pruebas y entrega | Paquete de pruebas ([WBSO-18](https://martinporto.atlassian.net/browse/WBSO-18)) y entrega del MVP ([WBSO-19](https://martinporto.atlassian.net/browse/WBSO-19)), que incluye código fuente, manuales, documentación técnica y demo. |

- Se eliminaron las subtareas duplicadas `WBSO-124` (Aplicación desplegada) y `WBSO-126` (Base de datos configurada). Se verificó que `WBSO-28`, `WBSO-29` y `WBSO-30` siguen bajo `WBSO-6`, dentro de la épica 1.
- El usuario eliminó `WBSO-16` (Aplicación web integrada). Se verificó que la épica 4 agrupa a `WBSO-18` y `WBSO-19` y se actualizó su título a «Pruebas y entrega».

## Pendientes de definir

- Si los estados de sesión se mantienen exactamente como Pendiente, Aceptada, Completada y Cancelada.
- Qué ocurre con los créditos ante cancelación, cancelación tardía o inasistencia.
- Qué issues concretos se crearán a partir de cada nota.
