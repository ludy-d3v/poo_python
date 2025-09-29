class Calculadora:

    def somar(self, x, y):
        return x + y
    
    def subtrair(self, x, y):
        return x - y
    
    def multiplicar(self, x, y):
        return x * y
    
    def dividir(self, x, y):
        if y == 0:
            raise ZeroDivisionError("Divisão por zero não é permitida.")
        return x / y

class Interface:
    def __init__(self):
        self.calc = Calculadora()
    
    def menu(self):

        while True:

            print("\n==== Calculadora Simples ====")
            print("\n1 - Soma")
            print("2 - Subtração")
            print("3 - Multiplicação")
            print("4 - Divisão")
            print("5 - Sair")

            opcao = input("\nEscolha uma opção (1-5): ").strip()

            if opcao == "5":
                print("\nSaindo do programa...")
                break

            if opcao not in {"1", "2", "3", "4", "5"}:
                print("\nOpção inválida. Tente novamente.")
                continue

            try:
                x = float(input("\nInsira um número: "))
                y = float(input("\nInsira outro número: "))

                if opcao == "1":
                    resultado = self.calc.somar(x,y)

                elif opcao == "2":
                    resultado = self.calc.subtrair(x,y)

                elif opcao == "3":
                    resultado = self.calc.multiplicar(x,y)

                elif opcao == "4":
                    resultado = self.calc.dividir(x,y)

                print(f"\nResultado: {resultado}")

            except ZeroDivisionError as erro:
                print("\nErro:", erro)
            except TypeError as erro:
                print("\nErro:", erro)
            except ValueError:
                print("\nErro: Por favor, insira um número válido.")
            finally:
                print("\nOperação finalizada.")

if __name__ == "__main__":
    interface = Interface()
    interface.menu()