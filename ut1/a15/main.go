package main

import (
	"errors"
	"fmt"
	"os"
	"strconv"
)

const (
	LimiteSistema = 1023
	LimiteUsuario = 49151
	LimiteMaximo  = 65535
)

// 1. FUNCIÓN (Línea 17)
func ClasificarPuerto(numero int) (string, error) {
	// 4. CASO DE ERROR (Líneas 19-21)
	if numero < 0 || numero > LimiteMaximo {
		return "", errors.New(fmt.Sprintf("puerto fuera de rango válido (0-%d): %d", LimiteMaximo, numero))
	}
	// 2. DECISIÓN (Líneas 23-30)
	switch {
	case numero <= LimiteSistema:
		return "Sistema (bien conocido)", nil
	case numero <= LimiteUsuario:
		return "Usuario (registrado)", nil
	default:
		return "Dinámico o privado", nil
	}
}

func EsPrivilegiado(numero int) bool {
	return numero >= 0 && numero <= LimiteSistema
}

func main() {
	if len(os.Args) < 2 {
		fmt.Println("Uso: go run . <puerto1> <puerto2> ...")
		os.Exit(1)
	}
	// 3. BUCLE (Líneas 42-55)
	for _, arg := range os.Args[1:] {
		puerto, err := strconv.Atoi(arg)
		if err != nil {
			fmt.Printf("Error procesando '%s': valor no numérico (%v)\n", arg, err)
			continue
		}
		clase, err := ClasificarPuerto(puerto)
		if err != nil {
			fmt.Printf("Error procesando '%d': %v\n", puerto, err)
			continue
		}
		fmt.Printf("Puerto %d: %s\n", puerto, clase)
	}
}
