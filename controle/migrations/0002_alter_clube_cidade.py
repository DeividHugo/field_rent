# Generated by Django 4.0.4 on 2022-04-27 20:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('controle', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clube',
            name='Cidade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clube_cidade', to='controle.cidade'),
        ),
    ]
