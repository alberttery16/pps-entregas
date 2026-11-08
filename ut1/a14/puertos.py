import sys

LIMITE_SISTEMA = 1023
LIMITE_USUARIO = 49151
LIMITE_MAXIMO = 65535

def clasificar_puerto(numero: int) -> str:
    if numero < 0 or numero > LIMITE_MAXIMO:
        raise ValueError(f"Puerto fuera de rango válido (0-{LIMITE_MAXIMO}): {numero}")
    if numero <= LIMITE_SISTEMA:
        return "Sistema (bien conocido)"
    elif numero <= LIMITE_USUARIO:
        return "Usuario (registrado)"
    else:
        return "Dinámico o privado"

def es_privilegiado(numero: int) -> bool:
    return 0 <= numero <= LIMITE_SISTEMA

def main():
    if len(sys.argv) < 2:
        print("Uso: python3 puertos.py <puerto1> <puerto2> ...")
        sys.exit(1)
    for arg in sys.argv[1:]:
        try:
            puerto = int(arg)
            clase = clasificar_puerto(puerto)
            print(f"Puerto {puerto}: {clase}")
        except ValueError as err:
            print(f"Error procesando '{arg}': {err}")

if __name__ == "__main__":
    main()
