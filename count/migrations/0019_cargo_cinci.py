# Generated by Django 2.2 on 2021-09-26 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('count', '0018_remove_cargo_cinci'),
    ]

    operations = [
        migrations.AddField(
            model_name='cargo',
            name='cinci',
            field=models.ForeignKey(blank=True, db_column='oficina', null=True, on_delete=django.db.models.deletion.CASCADE, to='count.Cincuenta'),
        ),
    ]
