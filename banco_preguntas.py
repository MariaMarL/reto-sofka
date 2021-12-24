from typing import List
import pandas as pd

from pregunta import Pregunta

class BancoPreguntas:

    def __init__(self) -> None:
        url='https://drive.google.com/uc?id=1KYROAYVd476iSge4cPqdUiaZj4jN00TA&export=download&authuser=0'
        self.banco_preguntas = pd.read_csv(url, sep=';')

    def filtrar_por_ronda(self, ronda: int):
        return self.banco_preguntas[self.banco_preguntas["ronda"]==ronda]


    def seleccionar_pregunta(self, ronda_pregunta:int) -> Pregunta:
        pregunta_seleccionada = Pregunta(ronda=ronda_pregunta)
        
        pregunta_base = self.filtrar_por_ronda(ronda_pregunta).sample()
        pregunta_seleccionada.parse_pregunta(pregunta_base)

        return pregunta_seleccionada
