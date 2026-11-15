# ACT_UT1_2 · Go (a15)

Registro real: [evidencias/ejecucion.txt](evidencias/ejecucion.txt), Go 1.23.2 sobre Linux amd64. Se simplificó la creación del error con `fmt.Errorf`, se eliminaron comentarios con números de línea desactualizados y se añadió la configuración del depurador. Se mantiene la prueba que debe fallar.

## Parte 5 · Programa en Go con su README

### Qué hace el programa

Clasifica los mismos intervalos de puertos que [la versión Python](../a14/README.md). Convierte cada argumento con `strconv.Atoi`, comprueba el rango y continúa con el siguiente si hay un error. No realiza conexiones de red.

| Elemento | Ubicación |
|---|---|
| Función | `main.go:15`, `ClasificarPuerto` |
| Decisión | `main.go:19`, `switch` |
| Bucle | `main.go:38`, `for` sobre argumentos |
| Error | `main.go:16–17`, rango; `main.go:39–42`, conversión |

### Cómo se ejecuta

```bash
go run . 22 8080 50000 abc 70000
go build
```

```text
Puerto 22: Sistema (bien conocido)
Puerto 8080: Usuario (registrado)
Puerto 50000: Dinámico o privado
Error procesando 'abc': valor no numérico (strconv.Atoi: parsing "abc": invalid syntax)
Error procesando '70000': puerto fuera de rango válido (0-65535): 70000
```

`go.mod` declara el módulo `puertos` y la versión mínima indicada `1.22.2`. No contiene dependencias externas. `go build` genera el ejecutable `puertos`; en la revisión se utilizó `go build -o /tmp/pps-puertos-revision` para conservar el binario original del repositorio. El ejecutable reconstruido midió 2186306 bytes; depende de la versión de Go y las opciones de compilación.

Ante `abc`, Go devuelve un valor `error` desde `strconv.Atoi`, que el programa comprueba. Python lanza `ValueError`, capturada mediante `except`. Ambos programas existentes continúan y terminan con 0 tras procesar los argumentos.

## Parte 6 · Tres pruebas en Go, una falla

### Cómo se prueba

```bash
go test -v
gofmt -l .
go vet .
```

| Prueba | Qué comprueba | Resultado |
|---|---|---|
| `TestClasificacionClases` | Tres clases y ausencia de error | PASS |
| `TestPuertoFueraDeRango` | 65536 devuelve un error | PASS |
| `TestPuertoPrivilegiadoFallo` | Espera true para 8080 | FAIL intencionado |

La tercera prueba informa de `main_test.go:34`: se esperaba `true` y se obtuvo `false`. Este fallo es obligatorio en la rúbrica. `go test` termina con 1, mientras que `gofmt -l .` y `go vet .` no muestran problemas y terminan con 0.

## Parte 7 · Depuración en Go

### Cómo se depura

Abrir **esta carpeta a15** en VS Code, instalar la extensión Go y sus herramientas `dlv` y `gopls`. La nueva configuración [.vscode/launch.json](.vscode/launch.json) contiene `type: go`, `program: ${workspaceFolder}` y los argumentos `22`, `8080`, `abc`.

1. Poner un breakpoint en el `switch` de `main.go:19` y pulsar F5.
2. En Variables se espera `numero=22`; al continuar, `numero=8080`.
3. La pila debe mostrar `ClasificarPuerto` llamada desde `main`.
4. Salir de la función y avanzar hasta después de la asignación de la línea 44 para inspeccionar `clase`: «Sistema (bien conocido)» y luego «Usuario (registrado)».
5. `clase` pertenece a `main`, no a `ClasificarPuerto`. `abc` falla antes, en `Atoi`.

**Pendiente:** captura propia `capturas/debug-go.png`, con pie «Figura 2. Depuración del clasificador Go: variables locales y pila de llamadas». No se ha realizado esa sesión de VS Code en el entorno de revisión.

## Parte 8 · Tabla de diferencias entre Python y Go

| Observación | Python | Go |
|---|---|---|
| Entrada `abc` | `ValueError`: invalid literal for int() | `error` de `strconv.Atoi`: invalid syntax |
| Prueba deliberadamente fallida | Traceback y `AssertionError`, línea 15 | Mensaje de `testing` con `main_test.go:34` |
| Qué se distribuye | Fuente `puertos.py` (951 bytes) más un intérprete compatible | Binario reconstruido de 2186306 bytes para Linux amd64 |
| Variable local no utilizada | Se ejecuta: experimento de apoyo en `evidencias/variable-no-usada.txt` | Error de compilación: declared and not used, mismo registro |
| Tratamiento de errores | Excepciones capturadas | Retorno de error y comprobación explícita |

Los tamaños no incluyen las mismas cosas: un `.py` no incluye CPython. El ejemplo de variable local no usada se mantiene separado del programa entregado para no romper su compilación.
