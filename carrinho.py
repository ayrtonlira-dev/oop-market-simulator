class Carrinho:
    def __init__(self):
        self.itens = []

    def __str__(self):
            texto = "Itens adicionados ao carrinho:\n"

            for produto, quantidade in self.itens:
                subtotal = produto.preco * quantidade
                texto += f"{produto.nome} x{quantidade} → R$ {subtotal:.2f}\n"

            texto += f"\nTotal: R$ {self.calcular_total():.2f}"
            return texto

    def adicionar_produto(self, produto, quantidade):
        if produto.estoque >= quantidade:
            produto.reduzir_estoque(quantidade)
            self.itens.append((produto,quantidade))
        else:
            print("Quantidade maior que disponível.")

    def calcular_total(self):
        total = 0
        for produto, quantidade in self.itens:
            total += produto.preco * quantidade
        return total