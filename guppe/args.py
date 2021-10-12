"""
Entendendo o *args
Tipo especial de parâmetro
Recebe qualquer valor, desde que seja iniciado com asterisco *
Exemplo
*xis
Por convenção, utilizamos *args para definí-lo
O parâmetro * args utilizado em uma função coloca os valores extras informados como
entrada em uma tupla, que é imutável

# Exemplo
def soma_todos_numeros(num1, num2, num3):
    return num1 + num2 + num3

print(soma_todos_numeros(2, 3, 5))



# Entendeno *args
from funcoes_com_parametro import soma


def soma_todos_numeros(*args):
    return sum(args)
#    total = 0
#   for numero in args:
#        total += numero
#    return total


print(soma_todos_numeros())
print(soma_todos_numeros(1))
print(soma_todos_numeros(1, 2))
print(soma_todos_numeros(1, 2, 3))
print(soma_todos_numeros(1, 2, 3, 4))
print(soma_todos_numeros(1, 2, 3, 4, 5))


# uma função pode ter parâmetros obrigatórios e opcionais
def soma_todos_numeros1(nome, email, *args):
    return sum(args)


# outro exemplo de uso do *args
def verifica_info(*args):
    if 'Geek' in args and 'University' in args:
        return 'Bem-vindo Geek'
    return 'Não te conheço'


print(verifica_info())
print(verifica_info(1, True, 'University', 'Geek'))
print(verifica_info(1, 'University', 3.145))

"""


def soma_todos_numeros(*args):
    return sum(args)


numeros = [1, 2, 3, 4, 5, 6, 7]

# print(soma_todos_numeros(numeros)) # TypeError; o python não consegue converter uma lista em tupla

# Desempacotamento - add asterisco para indicar a necessidade de desempacotamento, pois passada uma coleção como
# parametro
print(soma_todos_numeros(*numeros))     # lista desempacotada no parametro


numeros = {1, 2, 3, 4, 5, 6, 7}
print(soma_todos_numeros(*numeros))     # set desempacotado no parametro

