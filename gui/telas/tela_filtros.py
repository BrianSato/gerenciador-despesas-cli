import tkinter as tk
from tkinter import ttk
from gui.config.estilos import *

class TelaFiltros(ttk.Frame):
    def __init__(self,parent,controller):
        super().__init__(parent)
        self.controller = controller
        self._configurar_grid()
        self.criar_widgets()

    def _configurar_grid(self):
        self.grid_columnconfigure(0,weight=1)

    def criar_widgets(self):
        #SubTitulo
        ttk.Label(self,text="Opções de Filtros:",font=(FONTE_SUBTITULO)
        ).grid(row=0,column=0,pady=(PADY_PADRAO_SUBTITULO),sticky="n")

        #Botões
        ttk.Button(self,text="Filtrar por Categoria",width=(WIDGET_PADRAO),command=lambda:self.controller.mostrar_tela("filtro_categoria")
            ).grid(row=1, column=0, pady=(PADY_BOTAO))

        ttk.Button(self, text="Filtrar por Periodo", width=(WIDGET_PADRAO),command=lambda: self.controller.mostrar_tela("filtro_periodo")
            ).grid(row=2, column=0, pady=(PADY_BOTAO))

        ttk.Button(self, text="👈 Voltar", width=(WIDGET_PADRAO),command=lambda: self.controller.mostrar_tela("menu")
            ).grid(row=3, column=0, pady=(PADY_BOTAO))