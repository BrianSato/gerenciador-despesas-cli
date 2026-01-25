import tkinter as tk
from tkinter import ttk
from core.despesas_mensagens_core import CATEGORIAS,ERROS
from core.despesas_filtrar_core import filtrar_por_periodo
from gui.telas.tela_filtro_categoria import TelaFiltroCategoria


class TelaFiltros(ttk.Frame):
    def __init__(self,parent,voltar_callback,filtrar_categoria_callback):
        super().__init__(parent)
        self.voltar_callback = voltar_callback
        self.filtrar_categoria_callback = filtrar_categoria_callback
        self.criar_widgets()

    def criar_widgets(self):

        ttk.Label(self,text="Opções de Filtros:",font=("Arial",14)
        ).grid(row=0,column=0,columnspan=2,pady=10)

        ttk.Button(self, text="Categoria", command= self.filtrar_categoria
        ).grid(row=1, column=0, pady=5)

        ttk.Button(self, text="Data", command=filtrar_por_periodo
        ).grid(row=2, column=0, pady=5)

        ttk.Button(self,text="👈 Voltar Menu",command=self.voltar_callback
        ).grid(row=3, column=0,pady=5)

    def filtrar_categoria(self):
        self.categoria_var = tk.StringVar()
        self.combo_categoria = ttk.Combobox(
            self,
            textvariable=self.categoria_var,
             values=list(CATEGORIAS.values()),
            state="readonly"
        )
        self.combo_categoria.grid(row=1, column=1, pady=5)
        self.combo_categoria.set("Selecione uma categoria")

        ttk.Button(self, text="Filtrar", command=lambda: self.filtrar_categoria_callback(self.categoria_var.get())
        ).grid(row=2, column=0, pady=5)

