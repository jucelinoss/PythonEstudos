"""
Erros mais comuns em Python

Atenção: É imporante prestar atenção e aprender a ler as saídas de erros geradas pela execução do nosso código
Exceptions e Error são sinônimos na programação

1 - SyntaxError -> Ocorre quano p Python encontra um erro de sintaxe, ou seja, vc escreveu algo que o Python nçao reconhece
 como parte da linguagem

# Exemplos

# a)
     def funcao:
        print('Geek')

# b)
    None = 1

# c)
    return

2 - NameError -> Ocorre quando uma variável pu função não foi definida

# Exemplo NameError

a)
    print(geek)

b)
    geek()

c)
    a = 18
    if a < 10:
        msg = 'É maior que 10'

print(msg) # msg é criado somente se entrar no if; se não entrar provoca erro

3 - TypeError
a)
    print(len(5)) # int has no len()

b)
    print('Geek' + [])
    print('Geek' + 4)

4 - IndexError - ocorre quando tentamos acessar um elemento em uma lista ou outro tipo de dado indexado utilizando um
índice inválido

lista = ['Geek']
print(lista[2]) # existe apenas um elemento na lista; indice correto lista[0]
print(lista[10])

5 - ValueError -> ocorre quando uma função/operação built-in (integrada) recebe um argumento com tipo correto mas valor
inapropriado
Exemplos ValueError
a) print(int('d')) # letra não dá pra converter pra int (valueError)

6 - Key Error -> ocorre quando tentamos acessar um dicionário com uma chave que não existe
a) dic = {}
print(dic['geek']) # chave não encontrada no dicionário

7 - AttributeError - ocorre quando uma variável nao tem um atributo/função
Exemplo AttributeError

a)
    tupla = (11, 2, 31, 4)
    print(tupla.sort()) # tupla não possui sort - attribute error

8 - IndentationError -> Ocorre quando não respeitamos a identação do Python, de 4 espaços (e seus múltiplos)
a)
def nova():
print('Geek')

b) for i in range(10):
i + 1       # falta add 4 espaços

"""



