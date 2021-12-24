from datetime import datetime
import pandas as pd
import csv

class Historico:

    @staticmethod
    def crear_registro(nombre, acumulado):
        with open('Historico.csv', 'a+', encoding='UTF8', newline='') as historico:
            writer = csv.writer(historico)
            writer.writerow([f"{datetime.now():%Y-%m-%d}", nombre, acumulado])

    @staticmethod
    def leer_registro():
        historico = pd.read_csv('Historico.csv', sep=',').tail()
        return historico.iloc[::-1].reset_index(drop=True)
