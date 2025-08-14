
class GestorTurnos:
    def __init__(self, jugador1, jugador2):
        self.jugador1 = jugador1
        self.jugador2 = jugador2
        self.turno = self.jugador1

    def cambiar_turno(self):
        if self.turno == self.jugador1:
            self.turno = self.jugador2
        else:
            self.turno = self.jugador1

    def obtener_turno_actual(self):
        return self.turno