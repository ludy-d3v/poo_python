class Produto:
    def __init__ (self, nome, preco, quantidade):
        self.__nome = nome
        self.__preco = preco
        self.__quantidade = quantidade

    def get__nome(self):
        return self.__nome
    
    def get__preco(self):
        return self.__preco
    
    def get__quantidade(self):
        return self.__quantidade
    
    def set__nome(self, novo_nome):
        self.__nome = novo_nome

    def set__preco(self, novo_preco):
        self.__preco = novo_preco

    def set__quantidade(self, nova_quantidade):
        self.__quantidade = nova_quantidade
    
class CarrinhoDeCompras:
    def __init__(self):
        self.__produtos = []
    
    def adicionar_produto(self, produto):
        self.__produtos.append(produto)

    def remover_produto(self, nome):
        for produto in self.__produtos:
            if produto.get__nome() == nome:
                self.__produtos.remove(produto)
                print(f"\nProduto removido com sucesso!")
                return
            else:
                print("\nProduto não encontrado no carrinho.")
    
    def calcular_valor_total(self):
        total = 0
        for produto in self.__produtos:
            total += produto.get__preco() * produto.get__quantidade()
        return total
    
    def listar_produtos(self):
        if not self.__produtos:
            print("\nO carrinho está vazio.")
            return
        else:
            print("\nPRODUTOS NO CARRINHO: ")
            for produto in self.__produtos:
                print(f"\nNome do produto: {produto.get__nome()}, Preço: {produto.get__preco()}, Quantidade: {produto.get__quantidade()}")

def main():
    carrinho = CarrinhoDeCompras()

    while True:
        print("\n==== SISTEMA DE CARRINHO DE COMPRAS ====")
        print("\n[ MENU ]")
        print("\n1 - Adicionar produto")
        print("2 - Remover produto")
        print("3 - Listar produtos")
        print("4 - Calcular valor total")
        print("5 - Sair")

        opcao = input("\nEscolha uma opção (1-5): ")

        if opcao == '1':
            nome = input("\nDigite o nome do produto: ")
            preco = float(input("Digite o preço do produto: "))
            quantidade = int(input("Digite a quantidade do produto: "))
            produto = Produto(nome, preco, quantidade)
            carrinho.adicionar_produto(produto)
            print("\nProduto adicionado com sucesso!")

        elif opcao == '2':
            nome = input("\nDigite o nome do produto a ser removido: ")
            carrinho.remover_produto(nome)

        elif opcao == '3':
            carrinho.listar_produtos()
        
        elif opcao == '4':
            print(f"\nO valor total do carrinho é: R$ {carrinho.calcular_valor_total():.2f}")
        
        elif opcao == '5':
            print("\nObrigada por usar nosso sistema. Até mais! ;)\n")
            break
        else:
            print("\nOpção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
            