# Desafio 04 — Tabuada Personalizada
# Aluno: (Leonardo Tupinambá)
# Data:  (21/05/2026)

# ── Escreva sua solução abaixo ──────────────────────────────────────────────
print("MINHA TABUADA PERSONALIZADA\n")
print("Digite 0 a qualquer momento para sair.\n")

while True:
    entrada = input("Digite um número de 1 a 10: ")

    numero = int(entrada)

    if numero == 0:
        print("Encerrando... Até mais!")
        break

    if numero < 1 or numero > 10:
        print("Número fora do intervalo. Digite entre 1 e 10.\n")
        continue

    print(f"\n--- Tabuada do {numero} ---")
    for i in range(1, 11):
        print(f"{numero} x {i:2} = {numero * i:3}")
    print() 