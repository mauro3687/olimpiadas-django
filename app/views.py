from django.shortcuts import render
from .models import Paciente

# Create your views here.

def Login(request):
    return render(request,'login-admin.html')


def Admin(request):
    return render(request, 'admin.html')


def Paciente(request):
    return render(request, 'paciente-admin.html')


def Agregar_paciente(request):
    if request.method == 'POST':
      
        dni=request.POST.get('dni-paciente')
        nombre=request.POST.get('nombre-paciente')
        apellido=request.POST.get('apellido-paciente')
        fecha_nacimiento=request.POST.get('nacimiento-paciente')
        sexo=request.POST.get('sexo-paciente')
        sangre=request.POST.get('grupo-sangre')
        patologia=request.POST.get('patoligia-paciente')
        alergia=request.POST.get('alergia')
        telefono=request.POST.get('telefono-paciente')
        dirrecion=request.POST.get('direccion-paciente')
        enfermero=request.POST.get('enfermero-acargo')

        

        

        mi_objeto=Paciente(nombre=nombre,apellido=apellido,fecha_nacimiento=fecha_nacimiento,sexo=sexo,sangre=tipo_sangre,patologia=patologia,alergia=alergia,telefono=telefono,dirrecion=dirrecion,enfermero=dni_enfermero)

        mi_objeto.save()
    return render(request, 'agregar-paciente.html')

def Enfermero(request):
    return render(request, 'enfermero.html')

def Agregar_enfermero(request):
    return render(request, 'agregar-enfermero.html')

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
