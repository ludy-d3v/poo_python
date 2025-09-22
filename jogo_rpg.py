class Personagem:
    def __init__ (self, nome, nivel):
        self._nome = nome
        self._nivel = nivel

    def atacar(self):
        print(f"\n{self._nome} realiza um ataque genérico!")

class Guerreiro(Personagem):
    def __init__(self, nome, nivel, forca):
        super().__init__(nome, nivel)
        self.__forca = forca 

    def atacar(self):
        print(f"\nGuerreiro {self._nome} realiza um ataque fisico com força! (Força: {self.__forca})")
    
class Mago(Personagem):
    def __init__ (self, nome, nivel, mana):
        super().__init__(nome, nivel)
        self.__mana = mana
    
    def atacar(self):
        print(f"\nMago {self._nome} realiza um ataque com magia e mana! (Mana: {self.__mana})\n")

def main():
    personagem = Personagem("Hero", 7)
    guerreiro = Guerreiro("Kratos", 8, 80)
    mago = Mago("Nextage", 9, 95)

    lista_personagens = [personagem, guerreiro, mago]

    print("\n=== AÇÃO DE ATAQUE DOS PERSONAGENS ===")
    for p in lista_personagens:
        p.atacar()

    """personagem.atacar()
    guerreiro.atacar()
    mago.atacar()"""

if __name__ == "__main__":
    main()
