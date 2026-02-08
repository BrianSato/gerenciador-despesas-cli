import tkinter as tk
from tkinter import ttk
from core.despesas_mensagens_core import CATEGORIAS,ERROS
from core.despesas_validacoes_core import validar_categoria
from gui.widgets.mensagem_gui import MensagemGUI
from gui.config.estilos import *


class TelaFiltroCategoria(ttk.Frame):
    def __init__(self, parent,controller):
        super().__init__(parent)
        self.controller=controller
        self._configurar_grid()
        self.criar_widgets()

    def _configurar_grid(self):
        self.grid_columnconfigure(0,weight=1)

    def criar_widgets(self):
        #Subtitulo
        ttk.Label(self, text="Filtrar por Categoria:", font=(FONTE_SUBTITULO)
                  ).grid(row=0, column=0, pady=(PADY_PADRAO_SUBTITULO))

        #Tabela
        texto_inicial = "Selecione uma categoria"
        self.categoria_selecionada = tk.StringVar()
        self.combo_categoria = ttk.Combobox(
            self,
            textvariable=self.categoria_selecionada,
            values=list(CATEGORIAS.values()),
            state="readonly"
        )
        self.combo_categoria.set(texto_inicial)
        self.combo_categoria.config(width=len(texto_inicial))
        self.combo_categoria.grid(row=2, column=0,pady=5)


        ttk.Button(self, text="Filtrar",width=(WIDGET_PADRAO), command=self.processar_filtro_categoria
        ).grid(row=3, column=0, pady=(PADY_BOTAO))

        ttk.Button(self, text="👈 Voltar Menu",width=(WIDGET_PADRAO), command=lambda :self.controller.mostrar_tela("filtro")
        ).grid(row=4, column=0, pady=(PADY_BOTAO))

        self.mensagem = MensagemGUI(self)
        self.mensagem.grid(row=1, column=0, pady=(PADY_MENSAGEM))


    def processar_filtro_categoria(self):

        try:
            categoria = validar_categoria(self.categoria_selecionada.get())
            self.controller.mostrar_tela("resultado_categoria",categoria = categoria)
        except ValueError:
            self.mensagem.erro(ERROS["erro_categoria"])


