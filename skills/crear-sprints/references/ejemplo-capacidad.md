# Ejemplo: seis integrantes

Escenario acordado como simulación, no como regla para otros equipos:

| Parámetro | Valor | Naturaleza |
|---|---:|---|
| Integrantes | 6 | Dato del usuario |
| Dedicación por persona | 15 h por semana | Supuesto del usuario |
| Duración del sprint | 1 semana | Dato del usuario |
| Reserva | 25 % | Supuesto de planificación |
| Velocidad inicial | 20 puntos por sprint | Hipótesis aceptada, aún no observada |

- Horas brutas: `6 × 15 × 1 = 90 h`.
- Reserva: `90 × 0,25 = 22,5 h`.
- Horas planificables: `90 − 22,5 = 67,5 h`.
- Se adoptaron **65 h** como redondeo conservador; no confundirlo con el resultado exacto.
- Los **20 puntos** son independientes del cálculo horario. No dividir 65 entre 20 para obtener una equivalencia de estimación.

La propuesta de estimación realizada en la conversación sumó **114 puntos en 20 HU**. Releer las historias actuales antes de reutilizar ese total; no es una estimación permanente del proyecto.

A 20 puntos por sprint, `techo(114 / 20) = 6` es la referencia aritmética. Cuatro sprints representan 80 puntos hipotéticos y dejan una brecha de 34 puntos. Esto no prueba que las dependencias y las historias indivisibles puedan acomodarse exactamente en seis sprints.

Si cambian a ocho integrantes o veinte horas semanales, recalcular horas. La velocidad sigue siendo una hipótesis hasta validarla; no aumentarla por regla de tres.

Si los primeros tres sprints comparables terminan 13, 18 y 16 puntos, el promedio observado es `47 / 3 = 15,67`, con un rango de 13–18. Usar esa evidencia para revisar el compromiso siguiente, considerando su disponibilidad y riesgos.
