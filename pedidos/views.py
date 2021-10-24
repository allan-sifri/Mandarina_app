from django.shortcuts import render, redirect
from .models import Pedido
from .forms import PedidoForm

#listar pedidos
def pedidos(request):
	lsita_pedidos = Pedido.objects.all()
	#funcion para crear pedidos
	if request.method == 'POST':
		print(request.POST)
		pedido_form = PedidoForm(request.POST)
		if pedido_form.is_valid():
			pedido_form.save()
			return redirect('pedidos')
	else:
		pedido_form = PedidoForm()	
	return render(request,'pedidos.html', {
		#diccionario
		'pedidos':lsita_pedidos,
		'pedido_form':pedido_form
		})

def elimiar_pedido(render, id):
	pedido = Pedido.objects.get(id = id)
	pedido.delete()
	return redirect('pedidos')
