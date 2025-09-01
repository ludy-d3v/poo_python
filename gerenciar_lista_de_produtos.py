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
    def __init__(self, adicionar_produto, remover_produto, calcular_valor_total, listar_produtos):
        self.__adicionar_produto = adicionar_produto
        self.__remover_produto = remover_produto
        self.__calcular_valor_total = calcular_valor_total
        self.__listar_produtos = listar_produtos
        self.__produtos = []
    
    def adicionar_produto(self, produto):
        self.__produtos.append(produto)