# Lista 01 — Questão 07: Progressão e Análise
# Aluno: (Leonardo Tupinambá)
# Data:  (24/05/2026)

# ── Enunciado ───────────────────────────────────────────────────────────────
# Leia 10 notas (0.0–10.0) com validação (try/except + while para inválidas).
# Exiba: maior nota, menor nota, média, quantidade acima da média e
# classificação (Aprovado ≥ 7.0, Recuperação ≥ 5.0, Reprovado).
# Explique em comentários por que escolheu for ou while em cada parte.

# ── Sua solução abaixo ──────────────────────────────────────────────────────
notas = []
i = 0

# Usei while aqui porque precisei validar cada entrada individualmente:
# se o usuário digitar inválido, repito a mesma posição até ser válido.
while i < 10:
    try:
        nota = float(input(f"Digite a nota {i+1} (0.0–10.0): "))
        if 0.0 <= nota <= 10.0:
            notas.append(nota)
            i += 1
        else:
            print("Erro: a nota deve estar entre 0.0 e 10.0.")
    except ValueError:
        print("Erro: digite um número válido (use ponto para decimais).")

# Após coletar todas as notas, usamos for para percorrer a lista:
# for é mais natural aqui porque sabemos exatamente o conjunto de elementos.
maior = max(notas)
menor = min(notas)
media = sum(notas) / len(notas)

# Contar quantas estão acima da média
acima_media = sum(1 for n in notas if n > media)

# Classificação geral pela média
if media >= 7.0:
    classificacao = "Aprovado"
elif media >= 5.0:
    classificacao = "Recuperação"
else:
    classificacao = "Reprovado"

# Exibir resultados
print("\n--- Resultados ---")
print(f"Notas: {notas}")
print(f"Maior nota: {maior}")
print(f"Menor nota: {menor}")
print(f"Média: {media:.2f}")
print(f"Quantidade acima da média: {acima_media}")
print(f"Classificação: {classificacao}")

# while na leitura: usei porque não sabemos quantas vezes o usuário precisará digitar até fornecer uma nota válida. O while permite repetir indefinidamente até que a condição seja satisfeita.

# for na análise: usei porque já temos uma lista completa de notas e queremos percorrer cada elemento uma vez. O for é mais simples e direto para iterar sobre coleções conhecidas.