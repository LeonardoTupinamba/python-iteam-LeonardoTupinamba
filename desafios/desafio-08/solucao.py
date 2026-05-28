# Desafio 08 — Banco Digital
# Aluno: (Leonardo Tupinambá)
# Data:  (28/05/2026)

# ── Escreva sua solução abaixo ──────────────────────────────────────────────
class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0.0):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, valor):
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser positivo.")
        self.saldo += valor

    def sacar(self, valor):
        if valor <= 0:
            raise ValueError("O valor do saque deve ser positivo.")
        if valor > self.saldo:
            raise ValueError("Saldo insuficiente para saque.")
        self.saldo -= valor

    def exibir_extrato(self):
        print(f"Titular: {self.titular} | Saldo atual: R$ {self.saldo:.2f}")


# Demonstração
if __name__ == "__main__":
    conta = ContaBancaria("Leonardo", 1000.0)
    conta.exibir_extrato()

    conta.depositar(500)
    conta.exibir_extrato()

    conta.sacar(200)
    conta.exibir_extrato()

    try:
        conta.sacar(2000)  # tentativa de saque além do saldo
    except ValueError as e:
        print("Erro:", e)

    conta.exibir_extrato()
