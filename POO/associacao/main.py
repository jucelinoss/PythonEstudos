from classes import Escritor
from classes import Caneta
from classes import MaquinaDeEscrever

escritor = Escritor('Joãozinho')
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()   

escritor.ferramenta = maquina
escritor.ferramenta.escrever()  # associação - o objeto associado não depende do objeto associador. Ao eliminá-lo, o objeto associado permanece 

del escritor
print(caneta.marca)
maquina.escrever()

