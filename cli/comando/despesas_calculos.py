def mostrar_total_e_media(despesas):
    if not  despesas:
        print("Nenhuma despesas adicionada.")
        return

    total = 0
    for despesa in despesas:
        total += despesa["valor"]
    media = total/ len(despesas)
    print(f"----- Despesas Totais: ----\n"
          f"💰 Total gasto: R$ {total:.2f}\n"
          f"📊A média de despesas: R$ {media:.2f}\n")

def maior_menor_valor(despesas):
    if not despesas:
        print("Nenhuma despesa adicionada")
        return
    maior = despesas[0]["valor"]
    menor = despesas[0]["valor"]
    for despesa in despesas:
        if despesa["valor"] > maior:
            maior = despesa["valor"]
        elif despesa["valor"] < menor:
            menor = despesa["valor"]
    print(f" A maior despesa foi: R${maior:.2f}")
    print(f" A menor despesa foi: R${menor:.2f}")