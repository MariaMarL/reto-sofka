from banco_preguntas import BancoPreguntas

class Presentador:

    def __init__(self):
        self.nombre=input('Ingrese su nombre: ')
           
    
    def bienvenida(self) -> None:
       print('¡Hola',self.nombre,'...¿Ready?')

