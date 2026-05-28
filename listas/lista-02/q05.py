# Lista 02 — Questão 05: Funções de Alta Ordem
# Aluno: (Leonardo Tupinambá)
# Data:  (27/05/2026)

# ── Enunciado ───────────────────────────────────────────────────────────────
# Em q05.py: escreva aplicar(lista, funcao) que retorna uma nova lista com a
# função aplicada a cada elemento. Demonstre com:
#   (a) função que eleva ao quadrado
#   (b) função que retorna True se o número for par
# 
# Em q05_resposta.txt: explique o que significa dizer que funções são
# 'cidadãs de primeira classe' em Python.

# ── Sua solução abaixo ──────────────────────────────────────────────────────
# ─────────────────────────────────────────
#  FUNÇÕES COMO CIDADÃS DE PRIMEIRA CLASSE
# ─────────────────────────────────────────

def aplicar(lista, funcao):
    """
    Aplica uma função a cada elemento de uma lista e retorna uma nova lista.

    Args:
        lista (list): Lista de entrada.
        funcao (callable): Qualquer função que aceite um elemento como argumento.

    Returns:
        list: Nova lista com os resultados de funcao(elemento) para cada item.
    """
    return [funcao(elemento) for elemento in lista]


# ── Funções a serem passadas como argumento ───────────────────────────────────

def quadrado(n):
    return n ** 2

def eh_par(n):
    return n % 2 == 0


# ── Demonstração ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    numeros = [1, 2, 3, 4, 5, 6, 7, 8]

    print(f"Lista original : {numeros}")
    print()

    # (a) elevar ao quadrado
    quadrados = aplicar(numeros, quadrado)
    print(f"(a) quadrado   : {quadrados}")

    # (b) verificar paridade
    paridade = aplicar(numeros, eh_par)
    print(f"(b) eh_par     : {paridade}")

    # bônus: mesma função com lambda, sem criar nome
    print()
    print("── Com lambda (sem definir função separada) ──")
    print(f"(a) quadrado   : {aplicar(numeros, lambda n: n ** 2)}")
    print(f"(b) eh_par     : {aplicar(numeros, lambda n: n % 2 == 0)}")