---
name: frontend-v5-human-visual-spec
description: Especificación viviente, arquitectura cognitiva de golpe de vista (Human-First + Enseño ⇄ Aprendo Visual + Progressive Disclosure + Flash/Blink Universal) sobre Lienzo Único para el frontend v5 del proyecto Intercambia 9524.
---

# Especificación e Iteración — Frontend V5: Human-First & Conexión Instantánea (Enseño ⇄ Aprendo de un Golpe de Vista)

Este documento es la **fuente de verdad técnica y conceptual** para la variante `v5` del frontend de Intercambia (`proyecto-sdd/frontend/v5`).
Construida sobre el motor de **Lienzo Único (Single-Canvas Zero-Navigation)** de `v4`, la versión **v5** explora una variante de **Revelación Progresiva (*Progressive Disclosure*) y Síntesis Visual con Íconos**: priorizar rostros humanos y el puente `Enseño ⇄ Aprendo` en las tarjetas cerradas, ocultando los textos largos hasta que el usuario toca para amplificar.

---

## 1. Principio Fundamental de V5: "Que entre en el cerebro de un saque"

> [!IMPORTANT]
> **Menos lectura en frío, más rostros humanos, íconos y conexión `Enseño ⇄ Aprendo`.**
> 1. **Rostros reales primero (Human-First):** Cada tarjeta compacta muestra la fotografía real del miembro, su nombre y su reputación (`★ 4.9`).
> 2. **Ecuación Visual `ENSEÑO ⇄ APRENDO` en cada tarjeta:** Dos bloques visuales conectados (`🎓 Enseña` y `🎯 Busca aprender`) en lugar de párrafos largos en la vista cerrada.
> 3. **Lenguaje de Íconos:** Modalidad (`🌐` / `📍`), tiempo (`⏱️ 1h`) y valor (`🪙 1`) expresados con íconos.
> 4. **Flash / Blink Universal (`.spatial-flash-blink`):** Incluye el pulso luminoso + badge `⚡` tanto cuando una acción produce scroll hacia otro sector del lienzo como cuando ocurre una micro-acción dentro del mismo panel (enviar un mensaje rápido en el chat de sesión, calificar, sumar horarios, cambiar habilidades del simulador o elegir franja horaria).

---

## 2. Registro de Decisiones e Iteraciones (V5)

| Fecha | Decisión / Idea | Justificación / Impacto | Estado |
|---|---|---|---|
| 2026-10-11 | Creación de variante V5 con síntesis visual e íconos. | Explorar una versión de lectura ultrarrápida centrada en rostros humanos y el par `Enseño ⇄ Aprendo`. | Implementada |
| 2026-10-11 | Incorporación de `.spatial-flash-blink` en scroll y micro-acciones internas. | Usar V5 como laboratorio para validar el destello visual en cambios con scroll y acciones dentro del mismo panel (ej. chat rápido en sesión). | Implementada |
| 2026-10-11 | Evaluación comparativa V5 vs V4. | Si bien V5 aporta impacto iconográfico rápido, resulta algo más fragmentada/granular; se prefiere la estructura informativa completa de V4 como base para V6. | Registrada |

---

## 3. Instrucciones de Ejecución (V5)

* Directorio: `proyecto-sdd/frontend/v5`
* Puerto asignado: `http://localhost:5176`
* Comando de desarrollo: `npm run dev`
