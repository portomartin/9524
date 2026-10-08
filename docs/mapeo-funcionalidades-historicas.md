# Mapeo de funcionalidades históricas

**Propósito:** conservar la trazabilidad entre el WBS original y el trabajo existente en Jira.

**Fuente de alcance:** [`mvp-v3.md`](mvp-v3.md).

**Naturaleza del documento:** auxiliar de reconciliación. No reemplaza el MVP V3, el backlog ni el WBS original.

## Convenciones

Cada elemento del WBS original se relaciona con un único check canónico y una única tarea Jira:

```text
WBS original → check canónico → tarea Jira
```

La numeración del check combina:

- el identificador actual de la subtarea;
- la referencia histórica del WBS original;
- el nombre exacto del elemento histórico.

Formato:

```text
[ID actual] [WBS ID] Nombre exacto del WBS.
```

## Mapeo histórico 1:1

| WBS original | Check canónico / tarea Jira |
|---|---|
| 1.3.1.1 Módulo de registro | `BH95-221` — `[1.3.1.1] [WBS 1.3.1.1]` Módulo de registro. |
| 1.3.2 Inicio y cierre de sesión | `BH95-222` — `[1.4.1.1] [WBS 1.3.2]` Inicio y cierre de sesión. |
| 1.3.3 Recuperación de contraseña | `BH95-223` — `[1.4.1.3] [WBS 1.3.3]` Recuperación de contraseña. |
| 1.3.4 Perfil de usuario | `BH95-224` — `[2.1.1.1] [WBS 1.3.4]` Perfil de usuario. |
| 1.3.5 Registro de conocimientos que puede enseñar | `BH95-225` — `[2.1.1.2] [WBS 1.3.5]` Registro de conocimientos que puede enseñar. |
| 1.3.6 Registro de conocimientos que desea aprender | `BH95-226` — `[2.3.1.1] [WBS 1.3.6]` Registro de conocimientos que desea aprender. |
| 1.3.7 Configuración de nivel | `BH95-227` — `[2.3.1.2] [WBS 1.3.7]` Configuración de nivel. |
| 1.3.8 Configuración de modalidad | `BH95-229` — `[2.3.1.3] [WBS 1.3.8]` Configuración de modalidad. |
| 1.3.9 Configuración de disponibilidad horaria | `BH95-230` — `[4.1.1.1] [WBS 1.3.9]` Configuración de disponibilidad horaria. |
| 1.3.10 Visualización del saldo de créditos | `BH95-228` — `[5.1.1.1] [WBS 1.3.10]` Visualización del saldo de créditos. |
| 1.4.1 Formulario de publicación | `BH95-231` — `[2.2.1.1] [WBS 1.4.1]` Formulario de publicación. |
| 1.4.2 Catálogo de categorías | `BH95-232` — `[2.2.1.2] [WBS 1.4.2]` Catálogo de categorías. |
| 1.4.3 Descripción del aprendizaje ofrecido | `BH95-233` — `[2.2.1.3] [WBS 1.4.3]` Descripción del aprendizaje ofrecido. |
| 1.4.4 Selección del nivel | `BH95-234` — `[2.2.1.4] [WBS 1.4.4]` Selección del nivel. |
| 1.4.5 Selección de modalidad | `BH95-235` — `[2.2.1.5] [WBS 1.4.5]` Selección de modalidad. |
| 1.4.6 Duración estimada | `BH95-236` — `[2.2.1.6] [WBS 1.4.6]` Duración estimada. |
| 1.4.7 Valor en créditos | `BH95-237` — `[2.2.1.7] [WBS 1.4.7]` Valor en créditos. |
| 1.4.8 Gestión de publicaciones | `BH95-238` — `[2.2.1.8] [WBS 1.4.8]` Gestión de publicaciones. |
| 1.4.9 Validación de contenido | `BH95-239` — `[2.2.1.9] [WBS 1.4.9]` Validación de contenido. |
