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
class ZitaForm(forms.ModelForm):    
    class Meta:        
        model=Zita        
        fields=['paziente','data']
    data = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label="Aukeratu zitaren data"
    )
    paziente = forms.ModelChoiceField(queryset=Paziente.objects.all(), label="Aukeratu Zita")

