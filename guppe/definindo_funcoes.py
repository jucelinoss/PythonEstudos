"""
Definindo Funções
- são pequenos partes de código que realizam tarefas específicas;
- pode receber ou não entrada / saida de dados
- muuito úteis para executar procedimentos similares repetidas vezes
obs.: cada função deve realizar apenas uma única tarefa

Exemplos de funções
- print()
- min()
- max()
- len()
- count()


# exemplo de utilização de funções

cores = ['verde', 'amarelo', 'azul', 'branco']

# Uso de função integrada (built-in) do python Print()
print(cores)

curso = 'programação em python essencial'
cores.append('roxo')
# .append é uma funlçao vinculada a uma lista

print(cores)

cores.clear()
# .clear() não recebe nenhum dado de entrada

# Princípio DRY - Don't repeat yourself - não repita você mesmo / não repita seu código



Em python, a forma geral de definir uma função é:
def nome_funcao (parametros_entrada):
    bloco_funcao
    
Onde:
nome_funcao -> sempre com letras minusculas, separados por underline (Snake case)
parametros_entrada -> opcionais, separados por vírgula 
bloco_função -> também chamado de corpo da função ou implementação, e onde ocorre o processamento da função
Neste bloco, pode ter ou não retorno

Obs.: veja que pare definir a função, utilizamos a palavra reservada 'def', informando ao Python que estamos 
definindo uma função. 
Também abrimos o bloco de código com o já conhecido dois pontos ':', utilizado em python para definir blocos

# definindo primeira função

def diz_oi():
    print('oi!')

1 - dentro de uma funlão podemos utilizar outras
2 - a função executa apenas uma tarefa
3 - a função não recebe nenhum parâmetro de entrada
4 - não retorna dados

# Chamar funlção definida
diz_oi()


Atenção: não se esqueça de utilizar parenteses ao chamar uma função




def cantar_parabens():
    print('parabens pra você')
    print('nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print('Viva o aniversariante')


# for n in range(5):  # 5x - de 0 a 5-1
#    cantar_parabens()


Em python, podemos inclusive criar variáveis do tipo de uma função e executá-la através da variável



#canta = cantar_parabens
#canta()
# não é recomendado colocar uma função dentro de uma variavel, pois dificulta a compreensão


def diz_oi2():
    return 'Oi '
    # o uso de retorno torna as funções mais flexiveis

alguem = 'Pedro'

print(diz_oi2() + alguem)
"""

"""
Observações sobre a clausula return
1 - finaliza a função
2 - uma função pode ter diferentes returns, mas somente um deles é executado
3 - podemos retornar qualquer tipo de dado e até mesmo múltiplos valores

# Exemplos 1
def diz_oi():
    print('Estou sendo executado antes o retorno')
    return 'Oi!'
    print('Estou sendo executado após o retorno') # este trecho não é executado
    
    



# Exemplo 2


def nova_funcao():
    variavel = None
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'


print(nova_funcao())


# Exemplo 3
def outra_funcao():
    return 2, 3, 4, 5  # return tupla


# num1, num2, num3, num4 = outra_funcao() # desempacotamento de tupla
# print(num1, num2, num3, num4)
print(outra_funcao())
print(type(outra_funcao()))

from random import random


def joga_moeda():
    # Gera um numero pseudo randômico entre 0 e 1
    if random() > 0.5:
        return 'Cara'
    return 'Coroa'


print(joga_moeda())

"""

# Codificação desnecessária


def eh_impar():
    numero = 5
    if numero % 2 != 0:
        return True
    return False


"""
    if numero % 2 != 0:
        return True
    else: # else é desnecessário
        return False
"""

print(eh_impar())


