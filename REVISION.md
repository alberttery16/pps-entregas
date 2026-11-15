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
