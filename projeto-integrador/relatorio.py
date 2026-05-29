"""
relatorio.py
─────────────────────────────────────────────────────────────────
Módulo de apuração e exibição de resultados.

Classes:
    Relatorio — formata e imprime o relatório final da eleição
"""

from datetime import datetime


# ──────────────────────────────────────────────────────────────────
# RELATÓRIO
# ──────────────────────────────────────────────────────────────────

class Relatorio:
    """Responsável por formatar e exibir o relatório final de apuração."""

    @staticmethod
    def gerar(candidatos: list, eleitores: list, votos: list) -> None:
        total_habilitados = len(eleitores)
        total_votos = len(votos)
        participacao = (total_votos / total_habilitados * 100) if total_habilitados > 0 else 0

        print("\n" + "═" * 60)
        print("          RELATÓRIO FINAL DE APURAÇÃO")
        print("═" * 60)
        print(f"  Data/Hora de encerramento : {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"  Eleitores habilitados     : {total_habilitados}")
        print(f"  Votos registrados         : {total_votos}")
        print(f"  Participação              : {participacao:.1f}%")
        print(f"  Abstenções                : {total_habilitados - total_votos}")
        print("─" * 60)
        print("  RESULTADO POR CANDIDATO (ordem decrescente de votos)")
        print("─" * 60)

        # Ordenar candidatos por votos (decrescente)
        candidatos_ord = sorted(candidatos, key=lambda c: c.votos, reverse=True)

        for pos, c in enumerate(candidatos_ord, start=1):
            pct = (c.votos / total_votos * 100) if total_votos > 0 else 0
            barra = "█" * int(pct / 5)  # barra proporcional (escala: cada █ = 5%)
            print(f"  {pos}º  {str(c):<40}")
            print(f"       Votos: {c.votos:>4}  ({pct:5.1f}%)  {barra}")
            print()

        # Vencedor / Empate
        print("─" * 60)
        max_votos = candidatos_ord[0].votos
        vencedores = [c for c in candidatos_ord if c.votos == max_votos]

        if len(vencedores) == 1:
            print(f"  🏆 VENCEDOR: {vencedores[0].nome} ({vencedores[0].partido})")
            print(f"             com {max_votos} voto(s) ({(max_votos / total_votos * 100) if total_votos else 0:.1f}%)")
        else:
            nomes = " | ".join(c.nome for c in vencedores)
            print(f"  ⚖  EMPATE entre: {nomes}")
            print("     O critério de desempate será definido pelo regulamento.")

        print("═" * 60 + "\n")