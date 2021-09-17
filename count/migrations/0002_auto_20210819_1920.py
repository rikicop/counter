# Generated by Django 2.2 on 2021-08-19 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('count', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaccion',
            name='asiento',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='transaccion',
            name='banco',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='transaccion',
            name='codant',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='transaccion',
            name='ctaabono',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='transaccion',
            name='ctacargo',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='transaccion',
            name='moneda',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='transaccion',
            name='nivel',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='transaccion',
            name='proyecto',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='transaccion',
            name='oficina',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
