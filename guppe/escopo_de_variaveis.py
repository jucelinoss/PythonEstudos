"""
Escopo de variáveis

Limitação de uma variável

1 - Variáveis globais
    - são reconhecidas em todo o programa

2 - Variáveis locais
    - são reconhecidas em apenas no bloco onde foram declaradas, ou seja,
    seu escopo está limitado ao blovo onde foi declarada

    Para declarar variáveis em Python, fazemos:

    nome_da_variavel = valor_da_variavel


Python é uma linguagem de tipagem dinãmica. Isso significa que ao declararmos uma variável,
não colocamos o tipo de dado dela.
Este tipo é iferido ao atribuírmos o valor

Exemplo em C:
int numero = 42;

Exemplo em Java:
int numero = 42;

"""
numero = 42        # Exemplo de variável global
print(numero)
print(type(numero))

# Reatribuição - recria o objeto de variável
numero = 'Teste42'
print(numero)
print(type(numero))

if numero > 10:
    novo = numero + 10 # A variável 'novo' está declarada localmente dentro do bloco if, portanto é local
    print(novo)
