"""
Funções com retorno

print(print('oi'))
# a função print não retorna dados, logo, o retorno da função que imprime o texto 'oi' é None
numeros = [1, 2, 3]

ret_pop = numeros.pop()  # -> retorna o elemento eliminado da lista
print(ret_pop)

ret_pr = print(numeros)  # print não retorna dados

print(ret_pr)

# em python, se funções sem retorno forem armazenadas, a variavel está nula (none)
# a cláusula return faz a função retornar os dados desejados
# não precisamos criar uma variavel para receber o retorno de uma função;
 Podemos passar a execução para outras funções.



def quadrado_de_7():
    return 7 * 7


# a chamada da função precisa ser realizada após a sua declaração em programação estruturada
ret = quadrado_de_7()
print(f'Retorno {ret}')
print(f'Retorno {quadrado_de_7()}')

print(f'Retorno {quadrado_de_7() + 1}')
"""
# Refatorando a primeira função
