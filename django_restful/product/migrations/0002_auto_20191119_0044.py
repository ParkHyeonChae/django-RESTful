# Generated by Django 2.2.7 on 2019-11-18 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.IntegerField(verbose_name='재고'),
        ),
    ]
