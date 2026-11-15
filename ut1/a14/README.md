# ACT_UT1_2 · Python (a14)

Registro real de revisión: [evidencias/ejecucion.txt](evidencias/ejecucion.txt), con Python 3.12.14. Falta incorporar una captura propia de VS Code; los archivos del repositorio no la incluían.

## Parte 1 · Lectura: cómo se ejecutan Python y Java

CPython compila el código fuente a bytecode y lo ejecuta mediante su máquina virtual.
Al importar módulos puede guardar ese bytecode en `__pycache__`, evitando repetir la compilación si el fuente no ha cambiado.
No es una carpeta que contenga un ejecutable independiente y su presencia no significa que Python haya comprobado todos los tipos.
Java también ejecuta bytecode mediante una máquina virtual, la JVM; normalmente lo genera `javac` en archivos `.class` y puede compilarlo a código nativo mediante JIT.
En esta práctica `python3 -m dis puertos.py` muestra instrucciones como `LOAD_CONST` y `CALL`; al ejecutar las pruebas se importa `puertos`.

Síntesis de apoyo: [documentación de módulos de Python](https://docs.python.org/3/tutorial/modules.html). **Pendiente contrastar con los PDF del aula `How Python Works.pdf` y `How Java Works.pdf`, que no se han facilitado.**

## Parte 2 · Programa en Python con su README

### Qué hace el programa

Clasifica puertos de 0 a 65535: sistema (0–1023), usuario (1024–49151) o dinámico/privado (49152–65535). Recorre los argumentos y muestra un error cuando no se convierten a entero o están fuera de rango. No abre conexiones de red.

| Elemento | Archivo y línea |
|---|---|
| Función | `puertos.py:7`, `clasificar_puerto` |
| Decisión | `puertos.py:10`, primer límite de clasificación |
| Bucle | `puertos.py:24`, argumentos de la línea de órdenes |
| Error | `puertos.py:8–9`, rango; `puertos.py:29–30`, captura de ValueError |

### Cómo se ejecuta

```bash
python3 puertos.py 22 8080 50000 abc 70000
```

```text
Puerto 22: Sistema (bien conocido)
Puerto 8080: Usuario (registrado)
Puerto 50000: Dinámico o privado
Error procesando 'abc': invalid literal for int() with base 10: 'abc'
Error procesando '70000': Puerto fuera de rango válido (0-65535): 70000
```

Los errores se capturan y el bucle continúa. La versión existente termina con estado 0 incluso si algunos argumentos eran incorrectos: se documenta ese comportamiento sin cambiar la práctica ya realizada.

## Parte 3 · Tres pruebas en Python, una falla

### Cómo se prueba

```bash
python3 -m unittest -v
```

| Prueba | Comprobación | Resultado real |
|---|---|---|
| `test_clasificacion_clases` | `assertEqual` para 80, 8080 y 50000 | ok |
| `test_puerto_fuera_de_rango` | `assertRaises(ValueError)` con 65536 | ok |
| `test_puerto_privilegiado_fallo` | `assertTrue(es_privilegiado(8080))` | FAIL intencionado |

```text
Traceback (most recent call last):
  File "test_puertos.py", line 15, in test_puerto_privilegiado_fallo
    self.assertTrue(es_privilegiado(8080))
AssertionError: False is not true

Ran 3 tests
FAILED (failures=1)
```

Extracto con la ruta abreviada; el registro incluye la salida completa. Falla la línea 15 porque esperaba `True` y recibió `False`: 8080 no es un puerto privilegiado. No se corrige esta aserción porque la rúbrica exige un fallo deliberado. El proceso de pruebas termina con estado 1.

## Parte 4 · Depuración en Python

### Cómo se depura

Abrir **esta carpeta a14** en VS Code e instalar las extensiones Python y Python Debugger. La configuración existente [.vscode/launch.json](.vscode/launch.json) utiliza `debugpy` y los argumentos `22`, `8080`, `abc`.

1. Poner un breakpoint en `puertos.py:10`, `if numero <= LIMITE_SISTEMA:`.
2. Iniciar con F5. En **Variables**, inspeccionar el parámetro local `numero`: primero se espera 22 y después 8080.
3. En **Pila de llamadas**, comprobar `clasificar_puerto` llamada desde `main`.
4. Para `abc`, `int(arg)` falla antes de invocar la función; por eso no habrá una tercera parada dentro de ella.
5. Avanzar hasta el `except` y comprobar el mensaje de error.

**Pendiente de evidencia:** guardar `capturas/debug-python.png` y enlazarla aquí con el pie «Figura 1. Depuración del clasificador Python: valor de numero y pila de llamadas». Los valores anteriores son los esperados según el código, no valores observados en una captura aún inexistente.
