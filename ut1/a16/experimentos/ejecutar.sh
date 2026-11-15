#!/usr/bin/env bash
# Los fallos deliberados son resultados; un fallo inesperado hace fallar la revisión.
set -uo pipefail
cd -- "$(dirname -- "$0")" || exit 1
for herramienta in bash python3 go; do
    if ! command -v "$herramienta" >/dev/null 2>&1; then
        printf 'Falta la herramienta: %s\n' "$herramienta" >&2
        exit 1
    fi
done
if ! go version >/dev/null 2>&1 || ! python3 --version >/dev/null 2>&1; then
    printf 'No se puede ejecutar Go o Python 3; no se sobrescriben las evidencias.\n' >&2
    exit 1
fi
mkdir -p salidas || exit 1
estado_global=0
for caso in tipos indice desbordamiento inyeccion; do
    for lenguaje in bash python go; do
        case "$lenguaje" in
            bash) orden=(bash "$caso.sh") ;;
            python) orden=(python3 "$caso.py") ;;
            go) orden=(go run "$caso/main.go") ;;
        esac
        esperado=0
        if [[ $caso == tipos || $caso == indice ]] && [[ $lenguaje != bash ]]; then
            esperado=1
        fi
        "${orden[@]}" >"salidas/${caso}_${lenguaje}.txt" 2>&1
        estado=$?
        printf '\nCódigo de salida: %s\n' "$estado" >>"salidas/${caso}_${lenguaje}.txt"
        if (( estado != esperado )); then
            printf '%s/%s: estado esperado %s, obtenido %s\n' "$caso" "$lenguaje" "$esperado" "$estado" >&2
            estado_global=1
        fi
    done
done
bash extra_nounset.sh > salidas/extra_nounset.txt 2>&1
estado=$?
printf '\nCódigo de salida: %s\n' "$estado" >> salidas/extra_nounset.txt
if (( estado != 1 )); then
    printf 'nounset: estado esperado 1, obtenido %s\n' "$estado" >&2
    estado_global=1
fi
exit "$estado_global"
