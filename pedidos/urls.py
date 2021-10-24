from django.urls import path
from django.contrib.auth.decorators import login_required
from. import views

urlpatterns = [
		##	path abierto
    #path('', views.pedidos, name="pedidos"),
		##	path seguro con login
		path('', login_required(views.pedidos), name="pedidos"),
		path('elimiar_pedido/<int:id>', login_required(views.elimiar_pedido), name = "elimiar_pedido"),
    ]