import tkinter as tk
from tkinter import ttk
from core.despesas_mensagens_core import CATEGORIAS,MENSAGENS,ERROS
from gui.widgets.mensagem_gui import MensagemGUI
from core.despesas_adicionar_core import adicionar_despesa_core
from  core.despesas_arquivo_core import carregar_despesas,salva_despesas

class TelaAdicionarDespesas(ttk.Frame):
    def __init__(self,parent,voltar_callback):
        super().__init__(parent)
        self.voltar_callback = voltar_callback
        self._criar_widgets()

    def _criar_widgets(self):

        ttk.Label(self,text = "Adicionar Despesas",font = ("Arial", 14)
        ).grid(row=0, column=0,columnspan=2, pady=10)

        ttk.Label(self,text="Valor").grid(row=2,column=0,sticky="w", pady=7)
        self.validar_valor = ttk.Entry(self)
        self.validar_valor.grid(row=2,column=1,pady=5)

        ttk.Label(self, text="Descrição").grid(row=3, column=0, sticky="w", pady=7)
        self.validar_descricao = ttk.Entry(self)
        self.validar_descricao.grid(row=3, column=1, pady=5)

        ttk.Label(self, text="Categoria").grid(row=4, column=0, sticky="w", pady=7)
        self.categoria_selecionada = tk.StringVar()
        self.combo_categoria = ttk.Combobox(
            self,
            textvariable=self.categoria_selecionada,
            values=list(CATEGORIAS.values()),
            state="readonly"
        )
        self.combo_categoria.grid(row=4,column=1,pady=5)
        self.combo_categoria.set("Selecione uma categoria")

        ttk.Label(self, text="Data").grid(row=5, column=0, sticky="w", pady=7)
        self.validar_data = ttk.Entry(self)
        self.validar_data.grid(row=5, column=1, pady=5)

        ttk.Button(self, text="👈 Voltar", command=self.voltar_callback
        ).grid(row=6, column=0, columnspan=2, pady=5)

        ttk.Button(self,text="💾 Salvar",command = self._salvar
        ).grid(row=6,column=2,columnspan=2,pady=5)

        self.mensagem = MensagemGUI(self)
        self.mensagem.grid(row=1, column=0, columnspan=2, pady=(0,10))

    def _salvar(self):
        self.mensagem.limpar()
        try:

            despesas= carregar_despesas()

            adicionar_despesa_core(
                despesas,
                    self.validar_valor.get(),
                    self.validar_descricao.get(),
                    self.categoria_selecionada.get(),
                    self.validar_data.get()
                )
            salva_despesas(despesas)

            self.mensagem.sucesso(MENSAGENS["despesa_adicionada"])
            self._limpar_campos()

        except ValueError as erro:
            self.mensagem.erro(str(erro))
        except Exception :
            self.mensagem.erro(ERROS["outros_erros"])


    def _limpar_campos(self):
        self.validar_valor.delete(0,"end")
        self.validar_descricao.delete(0, "end")
        self.validar_data.delete(0, "end")

