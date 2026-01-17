from datetime import datetime
from despesas_mensagens import CATEGORIAS, ERROS, MENSAGENS, INPUTS

def ler_opcao():
    try:
       return int(input(INPUTS["titulo_opcao"]))
    except ValueError:
        print(ERROS["erro_valor"])
        return None

def escolher_categorias():
    print(MENSAGENS["opcao_categoria"])
    for codigo, nome in CATEGORIAS.items():
        print(f"{codigo} - {nome}")
    try:
        opcao = int(input(INPUTS["categoria_n"]))
        return CATEGORIAS.get(opcao, MENSAGENS["outras_despesas"])
    except ValueError:
        return (MENSAGENS["outras_despesas"])

def adiciona_despesa(despesas):
    try:
        valor = float(input(INPUTS["categoria_v"]))
        descricao = input(INPUTS["descricao"])
        categoria = escolher_categorias()
        data = obter_data()

        despesa = {
            "valor": valor,
            "descricao": descricao,
            "categoria" : categoria,
            "data": data
        }

        despesas.append(despesa)
        print(MENSAGENS["despesa_adicionada"])
    except ValueError:
        print(ERROS["erro_valor"])

def obter_data():
    while True:
        data = input(INPUTS["data"]).strip()

        if not data:
            return datetime.today().strftime("%Y-%m-%d")

        try:
            datetime.strptime(data, "%Y-%m-%d")
            return data
        except ValueError:
            print(MENSAGENS["data_final"])
