"""
Funções com Parâmetro padrão (Default parameters)
- funções cuja passagem de parâmetro é opcional

print('Geek University')
print()
# print é uma função com parametro opcional

# exemplo de função com passagem de parâmetro obrigatória


def quadrado(numero):
    return numero ** 2


def exponencial(numero, potencia):
    return numero ** potencia

print(exponencial(2, 3))
print(exponencial(3, 2))

# elevar ao quadrado quando o expoente não for informado
def exponencial2(numero, potencia=2):  # o 2o parametro é opcional, já que possui um valor padrão (2)
    return numero ** potencia

# elevar um ao quadrado quando não parametro for informado
def exponencial2(numero=1, potencia=2):  # o 2o parametro é opcional, já que possui um valor padrão (2)
    return numero ** potencia

print(exponencial2())
"""


# Funções com parâmetros default devem estar ao final da declaração, após os parametros obrigatórios, pois
# parãmetros opcionais podem atrapalhar o mapaeamento de argumentos e parametros se não ficarem ao final

# incorreto
# def teste(num =2, potencia) # non-default parameter follows default parameter
#    return num ** potencia

# correto
def teste(potencia, num=2):  # non-default parameter follows default parameter
    return num ** potencia


def mostra_informacao(nome='Geek', instutor=False):
    if nome == 'Geek' and instutor:
        return 'Bem-vindo instrutor Geek'
    elif nome == 'Geek':
        return 'Eu pensei que você era o instrutor'
    return f'Olá {nome}'


print(mostra_informacao())
print(mostra_informacao(instutor=True))
print(mostra_informacao(True))
print(mostra_informacao('Ozzy'))
print(mostra_informacao(nome='Stephany'))


# porque utilizar parâmetros com valor default
# torna o c´ódigo mais flexível
# eveita erros com parâmetros incorretos
# permite trabalhar com exemplos de código mais legíveis

# Qualquer tipo de dado pode ser usado como valor default de parâmetros, inclusive funções de variável

# exemplo de função passada por parametro opcional


def soma(num1, num2):
    return num1 + num2


def subtracao(num1, num2, fun=soma):
    return num1 - num2


def mat(num1, num2, fun=soma):
    return fun(num1, num2)


print(mat(2, 3))
print(mat(2, 2, subtracao))

# Escopo de variáveis

# variáveis globais
# variáveis locais

instrutor = 'Geek'  # varivel global


def diz_oi():
    instrutor = 'Python'  # variável local tem preferência sobre à variável global
    return f'oi {instrutor}'


print(diz_oi())


def diz_oi2():
    prof = 'Python'  # variável local tem preferência sobre à variável global
    return f'oi {prof}'


# print(prof) Name Error

# ATENÇÂO com variáveis globais (evite na medida do possível

total = 0


def incrementa():
    #    total = total + 1 # não se pode fazer operações com uma variável que não foi inicializada
    # UnboundLocalError
    global total  # informar uso de variável global dentro da função
    total += 1
    return total


incrementa()
incrementa()
print(incrementa())
print(incrementa())


# Podemos ter funções que são declara das dentro de funções, e também tem uma forma especifial de escopo de variável


def fora():
    contador = 0

    def dentro():
        nonlocal contador  # nonlocal permite acessar a varíável de cima da função anterior (tbm não é global)
        contador += 1
        return contador

    return dentro()

print(fora())
print(fora())
