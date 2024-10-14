from django import forms 
from .models import *
class PazienteForm(forms.ModelForm):    
    class Meta:        
        model=Paziente        
        fields=['izena','abizena','gaixotasuna']
class MedikuForm(forms.ModelForm):    
    class Meta:        
        model=Mediku        
        fields=['izena','abizena','adina']
