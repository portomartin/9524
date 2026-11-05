# Notas de la Reunión / Clase (05/11/2026) - TP Proyecto WBS

---

## 📌 Hoja 1: Planificación de Entrega, Demo y Retrospectiva (Fecha: 05/11/26)

### Pre-entrega / Tareas previas
- **Borrar branches** que ya no se usen (limpieza del repo Git).
- **Estructura de la presentación:** Demo + Retrospectiva.

### Fechas y Dinámica de Exámenes / Finales
- **Presentar Demo**.
- **Fechas de Finales:** Diciembre y Febrero.
- **Entregables:**
  - Presentación en **PPT / Diapositivas**.
  - **Ale va a hacer preguntas** durante la defensa.
  - Incluir el **listado completo de entregables**.

### Retrospectiva (Duración: 15 minutos)
- **Listar aprendizajes** del equipo durante el proyecto.
- Utilizar los **templates de la clase de Ale** (dinámica tipo *Barquito* / Sailboat, etc.).

---

## 📌 Hoja 2: Pautas para la Demo del Frontend y Casos de Prueba

### Preparación de la Demo
- **Dinámica de Retro:** Ej: Barquito (Sailboat), etc.
- **Datos reales para las demos:** No usar datos genéricos tipo "asdf", sino casos verosímiles de cursos y habilidades.
- **Demostración en vivo:** **Llevar dos computadoras** para mostrar la interacción en tiempo real entre **dos perfiles distintos** (Docente y Alumno).

### Casos de prueba a mostrar
- **Usuario que compró la clase con anticipación** / Cancelación (explicación y crear este escenario/replay).
- **Regla de cancelación:** ¿Qué ocurre si la clase se cancela o cuando ya pasó?
- **Criterio:** Usar el criterio prudente de cada uno.
- **Filtros en frontend:** Filtro para clases cobradas / completadas.

---

## 📌 Hoja 3: Reglas de Negocio, Estados y Carga en Jira

### Gestión en Jira
- **Ingresar como issues en Jira** (cargar los tickets correspondientes a estos ajustes).
- **Al menos agregarle la unidad** (definir claramente la unidad de medida: créditos, horas, etc.).

### Estados de las Solicitudes y Sesiones
- **Que se entiendan con claridad los 4 estados**, incluyendo explícitamente el estado **"Cancelado"**:
  1. *Pendiente*
  2. *Aceptada / Confirmada*
  3. *Completada*
  4. *Cancelada*
- Contemplar el caso de **cancelación de clases desde ambos lados** (tanto el alumno como el docente pueden cancelar).

### Lógica de Créditos Virtuales
- **Retención / Reserva de créditos:** Los créditos quedan como en un **"freeze" (congelados / en custodia)**, similar a un **plazo fijo**, mientras la sesión está pactada y pendiente de realización.
- Definir qué puede pedir o recuperar el comprador si la sesión se cancela o no se concreta.
