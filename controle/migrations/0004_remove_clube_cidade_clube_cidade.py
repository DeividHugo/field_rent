# Generated by Django 4.0.4 on 2022-04-28 00:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('controle', '0003_alter_clube_cidade'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clube',
            name='Cidade',
        ),
        migrations.AddField(
            model_name='clube',
            name='cidade',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='clube_cidade', to='controle.cidade'),
            preserve_default=False,
        ),
    ]
