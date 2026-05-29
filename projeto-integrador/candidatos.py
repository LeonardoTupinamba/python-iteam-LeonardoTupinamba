"""
candidatos.py
─────────────────────────────────────────────────────────────────
Módulo de entidades do sistema eleitoral.

Classes:
    Pessoa    — classe base (herança)
    Candidato — representa um candidato na eleição
    Eleitor   — representa um eleitor habilitado
    Voto      — registro anônimo de um voto (garante o sigilo)
"""

from datetime import datetime


# ──────────────────────────────────────────────────────────────────
# CLASSE BASE
# ──────────────────────────────────────────────────────────────────

class Pessoa:
    """Classe base que representa uma pessoa (herdada por Candidato e Eleitor)."""

    def __init__(self, nome: str):
        self._nome = nome  # atributo protegido

    @property
    def nome(self) -> str:
        return self._nome

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(nome={self._nome!r})"


# ──────────────────────────────────────────────────────────────────
# CANDIDATO
# ──────────────────────────────────────────────────────────────────

class Candidato(Pessoa):
    """Representa um candidato na eleição."""

    def __init__(self, numero: int, nome: str, partido: str):
        super().__init__(nome)
        self._numero = numero       # protegido
        self._partido = partido     # protegido
        self.__votos = 0            # privado — name mangling, não editável externamente

    @property
    def numero(self) -> int:
        return self._numero

    @property
    def partido(self) -> str:
        return self._partido

    @property
    def votos(self) -> int:
        return self.__votos

    def _registrar_voto(self) -> None:
        """Método protegido: só a Urna deve chamar."""
        self.__votos += 1

    def __str__(self) -> str:
        return f"[{self._numero:02d}] {self._nome} — {self._partido}"


# ──────────────────────────────────────────────────────────────────
# ELEITOR
# ──────────────────────────────────────────────────────────────────

class Eleitor(Pessoa):
    """Representa um eleitor habilitado."""

    def __init__(self, identificacao: str, nome: str):
        super().__init__(nome)
        self._identificacao = identificacao   # protegido
        self.__ja_votou = False               # privado — name mangling

    @property
    def identificacao(self) -> str:
        return self._identificacao

    @property
    def ja_votou(self) -> bool:
        return self.__ja_votou

    def _marcar_como_votou(self) -> None:
        """Protegido: só a Urna deve alterar o status de votação."""
        self.__ja_votou = True

    def __str__(self) -> str:
        status = "✓ Votou" if self.__ja_votou else "✗ Não votou"
        return f"{self._nome} (ID: {self._identificacao}) — {status}"


# ──────────────────────────────────────────────────────────────────
# VOTO (registro anônimo — garante o SIGILO)
# ──────────────────────────────────────────────────────────────────

class Voto:
    """
    Registra um voto de forma anônima.
    Armazena apenas o número do candidato e o horário — sem vínculo com o eleitor.
    Isso garante o SIGILO do voto.
    """

    def __init__(self, numero_candidato: int):
        self.__numero_candidato = numero_candidato
        self.__horario = datetime.now().strftime("%H:%M:%S")

    @property
    def numero_candidato(self) -> int:
        return self.__numero_candidato

    @property
    def horario(self) -> str:
        return self.__horario