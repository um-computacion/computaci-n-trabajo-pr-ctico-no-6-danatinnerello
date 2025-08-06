from src.tateti import Tateti
from src.tablero import Tablero
import unittest 



class TestTateti(unittest.TestCase):
    
    def test_init(self):
        juego = Tateti()
        self.assertEqual(juego.turno, "X")
        self.assertIsInstance(juego.tablero, Tablero)
    
    def test_ocupar_casilla(self):
        juego = Tateti()
        juego.ocupar_una_de_las_casillas(1, 1)
        self.assertEqual(juego.tablero.obtener_contenedor()[1][1], "X")
    
    def test_cambiar_turno_x_a_o(self):
        juego = Tateti()
        self.assertEqual(juego.turno, "X")
        juego.cambiar_turno()
        self.assertEqual(juego.turno, "0")
    
    def test_cambiar_turno_o_a_x(self):
        juego = Tateti()
        juego.turno = "0"
        juego.cambiar_turno()
        self.assertEqual(juego.turno, "X")
    
    def test_hay_ganador_fila(self):
        juego = Tateti()
        juego.tablero.poner_la_ficha(0, 0, "X")
        juego.tablero.poner_la_ficha(0, 1, "X")
        juego.tablero.poner_la_ficha(0, 2, "X")
        self.assertTrue(juego.hay_ganador("X"))
    
    def test_hay_ganador_columna(self):
        juego = Tateti()
        juego.tablero.poner_la_ficha(0, 0, "X")
        juego.tablero.poner_la_ficha(1, 0, "X")
        juego.tablero.poner_la_ficha(2, 0, "X")
        self.assertTrue(juego.hay_ganador("X"))
    
    def test_hay_ganador_diagonal_principal(self):
        juego = Tateti()
        juego.tablero.poner_la_ficha(0, 0, "X")
        juego.tablero.poner_la_ficha(1, 1, "X")
        juego.tablero.poner_la_ficha(2, 2, "X")
        self.assertTrue(juego.hay_ganador("X"))
    
    def test_hay_ganador_diagonal_secundaria(self):
        juego = Tateti()
        juego.tablero.poner_la_ficha(0, 2, "X")
        juego.tablero.poner_la_ficha(1, 1, "X")
        juego.tablero.poner_la_ficha(2, 0, "X")
        self.assertTrue(juego.hay_ganador("X"))
    
    def test_no_hay_ganador(self):
        juego = Tateti()
        self.assertFalse(juego.hay_ganador("X"))