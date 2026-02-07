import tkinter as tk
from tkinter import ttk

class TelaMenu(ttk.Frame):
    def __init__(self,parent,controller):
        super().__init__(parent)
        self.controller=controller
        self._configurar_grid()
        self._criar_widgets()

    def _criar_widgets(self):

        tk.Label(self, text="Menu Principal", font=("Arial", 14),anchor="center").grid(row=0,column=0,pady=15)

        ttk.Button(self, text="Adicionar Despesa", command=lambda: self.controller.mostrar_tela("adicionar")
        ).grid(row=1,column=0,pady=5)
        ttk.Button(self, text="Listar Despesa", command=lambda: self.controller.mostrar_tela("listar")
        ).grid(row=2,column=0,pady=5)
        ttk.Button(self, text="Filtrar Despesa", command=lambda: self.controller.mostrar_tela("filtro")
        ).grid(row=3,column=0,pady=5)
        ttk.Button(self, text="Estatísticas", command=lambda :self.controller.mostrar_tela("filtro_estatistica")
        ).grid(row=4,column=0,pady=5)

    def _configurar_grid(self):
        self.grid_columnconfigure(0,weight=0)
        self.grid_columnconfigure(1,weight=1)