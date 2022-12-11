from django.contrib import admin
from .models import  Reserva, Mesa, Pedido, Menu, Boleta, Empleado, EstadoMesa, EstadoPedido, FormaPago, Insumo, Receta, Solicitud, TipoRol, Turno

# Register your models here.


admin.site.register(Reserva)
admin.site.register(Mesa)
admin.site.register(Pedido)
admin.site.register(Menu)
admin.site.register(Boleta)
admin.site.register(Empleado)
admin.site.register(EstadoMesa)
admin.site.register(EstadoPedido)
admin.site.register(FormaPago)
admin.site.register(Insumo)
admin.site.register(Receta)
admin.site.register(Solicitud)
admin.site.register(TipoRol)
admin.site.register(Turno)

