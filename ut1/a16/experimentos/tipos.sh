#!/usr/bin/env bash
# Sin nounset: Bash interpreta hola como nombre de variable aritmética.
unset hola
texto=hola
printf '%s\n' "$((texto + 1))"
