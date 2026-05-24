# Lista 01 — Questão 06: Validador de Senha
# Aluno: (Leonardo Tupinambá)
# Data:  (24/05/2026)

# ── Enunciado ───────────────────────────────────────────────────────────────
# Escreva um programa que solicite uma senha em loop até que atenda TODOS:
#   1. Mínimo 8 caracteres.
#   2. Pelo menos um dígito (use .isdigit() em cada caractere).
#   3. Pelo menos uma letra maiúscula.
# Para cada tentativa inválida, informe qual critério não foi atendido.
# Ao aceitar: 'Senha válida após X tentativa(s).'

# ── Sua solução abaixo ──────────────────────────────────────────────────────
tentativas = 0

while True:
    senha = input("Digite uma senha: ")
    tentativas += 1
    erros = []

    # Critério 1: mínimo 8 caracteres
    if len(senha) < 8:
        erros.append("A senha deve ter pelo menos 8 caracteres.")

    # Critério 2: pelo menos um dígito
    if not any(ch.isdigit() for ch in senha):
        erros.append("A senha deve conter pelo menos um dígito.")

    # Critério 3: pelo menos uma letra maiúscula
    if not any(ch.isupper() for ch in senha):
        erros.append("A senha deve conter pelo menos uma letra maiúscula.")

    # Verifica se todos os critérios foram atendidos
    if not erros:
        print(f"Senha válida após {tentativas} tentativa(s).")
        break
    else:
        # Exibe quais critérios falharam
        print("Senha inválida. Motivos:")
        for erro in erros:
            print("-", erro)
