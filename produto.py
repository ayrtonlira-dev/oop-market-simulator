class Produto:
    def __init__(self, nome, preco, estoque, id):

        self.nome = nome
        self.preco = preco
        self.estoque = estoque
        self.id = id

    def __str__(self):
        return f" Produto - {self.nome}//Preço R$ - {self.preco},00// Estoque - {self.estoque}"


    def info(self):
        return (f" {self.nome} - R$ {self.preco},00 - Disponível: - {self.estoque} Código: {self.id}")

    def reduzir_estoque(self, quantidade):
        self.estoque -= quantidade

    def aumentar_estoque(self, quantidade):
        self.estoque += quantidade
