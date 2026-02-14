import os
import tkinter as tk
from tkinter import ttk

from utils.caminhos import resource_path
from gui.config.estilos import *
from gui.telas.tela_listar import TelaListarDespesas
from gui.telas.tela_menu import TelaMenu
from gui.telas.tela_adicionar import TelaAdicionarDespesas
from gui.telas.tela_resultado_estatisticas import TelaResultadoEstatistica
from gui.telas.tela_filtro_periodo import TelaFiltroPeriodo
from gui.telas.tela_filtros import TelaFiltros
from gui.telas.tela_filtro_categoria import TelaFiltroCategoria
from gui.telas.tela_resultado_categoria import TelaResultadoCategoria
from gui.telas.tela_resultado_periodo import TelaResultadoPeriodo
from gui.telas.tela_filtro_estatistica import TelaFiltroEstatistica



class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Gerenciador de Despesas")
        caminho = resource_path("assets/GerenciadorDeDespesas.ico")

        self.iconbitmap(caminho)
        tk.Label(self, text="Gerenciador de Despesas", font=FONTE_TITULO).pack(pady=10,padx=10)

        self.container = ttk.Frame(self)
        self.container.pack(fill="both",expand=True)
        self.tela_atual = None
        self.telas={
            "menu": TelaMenu,
            "adicionar":TelaAdicionarDespesas,
            "listar": TelaListarDespesas,
            "filtro": TelaFiltros,
            "filtro_categoria": TelaFiltroCategoria,
            "filtro_periodo": TelaFiltroPeriodo,
            "filtro_estatistica": TelaFiltroEstatistica,
            "resultado_categoria": TelaResultadoCategoria,
            "resultado_periodo": TelaResultadoPeriodo,
            "resultado_estatistica": TelaResultadoEstatistica
        }
        self.mostrar_tela("menu")

    def mostrar_tela(self,nome_tela, **kwargs):
        if self.tela_atual:
            self.tela_atual.destroy()

        TelaClasse = self.telas[nome_tela]
        self.tela_atual = TelaClasse(
            parent=self.container,
            controller=self,
            **kwargs
        )
        self.tela_atual.pack(fill="both",expand=True)
        self.update_idletasks()
        self.geometry("")

    def trocar_tela(self,nova_tela):
        if self.tela_atual:
            self.tela_atual.destroy()
        self.tela_atual = nova_tela
        self.tela_atual.pack(fill="both",expand=True)

    def mostrar_filtros(self):
        if self.tela_atual:
            self.tela_atual.destroy()

        self.tela_atual= TelaFiltros(
            parent= self.container)
        self.tela_atual.pack(fill="both",expand=True)

    def mostrar_tela_categoria(self):
        if self.tela_atual:
            self.tela_atual.destroy()

        self.tela_atual= TelaFiltroCategoria(
            parent=self.container
        )
        self.tela_atual.pack(fill="both",expand=True)

    def mostrar_resultado_categoria(self,categoria):
        if self.tela_atual:
            self.tela_atual.destroy()

        self.tela_atual= TelaResultadoCategoria(
            parent=self.container,
            categoria=categoria
        )
        self.tela_atual.pack(fill="both",expand=True)

    def mostrar_tela_periodo(self):
        if self.tela_atual:
            self.tela_atual.destroy()

        self.tela_atual= TelaFiltroPeriodo(
            parent=self.container
        )
        self.tela_atual.pack(fill="both",expand=True)

    def mostrar_resultado_periodo(self,data_inicio,data_fim):

        if self.tela_atual:
            self.tela_atual.destroy()

        self.tela_atual= TelaResultadoPeriodo(
            parent=self.container,
            data_inicio=data_inicio,
            data_fim = data_fim
        )
        self.tela_atual.pack(fill="both",expand=True)

    def mostrar_filtro_estatistica(self):
        if self.tela_atual:
            self.tela_atual.destroy()

        self.tela_atual= TelaFiltroEstatistica(
            parent= self.container
        )
        self.tela_atual.pack(fill="both",expand=True)

    def mostrar_resultado_estatistica(self,lista_mes_ano):
        if self.tela_atual:
            self.tela_atual.destroy()

        self.tela_atual= TelaResultadoEstatistica(
            parent= self.container,
            lista_mes_ano= lista_mes_ano
        )
        self.tela_atual.pack(fill="both",expand=True)

