# Lista 01 — Questão 03: Ficha de Cadastro
# Aluno: (Leonardo Tupinambá)
# Data:  (24/05/2026)

# ── Enunciado ───────────────────────────────────────────────────────────────
# Solicite: nome completo, CPF (str), ano de nascimento (int), altura (float).
# O programa deve:
#   1. Calcular e exibir a idade em 2026.
#   2. Exibir todos os dados com f-string e tipos corretos.
#   3. Tratar com try/except o caso em que o ano não seja um número.
# Explique em comentário: por que float para altura e não int?

# ── Sua solução abaixo ──────────────────────────────────────────────────────
# Solicita os dados do usuário
nome = input("Digite seu nome completo: ")
cpf = input("Digite seu CPF: ")

try:
    ano_nascimento = int(input("Digite seu ano de nascimento (AAAA): "))
except ValueError:
    print("Erro: o ano de nascimento deve ser um número inteiro.")
    ano_nascimento = None

try:
    altura = float(input("Digite sua altura em metros (ex: 1.75): "))
except ValueError:
    print("Erro: a altura deve ser um número decimal.")
    altura = None

# Calcula idade em 2026, se o ano foi válido
if ano_nascimento is not None:
    idade_2026 = 2026 - ano_nascimento
else:
    idade_2026 = None

# Exibe os dados com f-string
print(f"\n--- Dados informados ---")
print(f"Nome: {nome} (tipo: {type(nome)})")
print(f"CPF: {cpf} (tipo: {type(cpf)})")
print(f"Ano de nascimento: {ano_nascimento} (tipo: {type(ano_nascimento)})")
print(f"Altura: {altura} (tipo: {type(altura)})")
print(f"Idade em 2026: {idade_2026} (tipo: {type(idade_2026)})")
# Foi usado float para altura porque a altura pode conter casas decimais (ex: 1.75m),