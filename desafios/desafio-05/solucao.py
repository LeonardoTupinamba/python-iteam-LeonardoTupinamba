# Desafio 05 — Gerenciador de Compras
# Aluno: (Leonardo Tupinambá)
# Data:  (24/05/2026)

# ── Escreva sua solução abaixo ──────────────────────────────────────────────
# solucao.py

produtos = []

while True:
    nome = input("Digite o nome do produto (ou 'fim' para encerrar): ")
    if nome.lower() == "fim":  
        break
    produtos.append(nome)      

print("\n--- Resultado ---")
print("Lista de produtos:", sorted(produtos))
print("Total de itens:", len(produtos))
