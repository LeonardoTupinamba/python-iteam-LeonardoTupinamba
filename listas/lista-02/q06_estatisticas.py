# Lista 02 — Questão 06: Módulo de Estatísticas (módulo estatísticas)
# Aluno: (Leonardo Tupinambá)
# Data:  (28/05/2026)

# ── Enunciado ───────────────────────────────────────────────────────────────
# q06_estatisticas.py: crie o módulo com as funções:
#   media(dados), mediana(dados), moda(dados), desvio_padrao(dados)
# Todas devem: receber lista de floats, validar que não está vazia
# (lançar ValueError se estiver), retornar resultado arredondado (2 casas).
# Use apenas stdlib (math permitido, não use statistics).
# 
# q06_main.py: importe o módulo e aplique as 4 funções sobre 10 notas
# digitadas pelo usuário.

# ── Sua solução abaixo ──────────────────────────────────────────────────────
import math

def validar(dados):
    if not dados:
        raise ValueError("A lista de dados não pode estar vazia.")

def media(dados):
    validar(dados)
    resultado = sum(dados) / len(dados)
    return round(resultado, 2)

def mediana(dados):
    validar(dados)
    dados_ordenados = sorted(dados)
    n = len(dados_ordenados)
    meio = n // 2
    if n % 2 == 0:
        resultado = (dados_ordenados[meio - 1] + dados_ordenados[meio]) / 2
    else:
        resultado = dados_ordenados[meio]
    return round(resultado, 2)

def moda(dados):
    validar(dados)
    frequencias = {}
    for valor in dados:
        frequencias[valor] = frequencias.get(valor, 0) + 1
    max_freq = max(frequencias.values())
    modas = [valor for valor, freq in frequencias.items() if freq == max_freq]
    # Se houver mais de uma moda, retorna a primeira
    return round(modas[0], 2)

def desvio_padrao(dados):
    validar(dados)
    m = media(dados)
    variancia = sum((x - m) ** 2 for x in dados) / len(dados)
    resultado = math.sqrt(variancia)
    return round(resultado, 2)
