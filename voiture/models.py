from django.db import models
from django.utils import timezone
from django.shortcuts import render ,redirect
from django import forms
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login

# Create your models here.
from django.db import models

class Voiture(models.Model):
    CATEGORIE_CHOICES = [
        ('compacte', 'Compacte'),
        ('berline', 'Berline'),
        ('SUV', 'VUS'),
        ('camionnette', 'Camionnette'),
        ('cabriolet', 'Cabriolet'),
        ('coupe', 'Coupé'),
        
    ]
    marque = models.CharField(max_length=50, verbose_name="Marque",null=True)
    modele = models.CharField(max_length=50, verbose_name="Modèle",null=True)
    prix = models.IntegerField(null=True)
    annee = models.PositiveIntegerField(verbose_name="Année",null=True)
    couleur = models.CharField(max_length=50, verbose_name="Couleur",null=True)
    image = models.ImageField(upload_to='images/')
    categorie = models.CharField(max_length=50, choices=CATEGORIE_CHOICES, verbose_name="Catégorie",null=True)
    publish = models.DateTimeField(default=timezone.now)
    discreption= models.TextField(null=True)
   
    class Meta:

        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]


    def __str__(self):
        return self.modele
class VoitureForm(forms.ModelForm):
    class Meta:
        model = Voiture
        fields = ['marque','modele', 'prix', 'annee', 'couleur', 'image','categorie', 'discreption']

    

