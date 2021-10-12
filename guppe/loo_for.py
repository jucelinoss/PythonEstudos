"""
Loop for
ddd

For em C ou Java
for (int i = 0; i< limitador; i++){
    //execução do loop
}

# For em Python
for item in iteravel:
    // execução do loop

Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis
Exemplos de iteráveis:
 - String
    nome = "Geek University"
 - Lista
    lista = [1,3,5,7,9]
 - Range
    numeros = range(1,10)
"""
from main import print_hi

nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10) # Temos que transformar em uma lista
"""
# Exemplo de for 1
for letra in nome:
    print(letra)

# Exemplo de for 2 (iteração sobre uma lista)
for numero in lista:
    print(numero)
"""

# Exemplo de for 3 (Iteração sobre um range)
"""
Range(valor_inicial, valor_final)
Obs.: o último valo não é incluído

for numero in range(1, 10):
    print(numero)
"""

"""
Enumerate:
((0, 'G'), (1, 'e'), (2, 'e'), (3, 'k'), (4 ' '), (5, 'U')

for indice, letra in enumerate(nome):
    print(nome[indice])

for indice, letra in enumerate(nome):
    print(letra)
"""
"""
_ -> permite descartar determinado elemento. Quando não precisamos de um valor, podemos descartá-lo utilizando underline

for _, letra in enumerate(nome):
    print(letra)

for valor in enumerate(nome):
    print(valor)

qtd = int(input("Quantas vezes esse loop deve rodar?"))
soma = 0
for n in range(1, qtd + 1):
    num = int(input(f'Informe o valor {n}/{qtd}:'))
    soma += num
print(f'A soma é {soma}')

Ao clicar na função com a tecla ctrl pressionada, o PyCharm abre a documentação da função.  


# Para não pular linha no comando print, basta passar o paramentro end=''
for letra in nome:
    print(letra, end='')
"""

nome = 'Geek'
# permite concatenar uma string n vezes
# print(nome * 3)

"""
Tabela de emojis unicode:
https://apps.timwhitlock.info/emoji/tables/unicode
"""

# Original: u+1F60D
# Modificado: u0001F60D

emoji = ''
for _ in range(3):
    for num in range(1, 10):
        print('\U0001F60D' * num)
