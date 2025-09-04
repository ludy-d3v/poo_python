class Criptografia:
    def __init__(self, frase):
        self.frase = frase

    def criptografar(self):
        #subtituicoes = {
        #    'a': '4', 'A': '4',
        #    'e': '3', 'E': '3',
        #    'i': '1', 'I': '1',
        #    'o': '0', 'O': '0',
        #    'u': '8', 'U': '8'
        #}
        #for caracter in subtituicoes:
        #  if caracter in self.frase:
        #       frase_criptografada += subtituicoes[caracter]
        # else:
        #   frase_criptografada += caracter  
        frase_criptografada = self.frase.replace('a', '4').replace('e', '3').replace('i', '1').replace('o', '0').replace('u', '8').replace('A', '4').replace('E', '3').replace('I', '1').replace('O', '0').replace('U', '8')
        return frase_criptografada

def main():
    frase = input("\nDigite uma frase para criptografar: ")
    criptografia = Criptografia(frase)
    frase_criptografada = criptografia.criptografar()
    
    print(f"\nFrase original: {frase}")
    print(f"\nFrase criptografada: {frase_criptografada}\n")

if __name__ == "__main__":
    main()