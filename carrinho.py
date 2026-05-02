class Carrinho:
    def __init__(self,mercado):
        self.itens = {}
        self.mercado = mercado

    def __str__(self):
        texto = "\n"+ "Itens adicionados ao carrinho:\n"
        total = 0

        for id_produto, quantidade in self.itens.items():
            produto = self.mercado.buscar_produto(id_produto)

            if produto:
                subtotal = produto.preco * quantidade
                total += subtotal
                texto += f"{produto.nome} x{quantidade} → R$ {subtotal:.2f}\n"

        texto += f"\nTotal: R$ {total:.2f}"
        return texto

    def comprar_produto(self, id_produto, quantidade):
        produto = self.mercado.buscar_produto(id_produto)

        if produto is None:

            return ("Produto não encontrado")

        if produto.estoque >= quantidade:
            produto.estoque -= quantidade

            # adiciona no carrinho
            if id_produto in self.itens:
                self.itens[id_produto] += quantidade
            else:
                self.itens[id_produto] = quantidade

            return (f"Adicionado {quantidade}x {produto.nome} ao carrinho")
        else:
            return ("não disponível")
##Função para remover o produto do carrinho
    def remover_produto(self, id_produto, quantidade):
        if id_produto in self.itens:
            produto = self.mercado.buscar_produto(id_produto)
            qtd_carrinho = self.itens[id_produto]

            if quantidade < qtd_carrinho:
                self.itens[id_produto] -= quantidade
                produto.aumentar_estoque(quantidade)
                return (f"{quantidade}x {produto.nome} removido!")

            elif quantidade == qtd_carrinho:
                del self.itens[id_produto]
                produto.aumentar_estoque(quantidade)
                return (f"{produto.nome} removido do carrinho!")

            else:
                return ("Quantidade maior que no carrinho.")
##retorna o total do valor dos itens adicionados no carrinho

    def calcular_total(self):
        total = 0
        for id_produto, quantidade in self.itens.items():
            produto = self.mercado.buscar_produto(id_produto)
            if produto:
               total += "\n" +produto.preco * quantidade
        return total

    ##def concluir_compra(self):
        compra = self.calcular_total()


