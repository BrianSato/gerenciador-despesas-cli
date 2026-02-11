import tkinter as tk
from tkinter import ttk, messagebox
from core.despesas_editar_core import editar_despesa_core
from core.despesas_mensagens_core import CATEGORIAS,MENSAGENS,ERROS
from core.despesas_adicionar_core import adicionar_despesa_core
from gui.config.estilos import *

class TelaAdicionarDespesas(ttk.Frame):
    def __init__(self,parent,controller, **kwargs):
        super().__init__(parent)
        self.despesa_edicao = kwargs.get("despesa")
        self.editar_valor = tk.StringVar()
        self.editar_descricao = tk.StringVar()
        self.editar_data = tk.StringVar()
        self.controller = controller

        self._configurar_grid()
        self._criar_widgets()

        if self.despesa_edicao:
            self.editar_id = (self.despesa_edicao["ID"])
            self._carregar_dados_para_edicao()
            self._configurar_modo_edicao()

    def _configurar_grid(self):
        self.grid_columnconfigure(0, weight=1) #responsavel pelos labels

    def _criar_widgets(self):
        #Subtitulo
        ttk.Label(self, text="Adicionar Despesas", font=FONTE_SUBTITULO
            ).grid(row=0, column=0,pady=PADY_PADRAO_SUBTITULO)

        #Frame do Formulário
        self.frame_formulario = ttk.Frame(self)
        self.frame_formulario.grid(row=2,column=0,padx=PADX_PADRAO,pady=PADY_FORM,sticky="ew")

        #Configurando as Colunas
        self.frame_formulario.grid_columnconfigure(0,weight=0)#Labels
        self.frame_formulario.grid_columnconfigure(1,weight=1)#Campos

        #Labels
        ttk.Label(self.frame_formulario,text="Valor").grid(row=0,column=0,pady=PADY_CAMPO,padx=PADX_LABEL,sticky="e")
        self.entrar_valor = ttk.Entry(self.frame_formulario, textvariable=self.editar_valor)
        self.entrar_valor.grid(row=0,column=1,padx=PADX_CAMPO,pady=PADY_CAMPO,sticky="ew")

        ttk.Label(self.frame_formulario, text="Descrição").grid(row=1, column=0, pady=PADY_CAMPO, padx=PADX_LABEL,sticky="e")
        self.entrar_descricao = ttk.Entry(self.frame_formulario,textvariable=self.editar_descricao)
        self.entrar_descricao.grid(row=1, column=1, padx=PADX_CAMPO, pady=PADY_CAMPO, sticky="ew")

        #ComboBox
        texto_inicial = "Selecione uma Categoria"

        ttk.Label(self.frame_formulario, text="Categoria").grid(row=2, column=0, pady=PADY_CAMPO, padx=PADX_LABEL,sticky="e")
        self.categoria_selecionada = tk.StringVar()
        self.combo_categoria = ttk.Combobox(
            self.frame_formulario,
            textvariable=self.categoria_selecionada,
            values=list(CATEGORIAS.values()),
            state="readonly"
        )
        self.combo_categoria.set(texto_inicial)
        self.combo_categoria.config(width=len(texto_inicial))
        self.combo_categoria.grid(row=2, column=1, padx=PADX_CAMPO, pady=PADY_CAMPO, sticky="ew")

        #Label
        ttk.Label(self.frame_formulario, text="Data").grid(row=3, column=0, pady=PADY_CAMPO, padx=PADX_LABEL,sticky="e")
        self.entrar_data = ttk.Entry(self.frame_formulario,textvariable=self.editar_data)
        self.entrar_data.grid(row=3, column=1, padx=PADX_CAMPO, pady=PADY_CAMPO, sticky="ew")

        #Botões
        self.botao_salvar = ttk.Button(self,text="💾 Salvar",width=WIDGET_PADRAO,command = self._salvar)
        self.botao_salvar.grid(row=6,column=0,pady=5, padx=PADY_BOTAO)

        ttk.Button(self, text="👈 Voltar", width=WIDGET_PADRAO, command=lambda: self.controller.mostrar_tela("menu")
            ).grid(row=7, column=0, pady=5, padx=PADY_BOTAO)

    def _salvar(self):
        self.mensagem.limpar()
        try:

            adicionar_despesa_core(
                    self.entrar_valor.get(),
                    self.entrar_descricao.get(),
                    self.categoria_selecionada.get(),
                    self.entrar_data.get()
                )

            messagebox.showinfo("Sucesso",MENSAGENS["despesa_add"])
            self._limpar_campos()

        except ValueError as erro:
            messagebox.showerror("Erro", str(erro))

    def _atualizar(self):

        try:

            editar_despesa_core(
                self.editar_id,
                self.editar_valor.get(),
                self.editar_descricao.get(),
                self.categoria_selecionada.get(),
                self.editar_data.get()
                )

            messagebox.showinfo("Sucesso",MENSAGENS["despesa_update"])
            self._limpar_campos()

        except ValueError as erro:
            messagebox.showerror("Erro",str(erro))


    def _carregar_dados_para_edicao(self):
            if self.despesa_edicao:
                self.editar_valor.set(self.despesa_edicao["valor"])
                self.editar_descricao.set(self.despesa_edicao["descricao"])
                self.categoria_selecionada.set(self.despesa_edicao["categoria"])
                self.editar_data.set(self.despesa_edicao["data"])

    def _configurar_modo_edicao(self):
        self.botao_salvar.config(text="Atualizar",command=self._atualizar)

    def _limpar_campos(self):
        self.entrar_valor.delete(0,"end")
        self.entrar_descricao.delete(0, "end")
        self.entrar_data.delete(0, "end")


