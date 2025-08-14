# test_gestor_turnos.py
import unittest
from src.jugador import Jugador
from src.turnos import GestorTurnos

class TestGestorTurnos(unittest.TestCase):
    
    def setUp(self):
        self.jugador1 = Jugador("Ana", "X")
        self.jugador2 = Jugador("Luis", "O")
        self.gestor = GestorTurnos(self.jugador1, self.jugador2)

    def test_inicializa_con_jugador1(self):
        turno_actual = self.gestor.obtener_turno_actual()
        self.assertEqual(turno_actual, self.jugador1)
        self.assertEqual(turno_actual.nombre, "Ana")
        self.assertEqual(turno_actual.ficha, "X")

    def test_cambiar_turno_a_jugador2(self):
        self.gestor.cambiar_turno()
        turno_actual = self.gestor.obtener_turno_actual()
        self.assertEqual(turno_actual, self.jugador2)
        self.assertEqual(turno_actual.nombre, "Luis")
        self.assertEqual(turno_actual.ficha, "O")


    def test_turno_inicial_es_jugador1(self):
        gestor_nuevo = GestorTurnos(self.jugador2, self.jugador1)  
        turno_actual = gestor_nuevo.obtener_turno_actual()
        self.assertEqual(turno_actual, self.jugador2)  


if __name__ == '__main__':
    unittest.main()