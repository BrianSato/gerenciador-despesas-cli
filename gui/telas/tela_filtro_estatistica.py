import tkinter as tk
from tkinter import ttk, messagebox
from core.despesas_mensagens_core import MESES,ERROS
from core.despesas_filtrar_core import filtrar_anos_disponiveis
from core.despesas_filtrar_core import filtrar_por_mes_ano
from gui.config.estilos import *

class TelaFiltroEstatistica(ttk.Frame):
    def __init__(self,parent,controller):
        super().__init__(parent)
        self.anos = filtrar_anos_disponiveis()#chamou funcao do do CORE levando os dados do arquivo
        self.anos_str = [str(ano)for ano in self.anos]#recebeu o resultado da funcao acima e converteu em STRING
        self.controller=controller
        self._configurar_grid()
        self.criar_widgets()

    def _configurar_grid(self):
        self.grid_columnconfigure(0, weight=1) #responsavel pelos labels

    def criar_widgets(self):
        #Subtitulo
        ttk.Label(self,text="Estatísticas de Despesas:",font=FONTE_SUBTITULO
        ).grid(row=0,column=0,pady=PADY_PADRAO_SUBTITULO)

        # Frame do Formulário
        self.frame_formulario = ttk.Frame(self)
        self.frame_formulario.grid(row=2, column=0, padx=PADX_PADRAO, pady=PADY_FORM, sticky="ew")

        # Configurando as Colunas
        self.frame_formulario.grid_columnconfigure(0, weight=0)  # Labels
        self.frame_formulario.grid_columnconfigure(1, weight=1)  # Campos

        # ComboBox
        texto_inicial_mes = "Selecione o Mês"
        texto_inicial_ano = "Selecione o Ano"

        ttk.Label(self.frame_formulario, text="Mês").grid(row=0, column=0, pady=PADY_CAMPO, padx=PADX_LABEL,
                                                                sticky="e")
        self.data_mes = tk.StringVar()
        self.combo_mes = ttk.Combobox(
            self.frame_formulario,
            textvariable=self.data_mes,
            values=list(MESES.keys()),
            state="readonly"
        )
        self.combo_mes.set(texto_inicial_mes)
        self.combo_mes.config(width=len(texto_inicial_mes))
        self.combo_mes.grid(row=0, column=1, padx=PADX_CAMPO, pady=PADY_CAMPO, sticky="ew")

        ttk.Label(self.frame_formulario, text="Ano").grid(row=1, column=0, pady=PADY_CAMPO, padx=PADX_LABEL,sticky="e")
        self.data_ano = tk.StringVar()
        self.combo_ano = ttk.Combobox(
            self.frame_formulario,
            textvariable=self.data_ano,
            values=self.anos_str,
            state="readonly"
        )
        self.combo_ano.set(texto_inicial_ano)
        self.combo_ano.config(width=len(texto_inicial_ano))
        self.combo_ano.grid(row=1, column=1, padx=PADX_CAMPO, pady=PADY_CAMPO, sticky="ew")

        ttk.Button(self, text="Próxima página",width=WIDGET_PADRAO, command=self.processar_filtro_estatistica
                   ).grid(row=4, column=0, pady=PADY_BOTAO)

        ttk.Button(self, text="👈 Voltar Menu",width=WIDGET_PADRAO, command=lambda :self.controller.mostrar_tela("menu")
                   ).grid(row=5, column=0, pady=PADY_BOTAO)


    def processar_filtro_estatistica(self):

        mes_nome = self.data_mes.get()#Pega o valor informado pelo usuário (ainda em formato "Janeiro")
        mes = MESES.get(mes_nome)  # Pega MES_NOME e converte para o valor correspondente dentro do dicionpario MESES
        if mes is None:
            messagebox.showerror("Erro",ERROS["error_month"])
            return
        try:
            ano = int(self.data_ano.get())  # Pega o valor informado pelo usuário e transforma em formato INT
        except ValueError:
            messagebox.showerror("Erro",ERROS["error_year"])
            return

        lista_mes_ano = filtrar_por_mes_ano(mes,ano)
        if not lista_mes_ano:
            messagebox.showerror("Erro",ERROS["error_period"])
            return

        # Chama a funcao no CORE para fazer a filtragem com base nos valores informados pelo usuário.
        # devolve lista_mes_ano
        self.controller.mostrar_tela("resultado_estatistica",lista_mes_ano = lista_mes_ano)



