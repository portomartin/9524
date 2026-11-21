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

## 3. Dinámica de Participación de la Clase (Onboarding Express por QR)

Para generar el mismo impacto que las demos mejor calificadas sin complicar los tiempos ni forzar coordinaciones de calendario largas:

### A. Mecánica Express para el Público (1 solo clic)
1. **Escaneo del QR:** Docentes y alumnos escanean el QR desde el proyector y aterrizan en el modo bienvenida express (`/demo/join`).
2. **Identidad instantánea:**
   - **Alias automático y simpático:** Ej. *"Ingeniero Curioso #14"*, *"Recursante Optimista"*, *"Estudiante Paseo Colón"*.
   - **Avatar por defecto con opción Selfie:** Un botón rápido *"📸 Sacarse selfie"* que usa la cámara del celular. Quien se saca la foto aparece con su cara real en el catálogo.
3. **Billetera cargada:** Se le acreditan automáticamente **3 créditos virtuales** de bienvenida.
4. **Materia FIUBA asignada para enseñar:** De un pool rotativo sin repetir (*Álgebra II*, *Análisis Matemático II*, *Algoritmos III*, *Sistemas Operativos*, *Física II*, *Bases de Datos*, etc.), el sistema le publica su clase automáticamente con disponibilidad inmediata (*"Disponible Ahora / Turno Demo"*).
5. **Materia FIUBA que DESEA APRENDER (Match Cruzado en 1 toque):**
   - El sistema le asigna también una materia que quiere aprender (`desired_skills`), encadenada deliberadamente con la que enseña otro compañero registrado por QR.
   - **Sugerencia Proactiva en Pantalla:** En cuanto entra, ve un banner destacado:
     *🎯 "¡Encontramos quién te puede enseñar! [Alias Compañero] ofrece [Materia deseada]. Tocá acá para solicitarle clase con tus créditos de bienvenida"*.
   - Esto evita que la clase se pierda buscando en el catálogo y desata solicitudes cruzadas instantáneas.

### B. Separación de Roles en la Puesta en Escena
* **Público / Docentes (Experiencia Match en Vivo):**
  - Entran, exploran las materias que les tocaron a sus compañeros, tocan **"Solicitar intercambio"** (1 solo clic gracias al turno express) y ven cómo **sus créditos quedan en custodia (Escrow)**.
  - El compañero receptor ve la notificación en vivo en su celular y toca **"Aceptar"** $\to$ ¡Match en vivo en el aula!
* **Presentadores Mateo y Lucía (Ciclo Transaccional Completo + IA):**
  - Muestran en el proyector el ciclo completo:
    1. **Moderación IA:** Intento de publicar contenido prohibido y rechazo instantáneo.
    2. **Estimador IA:** Publicación de curso legítimo con cálculo automático de créditos.
    3. **Cierre de clase:** Finalización de la sesión pactada, liberación atómica de créditos y calificación mutua de 5 estrellas reflejada en el Panel Admin.

### C. El Clímax Humorístico: "Efecto Máquina del Tiempo" (⏩ Fast-Forward 7 días)
Para no dejar las solicitudes de los alumnos del público abiertas y dar un cierre con humor que despierte risas y aplausos:
1. **Botón en Panel Admin/Demo:** *"⏩ Simular paso de 7 días (Time-Travel Demo)"*.
2. **Arquitectura de la Cadencia (Backend-Driven Paso a Paso):**
   - **Por qué en el Backend:** Si fuera una animación superficial del frontend, en el proyector se vería lento pero en el celular de un alumno todo aparecería resuelto de golpe en el segundo 0. Manejar la cadencia con el backend asegura que la base de datos mute de verdad cada 2 segundos.
   - **Mecánica Técnica (`POST /demo/fast-forward-step`):**
     - El frontend llama a `POST /demo/fast-forward-step` cada ~2 segundos en un bucle secuencial.
     - Cada petición es ultra liviana (30 ms, sin riesgo de timeout en Render/Cloud).
     - El backend toma la siguiente sesión pendiente, ejecuta la transición atómica (`completada` o `cancelada`), libera o devuelve créditos y persiste en la tabla `ratings` una reseña cómica.
   - **Contenido Humorístico con Folclore FIUBA:**
     - **Sesiones completadas (~80%):** Liberan créditos y dejan reviews hilarantes (ej.: *"Me explicó autovalores con analogías de milanesas, aprobé el parcial 10/10"*, *"El mate virtual estaba un poco frío pero el código compiló de una"*, *"Casi lloro en Sistemas Operativos pero me salvó la cursada"*).
     - **Sesiones canceladas (~20%):** Devuelven créditos con motivos simpáticos (*"Cancelada: Me quedé dormido en el 152 llegando a Paseo Colón"*, *"Cancelada: Cayó el campus 5 min antes"*).
