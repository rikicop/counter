# Generated by Django 2.2 on 2021-09-26 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('count', '0021_auto_20210926_1653'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cargo',
            name='cinci',
        ),
    ]
