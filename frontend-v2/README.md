# Frontend V1 — Plataforma de Intercambio de Aprendizajes

Implementación completa y desacoplada del frontend de la plataforma, desarrollada íntegramente desde cero respetando la especificación activa **MVP V3** ([`proyecto-sdd/mvp-v3.md`](../proyecto-sdd/mvp-v3.md)) y sus criterios de aceptación técnicos ([`proyecto-sdd/subtareas.md`](../proyecto-sdd/subtareas.md)).

---

## 1. Stack Tecnológico

* **Framework:** Vue 3 (Composition API, `<script setup>`).
* **Estilos & UI:** Tailwind CSS v4 con `@tailwindcss/vite` y sistema de componentes Shadcn-vue.
* **Iconografía:** Lucide Icons (`@lucide/vue`).
* **Utilidades de clases:** `clsx`, `tailwind-merge` y `class-variance-authority` (`cva`).
* **Estado:** Pinia (`authStore`, `platformStore`).
* **Enrutamiento:** Vue Router con Navigation Guards (`GUEST`, `USER`, `ADMIN`).
* **Bundler:** Vite 5.
* **Tipografía:** Plus Jakarta Sans.

---

## 2. Cobertura Integral de Subtareas del Backlog

| Subtarea | Alcance Técnico | Implementación en `frontend-v1` |
|---|---|---|
| **[1.1.4]** | Explorar contenido público | Navegación pública, tabs de propuestas para aprender y aprendizajes buscados, cards detalladas y estados de carga/vacío/error en [`ExploreView.vue`](src/views/ExploreView.vue). No requiere login. |
| **[1.2.4]** | Mostrar confianza pública | Rankings comunitarios por reputación, tópicos en tendencia y actividad reciente sin filtrar datos privados en [`TrustView.vue`](src/views/TrustView.vue). |
| **[1.3.2]** | Convertir acción protegida en registro | Al intentar solicitar una sesión o denunciar sin sesión, redirige a [`AuthView.vue`](src/views/AuthView.vue) conservando la ruta de retorno (`?redirect=...`). Registro breve con 3 campos. |
| **[1.4.2]** | Gestionar sesión y rutas protegidas | Login, registro, logout, persistencia reactiva en `localStorage` y guards para rutas de usuario y administrador en [`router/index.js`](src/router/index.js) y [`authStore.js`](src/stores/authStore.js). |
| **[2.1.2]** | Editar perfil | Edición de temas ofrecidos para enseñar, temas buscados para aprender, biografía, nivel, modalidad y visibilidad de agenda en [`WorkspaceView.vue`](src/views/WorkspaceView.vue). |
| **[2.2.2]** | Crear y publicar propuesta | Alta, borrador, edición, publicación y eliminación de propuestas de enseñanza con validación y estados. |
| **[2.3.2]** | Crear y mantener aprendizaje buscado | Alta, edición, pausa, reactivación y eliminación lógica de necesidades de aprendizaje. |
| **[3.1.2]** | Crear buscador público | Búsqueda diferenciada por término sobre ofertas y pedidos de aprendizaje, con estados vacíos sugerentes en [`SearchView.vue`](src/views/SearchView.vue). |
| **[3.2.2]** | Gestionar filtros combinables | Filtros de tipo, categoría, nivel y modalidad combinables y limpiables con un clic en [`SearchView.vue`](src/views/SearchView.vue). |
| **[3.3.2]** | Explicar compatibilidades | Motor de compatibilidad en [`mockStorage.js`](src/services/mockStorage.js) que explica afinidad temática, modalidad, porcentaje orientativo y badge de **¡Reciprocidad Directa!** con CTA de solicitud directa. |
| **[4.1.3]** | Crear agenda y carga asistida | Franjas concretas por fecha y hora (mínimo 1 hora). Asistente modal para generar múltiples franjas por rango de fechas sin persistir recurrencias. |
| **[4.2.3]** | Publicar y consultar agenda | Toggle de visibilidad pública de agenda. Consulta pública en [`PublicAvailabilityView.vue`](src/views/PublicAvailabilityView.vue) que expone **únicamente franjas libres**, protegiendo la privacidad. |
| **[4.3.3]** | Crear solicitud y resumen | Diálogo modal en [`OfferDetailView.vue`](src/views/OfferDetailView.vue) con fecha, hora, duración (60 min), modalidad, intercambio (1 crédito o reciprocidad) y confirmación. |
| **[4.4.5]** | Gestionar acciones de sesión | Ciclo de vida completo: `SOLICITADA` → `CONFIRMADA` → `EN_CURSO` → `FINALIZADA` / `CANCELADA`, con cancelación justificada y liberación de franja horaria. |
| **[4.5.2]** | Completar sesión y habilitar acciones posteriores | Finalización desde `EN_CURSO`, liquidación automática de créditos, registro en el libro contable y habilitación de calificación única. |
| **[5.1.3]** | Mostrar créditos y resultado | Saldo de créditos internos en navbar y panel. Libro de movimientos con créditos de bienvenida (+3), dictado (+1) y aprendizaje (-1). **Enfatiza que no son dinero**. |
| **[5.2.2]** | Crear historial de actividad | Historial unificado de sesiones y movimientos de créditos en la pestaña correspondiente de [`WorkspaceView.vue`](src/views/WorkspaceView.vue). |
| **[5.3.3]** | Calificar y consultar reputación | Calificación posterior de 1 a 5 estrellas con comentario opcional, única por sesión, recalculando el promedio de reputación del usuario evaluado. |
| **[6.1.2]** | Crear flujo de denuncia | Diálogo de reporte para propuestas y usuarios con motivo, detalles, advertencia y confirmación. |
| **[6.2.4]** | Crear panel administrativo | Panel protegido con guard `ADMIN` en [`AdminView.vue`](src/views/AdminView.vue) para supervisar reportes con revisión humana, suspender/reactivar usuarios y ocultar propuestas. |

---

## 3. Principios de Dominio Reflejados

1. **Rol único `USER`:** Tanto quien enseña como quien aprende tienen el mismo rol técnico. Una persona puede publicar propuestas de enseñanza y aprendizajes buscados en simultáneo.
2. **Créditos internos:** 1 crédito equivale a 1 hora de sesión de aprendizaje. No son dinero, no tienen precio en moneda de curso legal ni pueden cambiarse por dinero.
3. **Agenda por franjas concretas:** No existe recurrencia persistida en base de datos. Las disponibilidades son franjas puntuales de 1 hora.
4. **Separación pública / privada:** Las agendas públicas sólo listan franjas desocupadas.

---

## 4. Instrucciones de Ejecución

Desde la carpeta `frontend-v1`:

```bash
# Instalar dependencias (ya instaladas)
npm install

# Servidor de desarrollo
npm run dev

# Compilar para producción
npm run build

# Previsualizar el build
npm run preview
```

---

## 5. Cuentas de Prueba Preconfiguradas (Demo Switcher)

La barra superior incluye un selector rápido de identidades para probar todos los flujos sin cerrar sesión manualmente:

* **GUEST:** Navegación anónima pública de solo lectura.
* **Juan Carlos Pérez (`usr-1`):** Desarrollador Vue, saldo de 4 créditos, 4.9 estrellas.
* **Elena Rostova (`usr-2`):** Instructora de inglés IT, saldo de 6 créditos, 4.8 estrellas.
* **Carlos Mendoza (`usr-3`):** Especialista DevOps, saldo de 2 créditos, 4.6 estrellas.
* **Laura Moderadora (`usr-admin`):** Administradora con acceso al panel de control `/admin`.
