import tkinter as tk
from tkinter import ttk
from core.despesas_mensagens_core import CATEGORIAS,MENSAGENS,ERROS
from core.despesas_adicionar_core import adicionar_despesa_core
from  core.despesas_arquivo_core import carregar_despesas,salva_despesas
from gui.widgets.mensagem_gui import MensagemGUI
from gui.config.estilos import *

class TelaAdicionarDespesas(ttk.Frame):
    def __init__(self,parent,controller):
        super().__init__(parent)
        self.controller = controller
        self._configurar_grid()
        self._criar_widgets()

    def _configurar_grid(self):
        self.grid_columnconfigure(0, weight=1) #responsavel pelos labels

    def _criar_widgets(self):
        #Subtitulo
        ttk.Label(self, text="Adicionar Despesas", font=(FONTE_SUBTITULO)
            ).grid(row=0, column=0,pady=(PADY_PADRAO_SUBTITULO))

        #Area Mensagens de erro
        self.mensagem = MensagemGUI(self)
        self.mensagem.grid(row=1, column=0)

        #Frame do Formulário
        self.frame_formulario = ttk.Frame(self)
        self.frame_formulario.grid(row=2,column=0,padx=(PADX_PADRAO),pady=(PADY_FORM),sticky="ew")

        #Configurando as Colunas
        self.frame_formulario.grid_columnconfigure(0,weight=0)#Labels
        self.frame_formulario.grid_columnconfigure(1,weight=1)#Campos

        #Labels
        ttk.Label(self.frame_formulario,text="Valor").grid(row=0,column=0,pady=(PADY_CAMPO),padx=(PADX_LABEL),sticky="e")
        self.validar_valor = ttk.Entry(self.frame_formulario)
        self.validar_valor.grid(row=0,column=1,padx=(PADX_CAMPO),pady=(PADY_CAMPO),sticky="ew")

        ttk.Label(self.frame_formulario, text="Descrição").grid(row=1, column=0, pady=(PADY_CAMPO), padx=(PADX_LABEL),sticky="e")
        self.validar_descricao = ttk.Entry(self.frame_formulario)
        self.validar_descricao.grid(row=1, column=1, padx=(PADX_CAMPO), pady=(PADY_CAMPO), sticky="ew")

        #ComboBox
        texto_inicial = "Selecione uma Categoria"

        ttk.Label(self.frame_formulario, text="Categoria").grid(row=2, column=0, pady=(PADY_CAMPO), padx=(PADX_LABEL),sticky="e")
        self.categoria_selecionada = tk.StringVar()
        self.combo_categoria = ttk.Combobox(
            self.frame_formulario,
            textvariable=self.categoria_selecionada,
            values=list(CATEGORIAS.values()),
            state="readonly"
        )
        self.combo_categoria.set(texto_inicial)
        self.combo_categoria.config(width=len(texto_inicial))
        self.combo_categoria.grid(row=2, column=1, padx=(PADX_CAMPO), pady=(PADY_CAMPO), sticky="ew")

        #Label
        ttk.Label(self.frame_formulario, text="Data").grid(row=3, column=0, pady=(PADY_CAMPO), padx=(PADX_LABEL),sticky="e")
        self.validar_data = ttk.Entry(self.frame_formulario)
        self.validar_data.grid(row=3, column=1, padx=(PADX_CAMPO), pady=(PADY_CAMPO), sticky="ew")

        #Botões
        ttk.Button(self,text="💾 Salvar",width=(WIDGET_PADRAO),command = self._salvar
            ).grid(row=6,column=0,pady=5, padx=(PADY_BOTAO))

        ttk.Button(self, text="👈 Voltar", width=(WIDGET_PADRAO), command=lambda: self.controller.mostrar_tela("menu")
            ).grid(row=7, column=0, pady=5, padx=(PADY_BOTAO))

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

