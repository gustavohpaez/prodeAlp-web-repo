from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, "core/home.html")

def pagina1(request):
    return render(request, "core/pagina1.html")

def pagina2(request):
    return render(request, "core/pagina2.html")

def pagina3(request):
    return render(request, "core/pagina3.html")