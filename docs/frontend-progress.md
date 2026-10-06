# Progreso del frontend MVP 9524

Este registro es un índice operativo. El código y el backlog vigente son la evidencia definitiva. El skill `implementar-frontend-mvp` debe reconciliar esta tabla con ambos antes de continuar.

| Subtarea | Alcance | Estado | Evidencia |
|---|---|---|---|
| 1.1.4 | Explorar contenido público | Completada | Listados y detalles públicos con Router, PrimeVue y adaptador mock; build correcto. |
| 1.2.4 | Mostrar confianza pública | Completada | Ranking con reputación, contenido reciente y agendas públicas sin datos privados. |
| 1.3.2 | Convertir acción protegida en registro | Completada | Solicitar sesión redirige a acceso y conserva la ruta de retorno. |
| 1.4.2 | Gestionar acceso autenticado | Completada | Login, registro, logout, persistencia mock y guards de rutas/roles. |
| 2.1.2 | Editar perfil | Completada | Edición parcial de perfil, temas ofrecidos/buscados y datos públicos separados. |
| 2.2.2 | Crear y publicar propuesta | Completada | Alta, borrador, edición, publicación y acceso a vista pública. |
| 2.3.2 | Crear y mantener aprendizaje buscado | Completada | Alta, edición, pausa/reactivación y eliminación lógica local. |
| 3.1.2 | Crear buscador público | Completada | Búsqueda pública diferenciada, paginación y estado vacío. |
| 3.2.2 | Gestionar filtros combinables | Completada | Tipo, categoría, nivel y modalidad combinables, limpiables y conservados al paginar. |
| 3.3.2 | Explicar compatibilidades | Completada | Coincidencias explicadas, porcentaje orientativo, reciprocidad y acción de solicitud. |
| 4.1.3 | Crear agenda y carga asistida | Completada | Franjas concretas simples y múltiples, duración y eliminación, sin recurrencia persistida. |
| 4.2.3 | Publicar y consultar agenda | Completada | Visibilidad propia, mensajes de privacidad y consulta pública de franjas libres. |
| 4.3.3 | Crear solicitud y resumen | Completada | Diálogo de resumen con fecha, hora, duración, modalidad, intercambio y confirmación. |
| 4.4.5 | Gestionar acciones de sesión | Completada | Estados y transiciones, cancelación, feedback y acceso restringido. |
| 4.5.2 | Completar sesión y habilitar acciones posteriores | Completada | Finalización desde EN_CURSO y habilitación de créditos, historial y calificación. |
| 5.1.3 | Mostrar créditos y resultado | Completada | Saldo, costo, transferencia mock y movimientos sin tratarlos como dinero. |
| 5.2.2 | Crear historial de actividad | Completada | Historial paginado y filtrable de sesiones, créditos, propuestas y aprendizajes. |
| 5.3.3 | Calificar y consultar reputación | Completada | Calificación única posterior, comentario opcional y reputación pública. |
| 6.1.2 | Crear flujo de denuncia | Completada | Denuncias de propuestas y usuarios con motivos, advertencia y confirmación. |
| 6.2.4 | Crear panel administrativo | Completada | Guard ADMIN, filtros, denuncias, revisión humana, suspensión/reactivación y ocultamiento confirmado. |

## Decisiones vigentes

- La UI usa PrimeVue, Aura, PrimeIcons y PrimeFlex.
- La integración utiliza adaptadores mock intercambiables por HTTP.
- Los listados públicos se ordenan por fecha descendente.
- El detalle público muestra título, descripción, categoría, nivel, modalidad, duración y nombre público del autor.
- No se agregan tests automatizados por ahora.
- Las rutas se cargan de forma diferida para no enviar el espacio privado o administrativo durante la exploración pública.

