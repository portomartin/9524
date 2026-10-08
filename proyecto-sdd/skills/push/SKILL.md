---
name: push
description: Revisar y publicar cambios del repositorio mediante Git cuando el usuario solicite explícitamente hacer commit o push.
---

# Publicar cambios del repositorio

Usar esta skill únicamente para operaciones explícitas de Git relacionadas con publicar cambios. No modificar archivos de producto ni decidir por cuenta propia cuándo hacer `commit` o `push`.

## Variable de control

```text
confirmar_mensaje_commit = obligatorio
```

Antes de ejecutar cualquier `git commit`, mostrar el mensaje propuesto y esperar la aprobación explícita del usuario. Si el usuario lo rechaza, solicitar una alternativa y no crear el commit hasta recibir confirmación.

## Flujo

1. Revisar la rama actual, el remoto configurado y el estado del repositorio.
2. Inspeccionar el diff y separar cambios relevantes de cambios ajenos o no relacionados.
3. Informar qué archivos se incluirían, qué commit existe o se propone y hacia qué remoto y rama se publicaría.
4. Antes de una mutación externa, requerir una autorización explícita para esa operación. `commit` y `push` son autorizaciones distintas.
5. No usar `reset --hard`, `checkout --`, rebase destructivo ni sobrescribir cambios sin una instrucción específica del usuario.
6. Después del `push`, verificar el resultado y comunicar el remoto, la rama y el commit publicado.

## Reglas

- Si hay cambios sin commit y el usuario pide solo `push`, explicar que Git solo puede publicar commits y preguntar si desea preparar uno.
- Si el usuario pide `commit y push`, proponer un mensaje claro y mostrar el alcance antes de ejecutar.
- Usar mensajes de commit descriptivos: indicar la acción principal y el objetivo del cambio, evitando mensajes genéricos como `cambios`, `update` o `fix`.
- No ejecutar el commit solo porque el mensaje parezca correcto: la aprobación del mensaje es obligatoria.
- No incluir archivos no relacionados, secretos, credenciales ni archivos temporales.
- No hacer `git push --force` salvo que el usuario lo solicite explícitamente y se haya verificado la rama objetivo.
- No confundir publicar cambios en Git con sincronizar Jira: son operaciones independientes.
