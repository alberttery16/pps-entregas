import unittest
from puertos import clasificar_puerto, es_privilegiado

class TestPuertos(unittest.TestCase):
    def test_clasificacion_clases(self):
        self.assertEqual(clasificar_puerto(80), "Sistema (bien conocido)")
        self.assertEqual(clasificar_puerto(8080), "Usuario (registrado)")
        self.assertEqual(clasificar_puerto(50000), "Dinámico o privado")

    def test_puerto_fuera_de_rango(self):
        with self.assertRaises(ValueError):
            clasificar_puerto(65536)

    def test_puerto_privilegiado_fallo(self):
        self.assertTrue(es_privilegiado(8080))

if __name__ == "__main__":
    unittest.main()
