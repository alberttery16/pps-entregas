# Evidencia de depuración · Go

La captura exigida por el enunciado todavía no se ha aportado. No hay una imagen simulada que la sustituya.

1. Abrir la carpeta `a15` en VS Code (o abrir `ut1/actividades-2-3.code-workspace` y seleccionar su configuración).
2. Poner un breakpoint en `main.go:19` y ejecutar la configuración de esta carpeta con F5.
3. Detenerse con `numero=22` o `numero=8080` y dejar visibles Variables, Pila de llamadas y la línea resaltada.
4. Guardar la captura aquí como `debug-go.png` y añadirla al README principal, con el pie de figura indicado en él.

En Go, para inspeccionar `clase`, volver a `main` y avanzar hasta después de la asignación de la línea 44. El alcance de esa variable no es el mismo que el del parámetro `numero`.
