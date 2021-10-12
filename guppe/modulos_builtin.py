"""
Módulos Builtin (módulos integrados, que já vem instalados no Python)

_______________________
|Python|Módulos Builtin|
_______________________

https://docs.python.org/3/py-modindex.html

# Utilizando alias (apelidos) para mnódulos/funções
import random as rdm

print(rdm.random())

# Podemos importar todas as funções de um módulo utilizando asterisco

from random import *
# import random

print(random())



# Importar todo o módulo

import random

print(random.random())

# Utilizando alias para módulos

from random import randint as rdi, random as rdm  # alias de função

print(rdi(3, 69))
print(rdm())
"""

# Costumamos utilizar tuple para colocar multiplos imports de um mesmo módulo
# import pythônico
from random import (
    random,
    randint,
    shuffle,
    choice
)

list = [1, 2, 3]
print(random())
print(randint(3, 70))
print(choice('Geek University'))
print(list)
shuffle(list)    # embaralha a lista
print(list)
