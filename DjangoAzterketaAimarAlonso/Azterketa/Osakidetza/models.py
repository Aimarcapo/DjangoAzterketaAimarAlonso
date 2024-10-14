from django.db import models
from django.core.validators import MinValueValidator
# Create your models here.
class Mediku(models.Model):
    id = models.AutoField(primary_key=True)    
    izena = models.CharField(max_length=100)
    abizena = models.CharField(max_length=100)
    adina = models.IntegerField(validators=[
        MinValueValidator(0)])
    
    def __str__(self):
       return f"Mediku {self.id} {self.izena}  {self.abizena} {self.adina}."
    

class Paziente(models.Model):
    dni = models.AutoField(primary_key=True)    
    izena = models.CharField(max_length=100)
    abizena = models.CharField(max_length=100)
    gaixotasuna = models.CharField(max_length=100)
    
    def __str__(self):
        return f"Paziente {self.dni}  {self.izena} {self.abizena} {self.gaixotasuna}."
class Zita(models.Model):
    id = models.AutoField(primary_key=True)   
    data = models.DateField(null=True)
    paziente = models.ForeignKey(Paziente,on_delete=models.CASCADE)
    def __str__(self):
       return f"Zita  {self.data} {self.paziente} ."