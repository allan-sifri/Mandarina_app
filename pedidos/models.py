from django.db import models
from recetario.models import Receta

class Pedido(models.Model):
	id = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=30, blank = True, null= False)
	receta = models.ManyToManyField(Receta)
	entrega = models.DateField()
	descripcion = models.TextField()

	class Meta:
		verbose_name = 'Pedido'
		verbose_name_plural = 'Pedidos'
		
	def __str__(self):
		return self.nombre