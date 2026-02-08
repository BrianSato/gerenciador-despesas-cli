import tkinter as tk
from tkinter import ttk
from core.despesas_validacoes_core import validar_data
from core.despesas_mensagens_core import ERROS
from gui.widgets.mensagem_gui import MensagemGUI
from gui.config.estilos import *

class TelaFiltroPeriodo(ttk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self._configurar_grid()
        self.criar_widgets()

    def _configurar_grid(self):
        self.grid_columnconfigure(0,weight=1)

    def criar_widgets(self):
        #SubTitulo
        ttk.Label(self,text = "Filtrar por Periodo", font=(FONTE_SUBTITULO)
        ).grid(row=0, column=0, pady=(PADY_PADRAO_SUBTITULO))

        #Area Mensagem de erro
        self.mensagem = MensagemGUI(self)
        self.mensagem.grid(row=1, column=0, pady=(PADY_MENSAGEM),sticky="ew")

        # Frame do Formulário
        self.frame_formulario = ttk.Frame(self)
        self.frame_formulario.grid(row=2, column=0, padx=(PADX_PADRAO), pady=(PADY_FORM), sticky="ew")

        # Configurando as Colunas
        self.frame_formulario.grid_columnconfigure(0, weight=0)  # Labels
        self.frame_formulario.grid_columnconfigure(1, weight=1)  # Campos

        # Labels
        ttk.Label(self.frame_formulario, text="Data Início").grid(row=0, column=0, pady=(PADY_CAMPO), padx=(PADX_LABEL),sticky="e")
        self.data_inicio = ttk.Entry(self.frame_formulario)
        self.data_inicio.grid(row=0, column=1, padx=(PADX_CAMPO), pady=(PADY_CAMPO), sticky="ew")

        ttk.Label(self.frame_formulario, text="Data Fim").grid(row=1, column=0, pady=(PADY_CAMPO), padx=(PADX_LABEL),sticky="e")
        self.data_fim = ttk.Entry(self.frame_formulario)
        self.data_fim.grid(row=1, column=1, padx=(PADX_CAMPO), pady=(PADY_CAMPO), sticky="ew")

        #Botões
        ttk.Button(self, text="Filtrar", width=(WIDGET_PADRAO),command=self.processar_filtro_periodo
        ).grid(row=3, column=0, pady=(PADY_BOTAO))

        ttk.Button(self, text="👈 Voltar Menu",width=(WIDGET_PADRAO), command=lambda:self.controller.mostrar_tela("filtro")
        ).grid(row=4, column=0, pady=(PADY_BOTAO))

    def processar_filtro_periodo(self):
        try:
            data_inicio = validar_data(self.data_inicio.get())
            data_fim = validar_data(self.data_fim.get())
            self.controller.mostrar_tela("resultado_periodo",data_inicio = data_inicio,data_fim = data_fim)
        except ValueError:
            self.mensagem.erro(ERROS["erro_data"])
