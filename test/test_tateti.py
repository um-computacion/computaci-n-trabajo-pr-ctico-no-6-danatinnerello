# test_tateti.py
import unittest
from src.tateti import Tateti
from src.jugador import Jugador
from src.excepciones import CasillaFueradeRango, PosOcupadaExceptions

class TestTateti(unittest.TestCase):
    
    def setUp(self):
        self.jugador1 = Jugador("Ana", "X")
        self.jugador2 = Jugador("Luis", "O")
        self.juego = Tateti(self.jugador1, self.jugador2)

    def test_inicializacion_correcta(self):
        self.assertEqual(self.juego.turno, self.jugador1)
        self.assertFalse(self.juego.tablero.esta_lleno())

    def test_ocupar_casilla_valida(self):
        self.juego.ocupar_una_de_las_casillas(1,1)
    
        contenedor = self.juego.tablero.obtener_contenedor()
        self.assertEqual(contenedor[1][1], "X")

    def test_cambiar_turno_funciona(self):
        self.assertEqual(self.juego.turno, self.jugador1)
        
        # Cambiar turno
        self.juego.cambiar_turno()
        self.assertEqual(self.juego.turno, self.jugador2)
        

    def test_detecta_ganador_fila(self):
        self.juego.ocupar_una_de_las_casillas(0,0)  
        self.juego.ocupar_una_de_las_casillas(0,1)  
        self.juego.ocupar_una_de_las_casillas(0,2)  
        
        self.assertTrue(self.juego.hay_ganador("X"))
        self.assertFalse(self.juego.hay_ganador("O"))

    def test_detecta_ganador_columna(self):
        self.juego.ocupar_una_de_las_casillas(0,1)  
        self.juego.ocupar_una_de_las_casillas(1,1)  
        self.juego.ocupar_una_de_las_casillas(2,1)  
        
        self.assertTrue(self.juego.hay_ganador("X"))

    def test_detecta_ganador_diagonal(self):
        self.juego.ocupar_una_de_las_casillas(0,0)  
        self.juego.ocupar_una_de_las_casillas(1,1)  
        self.juego.ocupar_una_de_las_casillas(2,2)  
        
        self.assertTrue(self.juego.hay_ganador("X"))


    def test_excepcion_casilla_ocupada(self):
        self.juego.ocupar_una_de_las_casillas(1,1)
    
        with self.assertRaises(PosOcupadaExceptions):
            self.juego.ocupar_una_de_las_casillas(1,1)

    def test_excepcion_casilla_fuera_de_rango(self):
        with self.assertRaises(CasillaFueradeRango):
            self.juego.ocupar_una_de_las_casillas(-1,0)
        
        with self.assertRaises(CasillaFueradeRango):
            self.juego.ocupar_una_de_las_casillas(3,0)
        
        with self.assertRaises(CasillaFueradeRango):
            self.juego.ocupar_una_de_las_casillas(0,-1)
        
        with self.assertRaises(CasillaFueradeRango):
            self.juego.ocupar_una_de_las_casillas(0,3)

   
if __name__ == '__main__':
    unittest.main()