# Lista 02 — Questão 06: Módulo de Estatísticas (programa principal)
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
from q06_estatisticas import media, mediana, moda, desvio_padrao

def main(): #recebe as 10 notas do usuário
    notas = []
    print("Digite 10 notas (floats):")
    for i in range(10):
      while True:
        entrada = input(f"Nota {i+1}: ").strip()
        if entrada == "":
          print("Entrada vazia! Digite um número válido.") #Se não digitar nenhum valor e apertar enter, retorna essa mensagem.
          continue
        try:
          nota = float(entrada)
          notas.append(nota)
          break
        except ValueError:
          print("Valor inválido! Digite um número válido.") #Se digitar letra ou símbolo, retorna essa mensagem ao apertar enter.

    print("\nResultados:") #Mostra os resultados de cada função
    print(f"Média: {media(notas)}")
    print(f"Mediana: {mediana(notas)}")
    print(f"Moda: {moda(notas)}")
    print(f"Desvio Padrão: {desvio_padrao(notas)}")

if __name__ == "__main__":
    main()
