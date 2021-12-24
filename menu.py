from historico import Historico
from presentador import Presentador
from reglas import Reglas
from banco_preguntas import BancoPreguntas
from pregunta import Pregunta
import sys


class Menu:
    
    presentador = None
    ronda = 0
    premio_ronda = 500
    acumulado = 0

    @classmethod
    def iniciar_juego(cls):
        while True:
            print('Bienvenido!')
            print('Elija una opción')
            print('1) Conocer las reglas')
            print('2) Ver historial de jugadores')
            print('3) Iniciar juego')
            print('4) Salir')

            opcion = int(input('opcion'))
            
            if opcion==1:
                reglas=Reglas()

            elif opcion==2:
                print(Historico.leer_registro())
                
            elif opcion==3:
                cls.presentador=Presentador()
                validar=Pregunta()
                saludar=cls.presentador.bienvenida()
                for ronda_juego in range(1,6):
                    cls.ronda = ronda_juego
                    banco_preguntas = BancoPreguntas()
                    print(f'{ronda_juego} ronda por {cls.premio_ronda*ronda_juego}')
                    pregunta = banco_preguntas.seleccionar_pregunta(ronda_juego)
                    print(pregunta.sentencia)
                    print('1)',pregunta.opciones[0])
                    print('2)',pregunta.opciones[1])
                    print('3)',pregunta.opciones[2])
                    print('4)',pregunta.opciones[3])
                    #print(pregunta.respuesta)
                    eleccion=int(input('Elija una opcion :  '))
                    if pregunta.respuesta==eleccion:
                        print('Enhorabuena \n')
                        cls.acumulado += cls.premio_ronda * ronda_juego
                        print(f'Su acumulado es: {cls.acumulado}')
                        if ronda_juego < 5:
                            salirse=int(input("Desea continuar?: 1.Si  2.No\n"))
                            if salirse == 2:
                                break
                    else:
                        print('El juego ha terminado')
                        print('gracias por participar')
                        cls.acumulado = 0
                        print(f'Su acumulado es: {cls.acumulado}')
                        break
                print('fin del juego')
                Historico.crear_registro(cls.presentador.nombre, cls.acumulado)
                sys.exit()
                

            elif opcion==4:
                print('¡Hasta la proxima!')
                sys.exit()
            else:
                print('elija una opción correcta')
    pass
