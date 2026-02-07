import tkinter as tk
from tkinter import ttk
from gui.widgets.mensagem_gui import MensagemGUI

class TelaFiltros(ttk.Frame):
    def __init__(self,parent,controller):
        super().__init__(parent)
        self.controller = controller
        self.criar_widgets()

    def criar_widgets(self):

        ttk.Label(self,text="Opções de Filtros:",font=("Arial",14)
        ).grid(row=0,column=0,columnspan=2,pady=10)

        ttk.Button(self,text="Categoria",command=lambda:self.controller.mostrar_tela("filtro_categoria")
        ).grid(row=2, column=0, pady=5)

        ttk.Button(self, text="Data", command=lambda:self.controller.mostrar_tela("filtro_periodo")
        ).grid(row=3, column=0, pady=5)

        ttk.Button(self,text="👈 Voltar",command=lambda :self.controller.mostrar_tela("menu")
        ).grid(row=4, column=0,pady=5)

        self.mensagem = MensagemGUI(self)
        self.mensagem.grid(row=1, column=0, columnspan=2, pady=(0, 10))
