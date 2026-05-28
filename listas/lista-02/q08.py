# Lista 02 — Questão 08: Herança e Polimorfismo
# Aluno: (Leonardo Tupinambá)
# Data:  (28/05/2026)

# ── Enunciado ───────────────────────────────────────────────────────────────
# Implemente:
#   - Funcionario(nome, salario): calcular_bonus() → 10% do salário
#   - Gerente(departamento): bônus = 20%
#   - Estagiario(curso): bônus = 5%
# Crie lista com objetos dos 3 tipos, itere exibindo nome e bônus.
# Explique em comentário: por que o Python chama a versão correta de
# calcular_bonus() sem você verificar o tipo do objeto?

# ── Sua solução abaixo ──────────────────────────────────────────────────────
class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def calcular_bonus(self):
        return self.salario * 0.10


class Gerente(Funcionario):
    def __init__(self, nome, salario, departamento):
        super().__init__(nome, salario)
        self.departamento = departamento

    def calcular_bonus(self):
        return self.salario * 0.20


class Estagiario(Funcionario):
    def __init__(self, nome, salario, curso):
        super().__init__(nome, salario)
        self.curso = curso

    def calcular_bonus(self):
        return self.salario * 0.05


# Criando lista com objetos dos três tipos
funcionarios = [
    Funcionario("Ana", 3000),
    Gerente("Carlos", 8000, "TI"),
    Estagiario("Mariana", 1500, "Engenharia")
]

# Iterando e exibindo nome e bônus
for f in funcionarios:
    print(f"{f.nome} → Bônus: R$ {f.calcular_bonus():.2f}")

# O Python chama a versão correta de calcular_bonus() graças ao POLIMORFISMO.
# Quando usamos f.calcular_bonus(), o interpretador verifica o tipo real do objeto
# (Funcionario, Gerente ou Estagiario) e invoca automaticamente o método
# sobrescrito correspondente. Isso acontece porque em Python os métodos são
# resolvidos dinamicamente em tempo de execução, sem necessidade de verificar
# manualmente o tipo do objeto.
