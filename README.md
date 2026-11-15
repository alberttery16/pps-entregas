# Puesta en Producción Segura · Entregas

Repositorio de Albert Grigore. Documentación organizada según los enunciados revisados de UT1.

| Actividad | Carpetas | Estado comprobado en la revisión |
|---|---|---|
| 1 · Pruebas de aplicaciones | [a12](ut1/a12/README.md), [a13](ut1/a13/README.md) | Código existente correcto en sus correcciones; README y mediciones añadidos. Faltan evidencias de depuración/strace y PDF o aportar la entrega ya realizada |
| 2 · Ejecución de aplicaciones | [a14 Python](ut1/a14/README.md), [a15 Go](ut1/a15/README.md) | Programas y pruebas verificados; dos pruebas correctas y un fallo deliberado por lenguaje. Faltan capturas propias de VS Code |
| 3 · Bash programming | [a16](ut1/a16/README.md) | Script propio, dos trazas, tutorial resuelto, análisis seguro de LearnBash, doce experimentos y tabla. Falta contrastar lecturas y script con los apuntes del aula |
| 4 · Solidity + Git | [a17](ut1/a17/README.md) | Análisis y borrador de memoria preparados; pendientes los cursos, sus capturas y el PDF final |

## Cómo trabajar

Usar Linux/Ubuntu para las pruebas de terminal. Desde cada carpeta ejecutar las órdenes que aparecen en su README. Python y Go contienen una prueba que **debe fallar** según el enunciado; no es un defecto pendiente de corregir. No ejecutar LearnBash.sh completo.

Las salidas de `evidencias/` se han obtenido durante la revisión en un entorno Linux separado del equipo del alumno. Se identifican expresamente las limitaciones de ese entorno y los resultados esperados que todavía no se han observado. Los binarios existentes se conservan; se recomienda reconstruirlos desde el fuente antes de utilizarlos.

## Pendientes para cerrar las entregas

- [ ] Incorporar las capturas reales de las actividades 1 y 2, si ya se realizaron, y el PDF de la actividad 1.
- [ ] Ejecutar GDB y strace en Ubuntu: el entorno de revisión deniega ptrace; no hay mediciones válidas de syscalls ni captura de SIGSEGV en GDB.
- [ ] Aportar/contrastar las lecturas del aula y el script «Bash por dentro» para la actividad 3.
- [ ] Completar CryptoZombies y Learn Git Branching y añadir las ocho evidencias de logro de la actividad 4.
- [ ] Completar NIA, portada y normativa y generar el PDF final de la actividad 4.
- [ ] Comprobar acceso del profesor `jcalahorratovar` y visibilidad privada, como exigen los enunciados de las actividades 1 y 2. La consulta inicial del repositorio indicó visibilidad pública; no se ha cambiado la configuración de acceso.

## Entrega en Aules

Las actividades 1 y 4 requieren un PDF además del repositorio. Las actividades 2 y 3 se corrigen mediante sus README. Incluir la dirección del repositorio en el texto de cada entrega y revisar los apartados y evidencias de la rúbrica antes de enviar.
