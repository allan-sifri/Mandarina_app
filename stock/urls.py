from django.urls import path
from django.contrib.auth.decorators import login_required
from. import views

urlpatterns = [
		##	 Path seguro
    path('', login_required(views.stock), name="stock"),	
		##	Path abierto
		#path('', views.stock, name="stock"),
		path('editar_ingrediente/<int:id>', login_required(views.editar_ingrediente), name = "editar_ingrediente"),
		path('elimiar_ingrediente/<int:id>', login_required(views.elimiar_ingrediente), name = "elimiar_ingrediente"),
    ]