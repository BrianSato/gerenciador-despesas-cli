import tkinter as tk
from tkinter import ttk
from core.despesas_listar_core import listar_despesas
from core.despesas_arquivo_core import carregar_despesas

class TelaListarDespesas(ttk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.criar_widgets()
        self.carregar_dados()

    def criar_widgets(self):
        titulo = ttk.Label(self,text = "Lista De despesas", font=("Aria", 14,"bold"))
        titulo.pack(pady = 10)

        colunas = ("valor", "descricao","categoria","data")

        self.tabela = ttk.Treeview(self, columns=colunas, show = "headings")
        self.tabela.heading("valor",text = "Valor"),
        self.tabela.heading("descricao", text="Descrição"),
        self.tabela.heading("categoria", text="Categoria"),
        self.tabela.heading("data", text="Data")

        for col in colunas:
            self.tabela.column(col, anchor = "center")

        self.tabela.pack(fill = "both", expand = True, padx = 10, pady = 10)

        ttk.Button(self, text="👈 Voltar", command=lambda :self.controller.mostrar_tela("menu")
        ).pack(pady=10)

    def carregar_dados(self):
            despesas = carregar_despesas()
            dados = listar_despesas(despesas)

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
