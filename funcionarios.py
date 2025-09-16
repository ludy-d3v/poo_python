class Funcionario:
    def __init__ (self, nome, salario_base):
        self.nome = nome
        self.salario_base = salario_base

    def calcular_salario(self):
        return self.salario_base
    
    def exibir_dados(self):
        if not self.nome:
            print("\nNenhum funcionário cadastrado.")
            return
        print(f"\nNome: {self.nome}")
        print(f"\nSalário Base: {self.salario_base}")
    
class FuncionarioComissionado(Funcionario):
    def __init__ (self, nome, salario_base, comissao):
        super().__init__(nome, salario_base)
        self.comissao = comissao

    def calcular_salario(self):
        if not self.nome:
            print("\nNenhum funcionário cadastrado.")
            return 0
        total = super().calcular_salario() + self.comissao
        return total

    def exibir_dados(self):
        super().exibir_dados()
        print(f"\nComissão: {self.comissao}")

def main():

    while True:
        print("\n==== FUNCIONARIO ====")
        print("\n[ MENU ]")
        print("\n1 - Adicionar funcionario")
        print("2 - Adicionar comissão")
        print("3 - Calcular salario")
        print("4 - Exibir dados do funcionario")
        print("5 - Sair")

        opcao = input("\nEscolha uma opção (1-5): ")

        if opcao == "1":
            nome = input("\nNome do funcionário: ")
            salario_base = float(input("\nSalário base do funcionário: "))
            if salario_base < 0:
                print("\nSalário base não pode ser negativo. Tente novamente.")
                continue
            funcionario = Funcionario(nome, salario_base)
            print("\nFuncionário adicionado com sucesso!")

        elif opcao == "2":
            comissao = float(input("\nValor da comissão: "))
            funcionario_comissionado = FuncionarioComissionado(nome, salario_base, comissao)
            funcionario = funcionario_comissionado
            print("\nComissão adicionada com sucesso!")

        elif opcao == "3":
            funcionario.calcular_salario()
            print(f"\nSalário total: R$ {funcionario.calcular_salario():.2f}")

        elif opcao == "4":
            funcionario.exibir_dados()

        elif opcao == "5":
            print("\nEncerrando o sistema...")
            break
        else:
            print("\nOpção inválida. Tente novamente.")

if __name__ == "__main__":
    main()