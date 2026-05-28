# Lista 02 — Questão 09: Encapsulamento e Propriedades
# Aluno: (Leonardo Tupinambá)
# Data:  (28/05/2026)

# ── Enunciado ───────────────────────────────────────────────────────────────
# Em q09.py — classe Produto com:
#   1. __preco via @property com validação (preço > 0)
#   2. __estoque com getter, repor(qtd) e vender(qtd) — ValueError se sem estoque
#   3. __str__ informativo e __repr__ para debug
# Demonstre: criação, vendas, reposição e tentativa de venda além do estoque.
# 
# Em q09_resposta.txt: explique a diferença entre _atributo e __atributo em Python.

# ── Sua solução abaixo ──────────────────────────────────────────────────────
class Produto:
    def __init__(self, nome, preco, estoque=0):
        self.nome = nome
        self.__preco = None
        self.preco = preco  # usa o setter para validar
        self.__estoque = estoque

    # --- Preço com validação ---
    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, valor):
        if valor <= 0:
            raise ValueError("O preço deve ser maior que zero.")
        self.__preco = valor

    # --- Estoque ---
    @property
    def estoque(self):
        return self.__estoque

    def repor(self, qtd):
        if qtd <= 0:
            raise ValueError("Quantidade de reposição deve ser positiva.")
        self.__estoque += qtd

    def vender(self, qtd):
        if qtd <= 0:
            raise ValueError("Quantidade de venda deve ser positiva.")
        if qtd > self.__estoque:
            raise ValueError("Estoque insuficiente para a venda.")
        self.__estoque -= qtd

    # --- Representações ---
    def __str__(self):
        return f"Produto: {self.nome}, Preço: R$ {self.preco:.2f}, Estoque: {self.estoque}"

    def __repr__(self):
        return f"Produto(nome={self.nome!r}, preco={self.preco}, estoque={self.estoque})"


# Demonstração
if __name__ == "__main__":
    p = Produto("Caneta", 2.50, estoque=10)
    print(p)

    # Vendas
    p.vender(3)
    print("Após vender 3:", p)

    # Reposição
    p.repor(5)
    print("Após repor 5:", p)

    # Tentativa de venda além do estoque
    try:
        p.vender(20)
    except ValueError as e:
        print("Erro:", e)

    # Debug
    print("Debug:", repr(p))
