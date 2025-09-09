class Funcionario:
    def __init__ (self, nome, salario):
        self.nome = nome
        self.salario = salario

class Departamento:
    def __init__ (self, nome):
        self.nome = nome
        self.funcionarios = []

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)
    
    def listar_funcionarios(self):
        if not self.funcionarios:
            print("\nNenhum funcionário neste departamento.\n")
        else:
            for f in self.funcionarios:
                print(f"\n{f.nome} - Salário: R$ {f.salario:.2f}\n")

    def media_salarial(self):
        soma = 0
        if not self.funcionarios:
            return 0
        else:
            for f in self.funcionarios:
                soma += f.salario
            return soma/len(self.funcionarios)

def main():
    funcionarios = []
    departamentos = []

    while True:
        print("\n==== MENU ====")
        print("\n1. Criar funcionário")
        print("2. Criar departamento")
        print("3. Adicionar funcionário ao departamento")
        print("4. Listar funcionários de um departamento")
        print("5. Calcular média salarial do departamento")
        print("6. Sair")

        opcao = input("\nEscolha uma opção (1-6): ")

        if opcao == '1':
            nome = input("\nNome do funcionário: ")
            salario = float(input("Salário do funcionário: "))
            funcionarios.append(Funcionario(nome, salario))
            print(f"\nFuncionário {nome} criado com sucesso!")

        elif opcao == '2':
            nome = input("\nNome do departamento:")
            departamentos.append(Departamento(nome))
            print(f"\nDepartamento {nome} criado com sucesso!")

        elif opcao == '3':
            if funcionarios and departamentos:
                print("\nFuncionários:")
                for i, f in enumerate(funcionarios):
                    print(f"{i + 1}. {f.nome}")
                i_func = int(input("\nEscolha o número do funcionário: ")) - 1

                print("\nDepartamentos:")
                for j, d in enumerate(departamentos):
                    print(f"{j + 1}. {d.nome}")
                j_dep = int(input("\nEscolha o número do departamento: ")) - 1

                departamentos[j_dep].adicionar_funcionario(funcionarios[i_func])
                print(f"\nFuncionário {funcionarios[i_func].nome} adicionado ao departamento {departamentos[j_dep].nome}!")
            else:
                print("\nCrie funcionários e departamentos primeiro.")

        elif opcao == '4':
            print("\nDepartamentos:")
            for j, d in enumerate(departamentos):
                print(f"{j + 1}. {d.nome}")
            j_dep = int(input("\nEscolha o número do departamento: ")) - 1

            departamentos[j_dep].listar_funcionarios()

        elif opcao == '5':
            print("\nDepartamentos:")
            for j, d in enumerate(departamentos):
                print(f"{j + 1}. {d.nome}")
            j_dep = int(input("\nEscolha o número do departamento: ")) - 1

            media = departamentos[j_dep].media_salarial()
            if media == 0:
                print("\nNenhum funcionário neste departamento.\n")
            else:
                print(f"\nMédia salarial do {departamentos[j_dep].nome}: R$ {media:.2f}\n")

        elif opcao == '6':
            print("\nSaindo do programa...")
            break

        else:
            print("\nOpção inválida. Tente novamente.")

if __name__ == "__main__":
    main()