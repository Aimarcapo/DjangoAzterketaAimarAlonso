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
       return f"Etxea {self.izena}  {self.abizena} {self.adina}."
    
class Paziente(models.Model):
    dni = models.AutoField(primary_key=True)    
    izena = models.CharField(max_length=100)
    abizena = models.CharField(max_length=100)
    gaixotasuna = models.CharField(max_length=100)
    
    def __str__(self):
        return f"Pertsona {self.dni}  {self.izena} {self.abizena} {self.emaila}."
    
class Zita(models.Model):

    mediku = models.ForeignKey(Mediku,on_delete=models.CASCADE)
    paziente = models.ForeignKey(Paziente,on_delete=models.CASCADE)

    data = models.DateField(null=True)
    def __str__(self):
       return f"Zita {self.mediku}  {self.paziente} {self.data} ."