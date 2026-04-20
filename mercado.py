class Mercado:
    def __init__(self,nome):
        self.nome = nome
        self.produtos = []
    def adicionar_produto(self,produto):
        self.produtos.append(produto)
    def listar_produtos(self):
        for produto in self.produtos:
            print(produto.info())