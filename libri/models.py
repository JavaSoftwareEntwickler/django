from django.db import models

# Create your models here.

class Libro(models.Model):
    immagine = models.ImageField()
    titolo = models.CharField(max_length=30)
    prezzo = models.FloatField()
    descrizione = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.titolo