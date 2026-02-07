import tkinter as tk
from tkinter import ttk
from core.despesas_mensagens_core import CATEGORIAS,ERROS
from core.despesas_validacoes_core import validar_categoria
from gui.widgets.mensagem_gui import MensagemGUI


class TelaFiltroCategoria(ttk.Frame):
    def __init__(self, parent,controller):
        super().__init__(parent)
        self.controller=controller
        self.criar_widgets()

    def criar_widgets(self):
        ttk.Label(self, text="Filtrar por Categoria:", font=("Arial", 14)
                  ).grid(row=0, column=0, columnspan=2, pady=10)

        self.categoria_selecionada = tk.StringVar()
        self.combo_categoria = ttk.Combobox(
            self,
            textvariable=self.categoria_selecionada,
            values=list(CATEGORIAS.values()),
            state="readonly"
        )
        self.combo_categoria.grid(row=2, column=1, pady=5)
        self.combo_categoria.set("Selecione uma categoria")

        ttk.Button(self, text="Filtrar", command=self.processar_filtro_categoria
        ).grid(row=2, column=0, pady=5)

        ttk.Button(self, text="👈 Voltar Menu", command=lambda :self.controller.mostrar_tela("filtro")
        ).grid(row=4, column=0, pady=5)

        self.mensagem = MensagemGUI(self)
        self.mensagem.grid(row=1, column=0, columnspan=2, pady=(0, 10))


    def processar_filtro_categoria(self):

        try:
            categoria = validar_categoria(self.categoria_selecionada.get())
            self.controller.mostrar_tela("resultado_categoria",categoria = categoria)
        except ValueError:
            self.mensagem.erro(ERROS["erro_categoria"])


