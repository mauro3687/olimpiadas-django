from django.shortcuts import render

# Create your views here.

def Login(request):
    return render(request,'login-admin.html')


def Admin(request):
    return render(request, 'admin.html')


def Paciente(request):
    return render(request, 'paciente-admin.html')

def Agregar_paciente(request):
    return render(request, 'agregar-paciente.html')

def Enfermero(request):
    return render(request, 'enfermero.html')

def Agregar_enfermero(request):
    return render(request, 'agregar-enfermero')

def Area(request):
    return render(request, 'area.html')

def Agregar_area(request):
    return render(request, 'agregar-area.html')

# def llamada(request):
#     return render(request, 'admin.html')

# def Alerta(request):
#     return render(request, 'admin.html')

# def Estadistica(request):
#     return render(request, 'admin.html')

# def info(request):
#     return render(request, 'admin.html')
