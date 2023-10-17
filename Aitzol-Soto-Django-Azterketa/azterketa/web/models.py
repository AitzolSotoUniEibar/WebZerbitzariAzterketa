from django.db import models

# Create your models here.
class Pertsona(models.Model):
    izena = models.TextField()
    emaila = models.TextField()
    nan = models.CharField(max_length=9)

class Etxea(models.Model):
    izena = models.TextField()
    herria = models.TextField()
    pertsona_kop = models.CharField(max_length=10)

class Alokairua(models.Model):
    etxea = models.ForeignKey(Etxea,on_delete=models.CASCADE)
    pertsona = models.ForeignKey(Pertsona,on_delete=models.CASCADE)
    alokatze_hasiera = models.DateTimeField()
    alokatze_amaiera = models.DateTimeField()