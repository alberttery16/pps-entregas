# ACT_UT1_1 · Pruebas de aplicaciones (a12)

Revisión de los programas existentes. Las mediciones de esta carpeta se han ejecutado en un entorno Linux x86-64 de revisión, no en el ordenador del alumno. Registro completo: [evidencias/ejecucion.txt](evidencias/ejecucion.txt). Los ejecutables originales se conservan; los de revisión se construyeron en `/tmp` para no sustituirlos.

**Pendiente de entrega:** incorporar las capturas propias, completar las mediciones de `strace` y preparar el PDF con la plantilla del aula. Este README no sustituye ese PDF.

## Parte 1 · Lectura 3.1: arquitectura x86-64

Los registros son pequeños almacenes de la CPU: `rax` sirve aquí para el número de syscall y su resultado; `rdi`, `rsi` y `rdx`, para sus argumentos.
`rip` señala la siguiente instrucción y `rsp`, la parte superior de la pila.
Un modo de direccionamiento indica cómo se obtiene un operando: inmediato, registro o memoria mediante una dirección calculada.
En sintaxis Intel se escribe destino antes que origen: `mov rax, 1`; en AT&T se invierten y se añaden prefijos: `mov $1, %rax`.
En este programa, `mov rsi, message` carga la dirección del mensaje, no sus caracteres.

Fuente: [Stanford, guía x86-64](https://web.stanford.edu/class/cs107/guide/x86-64.html).

## Parte 2 · Lectura 3.2: ensamblador y depurador

El ensamblador convierte instrucciones como `mov` en código máquina dentro de un archivo objeto.
El enlazador crea el ejecutable a partir de ese objeto; aquí se utilizan NASM y `ld`.
Un depurador permite detener un programa e inspeccionar su estado para localizar un error.
Un punto de parada interrumpe la ejecución al llegar a una ubicación concreta, por ejemplo `_start`.
La ejecución paso a paso permite ver qué cambia después de cada instrucción; en GDB se usa `stepi`.

Fuente: [Conceptos básicos de Assembler y Debugger](https://www.w0lff4ng.org/conceptos-basicos-de-assembler-y-debugger/).

## Parte 3 · 3.3.1 Ejecutar el programa y corregir sus dos anomalías

`hola_enunciado.asm` se conserva sin corregir. `hola.asm` ya contenía las dos correcciones necesarias:

1. `rdx` debe valer 13: doce caracteres de `Hello World!` y el salto de línea. Con 14 se lee un byte adicional fuera del mensaje.
2. Después de preparar `rax=60` y `rdi=0` debe ejecutarse `syscall` para terminar. Cargar los registros no realiza por sí mismo la llamada al sistema.

Para reproducir desde esta carpeta:

```bash
nasm -f elf64 hola_enunciado.asm -o hola_enunciado.o
ld hola_enunciado.o -o hola_enunciado
./hola_enunciado
echo $?
nasm -f elf64 hola.asm -o hola.o
ld hola.o -o hola
./hola
echo $?
./hola | wc -c
```

En la revisión, el original recibe SIGSEGV y el corregido imprime el mensaje, termina con 0 y escribe 13 bytes. El recolector Python registra la señal como `-11`; en Bash, `echo $?` tras SIGSEGV suele mostrar `128 + 11 = 139`. No hay que confundir el código de `od` con el del programa anterior en una tubería.

Código corregido:

```asm
global _start

section .data
message: db "Hello World!", 10

section .text
_start:
    mov rax, 1
    mov rdi, 1
    mov rsi, message
    mov rdx, 13
    syscall
    mov rax, 60
    xor rdi, rdi
    syscall
```

## Parte 4 · 3.3.2 Salida real frente a la esperada y secciones del ejecutable

Salida esperada: `Hello World!\n` (13 bytes). La real del original en esta compilación incluye un NUL adicional:

```text
0000000   H   e   l   l   o       W   o   r   l   d   !  \n  \0
0000016
```

`0000016` está en octal: representa 14 bytes. Ese byte adicional no forma parte del mensaje y no se debe asumir que siempre será cero en cualquier disposición del ejecutable.

| Comprobación | Resultado observado |
|---|---|
| Texto del mensaje | `.data`, dirección `0x402000`, tamaño `0xd` = 13 bytes |
| Código | `.text`, dirección `0x401000`, tamaño `0x25` = 37 bytes |
| `_start` según `nm` | `0x401000` |
| Punto de entrada según `readelf -h` | `0x401000`: coincide |
| Flags de las secciones | `.text`: AX (asignada y ejecutable); `.data`: WA (escribible y asignada) |

Órdenes: `readelf -h hola`, `readelf -S hola`, `nm hola`, `objdump -d -M intel hola`, `objdump -s -j .data hola`. El registro enlazado incluye todas sus salidas sobre el binario reconstruido. Los permisos efectivos en memoria también dependen de los segmentos ELF, consultables con `readelf -l hola`.

## Parte 5 · 3.3 Comparación con el mismo programa en C y en Python

| Medida | Ensamblador | C | Python |
|---|---|---|---|
| Líneas (`wc -l`) | 15 | 6 | 1 |
| Tamaño medido | 8848 bytes | 15952 bytes | 22 bytes de fuente |
| Tipo (`file`) | ELF64 estático | ELF64 PIE dinámico | Texto ASCII |
| Bibliotecas (`ldd`) | No es ejecutable dinámico | libc y cargador dinámico; también aparece vDSO | No se aplica al `.py`; depende del intérprete |
| Número de syscalls medido | Pendiente: ptrace bloqueado | Pendiente: ptrace bloqueado | Pendiente: ptrace bloqueado |

Los tamaños son de la revisión, no valores universales; el fichero Python no incluye el tamaño de su intérprete. El programa ensamblador realiza directamente las llamadas del sistema. C necesita su código de arranque y biblioteca, y Python necesita cargar el intérprete y procesar el script. Los tres deberían acabar escribiendo los mismos 13 bytes en stdout, pero falta verificarlo con `strace` en un sistema que lo permita.

Para completar la comparación en Ubuntu:

```bash
gcc hola.c -o hola_c
strace -e trace=write ./hola
strace -e trace=write ./hola_c
strace -e trace=write python3 hola.py
strace -o asm.strace ./hola
strace -o c.strace ./hola_c
strace -o python.strace python3 hola.py
grep -c '^[a-zA-Z_][a-zA-Z0-9_]*(' asm.strace c.strace python.strace
```

Contar únicamente líneas con llamadas evita sumar las líneas informativas de salida de `strace`. Adjuntar las tres trazas antes de completar la fila pendiente.

## Parte 6 · 3.3.3 Análisis con depuradores: gdb y depurador web

La explicación y los comandos están en [a13/README.md](../a13/README.md).

## Conclusión

El texto visible no basta para dar un programa por correcto: había un byte sobrante y un fallo de terminación. La corrección se ha comprobado reconstruyendo los binarios, inspeccionando sus secciones y verificando la salida y el estado final. Faltan las pruebas de depuración y sus capturas para cerrar la entrega.
