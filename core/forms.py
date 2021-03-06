from django import forms
from django.db import models
from django.db.models.fields import NullBooleanField
from django.forms.widgets import NullBooleanSelect, Textarea
from .models import *
import datetime
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class DateForm(forms.Form):
    date = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])
    

class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', "first_name", "last_name", "email","password1", "password2","is_staff"]

    
        widgets = {
            "is_staff": forms.HiddenInput()
        }


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
    
        widgets = {
            "ped_fecha_emision": forms.SelectDateWidget()
        }
    


class PedidoOrdenProductoForm(forms.ModelForm):

    class Meta:
        model = PedidoOrdenProducto
        fields = "__all__"

   
   
class RecepcionPedidoForm(forms.ModelForm):

    class Meta:
        model = RecepcionPedido
        fields = "__all__"

        widgets = {
            "fecha_recepcion": forms.SelectDateWidget()
        }


class RecepcionPedidoProductoForm(forms.ModelForm):

    class Meta:
        model = RecepcionPedidoProducto
        fields = "__all__"
    
        widgets = {
            "fecha_recepcion": forms.SelectDateWidget()
        }

class DetalleServicioForm(forms.ModelForm):

    class Meta:
        model = DetalleServicio
        fields = "__all__"
    
        widgets = {
            "fecha_serv_realizado": forms.SelectDateWidget()
        }

class EmpleadoServicioForm(forms.ModelForm):

    class Meta:
        model = EmpleadoServicio
        fields = "__all__"

class BoletaFacturaPedidoForm(forms.ModelForm):

    class Meta:
        model = BoletaFactura
        fields = "__all__"
    
        widgets = {
            "bol_fac_fecha_emision": forms.SelectDateWidget()
        }

class ProductForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = '__all__'


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['name', 'order_quantity']
 