# Generated by Django 2.2 on 2021-08-29 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('count', '0012_auto_20210822_2304'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cincuenta',
            fields=[
                ('cuenta', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('movimiento', models.CharField(blank=True, max_length=100)),
                ('nivel', models.CharField(blank=True, max_length=100)),
                ('moneda', models.CharField(blank=True, max_length=100)),
                ('asiento', models.CharField(blank=True, max_length=100)),
                ('ctacargo', models.CharField(blank=True, max_length=100)),
                ('ctaabono', models.CharField(blank=True, max_length=100)),
                ('codant', models.CharField(blank=True, max_length=100)),
                ('oficina', models.CharField(blank=True, max_length=100)),
                ('banco', models.CharField(blank=True, max_length=100)),
                ('proyecto', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]