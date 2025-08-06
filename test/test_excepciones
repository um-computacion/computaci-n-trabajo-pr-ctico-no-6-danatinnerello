from src.excepciones import Exceptions, CasillaFueradeRango, PosOcupadaExceptions
import unittest


class TestExcepciones(unittest.TestCase):
    
    def test_pos_ocupada_exception(self):
        with self.assertRaises(PosOcupadaExceptions):
            raise PosOcupadaExceptions()
    
    def test_casilla_fuera_rango_exception(self):
        with self.assertRaises(CasillaFueradeRango):
            raise CasillaFueradeRango()
    
    def test_exceptions_base(self):
        with self.assertRaises(Exceptions):
            raise Exceptions()