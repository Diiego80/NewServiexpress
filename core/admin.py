from django.contrib.auth.forms import UserCreationForm
from core.forms import CustomUserCreationForm
from django.contrib import admin
from .models import *
from .forms import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

#Clase Para Reportes

class ReservaResource(resources.ModelResource):
    class Meta:
        model = Reserva

class EmpleadoResource(resources.ModelResource):
    class Meta:
        model = Empleado

class TipoMarcaResource(resources.ModelResource):
    class Meta:
        model = TipoMarca

class ServicioResource(resources.ModelResource):
    class Meta:
        model = Servicio

class BoletaFacturaResource(resources.ModelResource):
    class Meta:
        model = BoletaFactura

class CiudadResource(resources.ModelResource):
    class Meta:
        model = Ciudad

class UserResource(resources.ModelResource):
    class Meta:
        model = User

class ProductoResource(resources.ModelResource):
    class Meta:
        model = Producto

class ProveedorResource(resources.ModelResource):
    class Meta:
        model = Proveedor

class DetalleServicioResource(resources.ModelResource):
    class Meta:
        model = DetalleServicio

class EmpleadoServicioResource(resources.ModelResource):
    class Meta:
        model = EmpleadoServicio


#Desplegar Boton Import-Export
class ReservaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['serv_titulo']
    resource_class = ReservaResource

class EmpleadoAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['emp_rut']
    resource_class = EmpleadoResource

class TipoMarcaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['desc_marca']
    resource_class = TipoMarcaResource

class ServicioAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['desc_marca']
    resource_class = ServicioResource

class CiudadAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['desc_marca']
    resource_class = CiudadResource

class UserAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['desc_marca']
    resource_class = UserResource

class BoletaFacturaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['desc_marca']
    resource_class = BoletaFacturaResource

class ProductoAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['desc_marca']
    resource_class = ProductoResource

class ProveedorAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['desc_marca']
    resource_class = ProveedorResource

class DetalleServicioAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['desc_marca']
    resource_class = DetalleServicioResource

class EmpleadoServicioAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['desc_marca']
    resource_class = EmpleadoServicioResource


# Register your models here.


admin.site.register(BoletaFactura,BoletaFacturaAdmin)
admin.site.register(Ciudad)
admin.site.register(Cliente)
admin.site.register(Comuna)
admin.site.register(DetalleServicio,DetalleServicioAdmin)
admin.site.register(Empleado,EmpleadoAdmin)
admin.site.register(EmpleadoServicio,EmpleadoServicioAdmin)
admin.site.register(PagoServicio)
admin.site.register(PedidoOrden)
admin.site.register(PedidoOrdenProducto)
admin.site.register(Producto,ProductoAdmin)
admin.site.register(Proveedor,ProveedorAdmin)
admin.site.register(RecepcionPedido)
admin.site.register(RecepcionPedidoProducto)
admin.site.register(Region)
admin.site.register(Reserva,ReservaAdmin)
admin.site.register(Servicio,ServicioAdmin)
admin.site.register(TipoEmpleado)
admin.site.register(TipoMarca,TipoMarcaAdmin)
admin.site.register(TipoPago)
admin.site.register(TipoUsuario)
admin.site.register(Usuario)
admin.site.register(MisionVision)