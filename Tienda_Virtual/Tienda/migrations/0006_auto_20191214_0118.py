# Generated by Django 3.0 on 2019-12-14 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tienda', '0005_auto_20191214_0117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.CharField(max_length=200),
        ),
    ]
