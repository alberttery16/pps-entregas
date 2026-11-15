# ACT_UT1_3 · Bash programming

## Estado y reproducción

Código y resultados preparados y ejecutados en Linux x86-64 durante la revisión. Las trazas corresponden a los archivos de esta carpeta. **Las dos lecturas del aula ya se han contrastado con los PDF adjuntos. Falta únicamente contrastar la versión de `puertos.sh` con el apartado «Bash por dentro» de los apuntes**, que no se ha adjuntado. Se ha creado una versión propia del clasificador y se explica expresamente esta diferencia; no se presenta como transcripción de los apuntes.

```bash
chmod +x puertos.sh experimentos/ejecutar.sh
./puertos.sh 22 8080 50000 abc 70000 '*'
bash -n puertos.sh
bash -x ./puertos.sh 22 abc 2>&1 | tee traza1.txt
PS4='+ línea ${LINENO}: ' bash -x ./puertos.sh 8080 2>&1 | tee traza2.txt
bash experimentos/ejecutar.sh
```

Un estado distinto de cero es normal en los ejemplos que provocan errores. Los registros identifican dichos estados. No ejecutar `LearnBash.sh` entero.

## Parte 1 · Lectura 3.1: cómo ejecuta Bash una orden

Bash lee la línea, reconoce sus palabras y operadores y analiza cómo se relacionan.
Después realiza las expansiones que correspondan, como sustituir variables, ejecutar `$(...)` o expandir comodines no protegidos por comillas.
Resuelve si el nombre corresponde a una función, una orden interna o un ejecutable externo localizado mediante `PATH`.
En el caso habitual de una orden externa, crea un proceso con `fork` y carga el programa mediante `exec`; las internas no necesitan siempre ese proceso adicional.
Al terminar conserva el estado de salida en `$?`, donde cero indica éxito por convención.

Ejemplo propio: `printf '%s\n' "$HOME"` expande la variable pero conserva la ruta como un argumento; `printf` es una orden interna de Bash. En cambio, `/bin/ls` ejecuta un programa externo. Hay optimizaciones y contextos donde no se realiza exactamente un `fork` por orden.

