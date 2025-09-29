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

try:
    placa = input("\nDigite a placa do ônibus: ")
    if placa.strip() == "":
        raise TypeError("A placa não pode estar vazia.")
    
    capacidadePassageiros = int(input("\nDigite a capacidade de passageiros do ônibus: "))
    if capacidadePassageiros <= 0:
        raise ValueError("O valor não pode ser negativo ou zero.")
    
    consumoPorKm = float(input("\nDigite o consumo do ônibus por km (em litros): "))
    if consumoPorKm <= 0:
        raise ValueError("O consumo de energia por km não pode ser negativo ou zero.")
    
    onibus = Onibus(placa, capacidadePassageiros, consumoPorKm)

    placa = input("\nDigite a placa do metrô: ")
    if placa.strip() == "":
        raise ValueError("A placa não pode estar vazia.")
    
    capacidadePassageiros = int(input("\nDigite a capacidade de passageiros do metrô: "))
    if capacidadePassageiros <= 0:
        raise ValueError("O valor não pode ser negativo ou zero.")
    
    consumoEnergiaPorKm = float(input("\nDigite o consumo de energia por km: "))
    if consumoEnergiaPorKm <= 0:
        raise ValueError("O consumo de energia por km não pode ser negativo ou zero.")
    
    metro = Metro(placa, capacidadePassageiros, consumoEnergiaPorKm)

    transportes = [onibus, metro]

    for transporte in transportes:
        custo = transporte.calcularCustoOperacional()
        print(f"\nCusto operacional do veículo {transporte.placa}: R$ {custo:.2f}\n")
    
except TypeError as erro:
    print("Erro:", erro)
except ValueError as erro:
    print("Erro:", erro)
finally:
    print("\nPrograma finalizado.")