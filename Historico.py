import tkinter as tk
from tkinter import messagebox
import os.path
import pickle
 
# Exceptions de tratamento de erros
# Caso não haja dados cadastrados para tal operação
class NaoHaDados(Exception):
    pass


#  Classe que representa um histórico de diárias registradas
class Historico:
    def __init__(self):

        # Lista de diarias recebidas
        self.__diariasRecebidas = []

        # Lista de diarias pendentes
        self.__diariasPendentes = []

    # Método que retorna a lista de diarias recebidas
    def getDiariasRecebidas(self):
        return self.__diariasRecebidas
    
    # Método que retorna a lista de diarias pendentes
    def getDiariasPendentes(self):
        return self.__diariasPendentes
    
    # Método que adiciona uma diaria nova a lista de diarias recebidas
    def addDiariaRecebida(self, diaria):
        self.__diariasRecebidas.append(diaria)

    # Método que adiciona uma diaria nova a lista de diarias pendentes
    def addDiariaPendente(self, diaria):
        self.__diariasPendentes.append(diaria)

# Criando uma janela de consulta de históricos
class LimiteConsultaHistorico(tk.Toplevel):
    # Personalizando a janela de consulta de históricos
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('250x100')
        self.title("Consultar Histórico de Diárias")
        self.controle = controle

        # Frame de enunciado
        self.frameEnunciado = tk.Frame(self)
        self.frameEnunciado.pack()
        self.labelEnunciado = tk.Label(self.frameEnunciado, text='Escolha o histórico que deseja consultar:\n\n', font = ('Arial', 10))
        self.labelEnunciado.pack()

        # Frame dos botões
        self.frameButtons = tk.Frame(self)
        self.frameButtons.pack()

        # Botão de diárias recebidas
        self.buttonDiariasRecebidas = tk.Button(self.frameButtons, text='Diarias recebidas', font = ('Negrito', 10))
        self.buttonDiariasRecebidas.pack(side='left')
        self.buttonDiariasRecebidas.bind("<Button>", controle.MostraRecebidas)

        # Botão de diárias pendentes
        self.buttonDiariasPendentes = tk.Button(self.frameButtons, text='Diarias pendentes', font = ('Negrito', 10))
        self.buttonDiariasPendentes.pack(side='left')
        self.buttonDiariasPendentes.bind("Button", controle.MostraPendentes)

# Criando um controle para o histórico
class CtrlHistorico():       
    def __init__(self):
        # Verificando se não há dados salvos
        # Se não tiver dados salvos, é criada uma lista que conterá os dados
        if not os.path.isfile("historico.pickle"):
            self.dadosHistorico =  []
            # Os dados são uma instância de Historico, que possui a lista de diárias pendentes e recebidas
            dados = Historico()
            # Essa instâcia de Historico será adicionada à lista dadosHistorico
            self.dadosHistorico.append(dados)

        # Se tiver dados salvos, a lista com os dados é resgatada
        else:
            with open("historico.pickle", "rb") as f:
                self.dadosHistorico = pickle.load(f)
    
    # Função que salva os dados do histórico, se a lista não estiver vazia, claro
    def salvaHistorico(self):
        if len(self.dadosHistorico) != 0:
            with open("historico.pickle","wb") as f:
                pickle.dump(self.dadosHistorico, f)
    
    # Função que mostra mensagens
    def mensagem(self, titulo, msg):
        messagebox.showinfo(titulo, msg)
    
    # Função que retorna o conteúdo da lista dadosHistorico
    def getHistorico(self):
        for dados in self.dadosHistorico:
            return dados

    # Função que chama a janela de consulta de históricos
    def consultaHistorico(self):
        self.limiteCons = LimiteConsultaHistorico(self) 

    # Função que mostra as diárias recebidas
    def MostraRecebidas(self):
        listaDiariasReceb = self.getHistorico().getDiariasRecebidas()
        try: 
            # Se a lista estiver vazia, não há dados cadastrados
            if len(listaDiariasReceb) == 0:
                raise NaoHaDados()
        except NaoHaDados:
            self.mensagem('Não há dados cadastrados', 'Nenhuma diária foi recebida ainda!')   
        else:
            str = ''
            nroDiarias = 0
            salarioTotal = 0
            for diaria in listaDiariasReceb:
                nroDiarias += 1
                salarioTotal += int(diaria.getSalario())
            str += f'Foram recebidas {nroDiarias} diárias.'
            str += 'Valor total recebido em todo o período:\n'
            str += f'R${salarioTotal},00'
            self.mensagem('Histórico de diárias recebidas', str)
    
    # Função que mostra as diárias pendentes
    def MostraPendentes(self):
        listaDiariasPendent = self.getHistorico().getDiariasPendentes()
        try:
            # Se a lista estiver vazia, não há dados cadastrados
            if len(listaDiariasPendent) == 0:
                raise NaoHaDados()
        except NaoHaDados:
            self.mensagem('Não há dados cadastrados', 'Não há diárias pendentes!') 
        else:
            str = 'Estas são as diárias pendentes (que ainda precisam ser recebidas), ordenadas por dia do mês:\n'  
            nroDiarias = 0
            salarioTotal = 0
            for diaria in listaDiariasPendent:
                nroDiarias += 1
                salarioTotal += int(diaria.getSalario())
                str += f'{diaria.getDia()}/{diaria.getMes()}: {diaria.getSalario()}' + '\n'
            str += f'Faltam ser recebidas {nroDiarias} diárias' + '\n'
            str += f'Valor do salário total pendente: R${salarioTotal},00'
            self.mensagem('Histórico de diárias recebidas', str)

