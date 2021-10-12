# Generated by Django 2.2.4 on 2021-03-27 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('preco', models.DecimalField(decimal_places='2', max_digits=8, verbose_name='Preço')),
                ('estoque', models.IntegerField(verbose_name='Quantidade em Estoque')),
            ],
        ),
    ]
