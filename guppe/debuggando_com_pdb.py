"""
Debugando com PDB
PDB -> Python Debugger
Bug -> inseto
O uso de print para debugar código é uma prática ruim
# Existem formas mais profissionais de se debuggar com em vez de usar comandos de print.
# Em python, podemos fazer isso em diferentes IDE's, como o PyCharm ou utilizando o PDB (Python Debugger)

# Exemplo de debug com Pycharm
def dividir(a, b): # Toda entrada de dados deve ser validada
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema {err}'

print(dividir(4,7))

# Para utulizar o Python debugger, precisamos* importar a bilbitoeca pdb e utilizar a função set_Trace()

# Por quê utilizar este formato
# O debug é utilizado durante o desenvolvimento
# Costumamos realizar todos os imports de bibliotecas no inicio do arquivo
# Por isso, ao inves de colocarmos o import do pdb no início do arquivo, nós
# colocamos somente onde vamos debuggar, e ao finalizar já fazemos a remoção
# A partir do python 3.7, não é mais necessário importar a bilbioteca pdb, pois o comando de debug foi incorporado
# como função built-in chamada breakpoint()
# Comandos básicos do PDB
# l -> listar onde estamos no código
# n -> proxima linha
# p -> imprime variável
# c -> continua a execução; finaliza o debugging

import pdb
nome = 'Angelina'
sobrenome = 'Jolie'
pdb.set_trace() #
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python Essencal'
final = nome_completo + ' faz o curso ' + curso
print(final)
"""

import pdb
nome = 'Angelina'
sobrenome = 'Jolie'
#import pdb; pdb.set_trace() # ; aceita rodar dois comandos na mesma linha
breakpoint()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python Essencal'
final = nome_completo + ' faz o curso ' + curso
print(final)

# OBS.: cuidado com conflitos entre nomes de variáveis e os comandos do PDB

def soma(l, n, p, c):
    breakpoint()
    return l + n + p + c

print(soma(1, 3, 5, 7))

# Já que os nomes das variáveis são os mesos dos comandos do pdb, devemos utilizar o comando p para imprimir as
# variáveis, ou seja, p nome_da_variavel
# Não de colocar nomes não representativos em variáveis. Sempre optar por nomes signficativos
