#!/usr/bin/env bash
# Versión propia: no se adjuntó el script del apartado «Bash por dentro».
set -uo pipefail

clasificar_puerto() {
    local texto=$1 numero
    if [[ ! $texto =~ ^[0-9]+$ ]]; then
        printf 'Error: %s no es un número entero válido\n' "$texto"
        return 1
    fi
    # Quitar ceros iniciales antes de comparar evita octales y desbordamientos.
    while [[ ${#texto} -gt 1 && $texto == 0* ]]; do texto=${texto#0}; done
    if [[ ${#texto} -gt 5 ]] || (( 10#$texto > 65535 )); then
        printf 'Error: %s está fuera del rango 0-65535\n' "$1"
        return 1
    fi
    numero=$((10#$texto))
    if (( numero <= 1023 )); then
        printf 'Sistema (bien conocido)\n'
    elif (( numero <= 49151 )); then
        printf 'Usuario (registrado)\n'
    else
        printf 'Dinámico o privado\n'
    fi
}

if (( $# == 0 )); then
    printf 'Uso: %s <puerto1> <puerto2> ...\n' "$0" >&2
    exit 1
fi
estado=0
for texto in "$@"; do
    if clase=$(clasificar_puerto "$texto"); then
        printf 'Puerto %s: %s\n' "$texto" "$clase"
    else
        printf '%s\n' "$clase" >&2
        estado=1
    fi
done
exit "$estado"
