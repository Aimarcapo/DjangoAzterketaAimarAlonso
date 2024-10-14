from django.shortcuts import redirect, render
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