# Desafio 03 — Sistema de Multas
# Aluno: (Leonardo Tupinambá)
# Data:  (20/05/2026)

# ── Escreva sua solução abaixo ──────────────────────────────────────────────
velocidade = float(input("Digite a velocidade atual do carro (km/h): "))

LIMITE = 80

if velocidade > LIMITE:
    excesso = velocidade - LIMITE
    multa = excesso * 7
    print("Multado! Você excedeu o limite de 80km/h")
    print(f"Excesso: {excesso:.1f} km/h | Valor da multa: R$ {multa:.2f}")
else:
    print("Boa viagem! Dirija com segurança")