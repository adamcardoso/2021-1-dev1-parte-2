# Generated by Django 3.2 on 2021-06-03 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='doc',
            field=models.FileField(default=1, upload_to='docs', verbose_name='Documentos'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='photo',
            field=models.ImageField(default=1, upload_to='photos', verbose_name='Foto'),
            preserve_default=False,
        ),
    ]
