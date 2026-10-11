---
name: frontend-v1-primevue-spec
description: Especificación técnica y funcional de referencia para el Frontend V1 (MVP V3 completo con Vue 3 + PrimeVue 4 en modo multipágina clásico) del proyecto Intercambia 9524.
---

# Especificación — Frontend V1: Implementación Clásica con PrimeVue 4

Este documento registra la arquitectura y alcance de la variante **`v1`** del frontend (`proyecto-sdd/frontend/v1`), que implementa el alcance completo de `proyecto-sdd/mvp-v3.md` utilizando **Vue 3 + PrimeVue 4 (Aura Theme)** bajo un esquema multipágina clásico con Vue Router.

---

## 1. Propósito y Enfoque de V1

1. **Cobertura Funcional Completa del MVP V3:**
   - Autenticación, registro con otorgamiento de **1 Crédito de Bienvenida** y cambio rápido de usuario en modo demo.
   - Exploración de **Ofertas de Enseñanza** y **Necesidades de Aprendizaje** con filtros por categoría y modalidad.
   - Publicación y gestión de ofertas, necesidades y bloques de disponibilidad horaria.
   - Coordinación de sesiones (`PENDIENTE` -> `CONFIRMADA` -> `EN_CURSO` -> `COMPLETADA` / `CANCELADA`), mensajería asociada a la sesión y calificación cruzada de 1 a 5 estrellas.
   - Panel de moderación administrativa para resolución de denuncias.
2. **Pila Tecnológica:**
   - Vue 3 (`<script setup>`), Pinia (`authStore`, `platformStore`), Vue Router (`/`, `/explore`, `/workspace`, `/profile`, `/admin`, `/auth`) y componentes nativos de **PrimeVue 4**.
3. **Ejecución:**
   - Directorio: `proyecto-sdd/frontend/v1`
   - Puerto asignado: `http://localhost:5172`
