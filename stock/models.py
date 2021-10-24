from django.db import models

class Ingrediente(models.Model):
	id = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=30, blank = False, null= False)
	duracion = models.DurationField()
	cantidad = models.PositiveSmallIntegerField(null= True)

	class Meta:
		verbose_name = 'Ingrediente'
		verbose_name_plural = 'Ingredientes'
		
	def __str__(self):
		return self.nombre