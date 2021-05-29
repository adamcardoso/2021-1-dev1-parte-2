# Generated by Django 3.2 on 2021-05-29 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Socialnetwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nome')),
                ('description', models.TextField(max_length=100, verbose_name='Descricao')),
            ],
            options={
                'verbose_name': 'Rede Social',
                'verbose_name_plural': 'Redes Sociais',
                'ordering': ['id'],
            },
        ),
    ]
