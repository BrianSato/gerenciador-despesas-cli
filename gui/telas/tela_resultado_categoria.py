import tkinter as tk
from tkinter import ttk
from core.despesas_filtrar_core import filtrar_por_categoria
from gui.config.estilos import *

class TelaResultadoCategoria(ttk.Frame):
    def __init__(self, parent,categoria, controller):
        super().__init__(parent)
        self.categoria = categoria
        self.controller = controller
        self.criar_widgets()
        self.carregar_dados()


    def criar_widgets(self):
        #Subtitulo
        titulo = ttk.Label(self, text="Lista De despesas por Categoria", font=(FONTE_SUBTITULO))
        titulo.pack(pady=10)

        #Tabela
        colunas = ("valor", "descricao", "categoria", "data")

        self.tabela = ttk.Treeview(self, columns=colunas, show="headings")
        self.tabela.heading("valor", text="Valor"),
        self.tabela.heading("descricao", text="Descrição"),
        self.tabela.heading("categoria", text="Categoria"),
        self.tabela.heading("data", text="Data")

        for col in colunas:
            self.tabela.column(col, anchor="center")

        self.tabela.pack(fill="both", expand=True, padx=10, pady=10)

        #Botões
        ttk.Button(self, text="👈 Voltar Tela Filtros",width=(WIDGET_PADRAO), command=lambda :self.controller.mostrar_tela("filtro")
        ).pack(pady=10)

        ttk.Button(self, text="👈 Voltar Menu Inicial",width=(WIDGET_PADRAO), command=lambda :self.controller.mostrar_tela("menu")
        ).pack(pady=10)

    def carregar_dados(self):
        dados = filtrar_por_categoria(self.categoria)

        for despesa in dados:
            self.tabela.insert(
                "",
                "end",
                values=(
                    despesa.get("valor", ""),
                    despesa.get("descricao", ""),
                    despesa.get("categoria", ""),
                    despesa.get("data", "")
                )
            )