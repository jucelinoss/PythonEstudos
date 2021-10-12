"""
Recebendo dados do usuário

input() -> Todo dado recebido via input é do tipo String

Em Python, string é tudo que estiver entre:
- Aspas simples;
- Aspas duplas;
- Aspas simples triplas;
- Aspas duplas triplas;

Exemplos
- Aspas simples -> 'Angelina Jolie'
- Aspas duplas ->   "Angelina Jolie"
- Aspas simples triplas -> '''Angelina Jolie'''

"""
# Exibe recursos integrados da linguagem python
dir(__builtins__)  # input é uma função built-in

#print("Qual seu nome? ")
# nome = input()
nome = input("Qual seu nome? ")
# Exemplo de print 'antigo' 2.x - 1 argumento
# print('Seja bem vindo(a) %s' % nome)

# Exemplo de print 'moderno' 3.x - 1 argumento
# print('Seja bem vindo(a) {0}'.format(nome))

# Exemplo de print 'mais atual' 3.7 - 1 argumento
print(f'Seja bem vindo(a) {nome}')

# print('Qual sua idade? ')
# idade = input()     # entradas de console são do tipo string
idade  = int(input('Qual sua idade?'))

# Exemplo de print 'antigo' 2.x - 2 argumentos
# print('A %s tem %s anos' % (nome, idade))
#print('O(a) tem {1} anos'.format(nome, idade))

# Exemplo de print 'moderno' 3.x - 2 argumentos
print('O(a) tem {1} anos'.format(nome, idade))

# Exemplo de print 'mais atual' 3.7 - 2 argumentos
print(f'O(a) {nome} tem {idade} anos')
print(f'O(a) {nome} nasceu em {2020 - idade}')
# int(idade) => cast
