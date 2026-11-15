#!/usr/bin/env bash
entrada='hola; echo ORDEN_INYECTADA'
printf 'INSEGURO: texto concatenado (2 órdenes echo)\n'
bash -c "echo $entrada"
printf 'SEGURO: argumento separado (1 orden echo)\n'
bash -c 'echo "$1"' _ "$entrada"
