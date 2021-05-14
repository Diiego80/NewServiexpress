from django import forms
from django.db import models
from .models import *
import datetime


class UsuarioForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = ['user_nombre', 'user_contrasena']
        #fields = '__all__'

class ReservaForm(forms.ModelForm):
    
    class Meta:
        model = Reserva
        fields =  "__all__"

        widgets = {
            "res_fecha_pedido_reserva": forms.SelectDateWidget()
        }



class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = "__all__"
class RegionForm(forms.ModelForm):

    class Meta:
        model = Region
        fields = "__all__"


class CiudadForm(forms.ModelForm):

    class Meta:
        model = Ciudad
        fields = "__all__" 

class ComunaForm(forms.ModelForm):

    class Meta: 
        model = Comuna
        fields = "__all__"
       #fields = ['id_comuna','desc_comuna','id_ciudad']

class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = "__all__"

class EmpleadoForm(forms.ModelForm):

    class Meta:
        model = Empleado
        fields = "__all__"

class TipoMarcaForm(forms.ModelForm):

    class Meta:
        model = TipoMarca
        fields = "__all__"

class ProveedorForm(forms.ModelForm):

    class Meta:
        model = Proveedor
        fields = "__all__"

class TipoEmpleadoForm(forms.ModelForm):

    class Meta:
        model = TipoEmpleado
        fields = "__all__"

class TipoPagoForm(forms.ModelForm):

    class Meta:
        model = TipoPago
        fields = "__all__"

class TipoUsuarioForm(forms.ModelForm):

    class Meta:
        model = TipoUsuario
        fields = "__all__"

class PagoServicioForm(forms.ModelForm):

    class Meta:
        model = PagoServicio
        fields = "__all__"

class ServicioForm(forms.ModelForm):

    class Meta:
        model = Servicio
        fields = "__all__"
        #fields = ['serv_descripcion','serv_costo','serv_titulo']

class PedidoOrdenForm(forms.ModelForm):

    class Meta:
        model = PedidoOrden
        fields = "__all__"

class PedidoOrdenProductoForm(forms.ModelForm):

    class Meta:
        model = PedidoOrdenProducto
        fields = "__all__"


class RecepcionPedidoForm(forms.ModelForm):

    class Meta:
        model = RecepcionPedido
        fields = "__all__"

class RecepcionPedidoProductoForm(forms.ModelForm):

    class Meta:
        model = RecepcionPedidoProducto
        fields = "__all__"

class DetalleServicioForm(forms.ModelForm):

    class Meta:
        model = DetalleServicio
        fields = "__all__"

class EmpleadoServicioForm(forms.ModelForm):

    class Meta:
        model = EmpleadoServicio
        fields = "__all__"

class BoletaFacturaPedidoForm(forms.ModelForm):

    class Meta:
        model = BoletaFactura
        fields = "__all__"