# Generated by Django 2.2 on 2021-09-26 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('count', '0015_cargo_cinci'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cargo',
            name='cinci',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='count.Cincuenta'),
        ),
    ]
