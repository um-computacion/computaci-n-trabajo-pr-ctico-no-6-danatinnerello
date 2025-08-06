from src.tablero import Tablero

class Tateti:
    def __init__(self): #el constructor es: siempre que
        self.turno = "X"
        self.tablero = Tablero()

    def ocupar_una_de_las_casillas(self,fila,columna):
        # pongo la ficha
        self.tablero.poner_la_ficha(fila,columna, self.turno)
   

        
    def cambiar_turno(self):
        # cambio turno
        if self.turno == "X":
            self.turno = "0"
        else:
            self.turno = "X"


      #condicicon para ganar
    def hay_ganador(self,ficha):
        #fila
        for fila in self.tablero.obtener_contenedor():
            if fila == [ficha, ficha, ficha]:
                return True
          
        #columna
        for columna in range(3):
            if [self.tablero.obtener_contenedor()[fila][columna] for fila in range(3)] == [ficha, ficha, ficha]:
                return True
            
        #diagonal de izquierda a derecha
        if [self.tablero.obtener_contenedor()[i][i] for i in range(3)] == [ficha, ficha, ficha]:
            return True
        
        #diagonal de derecha a izquierda
        if [self.tablero.obtener_contenedor()[i][2 - i] for i in range(3)] == [ficha, ficha, ficha]:
            return True
        
        return False