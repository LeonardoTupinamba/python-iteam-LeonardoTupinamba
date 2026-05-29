# Desafio 10 — Projeto Final — Urna Eletrônica
# Aluno: (Leonardo Tupinambá)
# Data:  (29/05/2026)

# ── Escreva sua solução abaixo ──────────────────────────────────────

# from candidatos import Candidato, Eleitor, Voto
# from relatorio import Relatorio


# ──────────────────────────────────────────────────────────────────
# CLASSE PRINCIPAL: URNA
# ──────────────────────────────────────────────────────────────────

class Urna:
    
    def __init__(self):
        self.__candidatos: dict[int, Candidato] = {}   # chave: número do candidato
        self.__eleitores: dict[str, Eleitor] = {}       # chave: identificação do eleitor
        self.__votos: list[Voto] = []                   # lista de votos anônimos
        self.__encerrada = False

        # Pré-carregar dados
        self._carregar_candidatos()
        self._carregar_eleitores()

    # ── Configuração inicial ──────────────────────────────────────

    def _carregar_candidatos(self) -> None:
        # """Pré-carrega os candidatos da eleição."""
        candidatos_iniciais = [
            Candidato(13, "Ana Paula Ferreira",   "Chapa Renovação"),
            Candidato(22, "Leonardo Mendonça Tupinambá", "Chapa Liberal"),
            Candidato(45, "Carla Diniz Oliveira", "Chapa União"),
            Candidato(15, "Diego Ramos Costa",    "Chapa Transformação"),
            Candidato(50, "Bruno Souza Mendes",   "Chapa Progresso")
        ]
        for c in candidatos_iniciais:
            self.__candidatos[c.numero] = c

    def _carregar_eleitores(self) -> None:
        # """Pré-carrega o cadastro de eleitores habilitados."""
        eleitores_iniciais = [
            Eleitor("001.001.001-01", "Mariana Azevedo"),
            Eleitor("002.002.002-02", "Lucas Pereira"),
            Eleitor("003.003.003-03", "Fernanda Lima"),
            Eleitor("004.004.004-04", "Rafael Teixeira"),
            Eleitor("005.005.005-05", "Juliana Nascimento"),
            Eleitor("006.006.006-06", "Thiago Barbosa"),
            Eleitor("007.007.007-07", "Priya Santos"),
        ]
        for e in eleitores_iniciais:
            self.__eleitores[e.identificacao] = e

    # ── Exibição ──────────────────────────────────────────────────

    def _exibir_cabecalho(self) -> None:
        print("\n" + "═" * 60)
        print("       URNA ELETRÔNICA")
        print("═" * 60)

    def _exibir_candidatos(self) -> None:
        print("\n CANDIDATOS DISPONÍVEIS")
        for c in self.__candidatos.values():
            print(f"  │  {c}")
        print(" ")

    # ── Fluxo de votação ──────────────────────────────────────────

    def _registrar_voto(self, eleitor: Eleitor, numero_candidato: int) -> None:
        # """
        # Registra o voto de forma sigilosa:
        # - Incrementa o contador do candidato
        # - Marca o eleitor como já votou
        # - Armazena apenas um objeto Voto anônimo (sem referência ao eleitor)
        # """
        candidato = self.__candidatos[numero_candidato]
        candidato._registrar_voto()       # acesso protegido (mesmo pacote)
        eleitor._marcar_como_votou()      # acesso protegido (mesmo pacote)
        self.__votos.append(Voto(numero_candidato))

    def votar(self) -> None:
        # """
        # Executa o fluxo completo de votação para um eleitor.
        # Trata exceções para entradas inválidas, eleitor não cadastrado,
        # voto duplicado e candidato inexistente.
        # """
        self._exibir_cabecalho()

        # ── Etapa 1: Identificação ────────────────────────────────
        identificacao = input("\n  Digite sua identificação (CPF): ").strip()

        # ── Etapas 2 e 3: Validar eleitor ────────────────────────
        try:
            if identificacao not in self.__eleitores:
                raise KeyError(f"Identificação '{identificacao}' não encontrada no cadastro.")

            eleitor = self.__eleitores[identificacao]

            if eleitor.ja_votou:
                raise PermissionError("O eleitor já exerceu seu voto nesta eleição.")

        except KeyError as e:
            print(f"\n  ⚠  ERRO: {e}")
            print("  Verifique sua identificação e tente novamente.\n")
            return
        except PermissionError as e:
            print(f"\n  🚫 VOTO NEGADO: {e}\n")
            return

        # ── Etapa 4: Exibir candidatos ────────────────────────────
        print("\n  Bem-vindo(a)! Você está habilitado(a) a votar.")
        self._exibir_candidatos()

        # ── Etapas 5 e 6: Receber e validar número do candidato ──
        try:
            entrada = input("\n  Digite o NÚMERO do candidato: ").strip()
            numero = int(entrada)  # ValueError se não for número

            if numero not in self.__candidatos:
                raise ValueError(f"Número {numero} não corresponde a nenhum candidato.")

        except ValueError as e:
            print(f"\n  ⚠  ENTRADA INVÁLIDA: {e}")
            print("  Nenhum voto foi registrado.\n")
            return

        # ── Etapa 7: Registrar voto ───────────────────────────────
        self._registrar_voto(eleitor, numero)

        # ── Etapa 8: Confirmar ────────────────────────────────────
        candidato_escolhido = self.__candidatos[numero]
        print(f"\n  ✅ VOTO REGISTRADO COM SUCESSO!")
        print(f"     Candidato: {candidato_escolhido.nome}")
        print(f"     Horário  : {self.__votos[-1].horario}\n")

    # ── Encerramento ──────────────────────────────────────────────

    def encerrar(self) -> None:
        # """Encerra a votação e gera o relatório final."""
        if self.__encerrada:
            print("\n  A urna já foi encerrada.\n")
            return

        self.__encerrada = True
        print("\n  🔒 Votação encerrada pelo operador.")
        Relatorio.gerar(
            list(self.__candidatos.values()),
            list(self.__eleitores.values()),
            self.__votos
        )

    @property
    def encerrada(self) -> bool:
        return self.__encerrada


