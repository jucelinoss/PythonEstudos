from classes import CarrinhoDeCompras, Produto


carrinho = CarrinhoDeCompras()

p1 = Produto('Camiseta', 50)
p2 = Produto('iPhone', 10000)
p3 = Produto('Caneca', 15)


# Agregação é o tipo de associação no qual uma classe depende a outra para funcionar corretamente. Pneu e carro podem existir separadamente, mas um não funciona corretamente sem o outro. 

# Carrinho e produto podem existir sozinhos, mas as operações do carrinho só fazem sentido se ele estiver preenchido (não faz sentido listar carrinho vazio)
carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)
carrinho.inserir_produto(p1)
carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)

carrinho.lista_produto()
print(carrinho.soma_total())