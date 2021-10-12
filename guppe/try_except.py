"""
Bloco Try/Except

Utilizamos o bloco Try/Except para tratar erros que podem ocorrer no nosso código, previnindo assim que o programa
pare de funcionar e o usuário receba mensagens inesperadas de erro


A Forma geral mais simples é:

try:
    // execução problemática
except:
    // o que deve ser feito em caso de problema


# Exemplo 1 - Tratamento genérico de erro
try:
    geek()
except:
    print('Deu algum problema')

# Exemplo 2 - Tratamento de erro genérico
try:
    len(5)
except:
    print('Deu algum problema')

# Obs.: tratar erros de forma genérica não é a melhor forma. O ideal é SEMPRE tratar de forma específica
import random

try:
    if int(random.random() * 100) % 2:
        geek()
    else:
        len(5)
except NameError as err:
    print( f'Chamada de função ou uso de objeto inexistente. {err}')
except TypeError as err2:
    print(f'Erro de manipulação de tipo de dado. {err2}')

"""

def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return 'Chave não encontrada'
    except TypeError:
        return 'Chave com tipo incorreto'

dic = {"nome": "Geek"}

print(pega_valor(7, "nome"))
print(pega_valor(dic, "nomes"))
