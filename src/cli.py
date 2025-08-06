from src.tateti import Tateti
from src.tablero import Tablero
from src.excepciones import Exceptions , CasillaFueradeRango, PosOcupadaExceptions


def main():
    print ("Bienvenidos")
    juego = Tateti()
    while True:
        print("Tablero...")
        print(juego.tablero.mostrar_tablero())
        print("Turno: ")
        print(juego.turno)
        try:
            fila = int(input("ingrese fila entre 0 y 2: "))
            columna = int(input("Ingrese columna entre 0 y 2: "))

            juego.ocupar_una_de_las_casillas(fila,columna)
            print("ficha puesta")

            ganador = juego.turno
            if juego.hay_ganador(ganador):
                juego.tablero.mostrar_tablero()
                print(f"El ganador es {ganador}")
                break
            elif juego.tablero.esta_lleno():
                juego.tablero.mostrar_tablero()
                print("El juego ha terminado en empate")
                break
           
            juego.cambiar_turno()
        except CasillaFueradeRango as e:
            print("Esta casilla esta fuera de rango. Elije una entre 0 y 2")
        except PosOcupadaExceptions as e:
            print("Esta casilla ya esta ocupada. Elije otra")
        except Exceptions as e:
            print(e)
            continue 

if __name__ == '__main__':
    main()