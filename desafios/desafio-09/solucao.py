# Desafio 09 — Sistema de Frota
# Aluno: (Leonardo Tupinambá)
# Data:  (28/05/2026)

# ── Escreva sua solução abaixo ──────────────────────────────────────────────
class Veiculo:
    def __init__(self, marca, ano):
        self.marca = marca
        self.ano = ano
        self.__quilometragem = 0

    def rodar(self, km):
        if km <= 0:
            raise ValueError("Quilometragem deve ser positiva.")
        self.__quilometragem += km

    def exibir_dados(self):
        return f"Marca: {self.marca}, Ano: {self.ano}, Quilometragem: {self.__quilometragem} km"


class Caminhao(Veiculo):
    def __init__(self, marca, ano, capacidade_carga):
        super().__init__(marca, ano)
        self.capacidade_carga = capacidade_carga

    def exibir_dados(self):
        dados_base = super().exibir_dados()
        return f"{dados_base}, Capacidade de carga: {self.capacidade_carga} toneladas"


class Moto(Veiculo):
    def __init__(self, marca, ano, cilindradas):
        super().__init__(marca, ano)
        self.cilindradas = cilindradas

    def exibir_dados(self):
        dados_base = super().exibir_dados()
        return f"{dados_base}, Cilindradas: {self.cilindradas} cc"


# Demonstração
if __name__ == "__main__":
    caminhao = Caminhao("Volvo", 2020, 18)
    moto = Moto("Honda", 2022, 250)

    caminhao.rodar(500)
    moto.rodar(120)

    print(caminhao.exibir_dados())
    print(moto.exibir_dados())

    # Tentativa de rodar com valor inválido
    try:
        moto.rodar(-50)
    except ValueError as e:
        print("Erro:", e)
