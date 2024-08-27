from django.shortcuts import render, get_object_or_404, redirect
from .models import Material
from .forms import MaterialForm

def material_list(request):
    materiais = Material.objects.all()
    return render(request, 'material/material_list.html', {'materiais': materiais})

def material_detail(request, pk):
    material = get_object_or_404(Material, pk=pk)
    return render(request, 'material/material_detail.html', {'material': material})

def material_create(request):
    if request.method == "POST":
        form = MaterialForm(request.POST)
        if form.is_valid():
            material = form.save()
            return redirect('material_detail', pk=material.pk)
    else:
        form = MaterialForm()
    return render(request, 'material/material_form.html', {'form': form})

def material_update(request, pk):
    material = get_object_or_404(Material, pk=pk)
    if request.method == "POST":
        form = MaterialForm(request.POST, instance=material)
        if form.is_valid():
            material = form.save()
            return redirect('material_detail', pk=material.pk)
    else:
        form = MaterialForm(instance=material)
    return render(request, 'material/material_form.html', {'form': form})

def material_delete(request, pk):
    material = get_object_or_404(Material, pk=pk)
    if request.method == "POST":
        material.delete()
        return redirect('material_list')
    return render(request, 'material/material_confirm_delete.html', {'material': material})
