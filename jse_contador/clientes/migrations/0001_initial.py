# Generated by Django 4.2 on 2023-04-17 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnpj', models.IntegerField(max_length=14)),
                ('razao_social', models.CharField(max_length=200)),
                ('nome_cliente', models.CharField(max_length=200)),
                ('telefone', models.IntegerField(max_length=11)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
