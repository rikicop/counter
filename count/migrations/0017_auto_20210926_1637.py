# Generated by Django 2.2 on 2021-09-26 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('count', '0016_auto_20210926_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cargo',
            name='cinci',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='count.Cincuenta', verbose_name='cuenta'),
        ),
    ]
