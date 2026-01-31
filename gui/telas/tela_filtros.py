import tkinter as tk
from tkinter import ttk
from core.despesas_mensagens_core import CATEGORIAS,ERROS
from core.despesas_validacoes_core import validar_categoria
from core.despesas_filtrar_core import filtrar_por_periodo
from gui.telas.tela_filtro_categoria import TelaFiltroCategoria
from gui.widgets.mensagem_gui import MensagemGUI



class TelaFiltros(ttk.Frame):
    def __init__(self,parent,voltar_callback,mostrar_tela,filtrar_categoria_callback,filtrar_periodo_callback):
        super().__init__(parent)
        self.voltar_callback = voltar_callback
        self.mostrar_tela = mostrar_tela
        self.filtrar_categoria_callback = filtrar_categoria_callback
        self.filtrar_periodo_callback = filtrar_periodo_callback
        self.criar_widgets()

    def criar_widgets(self):

        ttk.Label(self,text="Opções de Filtros:",font=("Arial",14)
        ).grid(row=0,column=0,columnspan=2,pady=10)

        ttk.Button(self,text="Categoria",command=self.clicou_categoria
        ).grid(row=2, column=0, pady=5)

        ttk.Button(self, text="Data", command=self.clicou_periodo
        ).grid(row=3, column=0, pady=5)

        ttk.Button(self,text="👈 Voltar",command=self.voltar_callback
        ).grid(row=4, column=0,pady=5)

        self.mensagem = MensagemGUI(self)
        self.mensagem.grid(row=1, column=0, columnspan=2, pady=(0, 10))

    def clicou_categoria(self):
        self.filtrar_categoria_callback()

    def clicou_periodo(self):
        self.filtrar_periodo_callback()