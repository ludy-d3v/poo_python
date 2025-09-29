from abc import ABC, abstractmethod

class ClubeParticipante(ABC):
    def __init__ (self, nome, pais, confederacao, ranking_fifa, gols_marcados, vitorias):
        self.nome = nome
        self.pais = pais
        self.confederacao = confederacao
        self.ranking_fifa = ranking_fifa
        self.gols_marcados = gols_marcados
        self.vitorias = vitorias

    def exibir_dados(self):
        print(f"Dados do clube: {self.nome}")
        print(f"País: {self.pais}")
        print(f"Condeferação: {self.confederacao}")
        print(f"Ranking FIFA: {self.ranking_fifa}")
        print(f"Gols: {self.gols_marcados}")
        print(f"Vitórias: {self.vitorias}")


    @abstractmethod
    def calcular_desempenho(self):
        pass

    @abstractmethod
    def gerar_relatorio_tecnico(self):
        pass

class ClubeUEFA(ClubeParticipante):
    def __init__ (self, nome, pais, confederacao, ranking_fifa, gols_marcados, vitorias):
        super().__init__(nome, pais, confederacao, ranking_fifa, gols_marcados, vitorias)

    def calcular_desempenho(self):
        return (self.vitorias * 3) + (self.gols_marcados * 0.5)

    def gerar_relatorio_tecnico(self):
        self.exibir_dados()
        desempenho = self.calcular_desempenho()
        return f"Relatório Técnico UEFA: {self.nome} - Desempenho: {desempenho:.2f}"

class ClubeCONMEBOL(ClubeParticipante):
    def __init__ (self, nome, pais, confederacao, ranking_fifa, gols_marcados, vitorias):
        super().__init__(nome, pais, confederacao, ranking_fifa, gols_marcados, vitorias)

    def calcular_desempenho(self):
        return (self.vitorias * 3) + (self.gols_marcados * 0.7)

    def gerar_relatorio_tecnico(self):
        self.exibir_dados()
        desempenho = self.calcular_desempenho()
        return f"Relatório Técnico CONMEBOL: {self.nome} - Desempenho: {desempenho:.2f}"
    
def main():
    real_madrid = ClubeUEFA("Real Madrid", "Espanha", "UEFA", 1, 2, 10)

    botafogo = ClubeCONMEBOL("Flamengo", "Brasil", "Rio de Janeiro", 2, 2, 10)

    clubes = [real_madrid, botafogo]

    for clube in clubes:
        print("-" * 40 )
        clube.gerar_relatorio_tecnico()

if __name__ == "__main__":
    main()