

def processar_maior_despesa(lista_mes_ano):
    maior = lista_mes_ano[0]["valor"]

    for linha in lista_mes_ano:
        if linha["valor"] > maior:
            maior = linha["valor"]
    return maior

def processar_menor_despesa(lista_mes_ano):
    menor = lista_mes_ano[0]["valor"]

    for linha in lista_mes_ano:
        if linha["valor"] < menor:
            menor = linha["valor"]
    return menor

def processar_total_despesa(lista_mes_ano):
    total = 0
    for linha in lista_mes_ano:
        total += linha["valor"]
    return total

def processar_media_despesa(lista_mes_ano):
    total = 0
    media = 0
    for linha in lista_mes_ano:
        total += linha["valor"]
        quantidade = len(lista_mes_ano)
        media  = total / quantidade
    return media
