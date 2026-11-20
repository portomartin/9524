# 📌 Resumen Completo y Estratégico: Coloquio / Demos de la Cátedra (FIUBA TC017)

Buenas chicos, les paso en limpio un desglose detallado de lo que se vio en las presentaciones de ayer. Nos sirve un montón para entender **qué premia la cátedra, qué errores no cometer y cómo armar nuestra propia puesta en escena para Lerna**.

---

## ⏱️ 1. Dinámica, Tiempos y Evaluación de la Cátedra
* **Tiempo estricto:** **30 minutos por grupo** en total.
* **Estructura fija observada:**
  1. **Storytelling inicial:** Todos arrancaron con una secuencia narrativa de **6 a 7 imágenes/viñetas** (exactamente como tenemos planteado el nuestro) para contextualizar el problema real y la propuesta de valor.
  2. **Demo en vivo:** Foco absoluto en la interacción entre usuarios y estados.
  3. **Ronda de preguntas:** Al final de los 30 min, **3 a 4 preguntas en total**. Alejandro hizo unas 3 preguntas genéricas conceptuales por grupo; Mauro y Pilar intervinieron puntualmente, más alguna consulta aislada de alumnos. Alejandro quedó muy satisfecho con el nivel general.

---

## 🔍 2. Análisis Caso por Caso: Aciertos y Errores de las Demos

### 🥇 1. La app del Bar / Pagar la cuenta (Nivel 10/10 – La mejor de la fecha)
* **Concepto:** División y pago colectivo de la cuenta de un bar entre comensales.
* **Aspecto visual y técnico:** Frontend web (React) con pantalla ultra limpia, animaciones fluidas, transiciones sin parpadeos y objetivo de negocio clarísimo.
* **El gran acierto de la demo (Efecto WOW):**
  * **Proyectaron un código QR en pantalla** para que los alumnos y docentes de la clase se conectaran con sus propios celulares en tiempo real.
  * La clase empezó a hacer pedidos y pagar juntos en vivo. Fue participativa, dinámica y generó impacto inmediato.

### 🥈 2. Barrio Ahorro (Nivel 9/10 – Excelente puesta en escena)
* **Concepto:** Geolocalización de ofertas y descuentos en comercios de cercanía.
* **Aspecto visual:** Muy mobile, diseño prolijo.
* **El gran acierto de la demo:**
  * **Puesta en escena coordinada entre 4 integrantes con sus smartphones en simultáneo**, proyectando la pantalla:
    1. *Integrante A:* publicaba una oferta como comerciante.
    2. *Integrante B:* la encontraba y la compraba en vivo.
    3. *Integrante C:* dejaba la calificación/reseña.
    4. *Integrante D (o PC proyector):* mostraba en tiempo real el impacto en el panel administrativo.
  * Cero improvisación: flujo ensayado de punta a punta.

### 🥉 3. MediTrace (Nivel 9/10 – Muy sólida pero con detalle en la demo)
* **Concepto:** Gestión y recordatorio de medicación para personas polimedicadas.
* **Puntos fuertes:** Panel administrativo impecable, carga de datos inicial muy consistente (simularon el historial médico de un paciente tras 1 año de tratamiento) y mostraron el rol del familiar/cuidador.
* **Oportunidad de mejora:**
  * En vivo intentaron agregar registros de forma aleatoria y se sintió algo improvisado (*"a ver, ahora podemos hacer esto..."*). Si bien funcionó, perdió la fluidez de un guion cerrado.

### ⚠️ 4. GameMatch (Nivel 7-8/10 – La más floja)
* **Concepto:** Búsqueda y reserva de juegos de mesa en bares.
* **Qué falló:**
  * Aunque era colorida y con buena idea de fondo, el **mock de la base de datos no fue bueno**: había datos cargados pero sin coherencia que reflejara actividad real de usuarios.
  * El flujo entre usuarios se sintió confuso y poco representativo de una interacción real.

---

## 🎯 3. Plan de Acción y Propuesta para Lerna (Puntos Clave para Ganar)

Con lo visto ayer, tenemos todo para que nuestra presentación sea de las mejores si aplicamos estas ideas:

1. **Idea de Alto Impacto: Código QR para la Clase / Docentes**
   * Podemos proyectar un QR al inicio de la demo para que Alejandro, Mauro, Pilar o los compañeros escaneen e ingresen al catálogo desplegado.
   * Con solo darles 1 crédito de bienvenida, pueden buscar una materia, ver nuestras publicaciones o solicitar un intercambio en vivo mientras nosotros mostramos la pantalla docente/admin. Es fácil de orquestar y suma muchísimo puntaje.
2. **Demo a Dos / Tres Pantallas Coordinadas (Efecto Barrio Ahorro):**
   * Una pantalla/celular para **Mateo** (busca clase de piano, solicita y se le congelan los créditos en escrow).
   * Otra pantalla para **Lucía** (recibe la notificación, acepta la sesión, genera el link de Meet y confirma la clase).
   * Liberación de créditos en vivo y calificación de 5 estrellas con actualización instantánea de la reputación.
3. **Seeding Robusto (Efecto MediTrace vs GameMatch):**
   * Que el catálogo no arranque vacío ni con "datos de prueba genéricos". Nuestro dataset con perfiles, materias reales, valoraciones previas y fotos de portadas le da apariencia de producto terminado y en producción.
4. **Guion Cerrado de 20 minutos:**
   * 4 min: Introducción con las 7 viñetas del Storytelling.
   * 16 min: Demo en vivo (flujo alumno $\to$ profesor $\to$ escrow $\to$ calificación $\to$ panel admin).
   * 10 min: Preguntas de la cátedra. Cero improvisación.
