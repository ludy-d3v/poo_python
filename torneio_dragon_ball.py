from abc import ABC, abstractmethod

class Lutador(ABC):

    @abstractmethod
    def obter_nome(self):
        pass

    @abstractmethod
    def obter_nivel_de_poder(self):
        pass

    @abstractmethod
    def atacar(self):
        pass

class Saiyajin(Lutador):
    def __init__ (self, nome, nivel_de_poder):
        self.nome = nome
        self.nivel_de_poder = nivel_de_poder

    def obter_nome(self):
        return self.nome
    
    def obter_nivel_de_poder(self):
        return self.nivel_de_poder

    def atacar(self):
        return f"\n{self.nome} se transforma em Super Saiyajin e lança com poder {self.nivel_de_poder}"
    
class Androide(Lutador):
    def __init__ (self, nome, nivel_de_poder):
        self.nome = nome
        self.nivel_de_poder = nivel_de_poder

    def obter_nome(self):
        return self.nome
    
    def obter_nivel_de_poder(self):
        return self.nivel_de_poder

    def atacar(self):
        return f"\n{self.nome} usa energia infinita com poder {self.nivel_de_poder}"

class Namekuseijin(Lutador):
    def __init__ (self, nome, nivel_de_poder):
        self.nome = nome
        self.nivel_de_poder = nivel_de_poder

    def obter_nome(self):
        return self.nome
    
    def obter_nivel_de_poder(self):
        return self.nivel_de_poder

    def atacar(self):
        return f"\n{self.nome} estica os braços e ataca com golpes seguidos com poder {self.nivel_de_poder}"
    
def main():
    lutadores = []

    while True:
        print("\n--- TORNEIO DE ARTES MARCIAIS ---")
        print("\n1. Cadastrar lutadores")
        print("2. Listar lutadores")
        print("3. Simular ataque")
        print("4. Sair")

        opcao = input("\nEscolha uma opção (1-4): ")

        if opcao == "1":
            print("\nCadastro de Lutadores")

            try:
                raca = input("\nRaça do lutador: (1) Saiyajin, (2) Androide, (3) Namekuseijin: ").strip()

                if raca not in ["1", "2", "3"]:
                    raise ValueError("Raça inválida. Escolha 1, 2 ou 3.")
                
                nome = input("\nNome do lutador: ").strip()
                if nome == "":
                    raise ValueError("O nome não pode estar vazio.")
                
                nivel_de_poder = int(input("\nNível do poder: "))
                if nivel_de_poder <= 0:
                    raise ValueError("O nível de poder deve ser positivo.")
                
                if raca == "1":
                    lutadores.append(Saiyajin(nome, nivel_de_poder))
                elif raca == "2":
                    lutadores.append(Androide(nome, nivel_de_poder))
                elif raca == "3":
                    lutadores.append(Namekuseijin(nome, nivel_de_poder))

                print(f"\nLutador {nome} cadastrado com sucesso!")
            
            except ValueError as e:
                print(f"\nErro: {e}")
        
        elif opcao == "2":
            if not lutadores:
                print("\nNenhum lutador cadastrado.")
            else:
                print("\nLutadores cadastrados no torneio: ")
                for i, l in enumerate(lutadores, start=1):
                    print(f"\n{i}. {l.nome} (Nível de poder: {l.nivel_de_poder})")
        
        elif opcao == "3":
            if not lutadores:
                print("\nNenhum lutador cadastrado para atacar.")
            else:
                print("\nLutadores do Torneio para atacar:")
                for i, l in enumerate(lutadores, start=1):
                    print(f"\n{i}. {l.nome} (Nível de poder: {l.nivel_de_poder})")

            try:
                escolha = int(input("\nEscolha o número do lutador para atacar: "))
                if 1 <= escolha <= len(lutadores):
                    print(f"\n{lutadores[escolha - 1].obter_nome()} ataca!")
                    print(lutadores[escolha - 1].atacar())
                else:
                    raise Exception("Número inválido para escolha do lutador.")
                
            except Exception as e:
                print(f"\nErro: {e}")

        elif opcao == "4":
            print("\nEncerrando o torneio...\n")
            break

        else: 
            print("\nOpção inválida. Tente novamente.")

if __name__ == "__main__":
    main()