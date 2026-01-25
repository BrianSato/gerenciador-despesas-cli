import tkinter as tk
from os.path import expanduser
from tkinter import ttk
from gui.telas.tela_adicionar import TelaAdicionarDespesas
from gui.telas.tela_listar import TelaListarDespesas
from gui.telas.tela_filtros import TelaFiltros
from gui.telas.tela_filtro_categoria import TelaFiltroCategoria
from core.despesas_mensagens_core import ERROS

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Gerenciador de Despesas")
        tk.Label(self, text="Gerenciador de Despesas", font=("Arial", 16, "bold")).pack(pady=10)
        self.container = ttk.Frame(self)
        self.container.pack(fill="both",expand=True)
        self.tela_atual = None
        self.mostrar_menu()

    def mostrar_tela(self,TelaClasse):
        if self.tela_atual:
            self.tela_atual.destroy()
        self.tela_atual = TelaClasse(
            parent=self.container,
            voltar_callback= self.mostrar_menu
        )
        self.tela_atual.pack(fill="both",expand=True)

    def trocar_tela(self,nova_tela):
        if self.tela_atual:
            self.tela_atual.destroy()
        self.tela_atual = nova_tela
        self.tela_atual.pack(fill="both",expand=True)

    def mostrar_menu(self):
        if self.tela_atual:
            self.tela_atual.destroy()
        menu = tk.Frame(self.container)

        tk.Label(menu,text="Menu Principal",font=("Arial",14)).pack(pady=10)

        ttk.Button(menu,text = "Adicionar Despesa", command =lambda :self.mostrar_tela(TelaAdicionarDespesas)).pack(pady=5)
        ttk.Button(menu, text="Listar Despesa", command=lambda :self.mostrar_tela(TelaListarDespesas)).pack(pady=5)
        ttk.Button(menu, text="Filtrar Despesa", command=self.mostrar_filtros).pack(pady=5)

        self.tela_atual = menu
        menu.pack(fill="both",expand=True)

    def mostrar_filtros(self):
        if self.tela_atual:
            self.tela_atual.destroy()

        self.tela_atual= TelaFiltros(
            parent= self.container,
            voltar_callback=self.mostrar_menu,
            filtrar_categoria_callback=self.mostrar_tela_categoria
        )
        self.tela_atual.pack(fill="both",expand=True)

    def mostrar_tela_categoria(self,categoria):
        if self.tela_atual:
            self.tela_atual.destroy()

        self.tela_atual= TelaFiltroCategoria(
            parent=self.container,
            categoria=categoria,
            voltar_callback=self.mostrar_filtros
        )
        self.tela_atual.pack(fill="both",expand=True)