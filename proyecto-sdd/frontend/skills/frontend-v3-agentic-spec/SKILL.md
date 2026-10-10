---
name: frontend-v3-agentic-spec
description: Especificación viviente, principios de diseño, arquitectura, gobierno SDD y guía de iteración para el frontend v3 (Agentic Experience / Alto Impacto Visual Sin Depender de Chatbox) del proyecto Intercambia 9524.
---

# Especificación e Iteración — Frontend V3: Agentic Experience (AX) & Alto Impacto Visual

Este documento es la **fuente de verdad técnica y conceptual** para la variante `v3` del frontend de Intercambia (`proyecto-sdd/frontend/v3`).
A diferencia de `v1` (implementación de referencia MVP con PrimeVue) y `v2` (diseño utilitario con Tailwind), la versión **v3** está diseñada como un producto orientado a **cautivar al visitante desde el primer segundo** mediante una **Agentic Experience (AX) rica y visual, sin reducirse a un chatbox**.

Cualquier mejora, cambio de enfoque estético o nueva idea interactiva para v3 **debe registrarse y actualizarse directamente en este archivo**.

---

## 1. Principio Fundamental: Agentic Experience Visual (Anti-Chatbox)

> [!IMPORTANT]
> **AX ≠ Chatbot.** No queremos un simple cuadro de texto donde el usuario esté obligado a escribir como en WhatsApp o ChatGPT. 
> La interacción agentic en una aplicación visual moderna se expresa a través de **componentes proactivos, directos y visuales**:
> - **Acción de 1 clic:** Chips dinámicos, selectores táctiles, sliders y widgets de exploración guiada.
> - **Cero fricción cognitiva:** El sistema anticipa intenciones y calcula compatibilidades en segundo plano mientras el usuario solo hace clics o pasa el cursor.
> - **Impacto estético y sensorial:** Fotografía cuidada, tarjetas vivas con avatares reales, micro-animaciones fluidas y métricas de reputación claras.

---

## 2. Visión y Propósito de V3

1. **Impacto visual inmediato (Hook):** El visitante no debe encontrarse con una grilla estática o aburrida de tablas y filtros. Debe percibir una plataforma moderna, viva, con tipografía cuidada, micro-interacciones cinematográficas e imágenes reales de personas colaborando.
2. **Vitalidad y Pulso Comunitario Inmediato (Social Proof & Hook de Venta):**
   - El visitante, antes de tocar nada, debe ver y sentir que **la plataforma está viva**:
     - **Ticker de Actividad en Tiempo Real (Live Activity Ticker):** *"Hace 4 min: Juan coordinó una sesión de Vue 3 con Elena"*, *"Carlos publicó: Introducción a Docker"*, *"Mariana completó su intercambio y sumó 1 crédito"*.
     - **Avatares flotantes y micro-badges:** Personas reales activas, valoraciones con estrellas doradas ("4.9 ★"), badges de confianza y horarios libres para hoy.
     - **Contadores de impacto con números en movimiento:** *"148 horas de conocimiento intercambiadas"*, *"0 pesos gastados"*, *"98% de sesiones calificadas 5 estrellas"*.
3. **Concierge Visual y Guiado (Zero-Prompt Interface):**
   - El visitante puede elegir con un clic: *"Quiero aprender algo nuevo"* o *"Quiero enseñar lo que sé"*.
   - Se despliegan píldoras interactivas de temas populares (*"Inglés IT", "Vue 3", "Docker", "Diseño UX"*).
   - Al tocar una píldora, la pantalla cobra vida al instante mostrando matches sugeridos, con compatibilidad calculada y horarios recomendados, sin obligar a escribir una sola palabra.
4. **Simulador de Intercambio en Vivo ("Playground de Trueque"):**
   - Un widget visual interactivo de dos columnas: *"Lo que ofrezco"* <—> *"Lo que busco"*.
   - El usuario conecta dos habilidades visualmente y ve en tiempo real cómo se desbloquea una sesión, se calculan compatibilidades y fluyen los créditos simbólicos (reforzando que **no interviene dinero real**).
