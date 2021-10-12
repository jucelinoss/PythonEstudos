"""
Reduce

Obs.: a função reduce deixou de ser uma função built-in no Python 3.x.
Para utilizá-la, é necessário importar o módulo 'functools'

Guido van Rossum: utilize a função reduce() se realmente precisa dela. Em todo caso,
99% das vezes um loop for é mais legível
Para entender o reduce()
# imagine que tenha uma coleção de dados:
dados = [a1, a2, a3, ..., aN]
# e que vc tem uma função que recebe dois parametros:
def funcao(x, y)
    return x * y

Assim como map() e filter(), a função reduce recebe dois parametros: a função e o iterável
reduce(funcao, dados)

A função reduce() funciona da seguinte forma:
    Passo 1: res1 = f(a1, a2) # Aplicação a finção aos dois primeiros elementos da coleção e guarda o resultado
    Passo 2: res2 = f(res1, a3) # aplica a função passando o resultado do passo1 + o terceiro elemento + guarda o result

    Isso é repetido até o final.
    Passo 3: res3 = f(res2, a4)

    ...
    Passo n: resN = f(resN, aN)

    A cada passo, é passado o resultado da função anterior, de forma cumulativa.

    Alternativamente, poderíamos ver a função reduce() como:
    funcao(funcao(funcao(a1, a2), a3), a4), .... aN)
"""
from functools import reduce

dados = [2, 3, 4, 5, 6, 11, 17, 19, 23, 29]

# para utilizar o reduce() nós precisamos de uma função que receba dois parametros
multi = lambda x, y: x * y
res = reduce(multi, dados)
print(res)

# via loop
res = 1
for n in dados:
    res *= n

print(res)
