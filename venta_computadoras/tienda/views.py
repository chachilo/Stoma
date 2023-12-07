# tienda/views.py
from django.shortcuts import render, redirect
from .models import Computadora
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt


def iniciar_sesion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('pagina_principal')
        else:
            mensaje_error = "Credenciales incorrectas. Por favor, inténtalo de nuevo."
            return render(request, 'tienda/iniciar_sesion.html', {'mensaje_error': mensaje_error})

    return render(request, 'tienda/iniciar_sesion.html')

def pagina_principal(request):
    mensaje_bienvenida = "Bienvenido a CompuMas - Tu tienda de computadoras"
    return render(request, 'tienda/pagina_principal.html', {'mensaje_bienvenida': mensaje_bienvenida})

def lista_computadoras(request):
    computadoras = Computadora.objects.all()
    return render(request, 'tienda/lista_computadoras.html', {'computadoras': computadoras})

def detalle_computadora(request, computadora_id):
    computadora = Computadora.objects.get(id=computadora_id)
    return render(request, 'tienda/detalle_computadora.html', {'computadora': computadora})

# tienda/views.py


