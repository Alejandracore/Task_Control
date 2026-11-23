import unittest
import gestion_de_tareas as main
class TestTaskControl(unittest.TestCase):

    def setUp(self):   
        main.tareas.clear()
        main.siguiente_id = 1

    def test_completar_tarea(self):
        main.registrar_tarea("Estudiar Python")

        resultado = main.cambiar_estado(1, True)

        self.assertTrue(resultado)
        self.assertTrue(main.tareas[0].completada)


if __name__ == "__main__":
    unittest.main()