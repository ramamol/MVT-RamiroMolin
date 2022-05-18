
from django.http import HttpResponse
from django.template import loader, Template

from django.shortcuts import render
from familia.models import Familiar


# esta función permite agregar familiares a la base de datos ingresando
def agregar_familiar(self, name: str = 'name', age: int = 0, birthday: str = '0000-00-00'):
    template = loader.get_template('template_add.html')   #el path esta guardado en DIRS desntro de settings.py
    
    familiar = Familiar (name=name, age=age, birthday=birthday )
    familiar.save() 
    context_dict = {
        'familiar': familiar
        
    }
    
    render = template.render(context_dict)    # al usar loader me salto el paso de pasarlo como contexto, directamente renderizo
    return HttpResponse(render)


# esta función permite ver la lista completa de integrantes en la base de datos. 
def familia_completa(request):
    todos=Familiar.objects.all()      
    return render(request, "template_todos.html",{"familiares":todos})


 