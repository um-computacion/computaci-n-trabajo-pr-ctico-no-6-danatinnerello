# tateti.py
from src.tablero import Tablero
from src.ganador import DetectorGanador
from src.turnos import GestorTurnos

class Tateti:
    def __init__(self, jugador1, jugador2):
        self.tablero = Tablero()
        self.gestor_turnos = GestorTurnos(jugador1, jugador2)
        self.detector_ganador = DetectorGanador(self.tablero)

    @property   #hace que el metodo turno se comporte como un atributo
    def turno(self):
        return self.gestor_turnos.obtener_turno_actual()

    def ocupar_una_de_las_casillas(self, fila, columna):
        self.tablero.poner_la_ficha(fila, columna, self.turno.ficha)
   
    def cambiar_turno(self):
        self.gestor_turnos.cambiar_turno()

    def hay_ganador(self, ficha):
        return self.detector_ganador.hay_ganador(ficha)