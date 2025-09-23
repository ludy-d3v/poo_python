class Personagem:
    def __init__ (self, nome, constelacao):
        self._nome = nome
        self._constelacao = constelacao
    
    def apresentar(self):
        print(f"{self._nome}, cavaleiro da constelação {self._constelacao}!")
    
class CavaleiroDeBronze(Personagem):
    def __init__ (self, nome, constelacao, poder_de_luta):
        super().__init__(nome, constelacao)
        self.poder_de_luta = poder_de_luta
    
    def golpe_especial(self):
        print(F"\n{self._nome} executa seu golpe especial com poder de luta {self.poder_de_luta}!")

class CavaleiroDeOuro(Personagem):
    def __init__ (self, nome, constelacao, casa_do_zodiaco):
        super().__init__(nome, constelacao)
        self.casa_do_zodiaco = casa_do_zodiaco

    def defender_casa(self):
        print(f"{self._nome} defende a casa de {self.casa_do_zodiaco} com honra!")

class CavaleiroHibrido(CavaleiroDeBronze, CavaleiroDeOuro):
    def __init__ (self, nome, constelacao, poder_de_luta, casa_do_zodiaco):
        CavaleiroDeOuro.__init__(self, nome, constelacao, casa_do_zodiaco)
        self.poder_de_luta = poder_de_luta
    
    def golpe_especial(self):
        print(F"\n{self._nome} realiza um golpe híbrido com poder de luta {self.poder_de_luta}!")

    def defender_casa(self):
        print(f"{self._nome} defende a casa de {self.casa_do_zodiaco} com honra!")

def main():
    personagens = []

    while True:
        print("\n==== CAVALEIROS DO ZODÍACO ====")
        print("\n[ MENU ]")
        print("\n1 - Cadastrar personagens")
        print("2 - Listar todos os personagens")
        print("3 - Executar habilidades")
        print("0 - Encerrar o programa")

        opcao = input("\nEscolha uma opção (0-3): ")

        if opcao == "1":
            tipo = input("Tipo de Cavaleiro (1 - Cavaleiro de Bronze, 2 - Cavaleiro de Ouro, 3 - Cavaleiro Híbrido): ")

            if tipo == "1":
                nome = input("\nNome do personagem: ")
                constelacao = input("Constelação do personagem: ")
                poder_de_luta = input("Seu poder de luta: ")
                personagem = CavaleiroDeBronze(nome, constelacao, poder_de_luta)
                
            elif tipo == "2":
                nome = input("\nNome do personagem: ")
                constelacao = input("Constelação do personagem: ")
                casa_do_zodiaco = input("Casa do zodíaco: ")
                personagem = CavaleiroDeOuro(nome, constelacao, casa_do_zodiaco)
                

            elif tipo == "3":
                nome = input("\nNome do personagem: ")
                constelacao = input("Constelação do personagem: ")
                casa_do_zodiaco = input("Casa do zodíaco: ")
                poder_de_luta = input("Seu poder de luta: ")
                personagem = CavaleiroHibrido(nome, constelacao, casa_do_zodiaco, poder_de_luta)
                
            else:
                print("\nConstelação inválido. Tente novamente.")
                continue

            personagens.append(personagem)
            print("\nCavaleiro adicionado com sucesso!")

        elif opcao == "2":
            if personagens:
                print("\n==== LISTA DE PERSONAGENS ====\n")
                for p in personagens:
                    p.apresentar()
            else:
                print("\nNenhum personagem cadastrado.")
                continue 
            
        elif opcao == "3":
                for p in personagens:
                    if isinstance(p, CavaleiroDeBronze):
                        p.golpe_especial()
                    if isinstance(p, CavaleiroDeOuro):
                        p.defender_casa()
            
        elif opcao == "0":
            print("\nSaindo do sistema...\n")
            break

        else:
            print("\nOpção inválida. Tente novamente.")

if __name__ == "__main__":
    main()