# ──────────────────────────────────────────────────────────────────
# SISTEMA ELEITORAL — CONTROLADOR PRINCIPAL
# ──────────────────────────────────────────────────────────────────

class SistemaEleitoral:
    # """
    # Controlador de alto nível: gerencia o menu principal
    # e o ciclo de vida da sessão de votação.
    # """

    MENU = """
  ┌─────────────────────────────────┐
  │         MENU DO OPERADOR        │
  ├─────────────────────────────────┤
  │  [V] Iniciar votação            │
  │  [E] Encerrar e apurar          │
  │  [S] Sair do sistema            │
  └─────────────────────────────────┘
  Opção: """

    def __init__(self):
        self._urna = Urna()

    def executar(self) -> None:
        print("\n" + "═" * 60)
        print("   BEM-VINDO AO SISTEMA DE VOTAÇÃO ELETRÔNICA")
        print("═" * 60)

        while True:
            try:
                opcao = input(self.MENU).strip().upper()

                if opcao == "V":
                    if self._urna.encerrada:
                        print("\n  A votação já foi encerrada. Não é possível votar.\n")
                    else:
                        self._urna.votar()

                elif opcao == "E":
                    confirmacao = input("\n  Confirma encerramento? (S/N): ").strip().upper()
                    if confirmacao == "S":
                        self._urna.encerrar()
                    else:
                        print("  Encerramento cancelado.\n")

                elif opcao == "S":
                    print("\n  Sistema encerrado. Até logo!\n")
                    break

                else:
                    print("\n  ⚠  Opção inválida. Use V, E ou S.\n")

            except KeyboardInterrupt:
                print("\n\n  Interrupção detectada. Encerrando sistema...\n")
                break
            except Exception as e:
                # Captura qualquer exceção inesperada sem travar o sistema
                print(f"\n  ⚠  Erro inesperado: {e}. O sistema continua operando.\n")


# ──────────────────────────────────────────────────────────────────
# PONTO DE ENTRADA
# ──────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    sistema = SistemaEleitoral()
    sistema.executar()