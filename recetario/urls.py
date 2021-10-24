from django.urls import path
from django.contrib.auth.decorators import login_required
from. import views

urlpatterns = [
		##	 Path seguro
    path('', login_required(views.recetario), name="recetario"),
		##	Path abierto
		#path('', views.recetario, name="recetario"),
    path('', login_required(views.crear_receta), name ="crear_receta"),
		path('elimiar_receta/<int:id>', login_required(views.elimiar_receta), name = "elimiar_receta"),
    ]