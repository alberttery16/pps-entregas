# Comprobación de la revisión

Pruebas ejecutadas en Linux durante la revisión, no en el ordenador del alumno. Los códigos 1 indicados en las suites son los fallos deliberados exigidos por la rúbrica.

- `ut1/a14`: `python3 -m unittest -v` → estado 1.
- `ut1/a15`: `go test -v` → estado 1.
- `ut1/a15`: `go vet .` → estado 0.
- `ut1/a15`: `gofmt -l .` → estado 0.
- `ut1/a16`: `bash -n puertos.sh` → estado 0.
- `ut1/a16`: `shellcheck puertos.sh experimentos/ejecutar.sh` → estado 0.
- `ut1/a16`: `bash -n LearnBash.sh` → estado 0.
- `ut1/a16`: `./puertos.sh 0 1023 1024 49151 49152 65535 00080` → estado 0.
- `ut1/a16`: `./puertos.sh abc 70000 * 99999999999999999999999999` → estado 1.
- `ut1/a16`: `bash experimentos/ejecutar.sh` → estado 0.

Se comprobaron también los enlaces relativos y los ocho/siete apartados de a16/a17. Pendientes: capturas personales, ejecución con ptrace (GDB/strace), materiales del aula y logros de los cursos. Consultar el README principal.

## Cierre del código de las actividades 2 y 3

- `ut1/a14` · `python3 -m unittest -v` → 1.
- `ut1/a15` · `go test -v` → 1.
- `ut1/a15` · `go vet .` → 0.
- `ut1/a15` · `gofmt -l .` → 0.
- `ut1/a15` · `go build -o /tmp/pps-final-go` → 0.
- `ut1/a16` · `shellcheck puertos.sh experimentos/ejecutar.sh` → 0.
- `ut1/a16` · `bash -n LearnBash.sh` → 0.
- `ut1/a16` · `bash experimentos/ejecutar.sh` → 0.
- `ut1/a16` · `bash puertos.sh 0` → 0.
- `ut1/a16` · `bash puertos.sh 1023` → 0.
- `ut1/a16` · `bash puertos.sh 1024` → 0.
- `ut1/a16` · `bash puertos.sh 49151` → 0.
- `ut1/a16` · `bash puertos.sh 49152` → 0.
- `ut1/a16` · `bash puertos.sh 65535` → 0.
- `ut1/a16` · `bash puertos.sh abc 70000 *` → 1.

Verificados los enlaces, los JSON de VS Code y los ocho apartados de Bash. LearnBash coincide byte a byte con el adjunto. La traza adicional de pdb acredita dos paradas reales, con numero=22 y numero=8080. Siguen pendientes las capturas de VS Code de la actividad 2 y contrastar el script Bash con el original de los apuntes; estos requisitos no se dan por cumplidos.
