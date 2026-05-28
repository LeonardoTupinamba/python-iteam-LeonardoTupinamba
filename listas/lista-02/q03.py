# Lista 02 — Questão 03: Sistema de Inventário
# Aluno: (Leonardo Tupinambá)
# Data:  (27/05/2026)

# ── Enunciado ───────────────────────────────────────────────────────────────
# Implemente com lista de dicionários:
#   1. adicionar_produto(inventario, nome, codigo, quantidade, preco)
#   2. buscar_por_codigo(inventario, codigo)  → produto ou None
#   3. listar_abaixo_do_minimo(inventario, minimo)
#   4. valor_total(inventario)  → soma de quantidade × preço
# Use funções para cada operação. Demonstre as 4 no código principal.

# ── Sua solução abaixo ──────────────────────────────────────────────────────
# ─────────────────────────────────────────
#  GERENCIADOR DE INVENTÁRIO
# ─────────────────────────────────────────

def adicionar_produto(inventario, nome, codigo, quantidade, preco):
    """
    Adiciona um novo produto ao inventário.

    Args:
        inventario (list): Lista de dicionários de produtos.
        nome (str): Nome do produto.
        codigo (str): Código único do produto.
        quantidade (int): Quantidade em estoque.
        preco (float): Preço unitário.

    Returns:
        bool: False se o código já existir, True se adicionado com sucesso.
    """
    if buscar_por_codigo(inventario, codigo) is not None:
        print(f"  ✗ Código '{codigo}' já existe no inventário.")
        return False

    produto = {
        "nome": nome,
        "codigo": codigo,
        "quantidade": quantidade,
        "preco": preco,
    }
    inventario.append(produto)
    return True


def buscar_por_codigo(inventario, codigo):
    """
    Busca um produto pelo seu código único.

    Args:
        inventario (list): Lista de dicionários de produtos.
        codigo (str): Código do produto a buscar.

    Returns:
        dict | None: O dicionário do produto se encontrado, None caso contrário.
    """
    for produto in inventario:
        if produto["codigo"] == codigo:
            return produto
    return None


def listar_abaixo_do_minimo(inventario, minimo):
    """
    Retorna produtos cuja quantidade está abaixo do estoque mínimo.

    Args:
        inventario (list): Lista de dicionários de produtos.
        minimo (int): Quantidade mínima de referência.

    Returns:
        list: Lista de produtos com estoque abaixo do mínimo.
    """
    return [p for p in inventario if p["quantidade"] < minimo]


def valor_total(inventario):
    """
    Calcula o valor total do inventário (quantidade × preço de cada item).

    Args:
        inventario (list): Lista de dicionários de produtos.

    Returns:
        float: Soma do valor de todos os produtos em estoque.
    """
    return sum(p["quantidade"] * p["preco"] for p in inventario)


# ─────────────────────────────────────────
#  HELPERS DE EXIBIÇÃO
# ─────────────────────────────────────────

def exibir_produto(produto):
    print(f"  [{produto['codigo']}] {produto['nome']:<20} "
          f"Qtd: {produto['quantidade']:>4}   "
          f"Preço: R$ {produto['preco']:>7.2f}")

def separador(titulo=""):
    linha = "─" * 48
    print(f"\n{linha}")
    if titulo:
        print(f"  {titulo}")
        print(linha)


# ─────────────────────────────────────────
#  PROGRAMA PRINCIPAL
# ─────────────────────────────────────────

if __name__ == "__main__":
    inventario = []

    # 1. ADICIONAR PRODUTOS
    separador("1. ADICIONANDO PRODUTOS")
    adicionar_produto(inventario, "Teclado Mecânico",  "KB-001", 15,  349.90)
    adicionar_produto(inventario, "Mouse Gamer",       "MS-002", 3,   189.90)
    adicionar_produto(inventario, "Monitor 24\"",      "MN-003", 8,  1299.00)
    adicionar_produto(inventario, "Headset USB",       "HS-004", 2,   249.90)
    adicionar_produto(inventario, "Webcam Full HD",    "WC-005", 12,  199.90)

    # Tentativa de código duplicado
    adicionar_produto(inventario, "Teclado Clone",     "KB-001", 5,   99.90)

    print()
    for p in inventario:
        exibir_produto(p)

    # 2. BUSCAR POR CÓDIGO
    separador("2. BUSCA POR CÓDIGO")

    for codigo in ("MS-002", "ZZ-999"):
        resultado = buscar_por_codigo(inventario, codigo)
        if resultado:
            print(f"  ✓ Encontrado: ", end="")
            exibir_produto(resultado)
        else:
            print(f"  ✗ Código '{codigo}' não encontrado.")

    # 3. ESTOQUE ABAIXO DO MÍNIMO
    separador("3. ESTOQUE ABAIXO DO MÍNIMO (< 5 unidades)")

    criticos = listar_abaixo_do_minimo(inventario, minimo=5)
    if criticos:
        for p in criticos:
            print(f"  ⚠  ", end="")
            exibir_produto(p)
    else:
        print("  Nenhum produto abaixo do mínimo.")

    # 4. VALOR TOTAL DO INVENTÁRIO
    separador("4. VALOR TOTAL DO INVENTÁRIO")

    total = valor_total(inventario)
    print(f"  Produtos cadastrados : {len(inventario)}")
    print(f"  Valor total em estoque: R$ {total:,.2f}")
    print()