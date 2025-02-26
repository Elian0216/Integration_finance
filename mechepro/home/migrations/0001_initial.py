# Generated by Django 5.1.6 on 2025-02-26 22:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_utilisateur', models.CharField(max_length=10)),
                ('mot_de_passe', models.CharField(max_length=10)),
                ('adress_courriel', models.EmailField(max_length=254, unique=True)),
                ('prenom', models.CharField(max_length=10)),
                ('nom', models.CharField(max_length=10)),
                ('numero_telephone', models.CharField(max_length=10)),
                ('date_de_naissance', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Adresse',
            fields=[
                ('rue', models.CharField(max_length=10)),
                ('ville', models.CharField(max_length=10)),
                ('code_zip', models.CharField(max_length=10)),
                ('pays', models.CharField(max_length=10)),
                ('utilisateur', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='home.utilisateur')),
            ],
        ),
    ]
