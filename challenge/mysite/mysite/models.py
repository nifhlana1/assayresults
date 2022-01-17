from django.db import models

"""Note, database not used but below demonstrated the creation of ORM"""
class CompoundInfo(models.Model):
    compound_id = models.CharField(primary_key=True,max_length=50)
    molecular_weight = models.CharField(max_length=100)
    ALogP = models.CharField(max_length=50)
    molecular_formula = models.TextField(max_length=50)
    num_rings = models.CharField(max_length=50)
    image = models.CharField(max_length=255)

class CompoundAssayResults(models.Model):
    unique_together = (('compound_id', 'molecular_weight'),)
    compound_id = models.CharField(primary_key=True,max_length=50)
    molecular_weight = models.CharField(max_length=100)