5. **Respeto irrestricto al modelo de dominio (Reglas de Oro del MVP):**
   - Rol único: **USER** (una persona puede enseñar y aprender alternativamente).
   - Los créditos son **fichas internas de tiempo**: no representan dinero ni se monetizan.
   - Conexión transparente al backend FastAPI (`http://127.0.0.1:8000`) con soporte de fallback para demostraciones fluidas.

---

## 3. Protocolo de Gobernanza SDD (SDD Gatekeeper)

Para mantener a `proyecto-sdd/mvp-v3.md` como la **única fuente de verdad** del proyecto:

1. **Innovación de Presentación (Permitida):** Mejoras de layout, animaciones, widgets interactivos, simuladores y assets visuales no contradicen el MVP; se implementan y documentan en este skill.
2. **Detección de Fricción / Contradicción:** Si una idea para V3 entra en conflicto con las invariantes del producto (ej. introducir pagos con dinero, alterar el flujo de estados de sesión, crear roles separados de profesor/alumno):
   - El asistente **debe detenerse y emitir una alerta explícita de contradicción SDD**.
   - Se evalúan las opciones: adaptar la idea dentro del modelo existente, o realizar una evolución formal de la especificación general del proyecto (`proyecto-sdd/cambios.md` y nuevo incremento de versión del MVP).

---

## 4. Pila Tecnológica Aprobada para V3

* **Framework:** Vue 3 con Composition API (`<script setup>`).
* **Estilos:** Tailwind CSS v4 con variables semánticas modernas, efectos de glassmorphism, gradientes suaves y animaciones de entrada.
* **Íconos:** Lucide Vue (`lucide-vue-next`).
* **Estado:** Pinia (`authStore`, `platformStore`).
* **Integración API:** Cliente HTTP centralizado (`apiClient.js`) con proxy Vite (`/api` -> `http://127.0.0.1:8000`).
* **Assets Visuales:** Ilustraciones y fotografías de estilo mentoría humana, cálido y profesional en `/src/assets/images/`.

---

## 5. Componentes Clave de V3

### 5.1. Hero Inmersivo con Matchmaker Visual (`VisualMatchmakerHero.vue`)
- Selector de intención rápida de 2 toques: *¿Qué querés compartir?* y *¿Qué te gustaría aprender?*.
- Sugerencias visuales instantáneas con tarjetas de mentoría viva sin necesidad de tipear.

### 5.2. Simulador de Intercambio en Vivo (`InteractiveMatchSimulator.vue`)
- Muestra gráficamente el intercambio de 1 hora de conocimiento por 1 crédito de tiempo interno.
- Cálculo de compatibilidad recíproca en tiempo real con datos del backend FastAPI.

### 5.3. Vitrina de Confianza Comunitaria (`LiveCommunityPulse.vue`)
- Métricas dinámicas: sesiones activas, horas intercambiadas, 0 pesos gastados.
- Reseñas destacadas de usuarios reales de la base de datos.

### 5.4. Grilla Exploratoria Viva (`ExploreLiveGrid.vue`)
- Tarjetas con diseño editorial moderno, tags de modalidad, avatar y botón de acción directa.

---

## 6. Registro de Decisiones e Iteraciones

| Fecha | Decisión / Idea | Justificación / Impacto | Estado |
|---|---|---|---|
| 2026-10-10 | Creación de Frontend V3 con Agentic Experience Visual. | Superar el formato estático de tablas/filtros sin caer en un chatbox; uso de selectores visuales y micro-interacciones. | En curso |
| 2026-10-10 | Criterio Anti-Chatbox ratificado. | El usuario no debe estar obligado a escribir prompts; la AX debe ser navegable con clics, chips y gestos táctiles. | Aprobada |
| 2026-10-10 | Integración del protocolo de gobernanza SDD. | Preservar `mvp-v3.md` como la única fuente de verdad ante posibles divergencias. | Aprobada |

---

## 7. Instrucciones para Ejecutar y Desarrollar V3

* Directorio: `proyecto-sdd/frontend/v3`
* Puerto asignado: `http://localhost:5174` (o integrado en `start-dev.ps1 -v3`)
* Comando de desarrollo: `npm run dev`
* Build de producción: `npm run build`
