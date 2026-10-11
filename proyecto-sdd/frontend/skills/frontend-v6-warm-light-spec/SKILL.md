---
name: frontend-v6-warm-light-spec
description: Especificación viviente de diseño y arquitectura para el Frontend V6 (Warm Light / Solarized Parchment Spatial Edition). Basado íntegramente en la riqueza funcional y narrativa de V4 (Lienzo Único sin cambios de página + Flash/Blink en cada acción), con estética cálida editorial inspirada en el tema claro (Solarized Light / Parchment Cream) de Antigravity IDE y arquitectura de Panel Maestro por sección.
---

# Especificación e Iteración — Frontend V6: Warm Parchment Light Spatial Edition

Este documento es la **fuente de verdad técnica y conceptual** para la variante **`v6`** del frontend de Intercambia (`proyecto-sdd/frontend/v6`).
El **Frontend V6** toma como base la **Versión V4** (conservando toda su riqueza informativa, explicaciones completas, Lienzo Único sin cambios de URL y *Flash / Blink* en todas las acciones con scroll o dentro del mismo panel) y la eleva con dos pilares de diseño:
1. **Tema Claro Cálido Editorial (*Warm Parchment / Solarized Light*)** inspirado en el tema claro de Antigravity IDE.
2. **Arquitectura de Panel Maestro por Sección (Cero tarjetas huérfanas y cero chips decorativos superiores)**.

---

## 1. Principios de Diseño y Experiencia (V6)

### 1.1. Tema Claro Cálido (Antigravity IDE Solarized Light)
- **Cero Blanco Frío Quirúrgico (`#ffffff` evitado en fondos):** Utiliza un lienzo principal de **papel crema / pergamino cálido (`#fdf6e3`)** combinado con paneles de **arena suave (`#f3edda` / `#eee8d5`)**, superficies interactivas (`#e7e0cb`) y bordes de **piedra cálida (`#d6ceb8` / `#d2c9b0`)** que descansan la vista y transmiten calidez humana e intelectual.
- **Tinta Profunda de Alta Legibilidad:** Tipografía principal en azul-petróleo profundo (`#073642`) y textos secundarios en pizarra cálido (`#2c4249` / `#52676f`), logrando contraste editorial nítido.
- **Acentos Cromáticos Inspirados en el Resaltado de Sintaxis del IDE:**
  - **Turquesa / Esmeralda Botánico (`#0d9488` / `#0f766e`):** Propuestas de enseñanza, confirmaciones y primer pulso del `.spatial-flash-blink`.
  - **Azul Cobalto Editorial (`#268bd2` / `#1b6ca8`):** Títulos en gradiente, necesidades de aprendizaje y acciones secundarias.
  - **Ámbar / Terracota (`#b58900` / `#cb4b16`):** Créditos de tiempo, estrellas de reputación y segundo pulso del `.spatial-flash-blink`.

### 1.2. Arquitectura de Panel Maestro por Sección (Cero Tarjetas Huérfanas)
- **Modelo Unificado basado en el Hero:** Todas las secciones del lienzo (`Hero`, `Tablero de Propuestas y Necesidades`, `Intercambios que están pasando hoy`, `Simulador 1 a 1` y `Garantías de Confianza`) siguen exactamente el mismo modelo contenedor:
  - Un **Panel Maestro (`rounded-3xl`)** con borde cálido y resplandor ambiental sutil.
  - Un **Encabezado Editorial de dos líneas** en la parte superior del panel (primera línea en tinta petróleo `#073642`, segunda línea en gradiente turquesa-a-cobalto) acompañado de su bajada explicativa.
  - **Todo el contenido derivado de esa sección (buscadores, filtros, grillas de tarjetas expandibles y detalles desplegables) vive contenido adentro del mismo panel**, eliminando por completo las tarjetas sueltas o "huérfanas" fuera de su sección.
- **Sin Chips Verdes Decorativos Superiores:** Se eliminan las píldoras/chips decorativos encima de los títulos de cada sección para que el encabezado principal respire limpio y directo.

### 1.3. Flash / Blink Universal Calibrado para Tema Claro (`.spatial-flash-blink`)
- Tanto las acciones que producen scroll como las micro-acciones que ocurren dentro del mismo panel (enviar un mensaje rápido en el chat de sesión, elegir un horario, confirmar/calificar sesión, cambiar habilidades del simulador, etc.) disparan la animación `@keyframes spatialFlashPulse` calibrada para fondo crema (halo doble Turquesa `#0d9488` + Terracota `#cb4b16` con tinte interior `#e4f3ec` → `#f9edd2`).

---

## 2. Registro de Decisiones e Iteraciones (V6)

| Fecha | Decisión / Idea | Justificación / Impacto | Estado |
|---|---|---|---|
| 2026-10-11 | Creación de Frontend V6 sobre base V4 con Light Theme de Antigravity IDE. | Combinar la riqueza informativa y mecánica espacial de V4 con la calidez visual del tema claro Solarized/Pergamino (`#fdf6e3` / `#eee8d5`). | Implementada |
| 2026-10-11 | Estandarización del Panel Maestro por sección (cero tarjetas huérfanas). | Todas las secciones adoptan el modelo del Hero: título + bajada + todas sus tarjetas hijas contenidas dentro del mismo panel. | Implementada |
| 2026-10-11 | Eliminación del chip verde superior en los encabezados de sección. | Evitar ruido visual encima de los títulos principales de cada bloque. | Implementada |

---

## 3. Instrucciones de Ejecución (V6)

* Directorio: `proyecto-sdd/frontend/v6`
* Puerto asignado: `http://localhost:5177`
* Comando de desarrollo: `npm run dev`
