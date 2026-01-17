# 💰 Gerenciador de Despesas em Python (CLI)

Projeto desenvolvido com o objetivo de consolidar conceitos fundamentais de programação em Python
por meio da construção de um sistema real de gerenciamento de despesas pessoais via terminal.

O foco do projeto é sair de exercícios isolados e aplicar boas práticas de organização, modularização
e persistência de dados, resultando em um código claro, evolutivo e adequado para portfólio.

---

## 🎯 Funcionalidades

- Adicionar despesas com:
  - valor
  - descrição
  - categoria padronizada
- Listar todas as despesas cadastradas
- Exibir estatísticas:
  - total gasto
  - média das despesas
  - maior e menor valor
- Filtrar despesas por categoria
- Persistência de dados em arquivo JSON
- Interface via menu no terminal (CLI)

---

## 🧱 Estrutura do Projeto

```text
.
├── despesas_principal.py      # Ponto de entrada do programa
├── despesas_menu.py           # Exibição do menu e opções
├── despesas_adiciona.py       # Inclusão de despesas e escolha de categorias
├── despesas_listar.py         # Listagem de despesas
├── despesas_filtrar.py        # Filtros (ex: por categoria)
├── despesas_calculos.py       # Estatísticas e cálculos
├── despesas_arquiva.py        # Persistência (JSON)
└── despesas.json              # Arquivo de dados
```
---
## 🧠 Conceitos Aplicados

- Estruturas de dados (listas e dicionários)
- Modularização e separação de responsabilidades
- Funções puras para regras de negócio
- Persistência de dados com JSON
- Tratamento de exceções (try/except)
- Boas práticas de organização de código
- Padrão de commits (Conventional Commits)
---
## 📌 Arquitetura

O projeto segue uma separação clara entre:

- Interface (UI)
  
Entrada de dados e exibição de informações ao usuário.

- Domínio (Regras de Negócio)
  
Funções responsáveis apenas por processar dados, sem input ou print.

Essa abordagem facilita manutenção, testes e futuras evoluções
(ex: interface gráfica ou aplicação web).
---

## 🚀 Como Executar

1- Clone o repositório:
```
git clone <url-do-repositorio>
```

2- Acesse a pasta do projeto:
```
cd gerenciador-despesas-python
```

3- Execute o programa:
```
python despesas_principal.py
```
---
## 🔮 Próximos Passos (Roadmap)

- Adicionar data da despesa
- Relatórios por período
- Totais por categoria
- Melhorias na experiência do usuário
- Evolução para interface gráfica ou web
---
## 🧑‍💻 Autor

Projeto desenvolvido como parte da jornada de aprendizado em programação,
com foco em Python, lógica, organização e boas práticas.

