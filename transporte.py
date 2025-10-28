from abc import ABC, abstractmethod

class VeiculoTransporte(ABC):
    def __init__ (self, placa, capacidadePassageiros):
        self.placa = placa
        self.capacidadePassageiros = capacidadePassageiros

    @abstractmethod
    def calcularCustoOperacional(self):
        pass

class Onibus(VeiculoTransporte):
    def __init__ (self, placa, capacidadePassageiros, consumoPorKm):
        super().__init__(placa, capacidadePassageiros)
        self.consumoPorKm = consumoPorKm

    def calcularCustoOperacional(self):
        custoPorKm = 6.0
        return self.consumoPorKm * custoPorKm
    
class Metro(VeiculoTransporte):
    def __init__ (self, placa, capacidadePassageiros, consumoEnergiaPorKm):
        super().__init__(placa, capacidadePassageiros)
        self.consumoEnergiaPorKm = consumoEnergiaPorKm

    def calcularCustoOperacional(self):
        custoPorKwh = 0.8
        return self.consumoEnergiaPorKm * custoPorKwh
    
def main():
    veiculos = []

    while True:
        print("\n--- Cadastro de Veículos de Transporte ---")
        print("\n1. Cadastrar ônibus")
        print("2. Cadastrar metrô")
        print("3. Mostrar custos operacionais")
        print("4. Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            print("\nCadastro de Ônibus")
            
            try:
                placa = input("\nDigite a placa do ônibus: ").strip()
                if placa == "":
                    raise ValueError("A placa não pode estar vazia.")
                
                capacidadePassageiros = int(input("\nCapacidade de passageiros: "))
                if capacidadePassageiros <= 0:
                    raise ValueError("A capacidade deve ser um número positiva.")
                
                consumoPorKm = float(input("\nConsumo do ônibus por km (em litros): "))
                if consumoPorKm <= 0:
                    raise ValueError("O consumo deve ser um número positivo.")
                
                veiculos.append(Onibus(placa, capacidadePassageiros, consumoPorKm))

                print("\nÔnibus cadastrado com sucesso!")

            except ValueError as e:
                print(f"\nErro: {e}")

        elif opcao == "2":
            print("\nCadastro de Metrô")
            
            try:
                placa = input("\nDigite a identificação do metrô: ").strip()
                if placa == "":
                    raise ValueError("A identificação não pode estar vazia.")
                
                capacidadePassageiros = int(input("\nCapacidade de passageiros: "))
                if capacidadePassageiros <= 0:
                    raise ValueError("A capacidade deve ser um número positiva.")
                
                consumoEnergiaPorKm = float(input("\nConsumo de energia do metrô por km (kWm/km): "))
                if consumoEnergiaPorKm <= 0:
                    raise ValueError("O consumo deve ser um número positivo.")
                
                veiculos.append(Metro(placa, capacidadePassageiros, consumoEnergiaPorKm))

                print("\nMetrô cadastrado com sucesso!")

            except ValueError as e:
                print(f"Erro: {e}\n")

        elif opcao == "3":
            if not veiculos:
                print("\nNenhum veículo cadastrado.")
            else:
                print("\n--- Custos Operacionais dos Veículos ---")
                for veiculo in veiculos:
                    tipo = "Ônibus" if isinstance(veiculo, Onibus) else "Metrô"
                    custo = veiculo.calcularCustoOperacional()
                    print(f"\n{tipo} - {veiculo.placa}: R$ {custo:.2f}")
        
        elif opcao == "4":
            print("\nEncerrando o programa...\n")
            break

        else: 
            print("\nOpção inválida. Tente novamente.")

if __name__ == "__main__":
    main()