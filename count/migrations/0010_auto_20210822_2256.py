# Generated by Django 2.2 on 2021-08-22 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('count', '0009_auto_20210822_2243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaccion',
            name='movimiento',
            field=models.BooleanField(default=False, verbose_name='SI'),
        ),
    ]
