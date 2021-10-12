from django.db import models


class Produto(models.Model):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', decimal_places='2', max_digits=8)
    estoque = models.IntegerField('Quantidade em Estoque')


def __str__(self):
    return self.nome


class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=100)
    sobrenome = models.CharField('Sobrenome', max_length=100)
    email = models.EmailField('E-mail', max_length=100)

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'


#class AlunoUnivesp(models.Model):
#    nome = models.CharField(max_length=255, null=False, blank=False)
#    sobrenome = models.CharField(max_length=255)
#    matricula = models.CharField(max_length=14, null=False, blank=False)
