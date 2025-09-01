class Impressao:
    def __init__(self, string):
        self.string = string

    def numeros_caracteres(self):
        num_caracteres = len(self.string)
        return num_caracteres
    
    def string_maiscula(self):
        return self.string.upper()
    
    def string_minuscula(self):
        return self.string.lower()
    
    def string_vogais(self):
        vogais = 'aeiouAEIOU'
        encontradas = [char for char in self.string if char in vogais]
        return encontradas

    def substring(self):
        if 'IFB' in self.string:
            print("A substring 'IFB' foi encontrada na string.")
            
        else:
            print("A substring 'IFB' não foi encontrada na string.")

def main():
    texto = input("\nDigite uma string: ")
    impressao = Impressao(texto)
    print(f"\nNúmero de caracteres: {impressao.numeros_caracteres()}")
    print(f"\nString em maiúsculas: {impressao.string_maiscula()}")
    print(f"\nString em minúsculas: {impressao.string_minuscula()}")
    print(f"\nVogais na string: {impressao.string_vogais()}\n")
    print(impressao.substring())

if __name__ == "__main__":
    main()