import tkinter as tk
from tkinter import ttk
from core.despesas_mensagens_core import MESES,ERROS
from core.despesas_filtrar_core import filtrar_anos_disponiveis
from core.despesas_filtrar_core import filtrar_por_mes_ano
from core.despesas_arquivo_core import carregar_despesas
from gui.widgets.mensagem_gui import MensagemGUI

class TelaFiltroEstatistica(ttk.Frame):
    def __init__(self,parent,controller):
        super().__init__(parent)
        self.despesas = carregar_despesas()#carregou o arquivo em despesas_arquivo_CORE
        self.anos = filtrar_anos_disponiveis(self.despesas)#chamou funcao do do CORE levando os dados do arquivo
        self.anos_str = [str(ano)for ano in self.anos]#recebeu o resultado da funcao acima e converteu em STRING
        self.controller=controller
        self.criar_widgets()

    def criar_widgets(self):

        ttk.Label(self,text="Estatísticas de Despesas:",font=("Arial",14)
        ).grid(row=0,column=0,columnspan=2,pady=10)

        ttk.Label(self, text="Mês").grid(row=2, column=0, sticky="w", pady=7)
        self.data_mes = tk.StringVar()
        self.combo_mes = ttk.Combobox(
            self,
            textvariable=self.data_mes,
            values=list(MESES.keys()),
            state="readonly"
        )
        self.combo_mes.grid(row=2, column=1, pady=5)
        self.combo_mes.set("Escolha o mês")

        ttk.Label(self, text="Ano").grid(row=3, column=0, sticky="w", pady=7)
        self.data_ano = tk.StringVar()
        self.combo_ano = ttk.Combobox(
            self,
            textvariable=self.data_ano,
            values=self.anos_str,
            state="readonly"
        )
        self.combo_ano.grid(row=3, column=1, pady=5)
        self.combo_ano.set("Escolha o Ano")

        ttk.Button(self, text="Próxima página", command=self.processar_filtro_estatistica
                   ).grid(row=4, column=0, pady=5)

        ttk.Button(self, text="👈 Voltar Menu", command=lambda :self.controller.mostrar_tela("menu")
                   ).grid(row=5, column=0, pady=5)

        self.mensagem = MensagemGUI(self)
        self.mensagem.grid(row=1, column=0, columnspan=2, pady=(0, 10))


    def processar_filtro_estatistica(self):

        despesas = carregar_despesas()
        mes_nome = self.data_mes.get()#Pega o valor informado pelo usuário (ainda em formato "Janeiro")
        mes = MESES.get(mes_nome)  # Pega MES_NOME e converte para o valor correspondente dentro do dicionpario MESES
        if mes is None:
            self.mensagem.erro(ERROS["erro_mes"])
            return
        try:
            ano = int(self.data_ano.get())  # Pega o valor informado pelo usuário e transforma em formato INT
        except ValueError:
            self.mensagem.erro(ERROS["erro_ano"])
            return

        lista_mes_ano = filtrar_por_mes_ano(despesas, mes,ano)
        self.controller.mostrar_tela("resultado_estatistica",lista_mes_ano = lista_mes_ano)
        # Chama a funcao no CORE para fazer a filtragem com base nos valores informados pelo usuário.
        #devolve lista_mes_ano


