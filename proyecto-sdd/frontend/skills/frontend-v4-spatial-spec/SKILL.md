---
name: frontend-v4-spatial-spec
description: Especificación viviente, arquitectura de interfaz espacial (Spatial UI / Single-Canvas Zero-Navigation) con feedback luminoso Flash/Blink en acciones de scroll e intra-panel para el frontend v4 del proyecto Intercambia 9524.
---

# Especificación e Iteración — Frontend V4: Spatial Canvas (Zero-Navigation, Riqueza Informativa & Flash/Blink Universal)

Este documento es la **fuente de verdad técnica y conceptual** para la variante `v4` del frontend de Intercambia (`proyecto-sdd/frontend/v4`).
Mientras que `v3` introdujo la **Agentic Experience (AX) visual** manteniendo páginas separadas, la versión **v4** lleva esa experiencia a una arquitectura **Single-Canvas / Spatial UI (Lienzo Único sin navegación)**: **todo sucede en la misma página**, conservando toda la riqueza informativa y narrativa de la plataforma, sin cambios de URL, sin saltos bruscos de pantalla y sin perder jamás el contexto.

---

## 1. Principio Fundamental: Spatial UI / Zero-Navigation (Intimidad y Continuidad)

> [!IMPORTANT]
> **Cero cambios de página. Todo vive, respira, se expande y se contrae en el mismo lienzo.**
> - **Prohibido romper el contexto:** El usuario nunca es expulsado a otra página (`/explore`, `/offers/123`, `/workspace`, `/auth`). La URL permanece limpia y estable.
> - **Interacción orgánica (Expand & Morph In-Place):** Cuando el usuario toca algo que le interesa (una tarjeta de mentoría, un intercambio en vivo, su saldo de créditos, sus sesiones o un filtro), el elemento **se amplifica suavemente en el lugar** mostrando toda su riqueza interactiva, y al cerrarlo o tocar otro elemento **se vuelve a achicar** con naturalidad.
> - **Riqueza informativa completa:** A diferencia de `v5` (que sintetiza al extremo con íconos), `v4` mantiene las descripciones completas, explicaciones claras y contexto narrativo en las tarjetas y secciones.

---

## 2. Mecánicas Interactivas del Lienzo Único (V4)

1. **Dock Superior de Cápsulas Vivas (`SpatialCapsuleStage.vue`):**
   - La barra superior presenta **cápsulas interactivas** que despliegan paneles vivos directamente sobre el lienzo (acordeón espacial):
     - **Cápsula "Mis Sesiones & Agenda":** Se despliega in-situ para confirmar pedidos, iniciar/completar intercambios, chatear con la contraparte, calificar con estrellas y gestionar franjas horarias sin abandonar la vista principal.
     - **Cápsula "+ Publicar / Mis Temas":** Permite crear o eliminar propuestas de enseñanza y pedidos de aprendizaje ahí mismo en segundos.
     - **Cápsula de Créditos (`X Créditos`):** Al tocarla se expande mostrando el balance detallado, el historial de movimientos y la garantía de economía sin dinero.
     - **Cápsula de Ingreso Rápido (para Visitantes):** Despliega una tarjeta íntima de acceso/registro o simulación en 1 clic sin redirigir a `/auth`.
     - **Cápsula de Moderación (para Admin):** Se expande en el lugar para resolver denuncias pendientes.

2. **Tarjetas con Zoom In-Place (`SpatialCatalogBento.vue`):**
   - El catálogo de **Propuestas para Aprender** y **Aprendizajes Buscados** vive integrado en el lienzo principal.
   - **Estado Compacto:** Muestra categoría, título, descripción, modalidad, nivel, autor y reputación.
   - **Estado Amplificado (Al tocar la tarjeta):** La tarjeta se expande ocupando las 3 columnas de la grilla, revelando selector directo de horarios libres, elección entre 1 Crédito o Trueque 1 a 1, confirmación en 1 clic y opción de reporte in-situ.

3. **Feedback Visual Luminoso Universal (`.spatial-flash-blink` en Scroll + Intra-Panel):**
   - Toda acción del usuario dispara un **doble pulso luminoso (`.spatial-flash-blink`) + badge indicador (`⚡ ...`)** sobre el contenedor exacto donde ocurrió el cambio (`spatialStore.triggerFlash(key, label)`):
     - **Acciones con scroll:** Tocar un chip del Hero, amplificar una coincidencia desde el Simulador 1:1, publicar una nueva oferta/necesidad o abrir una cápsula hace scroll suave y destella la tarjeta o cápsula destino.
     - **Micro-acciones dentro del mismo panel (sin scroll):** Enviar un mensaje rápido en el chat de una sesión (`session-chat-${id}`), confirmar/iniciar/completar/cancelar/calificar una sesión (`session-card-${id}`), agregar o borrar un horario en Mi Agenda (`agenda-slots-list`), cambiar de sub-pestaña interna, elegir una franja horaria o método de intercambio en una tarjeta abierta (`booking-box-${id}`), o cambiar habilidades en el Simulador 1:1 (`simulator-result`) disparan exactamente el mismo *blink* en su lugar.

---

## 3. Registro de Decisiones e Iteraciones (V4)

| Fecha | Decisión / Idea | Justificación / Impacto | Estado |
|---|---|---|---|
| 2026-10-11 | Arquitectura Single-Canvas Zero-Navigation (`v4`). | Evitar cambios de página o URL para mantener al usuario inmerso en un único lienzo íntimo donde todo se amplifica y achica en su lugar. | Implementada |
| 2026-10-11 | Animación `.spatial-flash-blink` en acciones con scroll. | Dar confirmación visual inmediata de qué tarjeta o panel cambió luego de un desplazamiento automático. | Implementada |
| 2026-10-11 | Desacople del Flash/Blink respecto del scroll (soporte intra-panel). | Las acciones que suceden dentro del mismo panel (como enviar un mensaje rápido en el chat o elegir un horario) reciben el mismo pulso visual `.spatial-flash-blink`. | Implementada |

---

## 4. Instrucciones de Ejecución (V4)

* Directorio: `proyecto-sdd/frontend/v4`
* Puerto asignado: `http://localhost:5175`
* Comando de desarrollo: `npm run dev`
