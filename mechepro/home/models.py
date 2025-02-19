from django.db import models

# Create your models here.


class Utilisateur(models.Model):
    nom_utilisateur = models.CharField(max_length=10)
    mot_de_pass = models.CharField(max_length=10)
    adress_courriel = models.EmailField(unique=True)
    prenom = models.CharField(max_length=10)
    nom = models.CharField(max_length=10)
    numero_telephone = models.CharField(max_length=10)
    date_de_naissance = models.DateField(null=True)


class Adress(models.Model):
    rue = models.CharField(max_length=10)
    ville = models.CharField(max_length=10)
    code_zip = models.CharField(max_length=10)
    pays = models.CharField(max_length=10)
    utilisateur = models.OneToOneField(
        Utilisateur, on_delete=models.CASCADE, primary_key=True)
