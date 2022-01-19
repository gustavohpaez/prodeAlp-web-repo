from django.shortcuts import redirect, render, HttpResponse
from . import forms


def prueba(request):

    #utilizamos el contexto, condicionales, bucles
    
    ctx = { 
        "nombre" : "Gustavo",
        "cursos" : 0,    
        "curso_actual": {"nombre": "Python & Django", "turno": "Noche"},
        "cursos_anteriores": ["Java", "PHP", "JavaScript", "Python"],   

        "alumnos": ["Juan", "Sofia", "Matias"],    
    }
    return render(request, "register/prueba.html", ctx)

def register(request):
    
    if request.method == "POST":
        form = forms.Formulario_Ingreso(request.POST)
        if form.is_valid():
            return HttpResponse("Se ingreso al usuario")
    else:
        form = forms.Formulario_Ingreso()
                 
    ctx = {"form" : form}
    return render(request, "register/register.html", ctx)

