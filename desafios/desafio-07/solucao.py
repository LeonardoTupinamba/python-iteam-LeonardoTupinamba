# Desafio 07 — Bio-Calculadora
# Aluno: (Leonardo Tupinambá)
# Data:  (26/05/2026)

# ── Escreva sua solução abaixo ──────────────────────────────────────────────
from funcoes_mat import area_circulo, volume_esfera, hipotenusa

MENU = """
|-----------------------------|
|     CALCULADORA GEOMÉTRICA  |
|                             |
|  1. Área do Círculo         |
|  2. Volume da Esfera        |
|  3. Hipotenusa              |
|  0. Sair                    |
|-----------------------------|
Escolha uma opção: """       


def pedir_numero(mensagem):
    """Solicita um número float ao usuário, repetindo em caso de entrada inválida."""
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("  ✗ Entrada inválida. Digite um número.\n")


def main():
    while True:
        opcao = input(MENU).strip()

        if opcao == "1":
            raio = pedir_numero("  Raio: ")
            resultado = area_circulo(raio)
            print(f"\n  ✓ Área do círculo: {resultado:.2f}\n")

        elif opcao == "2":
            raio = pedir_numero("  Raio: ")
            resultado = volume_esfera(raio)
            print(f"\n  ✓ Volume da esfera: {resultado:.2f}\n")

        elif opcao == "3":
            a = pedir_numero("  Cateto A: ")
            b = pedir_numero("  Cateto B: ")
            resultado = hipotenusa(a, b)
            print(f"\n  ✓ Hipotenusa: {resultado:.2f}\n")

        elif opcao == "0":
            print("\n  Encerrando. Até mais!\n")
            break

        else:
            print("\n  ✗ Opção inválida. Tente novamente.\n")


if __name__ == "__main__":
    main()