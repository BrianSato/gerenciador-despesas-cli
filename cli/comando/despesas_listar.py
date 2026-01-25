from despesas_mensagens import ERROS,MENSAGENS

def msg_lista():
    print(MENSAGENS["titulo_despesa"])

def listar_despesas(despesas):
    if not despesas:
        print(ERROS["sem_despesa"])
        return

    msg_lista()
    for i, despesa in enumerate(despesas, start=1):
        print(
            f"{i}.{despesa.get('data', 'sem data')} - " 
            f" R$ {despesa['valor']:.2f} - "
            f"{despesa['descricao']} - "
            f"{despesa.get('categoria', 'Sem categoria')}"
        )