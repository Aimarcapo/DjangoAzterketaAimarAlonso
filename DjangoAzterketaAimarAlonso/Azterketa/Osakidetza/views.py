from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from .forms import *
# Create your views here.
def pazienteak(request):
    pazienteak=Paziente.objects.all
    return render(request, 'pazienteak.html', {'pazienteak':pazienteak })
def pazienteak_new(request):    
    if request.method == 'POST':        
        form=PazienteForm(request.POST)       
        if form.is_valid:            
            paziente = form.save()            
            paziente.save()        
            return redirect('paziente')
    else:        
        form=PazienteForm()        
        return render(request, 'paziente_new.html', {'form':form})
def pazienteak_delete(request, variable):
    pazientea = get_object_or_404(Paziente, dni=variable)  # Busca por el nombre 'izena'

    if request.method == 'POST':
        pazientea.delete()  # Elimina la casa
        return redirect('paziente')  # Redirecciona a la lista de casas
    
    return render(request, 'delete.html', {'pazientea': pazientea})
def pazienteak_edit(request, variable):
    pazientea = get_object_or_404(Paziente, dni=variable)  
    if request.method == 'POST':
        form = PazienteForm(request.POST, instance=pazientea) 
        if form.is_valid():  
            form.save() 
            return redirect('paziente') 
    else:
        form = PazienteForm(instance=pazientea)  

    return render(request, 'edit.html', {'form': form, 'pazientea': pazientea})
def medikuak(request):
    medikuak=Mediku.objects.all
    return render(request, 'medikuak.html', {'medikuak':medikuak })
def medikuak_new(request):    
    if request.method == 'POST':        
        form=MedikuForm(request.POST)       
        if form.is_valid:            
            mediku = form.save()            
            mediku.save()        
            return redirect('mediku')
    else:        
        form=MedikuForm()        
        return render(request, 'mediku_new.html', {'form':form})
def medikuak_delete(request, variable):
    medikua = get_object_or_404(Mediku, id=variable)  # Busca por el nombre 'izena'

    if request.method == 'POST':
        medikua.delete()  # Elimina la casa
        return redirect('mediku')  # Redirecciona a la lista de casas
    
    return render(request, 'delete.html', {'medikua': medikua})
def medikuak_edit(request, variable):
    medikua = get_object_or_404(Mediku, id=variable)  
    if request.method == 'POST':
        form = MedikuForm(request.POST, instance=medikua) 
        if form.is_valid():  
            form.save() 
            return redirect('mediku') 
    else:
        form = MedikuForm(instance=medikua)  

    return render(request, 'edit.html', {'form': form, 'medikua': medikua})
