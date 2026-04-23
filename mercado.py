class Mercado:
    def __init__(self,nome):
        self.nome = nome
        self.produtos = {}
    def adicionar_produto(self,produto):
        self.produtos[produto.id]= produto
    def listar_produtos(self):
        for produto in self.produtos.values():
            print(produto.info())
    def buscar_produto(self, id_produto):
        return self.produtos.get(id_produto)