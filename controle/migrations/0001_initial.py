<<<<<<< HEAD
# Generated by Django 4.0.4 on 2022-04-27 20:20
=======
# Generated by Django 4.0.4 on 2022-04-27 17:51
>>>>>>> 0c47fd46b6934b46aaaf3291c5edf8dde05cb55c

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Clube',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('dono', models.CharField(max_length=255)),
                ('endereco', models.CharField(max_length=255)),
                ('dimensao', models.CharField(max_length=255)),
                ('preco_hora', models.FloatField(max_length=255)),
<<<<<<< HEAD
                ('Cidade', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='cidade_clube', to='controle.cidade')),
=======
                ('cidade', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='controle.cidade')),
>>>>>>> 0c47fd46b6934b46aaaf3291c5edf8dde05cb55c
            ],
        ),
    ]
