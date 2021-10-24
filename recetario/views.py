from django.shortcuts import render, redirect
from .models import Receta
from .forms import RecetaForm

#listar recetas
def recetario(request):
	lsita_recetas = Receta.objects.all()
	if request.method == 'POST':
		print(request.POST)
		receta_form = RecetaForm(request.POST)
		if receta_form.is_valid():
			receta_form.save()
			return redirect('recetario')
	else:
		receta_form = RecetaForm()	
	return render(request,'recetario.html', {
		#diccionario
		'recetas':lsita_recetas,
		'receta_form':receta_form
		})

def elimiar_receta(render, id):
	receta = Receta.objects.get(id = id)
	receta.delete()
	return redirect('recetario')

def crear_receta(request, id):
	if request.method == 'POST':
		print(request.POST)
		receta_form = RecetaForm(request.POST)
		if receta_form.is_valid():
			receta_form.save()
			return redirect('recetario')
	else:
		receta_form = RecetaForm()
	return render(request,'recetario',{
		'receta_form':receta_form
	})