Fuente de apoyo: [manual de Bash, funcionamiento de la shell](https://www.gnu.org/software/bash/manual/html_node/Shell-Operation.html). Lectura contrastada: Brennan D Baraban, `How Does the Shell Command ls Work Internally.pdf`, aportada por el alumno. Describe la lectura de la orden, su separación, la resolución de nombres, PATH y la secuencia fork/exec/wait. Matiz técnico: execve no devuelve cero si tiene éxito, sino que sustituye la imagen del proceso; el estado final de la orden es otra cosa.

## Parte 2 · Lectura 3.2: introducción a los scripts de Bash

Un script reúne una secuencia de órdenes en un fichero que puede repetirse sin volver a escribir cada paso.
Permite recibir argumentos, reutilizar funciones y tomar decisiones con condiciones.
Los bucles repiten operaciones sobre varios datos y evitan copiar órdenes casi iguales.
También se pueden comprobar errores y guardar resultados para reproducir una prueba.
En esta actividad, `puertos.sh` procesa todos los puertos recibidos, informa de los incorrectos y continúa con los demás.

Ejemplo propio: `./puertos.sh 22 8080 50000` aplica la misma función a tres argumentos. El shebang selecciona Bash y `chmod +x` permite ejecutarlo directamente. Lectura contrastada: Saquib Khan, `Introduction to Bash Scripting.pdf`, aportada por el alumno. Presenta automatización, variables, condiciones, bucles, permisos y códigos de salida. En su ejemplo del bucle for aparece `$1`; para imprimir la variable iterada `i` debe usarse `$i`.

## Parte 3 · Script de Bash y su depuración

El script clasifica 0–1023 como sistema, 1024–49151 como usuario y 49152–65535 como dinámico/privado. Rechaza texto y números fuera de rango. No contacta con puertos de red.

Salida real de `./puertos.sh 22 8080 50000 abc 70000 '*'`:

```text
Puerto 22: Sistema (bien conocido)
Puerto 8080: Usuario (registrado)
Puerto 50000: Dinámico o privado
Error: abc no es un número entero válido
Error: 70000 está fuera del rango 0-65535
Error: * no es un número entero válido
```

Código de salida: 1 porque hubo entradas inválidas. Las comillas de `'*'` evitan que el Bash que lanza el programa lo expanda a nombres de archivos.

- `bash -n` comprueba la sintaxis sin ejecutar. Terminó con 0.
- `bash -x` escribe cada orden expandida en stderr. [traza1.txt](traza1.txt) contiene la ejecución con 22 y abc.
- `PS4` incorpora `${LINENO}`: [traza2.txt](traza2.txt) contiene la ejecución con 8080 y sus líneas.

**¿Por qué aparecen `+` y `++`?** Bash repite el primer carácter de `PS4` para ciertos niveles de anidamiento. En estas trazas las órdenes exteriores llevan `+`; las que se ejecutan dentro de la sustitución `$(clasificar_puerto "$texto")` llevan `++`. No significa que todas las funciones añadan siempre un signo más.

**¿Cuándo aparece `$texto` sustituido?** La traza se escribe después de la expansión y antes de ejecutar la orden. Por eso muestra `clasificar_puerto 22` o `local texto=abc numero`, no el valor pendiente de expandir. Las comillas que imprime la traza representan los argumentos y no tienen por qué ser idénticas a las del fuente.

**¿Qué línea comprueba `abc`?** La línea 7 de `puertos.sh`, `[[ ! $texto =~ ^[0-9]+$ ]]`. En `traza1.txt` aparece `[[ ! abc =~ ^[0-9]+$ ]]` dentro de la sustitución de órdenes; después la línea 8 imprime el error y la 9 devuelve 1. `traza2.txt` usa 8080 y por eso no contiene abc.

Aporte propio: se usan `set -u` y `pipefail`, comillas en los argumentos y validación de longitud antes de hacer aritmética. No se activa `set -e` de forma indiscriminada: los fallos se gestionan mediante `if` para seguir procesando. Se prueban también los límites y `00080`, convertido como decimal, y un número muy largo que no debe desbordar la validación. Ver [evidencias/puertos.txt](evidencias/puertos.txt) y [evidencias/analisis.txt](evidencias/analisis.txt).

## Parte 4 · Tutorial de krother

Fuente: [krother/bash_tutorial](https://github.com/krother/bash_tutorial), revisión `9b07e53aae429046d938ba5addea956b40894d95`. Los ejercicios se han resuelto en una copia temporal; registro de las órdenes: [evidencias/krother.txt](evidencias/krother.txt). Esta tabla es una resolución técnica reproducible, no una captura de progreso personal del alumno.

| Capítulo | Órdenes utilizadas | Letras y explicación |
|---|---|---|
| 1. Directories and files | `ls -a exercise_1/directoryB/solution_1.1`, `bash exercise_1/directoryB/program.sh`, `wc -c exercise_1/directoryC/text_file.txt` | **APTE**: nombres visible/oculto A y P; programa T; tamaño 69, ASCII E |
| 2. Edit text files | `cat exercise_2/solution_2.1.txt`, `nano letras.txt` | **NO**: archivo N; en nano Ctrl+O guarda, por tanto O |
| 3. Copy and remove files | `mkdir exercise_3/solution`, `cp exercise_3/part1/* exercise_3/part2/* exercise_3/solution/`, `rm exercise_3/data/*Y*` | **DYTE**: los signos + de `___+______+_` señalan D/Y en `UIMDELGKBCYF`; quedan los archivos con T y E |
| 4. Process text data | `diff exercise_4/ai.txt exercise_4/artificial_intelligence.txt`, `LC_ALL=en_US.utf8 sort exercise_4/elephant.txt`, `grep fire exercise_4/datascience.txt` | **SPA**: diferencia s en stupid/tupid; última palabra parameters, inicial p; línea «a fire station», inicial a |
| 5. Unzip files | `unzip wrapped.zip`, `tar -xf wrapped.tar`, `gunzip solution/solution.txt.gz` | **TA**: el texto descomprimido indica ambas letras |
| 6. Command-line tools | `chmod u+x exercise_6/permissions.sh`, `./exercise_6/permissions.sh`, `df --version`, `export GIVEME=SOLUTION`, `echo "$GIVEME" | wc -c`, `top -b -n 1` | **GONICUS**: script G/O; Torbjörn termina en n; 9 caracteres contando el salto de línea = I; opción `ping -c` = C; segunda cabecera USER = US |

La palabra de 22 caracteres es **APTENODYTESPATAGONICUS**. Es el nombre científico del pingüino rey, normalmente escrito *Aptenodytes patagonicus*.

Detalles de reproducción: se fija `en_US.utf8` para que el orden no cambie con la configuración regional. La pista 12 pide la inicial de la **última palabra**, no la inicial de la última línea. Nano se abrió y guardó en una sesión de terminal. `ping` no estaba instalado en el entorno; la opción `-c` se verificó en su [documentación oficial de iputils](https://github.com/iputils/iputils/blob/master/doc/ping.xml), no se afirma haber enviado paquetes. La resolución está adaptada del tutorial de Kristian Rother, [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); esta sección mantiene esa licencia.

## Parte 5 · Análisis de LearnBash.sh

Se conserva el archivo adjunto con sus números de línea originales, incluida una línea vacía antes del shebang. `bash -n LearnBash.sh` terminó con 0. Que pase la sintaxis no implica que todas las órdenes vayan a funcionar.

Solo se ejecutaron las líneas 1–115 y 122–164, por separado, dentro de una carpeta temporal vacía. No se ejecutaron borrados ni sudo del resto del archivo. Para reproducir desde a16:

```bash
origen=$PWD
trabajo=$(mktemp -d)
sed -n '1,115p' "$origen/LearnBash.sh" > "$trabajo/tramo1.sh"
sed -n '122,164p' "$origen/LearnBash.sh" > "$trabajo/tramo2.sh"
(cd "$trabajo" && bash -x tramo1.sh)
(cd "$trabajo" && bash tramo2.sh)
# En el segundo tramo introducir alumno y, después, 15.
```

Registros: [tramo 1](evidencias/learnbash-tramo1.txt), [tramo 2](evidencias/learnbash-tramo2.txt) y [sintaxis](evidencias/learnbash-sintaxis.txt).

| Línea | Comentario `# =>` | Salida real | ¿Coincide? |
|---|---|---|---|
| 8 | Hello world! | Hello world! | Sí |
| 19 | variable: command not found | variable: command not found, con prefijo de archivo/línea | Sí, en el error |
| 24 | Some string: command not found | Some string: command not found, con prefijo de archivo/línea | Sí, en el error |
| 31 | Some string | Some string | Sí |
| 32 | $variable | $variable | Sí |
| 47 | A string | A string | Sí |
| 52 | Some st | Some st | Sí |
| 54 | tring | tring | Sí |
| 59 | 11 | 11 | Sí |
| 75 | "one" | one | Coincide el contenido, no se imprimen comillas |
| 79 | "6" | 6 | Coincide el contenido, no se imprimen comillas |
| 99 | 1 2 3 4 5 6 7 8 9 10 | 1 2 3 4 5 6 7 8 9 10 | Sí |
| 105 | {$from..$to} | {1..10} | **No** |
| 160 | Always executed | Always executed | Sí |
| 162 | Always executed / Only executed if first command does NOT fail | Dos líneas con esos textos | Sí |

En la línea 105, la expansión de llaves ocurre antes que la de variables. En ese momento no hay límites numéricos literales, por lo que no se genera una secuencia; después se sustituyen `$from` y `$to` y queda `{1..10}`. No se vuelve atrás a expandir las llaves. En las líneas 75 y 79 las comillas del comentario delimitan el ejemplo; no son caracteres de salida.

Con las entradas `alumno` y `15` se obtuvo:

```text
What's your name?
Hello, alumno!
Your name isn't your username
Valid email!
Always executed
Always executed
Only executed if first command does NOT fail
```

El nombre se compara con `$USER`, no con una lista fija. En el entorno revisado `$USER` estaba vacío, por lo que `alumno` era distinto. En un Ubuntu con usuario `alumno` se imprimiría `Your name is your username`. Las condiciones de Steve/Daniya/Zach no se cumplen. `Valid email!` se refiere a la variable fija `me@example.com`, no al nombre introducido.

Aporte propio: los errores de las líneas 19 y 24 son de ejecución, no de sintaxis. Bash interpreta un nombre de orden y no una asignación correcta. La ejecución continúa porque este archivo no activa `set -e`. Para ejecutar el archivo directamente mediante su shebang, este tendría que estar en la primera línea; se ha preservado el original y se invoca explícitamente con Bash.

## Parte 6 · Cuatro experimentos en Go, Python y Bash

Ejecución: `bash experimentos/ejecutar.sh`. Cada caso tiene archivo independiente; los Go se ejecutan con `go run caso/main.go` para que el ejemplo que no compila no bloquee a los demás. Se almacenan stdout, stderr y estado en `experimentos/salidas/`.

En inyección se cuentan las órdenes `echo` que procesan la entrada: **dos** en la variante insegura y **una** en la segura. No se cuentan el proceso envoltorio ni los mensajes que rotulan cada variante. La aparición literal de `ORDEN_INYECTADA` en la variante segura no prueba una inyección: forma parte del único argumento.

### Tipos

#### Go

```go
package main

import "fmt"

func main() { texto := "hola"; fmt.Println(texto + 1) }
```

Salida real:

```text
# command-line-arguments
tipos/main.go:5:44: invalid operation: texto + 1 (mismatched types string and untyped int)

Código de salida: 1
```

Go rechaza string + entero en compilación; este fallo es el resultado buscado.

#### Python

```python
texto = "hola"
print(texto + 1)
```

Salida real:

```text
Traceback (most recent call last):
  File "/workspace/scratch/6eaef61f5d83/pps-entregas/ut1/a16/experimentos/tipos.py", line 2, in <module>
    print(texto + 1)
          ~~~~~~^~~
TypeError: can only concatenate str (not "int") to str

Código de salida: 1
```

Python rechaza la operación durante la ejecución con TypeError; la sintaxis por sí sola era válida.

#### Bash

```bash
#!/usr/bin/env bash
# Sin nounset: Bash interpreta hola como nombre de variable aritmética.
unset hola
texto=hola
printf '%s\n' "$((texto + 1))"
```

Salida real:

```text
1

Código de salida: 0
```

Sin `set -u`, Bash interpreta `hola` como nombre de variable aritmética; al estar ausente vale 0 y el resultado es 1. No es una suma de cadenas con comprobación de tipos.

### Indice

#### Go

```go
package main

import "fmt"

func main() { valores := []int{10, 20, 30}; indice := 10; fmt.Println(valores[indice]) }
```

Salida real:

```text
panic: runtime error: index out of range [10] with length 3

goroutine 1 [running]:
main.main()
	/workspace/scratch/6eaef61f5d83/pps-entregas/ut1/a16/experimentos/indice/main.go:5 +0x17
exit status 2

Código de salida: 1
```

El índice variable permite compilar, pero se produce panic al ejecutarlo. El programa termina con estado 2; el envoltorio go run informa exit status 2 y devuelve 1.

#### Python

```python
valores = [10, 20, 30]
indice = 10
print(valores[indice])
```

Salida real:

```text
Traceback (most recent call last):
  File "/workspace/scratch/6eaef61f5d83/pps-entregas/ut1/a16/experimentos/indice.py", line 3, in <module>
    print(valores[indice])
          ~~~~~~~^^^^^^^^
IndexError: list index out of range

Código de salida: 1
```

El acceso falla con IndexError; no se accede a memoria fuera de la lista.

#### Bash

```bash
#!/usr/bin/env bash
valores=(10 20 30)
indice=10
printf 'Resultado: <%s>\n' "${valores[indice]}"
```

Salida real:

```text
Resultado: <>

Código de salida: 0
```

El elemento no asignado se expande a texto vacío sin error en este modo. Los arrays Bash son dispersos.

### Desbordamiento

#### Go

```go
package main

import "fmt"

func main() { var numero int64 = 9223372036854775807; fmt.Println(numero + 1) }
```

Salida real:

```text
-9223372036854775808

Código de salida: 0
```

La variable int64 desborda a -9223372036854775808. Se usa variable porque una constante desbordada sería un error distinto de compilación.

#### Python

```python
numero = 9223372036854775807
print(numero + 1)
```

Salida real:

```text
9223372036854775808

Código de salida: 0
```

El entero crece hasta 9223372036854775808; su precisión es arbitraria dentro de los recursos disponibles.

#### Bash

```bash
#!/usr/bin/env bash
numero=9223372036854775807
printf '%s\n' "$((numero + 1))"
```

Salida real:

```text
-9223372036854775808

Código de salida: 0
```

En este Bash de 64 bits la suma da la vuelta a -9223372036854775808 sin avisar.

### Inyeccion

#### Go

```go
package main

import (
	"fmt"
	"os"
	"os/exec"
)

func ejecutar(cmd *exec.Cmd) {
	cmd.Stdout = os.Stdout
	cmd.Stderr = os.Stderr
	if err := cmd.Run(); err != nil {
		panic(err)
	}
}
func main() {
	entrada := "hola; echo ORDEN_INYECTADA"
	fmt.Println("INSEGURO: texto concatenado (2 órdenes echo)")
	ejecutar(exec.Command("bash", "-c", "echo "+entrada))
	fmt.Println("SEGURO: argumento separado (1 orden echo)")
	ejecutar(exec.Command("echo", entrada))
}
```

Salida real:

```text
INSEGURO: texto concatenado (2 órdenes echo)
hola
ORDEN_INYECTADA
SEGURO: argumento separado (1 orden echo)
hola; echo ORDEN_INYECTADA

Código de salida: 0
```

exec.Command no interpreta por sí mismo una shell. La variante insegura llama explícitamente a bash -c; la segura invoca echo con el argumento separado.

#### Python

```python
import os
import subprocess
entrada = "hola; echo ORDEN_INYECTADA"
print("INSEGURO: texto concatenado (2 órdenes echo)", flush=True)
os.system("echo " + entrada)
print("SEGURO: argumento separado (1 orden echo)", flush=True)
subprocess.run(["echo", entrada], check=True)
```

Salida real:

```text
INSEGURO: texto concatenado (2 órdenes echo)
hola
ORDEN_INYECTADA
SEGURO: argumento separado (1 orden echo)
hola; echo ORDEN_INYECTADA

Código de salida: 0
```

os.system entrega texto a la shell: se ejecutan dos echo. subprocess.run con una lista entrega un argumento literal y ejecuta un echo.

#### Bash

```bash
#!/usr/bin/env bash
entrada='hola; echo ORDEN_INYECTADA'
printf 'INSEGURO: texto concatenado (2 órdenes echo)\n'
bash -c "echo $entrada"
printf 'SEGURO: argumento separado (1 orden echo)\n'
bash -c 'echo "$1"' _ "$entrada"
```

Salida real:

```text
INSEGURO: texto concatenado (2 órdenes echo)
hola
ORDEN_INYECTADA
SEGURO: argumento separado (1 orden echo)
hola; echo ORDEN_INYECTADA

Código de salida: 0
```

bash -c interpreta el punto y coma al concatenar. Con $1 entre comillas la entrada se conserva como dato y solo se ejecuta un echo.

### Experimento adicional: activar nounset

```bash
#!/usr/bin/env bash
set -u
valores=(10 20 30)
printf '%s\n' "${valores[10]}"
```

Salida real:

```text
extra_nounset.sh: line 4: valores[10]: unbound variable

Código de salida: 1
```

`set -u` transforma el acceso al elemento no asignado en un error. Es una ayuda para detectar fallos, pero no convierte Bash en un lenguaje de tipado estático.

## Parte 7 · Tabla de seguridad de los tres lenguajes

La valoración mide la protección frente al fallo concreto, no una garantía global. **Alta**: detecta o evita el caso; **media**: exige cuidado/configuración; **baja**: el ejemplo falla silenciosamente o reinterpreta fácilmente datos. Cada celda indica una evidencia de esta revisión.

| Criterio | Go | Python | Bash |
|---|---|---|---|
| Tipado | **Alta**: `tipos/main.go` no compila | **Media**: `tipos.py` lanza TypeError al ejecutar; no se detecta solo con py_compile | **Baja**: texto hola en aritmética produce 1 sin aviso |
| Acceso a memoria | **Alta** en este acceso: índice 10 causa panic con comprobación de límites | **Alta** en este acceso: índice 10 causa IndexError | **Media**: no devuelve memoria arbitraria, pero el elemento ausente es vacío; nounset lo detecta |
| Aritmética entera | **Media**: int64 desborda sin error en ejecución | **Alta**: el entero crece y conserva el resultado | **Baja**: desbordamiento silencioso al mínimo negativo |
| Errores en ejecución | **Media**: el índice termina en panic; Atoi en a15 requiere comprobar error | **Alta** para estos fallos: TypeError/IndexError y traceback identifican la operación | **Baja** por defecto: tipos e índice finalizan con 0; nounset mejora el índice |
| Texto que acaba siendo código | **Media**: al añadir bash -c hay inyección; exec.Command con argumentos la evita | **Media**: os.system es vulnerable en el ejemplo; subprocess con lista la evita | **Baja** en el patrón concatenado: bash -c interpreta el punto y coma; con "$1" se evita |
| Dependencias | **Alta en este ejercicio**: `go list -m all` en a15 solo lista puertos, sin módulos externos | **Media**: los ejemplos importan os/subprocess de la biblioteca estándar, pero dependen de Python instalado | **Media**: depende de Bash y utilidades localizadas con PATH; el tutorial no encontró ping |
| Herramientas de análisis | **Alta**: compilador detecta tipos; gofmt y go vet en a15 terminan con 0 | **Media**: py_compile acepta tipos.py aunque falle al ejecutar; unittest detecta la aserción incorrecta | **Media**: bash -n acepta LearnBash.sh aunque haya command not found; ShellCheck aporta avisos adicionales |

Los experimentos no evalúan `unsafe`, extensiones nativas de Python ni toda la cadena de suministro. Registro adicional: [evidencias/analisis.txt](evidencias/analisis.txt). La valoración de dependencias se limita a lo comprobado, no significa que todo proyecto de Go tenga dependencias seguras.

## Parte 8 · Recomendación para tres casos

**Utilidad que recibe nombres de fichero de usuarios:** elegiría Python por sus operaciones de archivos y gestión de excepciones.
Evitaría os.system y emplearía pathlib o subprocess con argumentos separados si fuera necesario lanzar otra herramienta.
La prueba de inyección demuestra que concatenar el nombre con una orden permite ejecutar una segunda instrucción.
La ejecutaría en una sandbox con acceso solo a una carpeta autorizada y sin privilegios.
Además validaría rutas, enlaces simbólicos y opciones como nombres que empiecen por `-`; separar argumentos no elimina esos riesgos.

**Copia de seguridad nocturna del servidor:** usaría Bash para coordinar herramientas como tar o rsync.
Comprobaría los estados de salida, protegería las expansiones con comillas y evitaría eval.
Los experimentos muestran que no debo confiar en que Bash avise por sí solo de un índice ausente o un desbordamiento.
La ejecutaría con una cuenta dedicada y una sandbox de servicio con origen de solo lectura y destino limitado.
Comprobaría también una restauración y la retención: que la orden termine no demuestra que la copia sea utilizable.

**Servicio de red para desconocidos:** elegiría Go por la compilación, el manejo explícito de errores y la comprobación de índices.
La prueba de int64 demuestra que todavía hacen falta límites numéricos, y la de índice obliga a evitar panics no controlados.
Lo ejecutaría en un contenedor sin root, con capacidades reducidas, límites de CPU/memoria y filesystem de solo lectura cuando sea posible.
Separaría los secretos y restringiría las conexiones de salida; el contenedor comparte kernel y no sustituye la validación.
Si procesa contenido especialmente hostil o necesita mayor separación, lo alojaría además en una máquina virtual.
