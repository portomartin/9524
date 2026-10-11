---
name: frontend-v2-tailwind-spec
description: Especificación técnica y funcional para el Frontend V2 (MVP V3 moderno con Vue 3 + Tailwind CSS v4 + componentes estilo Shadcn en modo multipágina) del proyecto Intercambia 9524.
---

# Especificación — Frontend V2: Diseño Moderno con Tailwind CSS + Shadcn UI

Este documento registra la arquitectura y alcance de la variante **`v2`** del frontend (`proyecto-sdd/frontend/v2`), que reemplaza la librería de componentes PrimeVue de `v1` por un sistema de diseño limpio basado en **Tailwind CSS v4 y primitivos UI estilo Shadcn** manteniendo la navegación multipágina tradicional.

---

## 1. Propósito y Enfoque de V2

1. **Misma Cobertura Funcional del MVP V3 con Estética Minimalista:**
   - Mantiene las rutas multipágina (`/`, `/explore`, `/offers/:id`, `/needs/:id`, `/workspace`, `/profile`, `/admin`, `/auth`) y todas las reglas de negocio de `proyecto-sdd/mvp-v3.md` (rol único `USER`, créditos internos no monetarios).
   - Introduce tarjetas limpias, badges semánticos, modales livianos y tipografía `Plus Jakarta Sans`.
2. **Pila Tecnológica:**
   - Vue 3 (`<script setup>`), Tailwind CSS v4, Lucide Icons (`lucide-vue-next`), Pinia y cliente HTTP unificado con fallback local.
3. **Ejecución:**
   - Directorio: `proyecto-sdd/frontend/v2`
   - Puerto asignado: `http://localhost:5173`
