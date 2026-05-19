# Desafio 01 — Seu Primeiro Script
# Aluno: (Leonardo Tupinambá)
# Data:  (18/05/2026)

# ── Escreva sua solução abaixo ──────────────────────────────────────────────
nome = input("Qual é o seu nome? ")
ano_nascimento = int(input("Qual é o seu ano de nascimento? "))

ano_atual = 2026
idade = ano_atual - ano_nascimento

print(f"\nOlá, {nome}!")
print(f"Você tem {idade} anos.")

print("\nQuais são os seus hobbies principais?")
print("(Digite cada hobby e pressione Enter. Deixe em branco para terminar.)")

hobbies = []
while True:
    hobby = input("Hobby: ")
    if hobby == "":
        break
    hobbies.append(hobby)

if hobbies:
    print(f"\nOs hobbies principais de {nome} são:")
    for i, hobby in enumerate(hobbies, start=1):
        print(f"  {i}. {hobby}")
else:
    print(f"\n{nome} não informou nenhum hobby.")