#!/usr/bin/env bash
# Algunos ejemplos fallan deliberadamente; se registra su estado y se continúa.
set -uo pipefail
cd -- "$(dirname -- "$0")" || exit 1
mkdir -p salidas
for caso in tipos indice desbordamiento inyeccion; do
    for lenguaje in bash python go; do
        case "$lenguaje" in
            bash) orden=(bash "$caso.sh") ;;
            python) orden=(python3 "$caso.py") ;;
            go) orden=(go run "$caso/main.go") ;;
        esac
        "${orden[@]}" >"salidas/${caso}_${lenguaje}.txt" 2>&1
        estado=$?
        printf '\nCódigo de salida: %s\n' "$estado" >>"salidas/${caso}_${lenguaje}.txt"
    done
done
bash extra_nounset.sh > salidas/extra_nounset.txt 2>&1
printf '\nCódigo de salida: %s\n' "$?" >> salidas/extra_nounset.txt