3. **El impacto multi-dispositivo en el aula:** Cada 2 segundos cae una tarjeta en el proyector y, en simultáneo, le suena la notificación al alumno correspondiente en su propio teléfono. El aula vive el paso del tiempo coordinado y entretenido.

### D. Puesta en Escena Visual en el Proyector (Split-Screen Coordinado)
Para maximizar el impacto visual mientras los alumnos interactúan, el proyector proyecta una **pantalla dividida (Split-Screen 50/50 o 40/60)**:

```
┌───────────────────────────────┬────────────────────────────────────────────┐
│      📱 CELULAR EN VIVO        │       💻 PANEL ADMINISTRADOR / MONITOR     │
│   (Espejado / Formato Móvil)  │          (Torre de Control Lerna)          │
├───────────────────────────────┼────────────────────────────────────────────┤
│                               │ 🟢 Usuarios Activos: 18 (14 base + 4 QR)  │
│  [Mateo / Lucía en acción]    │ 🔒 Créditos en Escrow (Custodia): 9 cr.   │
│                               │ 📚 Sesiones pactadas: 5                   │
│  • Intento de curso prohibido │ 🛡️ Filtros de IA aplicados: 1 (Bloqueado) │
│    (Popup de rechazo IA)      │────────────────────────────────────────────│
│  • Estimador de créditos      │ 📜 Feed de Actividad en Tiempo Real:       │
│  • Solicitud con 1 clic       │ • [21:05] User_42 solicitó Álgebra II      │
│  • Notificación recibida      │ • [21:06] Lucía aceptó Piano (-2 cr. lock) │
│                               │ • [21:07] IA bloqueó publicación #59       │
└───────────────────────────────┴────────────────────────────────────────────┘
```

* **Lado Izquierdo (Móvil del Presentador):** Sirve de guía narrativa para mostrar la experiencia de usuario final, las interacciones táctiles y las respuestas en vivo de la IA.
  *(Setup recomendado: ventana de navegador en modo responsive/móvil F12 o espejo de smartphone con `scrcpy` vía USB con latencia cero).*
* **Lado Derecho (Panel Administrador / Torre de Control):** Muestra el pulso concurrente del sistema. Cuando alguien en el aula solicita una materia desde su celular con el QR, el proyector muestra instantáneamente cómo sube el contador de *Créditos en Escrow* y aparece la línea en el Feed transaccional. Demuestra consistencia, auditoría y que el sistema está 100% vivo.

---

## 4. Guion Recomendado para la Demo de Lerna (Distribución 30 Minutos)

```
[00:00 - 05:00]  BLOQUE 1: Storytelling & Contexto (5 min)
                 • 7 viñetas visuales (Lucía y Mateo).
                 • Dolor real: barrera económica, 1 hora = 1 crédito, custodia de créditos.

[05:00 - 22:00]  BLOQUE 2: Demo en Vivo Coordinada (17 min)
                 • Min 05: [QR INTERACTIVO] Proyección de QR. La clase escanea, se asigna alias/selfie,
                   recibe 3 créditos y su materia FIUBA para enseñar.
                 • Min 07: [MOMENTO IA 1 - Moderación] Intento de publicación de curso prohibido
                   (ej: "Hackeo de exámenes FIUBA"). La IA rechaza en vivo con la política infringida.
                 • Min 09: [MOMENTO IA 2 - Estimador de Créditos] Publicación de curso legítimo de Piano.
                   La IA analiza temario, duración y nivel técnico, sugiriendo la tasa justa de créditos.
                 • Min 11: [MATCH DE LA CLASE] Los alumnos en el aula se solicitan clases entre sí;
                   notificaciones en tiempo real y bloqueo atómico de créditos en Escrow.
                 • Min 14: [CICLO COMPLETO EN ESCENARIO] Mateo solicita la clase a Lucía; Lucía acepta
                   y se genera el enlace de la sesión.
                 • Min 17: Confirmación de clase dictada y liberación atómica de créditos a Lucía.
                 • Min 19: [MÁQUINA DEL TIEMPO / FAST-FORWARD] Clic en "Avanzar 7 días": se completan
                   las clases del público, se liberan créditos y aparecen reviews hilarantes en sus teléfonos.
                 • Min 21: Vista del Panel de Auditoría / Admin con el log transaccional y bloqueos.

[22:00 - 30:00]  BLOQUE 3: Cierre & Preguntas de la Cátedra (8 min)
                 • Responder con seguridad basándose en la WBS, la arquitectura FastAPI/SQLModel
                   y las decisiones registradas en `contexto/decisiones.md`.
```

