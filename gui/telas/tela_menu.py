import tkinter as tk
from tkinter import ttk
from gui.config.estilos import *

class TelaMenu(ttk.Frame):
    def __init__(self,parent,controller):
        super().__init__(parent)
        self.controller=controller
        self._configurar_grid()
        self._criar_widgets()

    def _configurar_grid(self):
        self.grid_columnconfigure(0,weight=1)

    def _criar_widgets(self):
        #SubTitulo
        ttk.Label(self, text="Menu Principal", font=(FONTE_SUBTITULO)
        ).grid(row=0,column=0,pady=(PADY_PADRAO_SUBTITULO),sticky="n")

        #Botoes
        botoes = [
            ("Adicionar Despesa","adicionar"),
            ("Listar Despesa", "listar"),
            ("Filtrar Despesa","filtro"),
            ("Estatisticas","filtro_estatistica")
        ]
        for i, (texto,tela) in enumerate(botoes,start=1):
            ttk.Button(self, text=texto,width=(WIDGET_PADRAO), command=lambda t=tela: self.controller.mostrar_tela(t)
            ).grid(row=i,column=0,pady=(PADY_BOTAO))

