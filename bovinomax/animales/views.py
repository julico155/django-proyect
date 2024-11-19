from django.shortcuts import render, redirect, get_object_or_404
from .models import Animal
from .forms import AnimalForm
from django.contrib.auth.decorators import login_required
# Crear
@login_required
def crear_animal(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_animales')
    else:
        form = AnimalForm()
    return render(request, 'animales/crear_animal.html', {'form': form})

# Leer
def listar_animales(request):
    animales = Animal.objects.all()
    return render(request, 'animales/listar_animales.html', {'animales': animales})

# Actualizar
def editar_animal(request, id):
    animal = get_object_or_404(Animal, id=id)
    if request.method == 'POST':
        form = AnimalForm(request.POST, instance=animal)
        if form.is_valid():
            form.save()
            return redirect('listar_animales')
    else:
        form = AnimalForm(instance=animal)
    return render(request, 'animales/editar_animal.html', {'form': form})

# Eliminar
def eliminar_animal(request, id):
    animal = get_object_or_404(Animal, id=id)
    if request.method == 'POST':
        animal.delete()
        return redirect('listar_animales')
    return render(request, 'animales/eliminar_animal.html', {'animal': animal})
