# Desafio 02 — Calculadora de IMC
# Aluno: (Leonardo Tupinambá)
# Data:  (19/05/2026)

# ── Escreva sua solução abaixo ──────────────────────────────────────────────
nome = input("Digite seu nome: ")
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

imc = peso / altura ** 2

print(f"Olá {nome}, seu IMC é {imc:.2f}")