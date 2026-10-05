# Trazabilidad de planificación — MVP V3

**Fecha de revisión:** 2026-10-05  
**Fuente de verdad:** [`mvp-v3.md`](mvp-v3.md)  
**Artefactos reconciliados:** [`wbs.md`](wbs.md) y [`backlog.md`](backlog.md)  
**Estado:** registro histórico de la reconciliación anterior. La planificación actual valida cobertura durante la derivación y no requiere mantener esta matriz. Este documento no reemplaza al MVP.

## Criterio de alineación

La WBS y el backlog se derivaron inicialmente de forma independiente desde el MVP V3. Esta matriz los relaciona después de la derivación para comprobar cobertura en ambos sentidos. La relación no es necesariamente uno a uno: una historia puede cubrir varios paquetes WBS y un paquete puede requerir varias historias.

## Matriz WBS → backlog → MVP

| Paquetes WBS | Épica / HU relacionada | Secciones del MVP V3 | Cobertura |
|---|---|---|---|
| 1.1.1–1.1.2 | [1.0.0] / [1.1.0] | 2; 4.1 | Completa |
| 1.1.3–1.1.4 | [1.0.0] / [1.2.0] | 2; 4.1; 4.7 | Completa; reglas exactas de ranking y trending pendientes |
| 1.1.5 | [4.0.0] / [4.2.0] | 2; 4.1; 4.3 | Completa |
| 1.2.1, 1.2.4 | [1.0.0] / [1.3.0] | 2; 3; 4.2 | Completa; campos mínimos pendientes |
| 1.2.2–1.2.3 | [1.0.0] / [1.4.0] | 5 | Completa |
| 2.1.1–2.1.5 | [2.0.0] / [2.1.0] | 4.2; 5 | Completa; campos y visibilidad pendientes |
| 2.2.1–2.2.2, 2.2.4 | [2.0.0] / [2.2.0] | 4.4; 5 | Completa |
| 2.2.3 | [2.0.0] / [2.3.0] | 4.2; 4.4 | Completa |
| 3.1.1 | [3.0.0] / [3.1.0] | 4.1; 4.4 | Completa |
| 3.1.2–3.1.3 | [3.0.0] / [3.2.0] | 4.4 | Completa; filtros mínimos pendientes |
| 3.2.1–3.2.4 | [3.0.0] / [3.3.0] | 4.4 | Completa; ponderación y umbral pendientes |
| 4.1.1–4.1.2, 4.1.4 | [4.0.0] / [4.1.0] | 4.3; 9 | Completa; zona horaria pendiente |
| 4.1.3 | [4.0.0] / [4.2.0] | 4.3; 9 | Completa |
| 4.1.5 | [4.0.0] / [4.2.0], [4.4.0] | 4.3; 4.5; 9 | Completa |
| 4.2.1–4.2.2 | [4.0.0] / [4.3.0] | 4.5 | Completa |
| 4.2.3–4.2.5 | [4.0.0] / [4.4.0] | 4.5 | Completa; rechazo y cancelación pendientes |
| 4.2.6 | [4.0.0] / [4.5.0] | 4.5 | Completa; confirmación de finalización pendiente |
| 5.1.1 | [2.0.0] / [2.2.0]; [5.0.0] / [5.1.0] | 4.6 | Completa; valor pendiente |
| 5.1.2–5.1.4 | [5.0.0] / [5.1.0] | 4.6 | Completa; saldo inicial pendiente |
| 5.2.1 | [5.0.0] / [5.2.0] | 5 | Completa |
| 5.2.2–5.2.3 | [5.0.0] / [5.3.0] | 4.7 | Completa |
| 5.2.4 | [1.0.0] / [1.2.0]; [5.0.0] / [5.3.0] | 2; 4.1; 4.7 | Completa |
| 6.1.1–6.1.2 | [6.0.0] / [6.1.0] | 5; 6 | Completa |
| 6.1.3, 6.2.1–6.2.3 | [6.0.0] / [6.2.0] | 5; 6 | Completa; permisos y auditoría pendientes |

## Control inverso del backlog

| Épica | HU incluidas | Bloques WBS cubiertos | Estado |
|---|---|---|---|
| [1.0.0] Descubrimiento y acceso público | [1.1.0]–[1.4.0] | 1.1; 1.2; 5.2.4 | Cubierta |
| [2.0.0] Perfil, propuestas y necesidades | [2.1.0]–[2.3.0] | 2.1; 2.2; 5.1.1 | Cubierta |
| [3.0.0] Búsqueda y compatibilidad | [3.1.0]–[3.3.0] | 3.1; 3.2 | Cubierta |
| [4.0.0] Agenda y sesiones | [4.1.0]–[4.5.0] | 1.1.5; 4.1; 4.2 | Cubierta |
| [5.0.0] Créditos, historial y reputación | [5.1.0]–[5.3.0] | 5.1; 5.2 | Cubierta |
| [6.0.0] Seguridad y administración | [6.1.0]–[6.2.0] | 6.1; 6.2 | Cubierta |

## Brechas y observaciones

- No hay paquetes WBS del MVP sin cobertura en el backlog.
- No hay historias del backlog sin correspondencia en la WBS.
- No se detectaron funcionalidades fuera del MVP incorporadas como historias aprobadas.
- Los refinamientos de borradores, pausas, paginación, saldos negativos e idempotencia se mantienen como detalles de implementación o calidad; no amplían el objetivo funcional del MVP.
- Las reglas todavía abiertas permanecen documentadas dentro de sus HU y deben resolverse antes de comprometer la implementación afectada.
- La WBS conserva granularidad de entregable y el backlog conserva granularidad de valor ejecutable; no se fuerza una equivalencia uno a uno.

## Decisiones pendientes con impacto de planificación

- Definir campos públicos y mínimos de registro, perfil y propuestas.
- Definir ranking, trending, filtros iniciales y criterios de compatibilidad.
- Definir zona horaria, conflictos, duración y reserva de disponibilidades.
- Definir confirmación de finalización y tratamiento de desacuerdos.
- Definir saldo inicial, valor y reglas operativas de créditos.
- Definir permisos administrativos, auditoría y reglas de denuncia.

Estas decisiones no modifican automáticamente `mvp-v3.md`, la WBS ni el backlog. Si una decisión cambia alcance o reglas de negocio, debe aprobarse y reflejarse primero en la especificación activa.
