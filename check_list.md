Proceso mandarina
inicia sesión *
	-pedidos
		+agregar 
			dar fecha estimada
			y tiempo que demorara
			#para esto se puede ingresar en la clase pedido una cantidad x de productos se evalúa según el tiempo optimo de preparación para que día se debe preparar y se calendariza por producto y estos llevan una etiqueta del pedido al que pertenecen
		+editar
		 cambiar hora/fecha entrega
		 cambiar preparación
		 cambiar descripción
		+revisar calendario
			visualizar e interactuar con el calendario
	#-stock
	#	actualizar stock
	#	aprobar pedido(depende de disponibilidad de ingredientes para cada receta)
	-inventario
		agregar ingredientes
		eliminar ingredientes


hacer conexion entre el frontend y la base de datos

funcion para agregar en google calendar con la información automáticamente

Notas de avance: (- importante, # se puede postergar)
- Las tres paginas (pedidos, recetario, inventario) están listas visualmente

- En pedidos falta conectar las funciones a google calendar, por ahora se muestran en tablas los pedidos existentes, a futuro cambiarlo solamente por botones con dropdowns como ya se hace con "agregar pedido"

- En recetario falta agregar la funcionalidad para abrir y ver más detalles de cada receta, ojala en una nueva plantilla html

- Falta actualizar los modelos a los de la BBDD creada por Diego

#	Falta calcular según los ingredientes ingresados y los pedidos realizados cuanto es el flujo de dinero

#	Falta función que estima cuando es optimo realizar un pedido

# Falta antes de eliminar un objeto pedir confirmación