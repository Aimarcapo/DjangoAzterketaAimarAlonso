from django import forms 
from .models import *
class PazienteForm(forms.ModelForm):    
    class Meta:        
        model=Paziente        
        fields=['izena','abizena','gaixotasuna']
