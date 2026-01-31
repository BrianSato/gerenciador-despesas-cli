import tkinter as tk
from tkinter import ttk
from core.despesas_validacoes_core import validar_data
from gui.widgets.mensagem_gui import MensagemGUI
from core.despesas_mensagens_core import ERROS

class TelaFiltroPeriodo(ttk.Frame):

    def __init__(self, parent, voltar_callback,resultado_periodo_callback):
        super().__init__(parent)
        self.voltar_callback = voltar_callback
        self.resultado_periodo_callback = resultado_periodo_callback
        self.criar_widgets()


    def criar_widgets(self):
        ttk.Label(self,text = "Filtrar por Periodo", font=("Aria", 14,"bold")
        ).grid(row=0, column=0, columnspan=2, pady=10)

        ttk.Label(self, text="Data Inicio").grid(row=2, column=0, sticky="w", pady=7)
        self.data_inicio = ttk.Entry(self)
        self.data_inicio.grid(row=2, column=1, pady=5)

        ttk.Label(self, text="Data Fim").grid(row=3, column=0, sticky="w", pady=7)
        self.data_fim = ttk.Entry(self)
        self.data_fim.grid(row=3, column=1, pady=5)

        ttk.Button(self, text="Filtrar", command=self.processar_filtro_periodo
        ).grid(row=4, column=0, pady=5)

        ttk.Button(self, text="👈 Voltar Menu", command=self.voltar_callback
        ).grid(row=5, column=0, pady=5)

        self.mensagem = MensagemGUI(self)
        self.mensagem.grid(row=1, column=0, columnspan=2, pady=(0, 10))

    def processar_filtro_periodo(self):
        try:
            data_inicio = validar_data(self.data_inicio.get())
            data_fim = validar_data(self.data_fim.get())
            self.resultado_periodo_callback(data_inicio,data_fim)
        except ValueError:
            self.mensagem.erro(ERROS["erro_data"])
