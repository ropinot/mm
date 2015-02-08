from django.db import models

# Create your models here.

class PlantModel(models.Model):
        component = models.CharField(max_length=150, null=True, blank=True)
        parent = models.ForeignKey('self', null=True, blank=True)   # 'self' per fare riferimento al modello stesso