---

## 5. Estrategia de Infraestructura y Red (Render vs Túnel Cloudflare)

Para garantizar que los ~30 alumnos concurrentes no saturen el servidor ni sufran demoras:

### Plan A: Render Cloud (Backend en la nube)
* **Precaución 1 (Cold Start):** En el plan gratuito, Render hiberna tras 15 minutos sin visitas. Despertar el contenedor 10 minutos antes de la exposición para evitar esperas de 60-90 segundos al escanear el QR.
* **Precaución 2 (Cadencia de Polling):** Configurar el polling de notificaciones de los móviles del público a **5-6 segundos** (o solo por acción), reservando el polling rápido (cada 2 segundos) exclusivamente para la pantalla del Administrador en la laptop.
* **Base de datos:** Utilizar PostgreSQL (Render Postgres o Supabase) para soportar escrituras concurrentes sin riesgo de bloqueos de archivo.

### Plan B: Túnel Local Cloudflare / Ngrok (Máxima potencia y blindaje total)
Si el Wi-Fi de la facultad o el plan gratuito de Render presentan latencia:
* **Ejecución local:** Correr el backend en la propia laptop (`uvicorn app.main:app --port 8000`).
* **Comando del túnel (gratuito, sin registro y con SSL automático):**
  ```bash
  cloudflared tunnel --url http://localhost:8000
  ```
* **Ventajas clave:**
  1. **Independiente de la red local:** Los alumnos se conectan desde sus teléfonos usando **sus propios datos móviles 4G/5G**; no necesitan estar en el Wi-Fi de la notebook ni compartir contraseñas.
  2. **Rendimiento nativo:** Utiliza el 100% de la CPU y memoria RAM de la laptop (sin límites de 512MB ni 0.1 CPU).
  3. **Cero Cold Starts:** Respuesta instantánea garantizada al escanear el QR.

---

## 6. Checklist Técnico Previo a la Defensa
- [ ] Backend FastAPI verificado:
  - [ ] **Opción Nube:** Despierto y caliente en Render con PostgreSQL.
  - [ ] **Opción Túnel (Plan B listo):** Binario `cloudflared` descargado y probado (`cloudflared tunnel --url http://localhost:8000`).
- [ ] Frontend desplegado accesible por URL pública (Vercel/Netlify/Render).
- [ ] Base de datos poblada con el seeder mock (`seed_mock.py`): catálogo con materias FIUBA, fotos y valoraciones.
- [ ] Endpoint / flujo de Onboarding Express por QR probado (`/demo/join` con pool rotativo de materias FIUBA y selfie opcional).
- [ ] Código QR generado que apunte directamente a la URL del onboarding express de demo.
- [ ] 2 computadoras o 2 teléfonos listos y logueados con las cuentas de demo (Mateo y Lucía).
- [ ] Hub de diapositivas abierto en pestaña secundaria: `proyecto-wbs/docs/Entrega/presentacion.html`.
- [ ] Endpoint / servicio de IA verificado:
  - [ ] Prompt/regla de moderación con respuesta inmediata para el curso prohibido de prueba.
  - [ ] Estimador de créditos respondiendo con cálculo sugerido según duración y dificultad.
