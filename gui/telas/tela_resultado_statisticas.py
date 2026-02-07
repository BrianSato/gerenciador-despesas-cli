import tkinter as tk
from tkinter import ttk
from core.despesas_estatisticas_core import *
from gui.widgets.mensagem_gui import MensagemGUI

class TelaResultadoEstatistica(ttk.Frame):
    def __init__(self,parent,controller,lista_mes_ano):
        super().__init__(parent)
        self.lista_mes_ano = lista_mes_ano
        self.controller = controller
        self._criar_widgets()
        self.carregar_dados()

    def _criar_widgets(self):

        ttk.Label(self,text = "Opções de Estatisticas",font = ("Arial", 14)
        ).grid(row=0, column=0,columnspan=2, pady=10)

        colunas = ("valor", "descricao", "categoria", "data")

        self.tabela = ttk.Treeview(self, columns=colunas, show="headings")
        self.tabela.heading("valor", text="Valor"),
        self.tabela.heading("descricao", text="Descrição"),
        self.tabela.heading("categoria", text="Categoria"),
        self.tabela.heading("data", text="Data")

        for col in colunas:
            self.tabela.column(col, anchor="center")

        self.tabela.grid(row=2, column=0, pady=5)

        ttk.Button(self,text="Mostrar Maior Despesa", command=self.clicou_maior_despesa
        ).grid(row=3,column=0,sticky="w", pady=7)

        ttk.Button(self, text="Mostrar Menor Despesa", command=self.clicou_menor_despesa
        ).grid(row=3, column=1, sticky="w", pady=7)

        ttk.Button(self, text="Mostrar Média Mensal", command=self.clicou_media_despesa
        ).grid(row=4, column=0, sticky="w", pady=7)

        ttk.Button(self, text="Mostrar Total de Depesas", command=self.clicou_total_despesa
        ).grid(row=4, column=1, pady=7)

        ttk.Button(self,text="👈 Voltar",command = lambda :self.controller.mostrar_tela("menu")
        ).grid(row=5,column=2,columnspan=2,pady=5)

        self.mensagem = MensagemGUI(self)
        self.mensagem.grid(row=1, column=0, columnspan=2, pady=(0, 10))

    def carregar_dados(self):
            dados = self.lista_mes_ano

            for despesa in dados:
                self.tabela.insert(
                    "",
                    "end",
                    values = (
                        despesa.get("valor",""),
                        despesa.get("descricao",""),
                        despesa.get("categoria",""),
                        despesa.get("data","")
                    )
                )


    def clicou_maior_despesa(self):
        res_maior = processar_maior_despesa(self.lista_mes_ano)#envia para o CORE processar
        self.mensagem.sucesso(f"O maior valor é: R$ {res_maior:.2f}")
    def clicou_menor_despesa(self):
        res_menor = processar_menor_despesa(self.lista_mes_ano)# envia para o CORE processar
        self.mensagem.sucesso(f"O menor valor é: R$ {res_menor:.2f}")
    def clicou_media_despesa(self):
        res_media = processar_media_despesa(self.lista_mes_ano)# envia para o CORE processar
        self.mensagem.sucesso(f"A média de despesa é: R$ {res_media: .2f}")
    def clicou_total_despesa(self):
        res_total = processar_total_despesa(self.lista_mes_ano)# envia para o CORE processar
        self.mensagem.sucesso(f"O total de despesas é: R$ {res_total: .2f}")