from interface import criar_interface
from mercado import Mercado
from carrinho import Carrinho
from produto import Produto




mercado = Mercado("Senna's Market")

##Cdastro de Produto para ser adicionado ao estoque
produto1 = Produto("Batata",  10, 10, 1)
produto2 = Produto("Banana", 10, 10, 2)
produto3 = Produto("Feijão", 15, 10, 3)
produto4 = Produto("Frango", 20, 10, 4)
produto5 = Produto("Açúcar", 5, 30,5)

##Adiciona o produto ao "Estoque"
mercado.adicionar_produto(produto1)
mercado.adicionar_produto(produto2)
mercado.adicionar_produto(produto3)
mercado.adicionar_produto(produto4)
mercado.adicionar_produto(produto5)

print(mercado.nome)

##Mostra os produtos disponiveis, com valor e quantidade em estoque
#mercado.listar_produtos()


##Mostra as movimentações do carrinho e total das "compras"

carrinho = Carrinho(mercado)
print(carrinho)
# ##Adiciona o produto

criar_interface(mercado,carrinho)

# while True:
#     opcao = input("""
#     1 - Checar produtos
#     2 - Adicionar ao carrinho
#     3 - Remover do carrinho
#     4 - Ver carrinho
#     5 - Sair
#     Escolha: """)
#
#     if opcao == "1":
#         mercado.listar_produtos()
#
#     elif opcao == "2":
#         id_produto = int(input("Código do produto: "))
#         qtd = int(input("Quantidade: "))
#         carrinho.comprar_produto(id_produto, qtd)
#
#     elif opcao == "3":
#         id_produto = int(input("Digite o código do produto: "))
#         qtd = int(input("Quantidade: "))
#         carrinho.remover_produto(id_produto, qtd)
#
#     elif opcao == "4":
#         print(carrinho)
#
#     elif opcao == "5":
#         print("Volte sempre...")
#         break
#
#     else:
#         print("Opção inválida")










