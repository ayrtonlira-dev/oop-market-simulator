from mercado import Mercado
from carrinho import Carrinho
from produto import Produto


mercado = Mercado("Senna's Market")


produto1 = Produto("Arroz", 10, 10, 1)
produto2 = Produto("Feijão", 9, 10,2)
produto3 = Produto("Banana", 5, 5,3)
produto4 = Produto("Frango",25,15,4)


mercado.adicionar_produto(produto1)
mercado.adicionar_produto(produto2)
mercado.adicionar_produto(produto3)
mercado.adicionar_produto(produto4)
print(mercado.nome)

##Mostra os produtos disponiveis, com valor e quantidade em estoque
mercado.listar_produtos()
carrinho = Carrinho()

##Adiciona o produto ao carrinho
carrinho.adicionar_produto(produto3,3)
carrinho.adicionar_produto(produto4,10)

print(carrinho)

mercado.listar_produtos()


