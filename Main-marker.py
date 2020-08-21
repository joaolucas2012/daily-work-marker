# Importando bibliotecas para criação de interfaces e para a persistência de arquivos
import tkinter as tk
from tkinter import messagebox
import os.path
import pickle

# Importando Diarias.py e Historico.py
import Diarias as diarias
import Historico as hist

# Criando uma janela principal
class LimitePrincipal():
    def __init__(self, janela, controle):
        self.controle = controle
        self.janela = janela

        # Definindo o tamanho da janela
        self.janela.geometry('330x80')

        # Criando uma barra de menu, com as opções historico, diarias e sair
        self.menubar = tk.Menu(self.janela)        
        self.diariaMenu = tk.Menu(self.menubar)
        self.historicoMenu = tk.Menu(self.menubar)
        self.sairMenu = tk.Menu(self.menubar)    

        # Adicionando opções ao menu Diárias
        self.diariaMenu.add_command(label="Cadastrar", \
                    command=self.controle.insereDiarias)
        self.diariaMenu.add_command(label="Registrar pagamento", \
                    command=self.controle.registraPagamentos)
        self.menubar.add_cascade(label="Diárias", \
                    menu=self.diariaMenu)

        # Adicionando opções ao menu Histórico
        self.historicoMenu.add_command(label="Consultar", \
                    command=self.controle.consultaHistoricos)        
        self.menubar.add_cascade(label="Histórico", \
                    menu=self.historicoMenu)   

        # Adicionando opções ao menu Sair
        self.sairMenu.add_command(label="Salvar tudo", \
                    command=self.controle.salvaDados)
        self.sairMenu.add_command(label="Sair sem salvar", \
                    command=self.controle.fechaJanela)
        self.menubar.add_cascade(label="Sair", \
                    menu=self.sairMenu)

        # Adicionando menu à janela principal
        self.janela.config(menu=self.menubar)

# Criando o controle pricipal
class ControlePrincipal():
    def __init__(self):
        # Criando a janela principal
        self.JanInicio = tk.Tk()

        # Atribuindo o controle das diárias e do histórico ao controle principal
        self.ctrlDiarias = diarias.CtrlDiarias()
        self.ctrlHistorico = hist.CtrlHistorico()

        # Instanciando um janela do tipo limite principal
        self.limite = LimitePrincipal(self.JanInicio, self) 

        # Entitulando a janela
        self.JanInicio.title("Sistema de Registro de Diárias")

        # Inicia o mainloop
        self.JanInicio.mainloop()

    # Função que chama a janela de inserir diárias
    def insereDiarias(self):
        self.ctrlDiarias.insereDiarias()

    # Função que chama a janela de registrar pagamentos
    def registraPagamentos(self):
        self.ctrlDiarias.registraPagamentos()

    # Função que chama a janela de consultar historico
    def consultaHistoricos(self):
        self.ctrlHistorico.consultaHistorico()

    # Função que salva todos os dados
    def salvaDados(self):
        self.ctrlDiarias.salvaDiarias()
        self.ctrlHistorico.salvaHistorico()
        self.JanInicio.destroy()
    
    # Função que fecha a janela sem salvar os dados
    def fechaJanela(self):
        self.JanInicio.destroy()

if __name__ == '__main__':
    c = ControlePrincipal()