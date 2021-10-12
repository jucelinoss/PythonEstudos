"""
Estruturas lógicas: and, or, not, is

Operadores unários:
    -  not,
Operadores binários
    - and, or, is
Operadores ternários

"""

ativo = True
logado = True

# is True é um trecho redundante
if ativo is True and logado:
    print('Bem-vindo usuário')
else:
    print('Você precisa ativar sua conta. Por favor cheque seu e-mail')


# Modo pythônico
if not ativo:
    print('Você precisa ativar sua conta. Por favor cheque seu e-mail')
else:
    print('Bem-vindo usuário')

print(ativo is False)

# is equivale a ==





