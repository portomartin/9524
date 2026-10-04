---
name: crear-sc
description: Generar un SC (Scope Canvas) del proyecto a partir del MVP, organizando necesidades, motivadores, propósito, impacto, objetivos, acciones y métricas.
---

# SC (Scope Canvas)

Usar esta skill cuando se solicite crear, revisar o completar el SC del proyecto.

## Fuente y límites

- Leer `AGENTS.md` y la versión indicada del MVP (`docs/mvp-v1.md`, `docs/mvp-v2.md` o `docs/mvp-v3.md`) antes de elaborar el canvas.
- Usar la versión indicada del MVP como única fuente de alcance aprobado.
- No incorporar funcionalidades, métricas objetivo ni reglas de negocio que el MVP no respalde.
- Marcar como `Propuesta pendiente de aprobación` cualquier definición necesaria que el MVP no resuelva.
- No modificar ninguna versión del MVP, WBS, USM, backlog ni Jira automáticamente.
- El SC no reemplaza al backlog, la WBS ni la USM; resume el sentido, alcance e impacto del producto.

## Estructura obligatoria

Organizar el canvas en siete bloques:

### Usuarios

1. **Necesidades:** qué necesitan los usuarios y qué problemas o dolores tienen.
2. **Motivadores:** qué valor o mejora les ofrece el producto para responder a esas necesidades.

### Negocio

3. **Propósito:** por qué vale la pena construir el producto y qué valor busca entregar el equipo.
4. **Impacto:** qué resultados de largo plazo se espera producir.
5. **Objetivos:** qué resultados de corto plazo se quieren alcanzar con el MVP.

### Comportamiento y medición

6. **Acciones:** qué se espera que hagan los usuarios y qué comportamientos observables muestran que el producto entrega valor.
7. **Métricas:** qué se medirá para saber si los objetivos se cumplen.

## Reglas de elaboración

- Considerar los roles Docente y Alumno; incluir Administrador solo cuando corresponda al MVP.
- Mantener explícito que los créditos son internos de la plataforma y no son dinero.
- Relacionar cada objetivo con acciones observables y métricas posibles.
- No inventar valores numéricos, fechas ni metas cuantitativas; marcarlos como pendientes si no están definidos.
- Separar indicadores de actividad —por ejemplo, usuarios registrados— de indicadores de resultado —por ejemplo, sesiones completadas o intercambios concretados—.
- Mantener el alcance del MVP en intercambios y sesiones individuales 1 a 1 cuando corresponda.
- Diferenciar necesidades de usuario, decisiones de negocio y tareas técnicas.

## Resultado esperado

Presentar:

1. El SC completo en Markdown, preferentemente como tabla o bloques claramente identificados.
2. La trazabilidad de cada bloque hacia secciones de la versión indicada del MVP.
3. Supuestos y propuestas pendientes de aprobación.
4. Una comprobación breve de coherencia entre propósito, objetivos, acciones y métricas.

Generar o actualizar automáticamente estos dos documentos cuando se ejecute la skill:

- `docs/sc.md`: versión canónica y editable en Markdown.
- `docs/sc-visual.png`: versión visual del canvas, organizada con tarjetas y preparada para presentar o insertar en entregas.

Ambos archivos deben expresar el mismo alcance. Presentar también en el chat un resumen del contenido creado o actualizado.

## Exclusión

Esta skill no genera storytelling ni utiliza la estructura Contexto → Problema → Solución → Desenlace feliz.
