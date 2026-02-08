import tkinter as tk
from tkinter import ttk
from core.despesas_estatisticas_core import *
from gui.widgets.mensagem_gui import MensagemGUI
from gui.config.estilos import *

class TelaResultadoEstatistica(ttk.Frame):
    def __init__(self,parent,controller,lista_mes_ano):
        super().__init__(parent)
        self.lista_mes_ano = lista_mes_ano
        self.controller = controller
        self._configurar_grid()
        self._criar_widgets()
        self.carregar_dados()

    def _configurar_grid(self):
        self.grid_columnconfigure(0,weight=1)

    def _criar_widgets(self):
        # posicionando Resultados ao lado dos Botões
        self.resultado = tk.StringVar(value="Clique em uma das opções abaixo 👇")

        #Titulo
        ttk.Label(self, text="Opções de Estatisticas", font=(FONTE_SUBTITULO)
                  ).grid(row=0, column=0, pady=(PADY_PADRAO_SUBTITULO))

        #O resultado das operações
        ttk.Label(self, textvariable=self.resultado, font=(FONTE_PADRAO)
                  ).grid(row=1, column=0, pady=(PADY_PADRAO_SUBTITULO))

        #Dicionário de Acões:
        acoes = {
            "Mostrar Maior Despesa": self._clicou_maior_despesa,
            "Mostrar Menor Despesa": self._clicou_menor_despesa,
            "Mostrar Média de Despesas": self._clicou_media_despesa,
            "Mostrar Total de Despesas": self._clicou_total_despesa
        }

        linha = 2
        for texto,funcao in acoes.items():
            ttk.Button(self, text=texto, width=(WIDGET_PADRAO),command=funcao
                ).grid(row=linha, column=0, pady=(PADY_BOTAO))
            linha += 1

        ttk.Button(self, text="👈 Voltar", command=lambda: self.controller.mostrar_tela("menu")
                 ).grid(row=linha + 2, column=0, pady=(PADY_BOTAO))

        #Tabela
        colunas = ("valor", "descricao", "categoria", "data")

        self.tabela = ttk.Treeview(self, columns=colunas, show="headings")
        self.tabela.heading("valor", text="Valor"),
        self.tabela.heading("descricao", text="Descrição"),
        self.tabela.heading("categoria", text="Categoria"),
        self.tabela.heading("data", text="Data")

        for col in colunas:
            self.tabela.column(col, anchor="center")

        self.tabela.grid(row=linha + 1, column=0, pady=5)

        self.mensagem = MensagemGUI(self)
        self.mensagem.grid(row=1, column=1, pady=(0, 10))

    def carregar_dados(self):
            dados = self.lista_mes_ano

            for despesa in dados:
                self.tabela.insert(
                    "",
                    "end",
                    values = (
                        despesa.get("valor",""),
                        despesa.get("descricao",""),
                        despesa.get("categoria",""),
                        despesa.get("data","")
                    )
                )

    def _clicou_maior_despesa(self):
        valor = processar_maior_despesa(self.lista_mes_ano)
        self.resultado.set(f"O maior valor é: R$ {valor:.2f}")
    def _clicou_menor_despesa(self):
        valor = processar_menor_despesa(self.lista_mes_ano)
        self.resultado.set(f"O menor valor é: R$ {valor:.2f}")
    def _clicou_media_despesa(self):
        valor = processar_media_despesa(self.lista_mes_ano)
        self.resultado.set(f"A média de despesa é: R$ {valor: .2f}")
    def _clicou_total_despesa(self):
        valor = processar_total_despesa(self.lista_mes_ano)
        self.resultado.set(f"O total de despesas é: R$ {valor: .2f}")