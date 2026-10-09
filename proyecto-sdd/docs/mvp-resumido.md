# MVP resumido

> Artefacto derivado de `proyecto-sdd/mvp-v3.md`. Este documento sirve como vista rápida y no es fuente de verdad.

## Idea central

La plataforma facilita que una persona encuentre a otra para aprender algo que sabe enseñar. El valor principal está en hacer posible ese intercambio sin que el dinero sea un requisito.

Una misma persona puede enseñar, aprender o hacer ambas cosas según la actividad.

## Flujo principal

```text
descubrir → ofrecer o buscar → encontrar compatibilidad → crear una sesión
→ acordar y coordinar → realizar → finalizar → calificar
```

La plataforma acerca a las personas, facilita la coordinación y registra el resultado. No reemplaza la relación ni la experiencia de aprendizaje entre los participantes.

## Roles

- **`GUEST`:** explora propuestas, reputaciones, rankings, tendencias y agendas públicas en modo solo lectura.
- **`USER`:** publica lo que puede enseñar, indica lo que desea aprender, encuentra compatibilidades, coordina sesiones y califica.
- **`ADMIN`:** realiza tareas mínimas de protección, revisión y administración.

El registro se solicita cuando la persona necesita realizar una acción protegida, no para explorar inicialmente.

## Sesión: entidad central

La Sesión conecta a quien aprende con quien enseña. La solicitud no es el objetivo separado: es el estado inicial de una Sesión.

Estados principales:

`SOLICITADA → CONFIRMADA → EN_CURSO → FINALIZADA`

Una Sesión también puede pasar a `CANCELADA` cuando no se realizará o se cancela antes de finalizar.

## Principios del producto

- El aprendizaje y la enseñanza son el centro de la experiencia.
- El camino hacia una sesión debe ser rápido, claro e intuitivo.
- No se requiere dinero: los créditos son internos de la plataforma.
- El registro y la administración deben facilitar el intercambio, no desplazarlo.
- La confianza se construye con historial y calificación mutua después de la sesión.
- Las agendas usan disponibilidades explícitas por fecha y hora, sin recurrencia persistida.

## Regla de mantenimiento

Si este resumen contradice a `proyecto-sdd/mvp-v3.md`, prevalece siempre `proyecto-sdd/mvp-v3.md`. El resumen debe regenerarse cada vez que cambie la especificación vigente.
