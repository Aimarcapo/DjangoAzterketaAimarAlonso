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
def pazienteak_edit(request, variable):
    pazientea = get_object_or_404(Paziente, dni=variable)  # Obtén la nota o muestra un error 404, despues del modelo ponemos el nombre del campo de ese modelo que hemos puesto en models.py en este caso matrikula y despues del igual ponemos el nombre que se va a pasar por el enlace
    if request.method == 'POST':
        form = PazienteForm(request.POST, instance=pazientea)  # Crea un formulario con la instancia de la nota
        if form.is_valid():  # Verifica si el formulario es válido
            form.save()  # Guarda los cambios en la nota
            return redirect('paziente')  # Redirige a la lista de notas después de editar
    else:
        form = PazienteForm(instance=pazientea)  # Carga el formulario con los datos actuales de la nota

    return render(request, 'paziente_edit.html', {'form': form, 'pazientea': pazientea})