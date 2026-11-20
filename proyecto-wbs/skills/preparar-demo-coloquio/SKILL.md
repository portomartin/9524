---
name: preparar-demo-coloquio
description: Guía estratégica, guion y mejores prácticas observadas en vivo para la presentación oral y demo del MVP ante la cátedra FIUBA TC017 (Gestión del Desarrollo de Sistemas Informáticos). Usar cuando se prepare, ensaye o ajuste la demo, la puesta en escena o la defensa oral del proyecto.
metadata:
  short-description: Estrategia y guion de demo para el coloquio TC017
---

# Preparación de la Demo y Coloquio Oral (TC017 FIUBA)

Este skill recopila las **observaciones de campo reales** tomadas durante las presentaciones de los otros grupos en la cátedra, y define la **estrategia de puesta en escena, guion y arquitectura de la demo** para Lerna.

---

## 1. Reglas y Dinámica Observadas en la Cátedra

| Parámetro | Criterio Observado en Vivo |
| :--- | :--- |
| **Tiempo Límite Estricto** | **30 minutos reloj por grupo** (sin prórroga). |
| **Estructura Esperada** | 1. Storytelling inicial (6-7 imágenes).<br>2. Demo interactiva en vivo.<br>3. Ronda de preguntas al cierre. |
| **Preguntas de Cátedra** | **3 a 4 preguntas por grupo** al final. Alejandro hace ~3 preguntas conceptuales/generales; Mauro y Pilar preguntan sobre decisiones técnicas, alcance y control de estados. |
| **Dispositivos en Demo** | Los grupos con mejor puntaje conectaron **múltiples smartphones en simultáneo** proyectando la pantalla. |
| **Participación de la Clase** | La demo mejor calificada (10/10) **proyectó un código QR** para que docentes y alumnos ingresaran a la web desde sus celulares. |

---

## 2. Lecciones Aprendidas de los Otros Grupos

### ✅ Lo que funcionó de forma sobresaliente:
1. **Interacción en Vivo vía QR (Caso "Pagar la cuenta" - 10/10):**
   - Compartir un QR visible en pantalla.
   - La clase entra al entorno real, interactúa y ve reflejados sus pedidos de inmediato.
2. **Coordinación Multidispositivo (Caso "Barrio Ahorro" - 9/10):**
   - 4 integrantes coordinados con sus teléfonos en vivo:
     - *Usuario 1:* Publica una oferta.
     - *Usuario 2:* Busca, filtra y solicita la compra.
     - *Usuario 3:* Confirma y califica con reseña pública.
     - *Pantalla Central / Proyector:* Panel administrativo mostrando las transacciones y estados en tiempo real.
3. **Carga de Datos Coherente y Extensa (Caso "MediTrace" - 9/10):**
   - Base de datos con historial creíble simulando 1 año de actividad previa. Evita la sensación de "sistema vacío recién creado".

### ❌ Lo que restó puntos o se vio improvisado:
1. **Mock de Base de Datos Pobre (Caso "GameMatch"):**
   - Datos sin contexto o que no mostraban actividad real entre usuarios restaron credibilidad al flujo.
2. **Improvisar la Carga en Vivo (Caso "MediTrace"):**
   - Tratar de inventar registros sobre la marcha (*"a ver, ahora creemos este otro..."*) rompe el ritmo. La demo debe seguir un **guion cerrado ensayado segundo a segundo**.

---

## 3. Guion Recomendado para la Demo de Lerna (Distribución 30 Minutos)

```
[00:00 - 05:00]  BLOQUE 1: Storytelling & Contexto (5 min)
                 • 7 viñetas visuales (Lucía y Mateo).
                 • Dolor real: barrera económica, 1 hora = 1 crédito, custodia de créditos.

[05:00 - 22:00]  BLOQUE 2: Demo en Vivo Coordinada (17 min)
                 • Min 05: Proyección de QR para que la cátedra/alumnos entren como invitados.
                 • Min 07: Mateo (Smartphone 1) busca clase de piano y solicita turno.
                 • Min 10: Bloqueo atómico de créditos (Escrow) visible en el balance.
                 • Min 12: Lucía (Smartphone 2 / Laptop) recibe solicitud, acepta y genera Meet.
                 • Min 15: Confirmación de clase, liberación de créditos a Lucía.
                 • Min 18: Calificación mutua 5 estrellas y actualización de reputación.
                 • Min 20: Vista del Panel de Auditoría / Admin mostrando el log transaccional.

[22:00 - 30:00]  BLOQUE 3: Cierre & Preguntas de la Cátedra (8 min)
                 • Responder con seguridad basándose en la WBS, la arquitectura FastAPI/SQLModel
                   y las decisiones registradas en `contexto/decisiones.md`.
```

---

## 4. Checklist Técnico Previo a la Defensa
- [ ] Backend FastAPI corriendo en servidor cloud con SSL (o túnel ngrok/Cloudflare estable).
- [ ] Frontend desplegado accesible por URL pública (Vercel/Netlify/Render).
- [ ] Base de datos poblada con el seeder mock (`seed_mock.py`): usuarios con fotos, ofertas variadas y calificaciones previas.
- [ ] Código QR generado que apunte directamente a la URL del catálogo de Lerna.
- [ ] 2 computadoras o 2 teléfonos listos y logueados con las cuentas de demo (Mateo y Lucía).
- [ ] Hub de diapositivas abierto en pestaña secundaria: `proyecto-wbs/docs/Entrega/presentacion.html`.
