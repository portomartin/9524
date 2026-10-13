---
name: frontend-v7-handdrawn-light-spec
description: Especificación viviente de diseño y arquitectura para el Frontend V7 (Hand-Drawn Warm Light Spatial Edition). Basado íntegramente en la base limpia de V6 (Tema Claro Cálido Solarized Light + Panel Maestro por Sección + Flash/Blink universal), incorporando un sistema de iconografía Hand-Drawn representativo por bloque principal y replicado en cada tarjeta hija para identificación visual de un golpe de vista.
---

# Especificación e Iteración — Frontend V7: Hand-Drawn Warm Light Spatial Edition

Este documento es la **fuente de verdad técnica y conceptual** para la variante **`v7`** del frontend de Intercambia (`proyecto-sdd/frontend/v7`).
El **Frontend V7** toma como punto de partida intacto la **Versión V6** (conservando `v6` como línea base limpia) y suma incrementos de refinamiento visual y semántico sobre esa base:

1. **Base V6 Intacta:** Tema Claro Cálido (*Warm Parchment / Solarized Light* `#fdf6e3` / `#f3edda`), Arquitectura de Panel Maestro por Sección (cero tarjetas huérfanas) y *Flash / Blink* universal calibrado para tema claro.
2. **Sistema de Iconografía *Hand-Drawn* por Bloque Maestro y Tarjetas Hijas (`HandDrawnIcon.vue`):** Cada bloque principal tiene su ícono representativo estilo boceto en tinta artesanal junto a su título, y ese mismo ícono se replica dentro de cada una de las tarjetas hijas del bloque para identificar de un golpe de vista a qué dimensión pertenece.

---

## 1. Sistema de Iconografía Hand-Drawn por Bloque y Tarjetas Hijas

Cada uno de los 5 bloques principales cuenta con un **sello ilustrado estilo *hand-drawn* (boceto orgánico en tinta con borde pespunteado artesanal)** en su cabecera, replicado en cada tarjeta hija (`src/components/ui/HandDrawnIcon.vue`):

1. **Bloque 1 · Aprender enseñando (`hero`):**
   - **Ícono:** Libro abierto con rayos de luz/idea trazados a mano.
   - **Presencia:** Junto al título principal del Hero, en cada chip rápido de temas y en la tarjeta flotante de métricas.
2. **Bloque 2 · Explorá, filtrá y reservá (`explore` + `teach` / `learn`):**
   - **Ícono del bloque (`explore`):** Brújula bocetada a mano en el título principal de la sección y repetida como sello en la esquina superior derecha de cada tarjeta del tablero.
   - **Ícono de Enseñar / Propuestas (`teach`):** Cuaderno inclinado con pluma estilográfica bocetada a mano en el filtro superior y en cada tarjeta de propuesta (compacta y amplificada).
   - **Ícono de Aprender / Pedidos (`learn`):** Diana con flecha en el blanco bocetada a mano en el filtro superior y en cada tarjeta de pedido de aprendizaje (compacta y amplificada).
3. **Bloque 3 · Intercambios que están pasando hoy (`exchanges`):**
   - **Ícono:** Dos arcos recíprocos en ciclo con una chispa central trazada a mano.
   - **Presencia:** Junto al título de la sección, en la píldora superior de categoría y en el puente `Trueque Recíproco 1 Hora = 1 Crédito` de cada tarjeta de intercambio en vivo.
4. **Bloque 4 · Simulá tu intercambio en 2 clics (`simulator` + `teach` / `learn`):**
   - **Ícono:** Dos nodos conectados por un puente punteado y un rayo de afinidad bocetado a mano.
   - **Presencia:** Junto al título del simulador, en el conector central `Trueque 1:1`, en cada tarjeta seleccionable de habilidades (combinado con `teach` en el Paso 1 y `learn` en el Paso 2) y en el banner de resultado de Match.
5. **Bloque 5 · Comunidad libre de dinero (`community`):**
   - **Ícono:** Escudo artesanal con costura punteada y corazón en el centro trazado a mano.
   - **Presencia:** Junto al título del bloque, arriba de cada una de las 4 tarjetas de garantías (`100%`, `1 a 1`, `4.8 ★`, `1 Crédito`) y en el encabezado de su vista expandida.

---

## 2. Registro de Decisiones e Iteraciones (V7)

| Fecha | Decisión / Idea | Justificación / Impacto | Estado |
|---|---|---|---|
| 2026-10-12 | Creación de Frontend V7 a partir de V6 preservando V6 como base limpia. | Mantener V6 congelada como referencia limpia del tema Warm Parchment Light y evolucionar los refinamientos en V7. | Implementada |
| 2026-10-12 | Sistema de íconos *hand-drawn* representativos por bloque y replicados en cada tarjeta hija (`HandDrawnIcon.vue`). | Identificación visual de un golpe de vista entre cada bloque maestro y sus tarjetas internas, sumando calidez artesanal. | Implementada |
| 2026-10-12 | Eliminación de los botones redundantes `"Amplificar ⤢"` en el pie de las tarjetas del catálogo. | Al ser toda la tarjeta clicable directamente (`cursor-pointer`), quitar ese botón limpia el pie de la tarjeta y deja respirar los datos del mentor/aprendiz. | Implementada |
| 2026-10-12 | Recuperación del efecto *rollover* en las tarjetas y agregado de avatares fotográficos reales en el catálogo. | Al pasar por arriba de cada tarjeta se eleva (`translateY(-5px)`), ilumina su borde/sombra e insignias *hand-drawn*, y muestra la foto real de cada usuario en lugar de solo su inicial. | Implementada |
| 2026-10-12 | Fortalecimiento de las entidades visuales **Enseñar (`teach`, Turquesa)** y **Aprender (`learn`, Azul Cobalto)**. | Rediseño de los íconos `teach` (bombilla radiante sobre libro abierto con trazos gruesos) y `learn` (diana doble con flecha audaz) presentados en medallones destacados (`w-9 h-9`) en cada tarjeta del catálogo, simulador e intercambios. | Implementada |

---

## 3. Instrucciones de Ejecución (V7)

* Directorio: `proyecto-sdd/frontend/v7`
* Puerto asignado: `http://localhost:5178`
* Comando de desarrollo: `npm run dev`
