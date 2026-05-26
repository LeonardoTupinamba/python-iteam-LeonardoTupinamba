# Desafio 06 — Bio-Cadastro
# Aluno: (Leonardo Tupinambá)
# Data:  (25/05/2026)

# ── Escreva sua solução abaixo ──────────────────────────────────────────────
equipe = []

while True:
    nome = input("Digite o nome do colaborador (ou 'sair' para encerrar): ")
    if nome.lower() == "sair":
        break
    cargo = input("Digite o cargo do colaborador: ")

    funcionario = {
        "nome": nome,
        "cargo": cargo
    }
    equipe.append(funcionario)

print("\n--- Lista de Funcionários ---")
for funcionario in equipe:
    print(f"Funcionário: {funcionario['nome']} | Cargo: {funcionario['cargo']}")
