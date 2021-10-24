from django.db import models
from stock.models import Ingrediente

class Receta(models.Model):
	id = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=30, blank = False, null= False)
	ingrediente = models.ManyToManyField(Ingrediente)
	descripcion = models.TextField()
	precio = models.PositiveIntegerField()

	class Meta:
		verbose_name = 'Receta'
		verbose_name_plural = 'Recetas'
		
	def __str__(self):
		return self.nombre