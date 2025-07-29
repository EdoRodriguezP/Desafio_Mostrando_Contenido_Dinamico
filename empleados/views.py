from django.shortcuts import render

def lista_empleados(request):
    empleados = ["Edo Rodriguez","Juan Rios", "Ana Gomez", "Pedro Martinez", "Maria Lopez"]
    return render(request, 'empleados/lista.html', {'empleados': empleados})
