"""
**kwargs (nome dado por conveção)

Diferente do *args, que coloca os valores extras em uma tupla, o **kwargs exige o uso de parametros nomeados,
transformando-os em um dicionário


# Exemplo
def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}')
    print(type(kwargs))     # dicionario

cores_favoritas(Marcos='Verde', julia='amarelo', fernanda='azul', vanessa='branco')

# obs os parâmetros *args e **kwargs n]ap são obrigatórios
cores_favoritas()
cores_favoritas(geek='navy')

def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Você recebeu um cumprimento Pythoônico Geek'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} Geek"
    return 'Não tenho certeza de quem você é...'

print(cumprimento_especial())
print(cumprimento_especial(geek='Python'))
print(cumprimento_especial(geek='oi'))
print(cumprimento_especial(geek='especial'))

# Nas nossas funções, podemos ter (NESTA ORDEM):
# - parâmetros obrigatórios
# - *args
# - parametros default (não obrigatórios
# ** kwargs


def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome.title()} tem {idade} anos')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('casado')
    print(kwargs)


minha_funcao(8, 'Julia')
minha_funcao(18, 'Felicty', 4, 5, 3, solteiro=True)
minha_funcao(34, 'Felipe', eu='Não', voce='Vai')
minha_funcao(19, 'Carla', 9, 4, 3, java=False, python=True)

"""


# Entenda porque é importante manter a ordem dos parâmetros na declaração

# Função com a ordem correta de parametros
def mostra_info(a, b, *args, instrutor='Geek', **kwargs):
    return [a, b, args, instrutor, kwargs]


"""
 a = 1
 b = 2
 args = (3, )
 instrutor = 'Geek'
 kwargs = {'sobrenome': 'University', 'cargo':'instrutor'}
"""
print('Forma correta')
print(mostra_info(1, 2, 3, sobrenome='University', cargo='Instrutor'))


# Função com a ordem incorreta de parametros
def mostra_info2(a, b, instrutor='Geek', *args, **kwargs):
    return [a, b, args, instrutor, kwargs]


print('Forma incorreta')
print(mostra_info2(1, 2, 3, sobrenome='University', cargo='Instrutor'))


# desempacotamento de dicionário **kwargs
def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"


nomes = {'nome': 'Felicity', 'sobrenome': 'Jones'}
print(mostra_nomes(**nomes))


def soma_multiplos_numeros(a, b, c):
    print(a + b + c)


lista = [1, 2, 3]
tupla = (1, 2, 3)
conjunto = {1, 2, 3}
dicionario = dict(a=1, b=2, c=3)
soma_multiplos_numeros(*lista)
soma_multiplos_numeros(*tupla)
soma_multiplos_numeros(*conjunto)

soma_multiplos_numeros(**dicionario)


# OBS: os nomes da chave de um dicionario devem ser os mesmos dos parametros da função
# dicionario = dict(d=1, e=2, f=3)
# soma_multiplos_numeros(**dicionario) # TypeError

def soma_multiplos_numeros2(a, b, c, **kwargs):
    print(a + b + c)


dicionario = dict(a=1, b=2, c=3, nome='Geek')
soma_multiplos_numeros2(**dicionario, lang='Python')  # chamada da função com desempacotamento do dict e **kwargs
