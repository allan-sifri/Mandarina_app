from django.shortcuts import render, redirect
from .models import Ingrediente
from django.core.exceptions import FieldDoesNotExist
from .forms import IngredienteForm

def stock(request):
	#funcion para listar ingredientes
	lsita_ingredientes = Ingrediente.objects.all()
	#funcion para crear ingrediente
	if request.method == 'POST':
		print(request.POST)
		ingrediente_form = IngredienteForm(request.POST)
		if ingrediente_form.is_valid():
			ingrediente_form.save()
			return redirect('stock')
	else:
		ingrediente_form = IngredienteForm()	
	return render(request,'stock.html', {
		'ingredientes':lsita_ingredientes,
		'ingrediente_form':ingrediente_form
		})


def editar_ingrediente(request, id):
	ingrediente_form = None
	error = None
	ingrediente = Ingrediente.objects.get(id = id)
	try:
		if request.method == "GET":
			ingrediente_form = IngredienteForm(instance = ingrediente)
		else:
			ingrediente_form = IngredienteForm(request.POST, instance = ingrediente)
			if ingrediente_form.is_valid():
				ingrediente_form.save()
			redirect('stock')
	except FieldDoesNotExist as e:
		error = e
	return render(request,'editar_ingrediente.html',{
		'ingrediente_form':ingrediente_form, 
		'error':error
		})

def elimiar_ingrediente(render, id):
	ingrediente = Ingrediente.objects.get(id = id)
	ingrediente.delete()
	return redirect('stock')