# Guía de Learn Git Branching · 25 niveles obligatorios

Guía para practicar en [el simulador](https://learngitbranching.js.org/), **no para ejecutar estas secuencias sobre pps-entregas**. Las referencias C2/C3 y la orden fakeTeamwork pertenecen al simulador. Las secuencias parten del estado inicial de cada nivel; si ya lo modificaste, reinicia ese nivel antes de seguirlas.

Basada en los objetivos y soluciones de referencia del [proyecto oficial](https://github.com/pcottle/learnGitBranching), revisión `6b9db44494ad62922c73936c5cef14b57492ae94`. No se ha completado una sesión del simulador durante esta revisión; esta guía no acredita logros. Lee la explicación, ejecuta las órdenes y comprueba el objetivo visual antes de pasar al siguiente nivel.

En la versión consultada `move` se llama **Moving and Staging Work** y contiene cuatro niveles. Si tu versión tiene otro nombre o un objetivo distinto, sigue el objetivo que aparece en pantalla. `switch` puede aparecer como `checkout` en materiales anteriores.

## Main · Introduction Sequence

### intro1 · Introduction to Git Commits

Crear dos commits consecutivos sobre main.

```bash
git commit
git commit
```

### intro2 · Branching in Git

Crear la rama bugFix y situar HEAD sobre ella.

```bash
git branch bugFix
git switch bugFix
```

### intro3 · Merging in Git

Crear un cambio en cada rama e integrarlos con merge. Observar el commit con dos padres.

```bash
git switch -c bugFix
git commit
git switch main
git commit
git merge bugFix
```

### intro4 · Rebase Introduction

Reaplicar el cambio de bugFix sobre main con rebase y comparar con el merge anterior.

```bash
git switch -c bugFix
git commit
git switch main
git commit
git switch bugFix
git rebase main
```

## Main · Ramping Up

### rampup1 · Detach yo' HEAD

Apuntar HEAD directamente al commit C4, sin seguir una rama.

```bash
git switch --detach C4
```

### rampup2 · Relative Refs (^)

Mover HEAD al padre del commit al que apunta bugFix.

```bash
git switch --detach bugFix^
```

### rampup3 · Relative Refs #2 (~)

Colocar main en C6 y mover HEAD y bugFix mediante referencias relativas.

```bash
git branch -f main C6
git switch --detach HEAD~1
git branch -f bugFix HEAD~1
```

### rampup4 · Reversing Changes in Git

Deshacer el cambio local moviendo la referencia; en pushed añadir un commit inverso mediante revert.

```bash
git reset HEAD~1
git switch pushed
git revert HEAD
```

## Main · Moving and Staging Work

### move1 · Cherry-pick Intro

Copiar los cambios de C3, C4 y C7 sobre la rama actual, en ese orden.

```bash
git cherry-pick C3 C4 C7
```

### move2 · Interactive Rebase Intro

Reordenar commits mediante el cuadro interactivo.

```bash
git rebase -i overHere
```

En el cuadro de rebase, dejar **C3, C5, C4** en ese orden y confirmar. No utilizar opciones internas del código del simulador.

### move3 · The Staging Area

Crear un commit solo con app.js y otro con styles.css. El índice decide qué se incluye.

```bash
git add app.js
git commit
git add styles.css
git commit
```

### move4 · Undoing with git restore

Sacar secret.env del índice, descartar la modificación de experiment.js y confirmar únicamente lo preparado.

```bash
git restore --staged secret.env
git restore experiment.js
git commit
```

## Main · A Mixed Bag

### mixed1 · Grabbing Just 1 Commit

Conservar solo el cambio útil C4, dejando fuera los commits de depuración.

```bash
git rebase -i main
```

En el cuadro, conservar únicamente **C4** y confirmar. Después:

```bash
git rebase bugFix main
```

### mixed2 · Juggling Commits

Mover un commit para editarlo y recuperar después el orden lógico.

```bash
git rebase -i HEAD~2
```

Ordenar **C3, C2** y confirmar. Ejecutar:

```bash
git commit --amend
git rebase -i HEAD~2
```

En el segundo cuadro, colocar el commit C2 ya modificado (normalmente **C2''**) antes del nuevo C3 (normalmente **C3'**). Confirmar y ejecutar:

```bash
git rebase caption main
```

Los apóstrofos indican commits nuevos creados al reescribir; comprobar sus nombres en el gráfico.

### mixed3 · Juggling Commits #2

Rehacer el resultado anterior seleccionando los commits con cherry-pick.

```bash
git switch main
git cherry-pick C2
git commit --amend
git cherry-pick C3
```

### mixed4 · Git Tags

Crear etiquetas v0 y v1 y situar HEAD en v1. Las etiquetas no avanzan automáticamente al confirmar.

```bash
git tag v1 side~1
git tag v0 main~2
git switch --detach v1
```

### mixed5 · Git Describe

Probar git describe sobre las referencias visibles y observar etiqueta, distancia y hash. El objetivo se cierra creando un commit.

```bash
git commit
```

## Remote · Push & Pull

### remote1 · Clone Intro

Clonar el repositorio del escenario. El simulador crea el remoto y la copia local.

```bash
git clone
```

### remote2 · Remote Branches

Comparar una rama local con la referencia remota o/main. Crear un commit en HEAD separado no mueve o/main.

```bash
git commit
git switch --detach o/main
git commit
```

### remote3 · Git Fetchin'

Descargar cambios remotos sin integrarlos en la rama local.

```bash
git fetch
```

### remote4 · Git Pullin'

Descargar e integrar los cambios remotos.

```bash
git pull
```

### remote5 · Faking Teamwork

Simular cambios de compañeros y un cambio local; integrar ambas historias.

```bash
git clone
git fakeTeamwork 2
git commit
git pull
```

### remote6 · Git Pushin'

Crear dos commits locales y publicarlos.

```bash
git commit
git commit
git push
```

### remote7 · Diverged History

Resolver la divergencia reaplicando los commits locales sobre el remoto antes de publicar.

```bash
git clone
git fakeTeamwork
git commit
git pull --rebase
git push
```

### remote8 · Locked Main

Restaurar la referencia main al remoto y publicar el trabajo en una rama feature, como pide el escenario de rama protegida.

```bash
git branch -f main o/main
git switch -c feature C2
git push origin feature
```

## Evidencias finales

Volver al selector de niveles y comprobar los cuatro bloques Main y el primer bloque Remote completos. Guardar sus capturas en `capturas/`, mantener el mismo navegador y perfil e incluir los pies de figura indicados en el README. Advanced Topics y To Origin And Beyond son extras, no sustituyen los niveles obligatorios.

## Atribución del código de referencia

Las secuencias de órdenes se han adaptado del proyecto de Peter Cottle. Se conserva su licencia:

## MIT License

Copyright (c) 2012-2025 Peter Cottle

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
