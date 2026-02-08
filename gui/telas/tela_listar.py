import tkinter as tk
from tkinter import ttk,messagebox
from core.despesas_listar_core import listar_despesas_core
from core.despesas_mensagens_core import ERROS,MENSAGENS
from core.despesas_deletar_core import deletar_despesa_core
from gui.widgets.mensagem_gui import MensagemGUI
from gui.config.estilos import *

class TelaListarDespesas(ttk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self._configurar_grid()
        self.criar_widgets()
        self.carregar_dados()

    def _configurar_grid(self):
        self.grid_columnconfigure(0,weight=1)

    def criar_widgets(self):
        #Subtitulo
        ttk.Label(self,text = "Lista de despesas", font=(FONTE_SUBTITULO)
        ).grid(row=0, column=0, pady=(PADY_PADRAO))

        # Area Mensagens de erro
        self.mensagem = MensagemGUI(self)
        self.mensagem.grid(row=1, column=0)

        #Tabela
        colunas = ("ID","valor", "descricao","categoria","data")

        self.tabela = ttk.Treeview(self, columns=colunas, show = "headings")
        self.tabela.heading("ID",text="ID")
        self.tabela.heading("valor",text = "Valor"),
        self.tabela.heading("descricao", text="Descrição"),
        self.tabela.heading("categoria", text="Categoria"),
        self.tabela.heading("data", text="Data")

        for col in colunas:
            self.tabela.column(col, anchor = "center")

        self.tabela.grid(row=2, column=0, pady=10,padx=(PADX_PADRAO))

        ttk.Button(self, text="🗑 Apagar Despesa",width=(WIDGET_PADRAO), command=self.deletar_selecionado
        ).grid(row=3, column=0, pady=(PADY_BOTAO))

        ttk.Button(self, text="👈 Voltar", width=(WIDGET_PADRAO), command=lambda: self.controller.mostrar_tela("menu")
        ).grid(row=4, column=0, pady=(PADY_BOTAO))

    def carregar_dados(self):
            dados = listar_despesas_core()

            for despesa in dados:
                self.tabela.insert(
                    "",
                    "end",
                    values = (
                        despesa.get("ID",""),
                        despesa.get("valor",""),
                        despesa.get("descricao",""),
                        despesa.get("categoria",""),
                        despesa.get("data","")
                    )
                )

    def deletar_selecionado(self):
        #pega o item selecionado
        selecionado = self.tabela.selection()

        if not selecionado:
            self.mensagem.erro("erro_sem_delete")
            return

        #pega o ID do item selecionado(supondo que ID esta na primeira coluna [0])
        item = self.tabela.item(selecionado)
        id_para_deletar = int(item["values"][0])

        #Confirmação
        confirm = messagebox.askyesno(
            title = "Confirmação",
            message = "Tem certeza que deseja deletar esta despesa?"
        )
        if not confirm:
            return #Usuário Cancelou

        #chama o CORE
        sucesso = deletar_despesa_core(id_para_deletar)
        if sucesso:
            #remove a linha da tabela
            self.tabela.delete(selecionado)
            self.mensagem.sucesso(MENSAGENS["despesa_delete_sucesso"])
        else:
            self.mensagem.erro(ERROS["erro_delete"])