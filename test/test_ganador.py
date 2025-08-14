# test_detector_ganador.py
import unittest
from src.tablero import Tablero
from src.ganador import DetectorGanador

class TestDetectorGanador(unittest.TestCase):
    
    def setUp(self):
        self.tablero = Tablero()
        self.detector = DetectorGanador(self.tablero)

    def test_no_hay_ganador_tablero_vacio(self):
        result = self.detector.hay_ganador("X")
        self.assertFalse(result)

    def test_ganador_fila_0(self):
        self.tablero.poner_la_ficha(0, 0, "X")
        self.tablero.poner_la_ficha(0, 1, "X")
        self.tablero.poner_la_ficha(0, 2, "X")
        
        result = self.detector.hay_ganador("X")
        self.assertTrue(result)

    def test_ganador_fila_1(self):
        self.tablero.poner_la_ficha(1,0, "O")
        self.tablero.poner_la_ficha(1,1, "O")
        self.tablero.poner_la_ficha(1,2, "O")
        
        result = self.detector.hay_ganador("O")
        self.assertTrue(result)

    def test_ganador_fila_2(self):
        self.tablero.poner_la_ficha(2,0,"X")
        self.tablero.poner_la_ficha(2,1,"X")
        self.tablero.poner_la_ficha(2,2,"X")
        
        result = self.detector.hay_ganador("X")
        self.assertTrue(result)

    def test_ganador_columna_0(self):
        self.tablero.poner_la_ficha(0,0,"X")
        self.tablero.poner_la_ficha(1,0,"X")
        self.tablero.poner_la_ficha(2,0, "X")
        
        result = self.detector.hay_ganador("X")
        self.assertTrue(result)

    def test_ganador_columna_1(self):
       
        self.tablero.poner_la_ficha(0,1,"O")
        self.tablero.poner_la_ficha(1,1,"O")
        self.tablero.poner_la_ficha(2,1,"O")
        
        result = self.detector.hay_ganador("O")
        self.assertTrue(result)

    def test_ganador_columna_2(self):
    
        self.tablero.poner_la_ficha(0,2,"X")
        self.tablero.poner_la_ficha(1,2,"X")
        self.tablero.poner_la_ficha(2,2,"X")
        
        result = self.detector.hay_ganador("X")
        self.assertTrue(result)

    def test_ganador_diagonal_principal(self):
        self.tablero.poner_la_ficha(0,0,"O")
        self.tablero.poner_la_ficha(1,1,"O")
        self.tablero.poner_la_ficha(2,2,"O")
        
        result = self.detector.hay_ganador("O")
        self.assertTrue(result)

    def test_ganador_diagonal_secundaria(self):
        self.tablero.poner_la_ficha(0,2,"X")
        self.tablero.poner_la_ficha(1,1,"X")
        self.tablero.poner_la_ficha(2,0,"X")
        
        result = self.detector.hay_ganador("X")
        self.assertTrue(result)

    def test_no_hay_ganador_ficha_diferente(self):
        self.tablero.poner_la_ficha(0,0,"X")
        self.tablero.poner_la_ficha(0,1,"X")
        self.tablero.poner_la_ficha(0,2,"X")
        
      
        result = self.detector.hay_ganador("O")
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()