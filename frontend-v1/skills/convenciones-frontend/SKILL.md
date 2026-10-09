---
name: convenciones-frontend
description: Definir y aplicar convenciones de implementación frontend para el MVP usando Vue y una librería de componentes, sin crear estilos visuales propios.
---

# Convenciones y validación de frontend

Aplicar este skill en todas las subtareas de Frontend del proyecto Plataforma de intercambio de aprendizajes. También usarlo como checklist para revisar una pantalla, componente o flujo existente.

## Stack y componentes

- Usar Vue como framework de frontend.
- Usar la librería de componentes UI adoptada por el proyecto.
- Priorizar los componentes, variantes, tokens y patrones de layout que ofrece esa librería.
- Reutilizar componentes compartidos antes de crear uno nuevo.

## Restricciones visuales

- No crear un sistema de estilos propio.
- No definir una identidad visual paralela ni objetos visuales ad hoc.
- No escribir CSS o estilos inline para reemplazar componentes existentes de la librería.
- Si la librería no cubre una necesidad, documentar la limitación y proponer una decisión antes de incorporar estilos propios.

## Criterios de implementación

- Construir pantallas claras, consistentes, accesibles y responsive.
- Respetar las convenciones de composición, nombres, rutas, estado y formularios ya existentes en el proyecto.
- Implementar estados de carga, vacío, error, éxito y permisos cuando correspondan.
- Mantener la lógica de negocio en servicios/composables y no duplicarla en las vistas.
- Integrar la pantalla con el contrato de la API REST definido por Backend.
- Validar entradas en la interfaz sin reemplazar las validaciones del backend.
- Cubrir la interacción principal y los estados relevantes con las pruebas frontend del proyecto.

## Instrucción para las subtareas

Las subtareas de Frontend deben indicar: “Consultar y aplicar el skill `convenciones-frontend`”. No es necesario repetir estas reglas dentro de cada ticket.

## Modo de validación

Cuando el usuario solicite validar una implementación frontend, revisar explícitamente:

- [ ] Está implementada con Vue y respeta la estructura del proyecto.
- [ ] Usa la librería de componentes adoptada por el proyecto.
- [ ] No incorpora CSS, estilos inline ni un sistema visual propio sin justificación aprobada.
- [ ] Reutiliza componentes, variantes, tokens y patrones existentes cuando están disponibles.
- [ ] La pantalla es consistente, accesible y responsive.
- [ ] Contempla estados de carga, vacío, error, éxito y permisos cuando corresponden.
- [ ] La lógica de negocio está fuera de la vista, en servicios o composables.
- [ ] La integración respeta el contrato de la API REST.
- [ ] Las validaciones de interfaz no reemplazan las del backend.
- [ ] Existen pruebas para la interacción principal y los estados relevantes.

El resultado de la validación debe separar hallazgos bloqueantes, observaciones y aspectos conformes. Si una regla no puede verificarse con la evidencia disponible, indicarlo como “no verificable” en lugar de asumir que se cumple.
