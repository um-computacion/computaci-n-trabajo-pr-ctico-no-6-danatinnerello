
class DetectorGanador:
    def __init__(self, tablero):
        self.tablero = tablero

    def hay_ganador(self, ficha):
        return (self._verificar_filas(ficha) or
                self._verificar_columnas(ficha) or
                self._verificar_diagonales(ficha))
    
    def _verificar_filas(self, ficha):
        for fila in self.tablero.obtener_contenedor():
            if fila == [ficha, ficha, ficha]:
                return True
        return False
          
    def _verificar_columnas(self, ficha):
        for columna in range(3):
            if [self.tablero.obtener_contenedor()[fila][columna] for fila in range(3)] == [ficha, ficha, ficha]:
                return True
        return False
            
    def _verificar_diagonales(self, ficha):
        # diagonal de izquierda a derecha
        if [self.tablero.obtener_contenedor()[i][i] for i in range(3)] == [ficha, ficha, ficha]:
            return True
        
        # diagonal de derecha a izquierda
        if [self.tablero.obtener_contenedor()[i][2 - i] for i in range(3)] == [ficha, ficha, ficha]:
            return True
        
        return False