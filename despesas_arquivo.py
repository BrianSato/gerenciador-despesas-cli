import json
import os

ARQUIVO = "despesas.json"

#  FUNCOES PARA SALVAR  E CARREGAR OS DADOS EM ARQUIVO

def salva_despesas(despesas):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(despesas,f,ensure_ascii=False, indent=4)

def carregar_despesas():
    if not os.path.exists(ARQUIVO):
        return[]

    with open(ARQUIVO, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return[]
