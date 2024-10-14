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
def zitak(request):
    zitak=Zita.objects.all
    return render(request, 'index.html', {'zitak':zitak })
def zitak_new(request):    
    if request.method == 'POST':        
        form=ZitaForm(request.POST)       
        if form.is_valid:            
            zita = form.save()            
            zita.save()        
            return redirect('index')
    else:        
        form=ZitaForm()        
        return render(request, 'zita_new.html', {'form':form})
def zitak_edit(request, id):
    zita = get_object_or_404(Zita, id=id)  
    if request.method == 'POST':
        form = ZitaForm(request.POST, instance=zita) 
        if form.is_valid():  
            form.save() 
            return redirect('index') 
    else:
        form = ZitaForm(instance=zita)  

    return render(request, 'edit.html', {'form': form, 'zita': zita})
def zita_delete(request, id):
    zita = get_object_or_404(Zita, id=id)  # Busca por el nombre 'izena'

    if request.method == 'POST':
        zita.delete()  # Elimina la casa
        return redirect('index')  # Redirecciona a la lista de casas
    
    return render(request, 'delete.html', {'zita': zita})


