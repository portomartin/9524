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

1. **Idea de Alto Impacto: Código QR + Onboarding Express con Materias FIUBA y Selfie:**
   * Proyectar un QR al inicio de la demo para que la cátedra y compañeros escaneen con sus celulares.
   * **Entrada sin fricción (1 clic):** Se les asigna un alias simpático (*"Ingeniero Curioso #14"*, *"Estudiante Paseo Colón"*), avatar por defecto con opción de **sacarse una selfie rápida** con la cámara, **3 créditos de bienvenida**, **1 materia para enseñar** y **1 materia que desea aprender** encadenada con otro alumno del aula.
   * **Sugerencia Proactiva de Match:** En lugar de buscar a ciegas, la app le muestra: *"🎯 ¡Encontramos a tu profesor ideal! [Compañero] te puede enseñar [Materia Deseada]. Tocá acá para pedirle turno con tus créditos de regalo"*.
   * **Agenda Express ("Turno Disponible Ahora"):** Para no enredar a la clase con calendarios complejos, las materias nacen con turno inmediato a un clic.
   * **El público juega al Match:** Al tocar la sugerencia, la solicitud viaja en el acto, los créditos quedan en Escrow y el compañero sentado al lado recibe la notificación en vivo en su teléfono.
2. **Puesta en Escena en Proyector: Split-Screen (Celular en Vivo + Panel Admin):**
   * El proyector se divide en dos:
     - **Lado izquierdo (Móvil del presentador):** Muestra el recorrido del usuario, la interfaz táctil, las selfies y los momentos de IA (moderación y estimación).
     - **Lado derecho (Panel Administrador / Torre de Control):** Muestra en vivo los contadores de usuarios activos del QR, créditos retenidos en Escrow y el feed de auditoría en tiempo real.
   * Cuando un compañero en el aula solicita una materia desde su celular, la cátedra ve al instante cómo impacta en el panel general: demuestra que el sistema está 100% vivo y distribuido.
   * Mientras tanto, los presentadores (**Mateo y Lucía**) ejecutan en el celular el **ciclo transaccional completo**: solicitud pactada, confirmación de clase dictada, liberación automática de créditos a Lucía y calificación mutua 5 estrellas.
3. **Seeding Robusto (Efecto MediTrace vs GameMatch):**
   * Que el catálogo no arranque vacío ni con datos genéricos: materias de la facultad, descripciones creíbles y valoraciones previas para dar sensación de producto maduro.
4. **Demostración de Inteligencia Artificial Aplicada (Efecto Diferenciador Tecnológico):**
   * **Filtro ético y moderación de contenido en tiempo real:** Intento de publicar una clase prohibida (ej. vulneración de exámenes o contenido ilícito/no académico). La IA la rechaza en el acto exponiendo la política infringida.
   * **Estimador inteligente de créditos:** Al redactar la propuesta legítima de piano, la IA evalúa complejidad, nivel y duración para sugerir el valor justo en créditos.
5. **El Clímax Divertido: "Efecto Máquina del Tiempo / Fast-Forward 7 días (Backend-Driven)":**
   * En vez de una animación artificial solo en el proyector, el avance se orquesta con el backend llamando a `POST /demo/fast-forward-step` cada 2 segundos.
   * **Mutación real paso a paso:** Cada 2 segundos el backend completa o cancela una sesión, transfiere créditos y guarda una **reseña cómica con folclore de FIUBA** en la base de datos.
   * **Reacción en cadena en el aula:** En el proyector van cayendo las tarjetas al feed y, en paralelo, a cada compañero le suena la notificación en su propio teléfono en vivo.
   * Reviews memorables (ej.: *"Explicó autovalores con analogías de milanesas, aprobé con 10"*, *"El mate virtual estaba frío pero el código compiló"*) y cancelaciones cómicas (*"Me dormí en el 152 llegando a Paseo Colón"*).
   * Genera 20 segundos de clímax, risas y aplausos que dejan la demo en el punto más alto antes de las preguntas.
6. **Guion Cerrado de 20 minutos (Distribución para el Coloquio):**
   * 4-5 min: Introducción con las 7 viñetas del Storytelling.
   * 16-17 min: Demo en vivo (QR interactivo $\to$ IA Moderación $\to$ IA Estimador $\to$ Match en el aula $\to$ Ciclo completo Mateo/Lucía $\to$ Fast-Forward con reviews graciosas $\to$ Auditoría Admin).
   * 8-10 min: Preguntas de la cátedra. Cero improvisación.
