class Progressao:
    def __init__(self, n, a1, r):
        self.n = n
        self.a1 = a1
        self.r = r

    def pa(self):
        termos = []
        for i in range(self.n):
            termo = self.a1 + i * self.r
            termos.append(termo)
        return termos
    
    def soma_pa(self):
        an = self.a1 + (self.n - 1) * self.r
        soma = self.n * (self.a1 + an) / 2
        return soma
    
def main():
    print("\n=== Progressão Aritmética ===")
    a1 = float(input("\nDigite o primeiro termo (a1): "))
    r = float(input("\nDigite a razão (r): "))
    n = int(input("\nDigite o número de termos (n): "))

    pa = Progressao(n, a1, r)
    termos = pa.pa()
    print(f"\nTermos da PA: {termos}")

    soma = pa.soma_pa()
    print(f"\nSoma dos termos da PA: {soma}\n")

if __name__ == "__main__":
    main()