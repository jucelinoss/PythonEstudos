"""
Módulo random + o que são módulos?

- Em python, módulos ão outros arquivos python
Módulo random - possui várias funções para geração de numeros peseudo-aleatórios


# OBS.: Existem duas formas de se utilizar um módulo ou função

# Forma 1 - Importar todo o módulo (não recomendado)

# import random

# random() -> gera um nuermo pseudo-aleatório entre 0 e 1
# Ao realizar o import do módulo, todas as funções, atributos, classes e propriedades disponíveis ficarão em memória
# Caso saiba quais funções utilizar, importe-as individualmente
#print(random.random())

# Para utilizar a função random() do pacote rndom, usaos o pacote e nome da função, separados por ponto.
# Não confunda a função random() com o pacote random. A função random() é apenas uma função do módulo random

# Forma 2 - importando uma função específica do módulo (Forma recomendada)

from random import random
# importa apenas a função random() do módulo random

for i in range(10):
    print(random())

# uniform() -> gera um número pseudo-aleatório dentro do intervalo especificado

from random import uniform

for i in range(10):
    print(uniform(3, 7))    # limite superior não é incluído

for i in range(10):
    print(uniform(0, 1))    # equivalente ao random()

# randint() -> gera valores pseudo-aleatórios dentro do intervalo especificado
# Gerador de apostas para a mega-sena

from random import randint

print("\nMega-sena")
for i in range(6):
    print(randint(1, 61))
"""

# choice() -> mostra um valor aleatório dentro de um conjunto especificado

from random import choice

jogadas = ['pedra', 'papel', 'tesoura']

for i in range(5):
    print(choice(jogadas))

print(choice('Geek university'))

# shuffle - embaralha dados

from random import shuffle

cartas = ['K', 'Q', 'J', 'A', '2', '3', '4', '5', '6', '7']

print(cartas)
shuffle(cartas)
print(cartas.copy())