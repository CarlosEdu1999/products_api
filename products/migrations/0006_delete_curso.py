# Generated by Django 4.1 on 2022-09-08 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_product_rating'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Curso',
        ),
    ]