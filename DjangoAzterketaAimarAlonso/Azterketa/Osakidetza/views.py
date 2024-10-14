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
            ikasle = form.save()            
            ikasle.save()        
            return redirect('paziente')
    else:        
        form=PazienteForm()        
        return render(request, 'paziente_new.html', {'form':form})
def pazienteak_delete(request, variable):
    pazientea = get_object_or_404(Paziente, dni=variable)  # Busca por el nombre 'izena'

    if request.method == 'POST':
        pazientea.delete()  # Elimina la casa
        return redirect('paziente')  # Redirecciona a la lista de casas
    
    return render(request, 'paziente_delete.html', {'pazientea': pazientea})
def pazienteak_edit(request, variable):
    pazientea = get_object_or_404(Paziente, dni=variable)  
    if request.method == 'POST':
        form = PazienteForm(request.POST, instance=pazientea) 
        if form.is_valid():  
            form.save() 
            return redirect('paziente') 
    else:
        form = PazienteForm(instance=pazientea)  

    return render(request, 'paziente_edit.html', {'form': form, 'pazientea': pazientea})
def medikuak(request):
    medikuak=Mediku.objects.all
    return render(request, 'medikuak.html', {'medikuak':medikuak })