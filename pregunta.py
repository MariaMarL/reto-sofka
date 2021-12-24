from typing import List


class Pregunta:

    def __init__(self, ronda: int = 0, sentencia: str = None, opciones: List[str] = None, respuesta: int = 0) -> None:
        self.ronda = ronda
        self.sentencia = sentencia
        self.opciones = opciones
        self.respuesta = respuesta

    def parse_pregunta(self, pregunta_dataframe):
        self.sentencia = pregunta_dataframe["pregunta"].values[0]
        self.opciones = [pregunta_dataframe["R1"].values[0], pregunta_dataframe["R2"].values[0], pregunta_dataframe["R3"].values[0], pregunta_dataframe["R4"].values[0]]
        self.respuesta = int(pregunta_dataframe["respuesta"].values[0])

    