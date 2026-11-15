package main

import "testing"

func TestClasificacionClases(t *testing.T) {
	casos := []struct {
		puerto   int
		esperado string
	}{
		{80, "Sistema (bien conocido)"},
		{8080, "Usuario (registrado)"},
		{50000, "Dinámico o privado"},
	}
	for _, c := range casos {
		obtenido, err := ClasificarPuerto(c.puerto)
		if err != nil {
			t.Fatalf("Error inesperado en puerto %d: %v", c.puerto, err)
		}
		if obtenido != c.esperado {
			t.Errorf("Puerto %d: esperado '%s', obtenido '%s'", c.puerto, c.esperado, obtenido)
		}
	}
}

func TestPuertoFueraDeRango(t *testing.T) {
	_, err := ClasificarPuerto(65536)
	if err == nil {
		t.Errorf("Se esperaba error para puerto 65536 y se obtuvo nil")
	}
}

func TestPuertoPrivilegiadoFallo(t *testing.T) {
	if !EsPrivilegiado(8080) {
		t.Errorf("Fallo intencionado: se esperaba true para puerto 8080 y se obtuvo false")
	}
}
