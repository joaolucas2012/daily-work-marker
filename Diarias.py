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