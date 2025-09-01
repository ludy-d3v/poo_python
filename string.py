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
        contador = 0
    
        for caracter in self.string:
            if caracter in vogais:
                contador += 1
        return contador

    def substring(self):
        return "IFB" in self.string.upper()

def main():
    texto = input("\nDigite um texto: ")
    impressao = Impressao(texto)
    print(f"\nNúmero de caracteres: {impressao.numeros_caracteres()}")
    print(f"\nString em maiúsculas: {impressao.string_maiscula()}")
    print(f"\nString em minúsculas: {impressao.string_minuscula()}")
    print(f"\nVogais na string: {impressao.string_vogais()}\n")
    
    if impressao.substring():
        print("A substring 'IFB' aparece no texto.\n")
    else:
        print("A substring 'IFB' NÃO está presente no texto.\n")

if __name__ == "__main__":
    main()