import tkinter as tk
from tkinter import messagebox
import os.path
import pickle
 
# Classe que representa uma diaria
class Diaria:
    # A diária é ganha em um dia do mês, e possui uma quantia para o salário
    def __init__(self, dia, mes, salario):
        self.__dia = dia 
        self.__mes = mes
        self.__salario = salario
    
    # Método que retorna o dia da diaria
    def getDia(self):
        return self.__dia
    
    # Método que retorna o mês da diaria
    def getMes(self):
        return self.__mes

    # Método que retorna o valor do salário da diaria
    def getSalario(self):
        return self.__salario


# Criando um controle para as diárias
class CtrlDiarias():       
    def __init__(self):
        # Verificando se não há dados salvos
        # Se não tiver dados salvos, é criada uma lista que conterá os dados
        if not os.path.isfile("diarias.pickle"):
            self.diarias = []
        # Se tiver dados salvos, a lista com os dados é resgatada
        else:
            with open("diarias.pickle", "rb") as f:
                self.diarias = pickle.load(f)
    
    # Função que salva os dados das diárias, se a lista não estiver vazia, claro
    def salvaDiarias(self):
        if len(self.diarias) != 0:
            with open("diarias.pickle","wb") as f:
                pickle.dump(self.diarias, f)
    