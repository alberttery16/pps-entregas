# ACT_UT1_1 · Depuradores (a13)

## Qué se analiza

Se conservan los dos programas: el original y el corregido. Esta carpeta desarrolla la parte 6 de la actividad 1; las partes 1 a 5 están en [a12](../a12/README.md).

**Estado:** análisis estático preparado. La ejecución con GDB está pendiente porque el entorno de revisión deniega `ptrace`, como muestra [gdb-entorno.txt](gdb-entorno.txt). Los valores siguientes son los deducidos del código y de la salida observada en a12; no son una captura de una sesión GDB completada.

## Parte 6 · 3.3.3 Análisis con depuradores: gdb y depurador web

### Preparar y ejecutar GDB en Ubuntu

```bash
nasm -f elf64 -g -F dwarf hola_enunciado.asm -o hola_enunciado.o
ld hola_enunciado.o -o hola_enunciado
nasm -f elf64 -g -F dwarf hola.asm -o hola.o
ld hola.o -o hola
gdb -q ./hola_enunciado
```

Dentro de GDB:

```gdb
set disassembly-flavor intel
set logging file gdb-original.txt
set logging enabled on
break _start
run
x/gx $rsp
x/s *(char**)($rsp+8)
stepi
info registers rax rdi rsi rdx
```

Repetir las dos últimas órdenes después de cada instrucción. Justo antes del primer `syscall` ejecutar `x/s $rsi` y `x/14xb $rsi`. Después del `xor rdi,rdi`, ejecutar `x/i $rip` para identificar la siguiente instrucción real; avanzar hasta SIGSEGV. No inventar esa instrucción a partir del fuente: está fuera de las instrucciones escritas y depende de los bytes siguientes.

### Tabla de instrucciones del original

| Instrucción | Cambio esperado |
|---|---|
| `mov rax,1` | `rax=1`, syscall write |
| `mov rdi,1` | `rdi=1`, stdout |
| `mov rsi,message` | `rsi` contiene la dirección del mensaje; en la compilación de a12 fue `0x402000` |
| `mov rdx,14` | `rdx=14`, bytes solicitados |
| `syscall` | `rax=14` si se escriben los 14 bytes, como en la ejecución de a12; también se alteran `rcx` y `r11` |
| `mov rax,60` | `rax=60`, número de exit |
| `xor rdi,rdi` | `rdi=0`, estado deseado para exit |

En el corregido, `write` escribe 13 bytes y devuelve 13 en `rax` cuando tiene éxito. Ese registro es un resultado, no el número de syscall una vez vuelve `write`. Tras `xor`, `rax` vale 60, pero falta la instrucción que invoca `exit`: el procesador sigue interpretando bytes ajenos al programa y acaba en SIGSEGV en la ejecución observada.

Repetir con `gdb -q ./hola`; avanzar hasta el último `syscall` y consultar `p $_exitcode`: debe ser 0. En la pila inicial se espera `argc=1` si no se pasaron argumentos; la dirección en `rsp+8` apunta a `argv[0]`, el nombre usado para ejecutar el programa. Copiar los valores reales y las direcciones de la sesión propia.

### Depurador web de 32 bits

Abrir [asmdebugger.com](http://asmdebugger.com/) y pegar:

```asm
start:
    mov eax, 0
    mov ecx, 5
suma:
    add eax, ecx
    dec ecx
    jnz suma
exit:
```

| Vuelta | `eax` después de sumar | `ecx` después de decrementar | ZF después de `dec` |
|---|---:|---:|---:|
| 1 | 5 | 4 | 0 |
| 2 | 9 | 3 | 0 |
| 3 | 12 | 2 | 0 |
| 4 | 14 | 1 | 0 |
| 5 | 15 | 0 | 1 |

Son valores calculados que hay que contrastar en el simulador. `jnz` examina la bandera que deja `dec`: la quinta vuelta produce cero y no salta. El simulador no admite los registros de 64 bits, `syscall`, ni las directivas NASM `section` y `db`; no puede ejecutar directamente el programa original.

### Capturas pendientes

Guardar una imagen real de GDB parado en SIGSEGV y otra del simulador al terminar. Ambas deben mostrar usuario o fecha. Pies propuestos:

- «Figura 1. Programa original detenido en SIGSEGV después de no invocar la salida del proceso».
- «Figura 2. Bucle del simulador finalizado con EAX=15, ECX=0 y ZF=1».

Incorporar las imágenes y los registros reales al PDF obligatorio de la actividad 1. No se han añadido imágenes simuladas ni capturas de terceros.
