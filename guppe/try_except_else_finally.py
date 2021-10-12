"""

Try / Except / Else / Finally

Dica de quando e onde tratar código:
- toda entrada de dados deve ser tratada
- conexão com recursos externos (arquivos, rede ou banco de dados)



num = 0
try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Valor incorreto')
else: # executado somente se não ocorrer o erro; para except podemos ter um else
    print(f'Voce digitou {num}')
finally: # sempre é executado, independente de ocorrer erro ou não
    print('Bloco finally sempre executado')

# Finally geralmente é utilizado para fechar conexoes ou desalocar recursos

# Exemplo mais complexo errado

def dividir(a, b):
    return a / b


# a forma correta é aplicar os tratamentos dentro da função
try:
    num1 = int(input('Informe o 1o numero'))
    num2 = int(input('Informe o 2o numero'))
except ValueError:
    print('Os valores precisam ser númerico')
except NameError:
    print('Valor(es) incorreto(s)')

print(dividir(num1, num2))



# Exemplo mais complexo correto
# Você é responsável pelas entrada das suas funções, então trate-as

def dividir(a, b): # Toda entrada de dados deve ser validada
    try:
        return int(a) / int(b)
    except ValueError:
        return 'Valor(es) Incorreto(s)'
    except ZeroDivisionError:
        return 'Impossível dividir por zero'

num1 = input('Informe o 1o numero')
num2 = input('Informe o 2o numero')

print(dividir(num1, num2))

"""




# Exemplo mais complexo correto (genérico)
# Você é responsável pelas entrada das suas funções, então trate-as

def dividir_generico(a, b): # Toda entrada de dados deve ser validada
    try:
        return int(a) / int(b)
    except:
        return 'Ocorreu um problema'


def dividir_semi_generico(a, b): # Toda entrada de dados deve ser validada
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema {err}'


num1 = input('Informe o 1o numero')
num2 = input('Informe o 2o numero')

print(dividir_generico(num1, num2))
print(dividir_semi_generico(num1, num2))