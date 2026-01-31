from tkinter import ttk
from core.despesas_filtrar_core import filtrar_por_periodo
from core.despesas_arquivo_core import carregar_despesas

class TelaResultadoPeriodo(ttk.Frame):
    def __init__(self, parent,data_inicio,data_fim, voltar_callback):
        super().__init__(parent)
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.voltar_callback = voltar_callback
        self.criar_widgets()
        self.carregar_dados()


    def criar_widgets(self):
        titulo = ttk.Label(self, text="Lista De despesas por Periodo", font=("Aria", 14, "bold"))
        titulo.pack(pady=10)

        colunas = ("valor", "descricao", "categoria", "data")

        self.tabela = ttk.Treeview(self, columns=colunas, show="headings")
        self.tabela.heading("valor", text="Valor"),
        self.tabela.heading("descricao", text="Descrição"),
        self.tabela.heading("categoria", text="Categoria"),
        self.tabela.heading("data", text="Data")

        for col in colunas:
            self.tabela.column(col, anchor="center")

        self.tabela.pack(fill="both", expand=True, padx=10, pady=10)

        ttk.Button(self, text="👈 Voltar", command=self.voltar_callback
                   ).pack(pady=10)

    def carregar_dados(self):

        despesas = carregar_despesas()
        dados = filtrar_por_periodo(despesas, self.data_inicio,self.data_fim)

        for despesa in dados:
            self.tabela.insert(
                "",
                "end",
                values=(
                    despesa.get("valor", ""),
                    despesa.get("descricao", ""),
                    despesa.get("categoria", ""),
                    despesa.get("data", "")
                )
            )