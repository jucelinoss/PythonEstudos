"""
Funções com parâmetro de entrada
- recebem dados como parâmetro para que sejam processdas pela função

Modelo de um programa
entrada -> processamento -> saída

Tipos de funções
- sem entrada
- sem entrada
- com entrada e sem saida
- com entrada e com saida
- sem entrada e com saida




# Refatoração de uma função


def quadrado(numero):  # o parametro é obrigatório
    return numero ** 2


def potencia(base, expoente):
    return base ** expoente


# print(quadrado()) typeError - função com parametro obrigatório

print(quadrado(7))
print(quadrado(2))
print(quadrado(5))
print(potencia(2, 19))


# Refatorando a função
def cantar_parabens(aniversariante):
    print('parabens pra você')
    print('nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print(f'Viva o(a) {aniversariante}')


cantar_parabens('Marcos')


# Funções podem ter n parâmetros de entrada, quantos forem necessários, separados por vírgula

# Exemplos


def soma(a, b):
    return a + b


def multiplica(num1, num2):
    return num1 * num2


def outra(num1, b, msg):
    return (num1 + b) * msg


print(soma(2, 5))
print(multiplica(2, 5))
print(outra(3, 2, 'Geek '))


# se a função for chamada com quantidade incorreta de argumentos, teremos TypeError

# Nomeação de parâmetros


def nome_completo(nome, sobrenome):
    return f'Seu nome completo é {nome} {sobrenome}'


nome_completo('Angelina', 'Jolie')

# Diferença entre parametros e argumentos
# parâmetros - variáveis declaradas na definição de uma função
# argumentos - dados passados durante a execução de uma função


# A ordem dos parâmetros importa
nome = 'Felicity'
sobrenome = 'Jones'
print(nome_completo(sobrenome, nome))

# Argumentos nomeados (keyword arguments)
# Caso utilizemos nomes dos parâmetros nos argumentos para informá-los, podemos utilizar qualquer ordem

print(nome_completo(nome='Angelina', sobrenome='jolie'))
print(nome_completo(sobrenome='jolie', nome='Angelina'))
print(nome_completo(sobrenome=sobrenome, nome=nome))
"""


# Erro de utilização do return
def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total += num
        # return total return errado nesta posição dentro do if - retorna após a 1a iteração
    return total


if __name__ == '__main__':
    lista = [1, 2, 3, 4, 5, 6, 7]
    print(soma_impares(lista))
    tupla = 1, 2, 3, 4, 5, 6, 7
    print(soma_impares(tupla))

# módulos python não deve ter print de código
