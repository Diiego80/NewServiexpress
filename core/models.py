
from datetime import datetime
from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import PROTECT
from django.db.models.fields import DateTimeCheckMixin
from django.db.models.fields.related import OneToOneField
from django.forms.formsets import formset_factory
from django.forms.widgets import DateTimeBaseInput, DateTimeInput
from django.utils.translation import deactivate


# Create your models here.

opciones_bol_fac = [
    ["Boleta","Boleta"],
    ["Factura","Factura"]

]

opciones_hora_reservada = [
    ["08:00","08:00"],
    ["09:00","09:00"],
    ["10:00","10:00"],
    ["11:00","11:00"],
    ["12:00","12:00"],
    ["13:00","13:00"],
    ["14:00","14:00"],
    ["15:00","15:00"],
    ["16:00","16:00"],
    ["17:00","17:00"],
    ["18:00","18:00"],
    ["19:00","19:00"],
    ["20:00","20:00"]

]




#OK
class BoletaFactura(models.Model):
    bol_fac_total = models.BigIntegerField(verbose_name="Ingrese el valor total de la Boleta o Factura:")
    bol_fac_fecha_emision = models.DateField(verbose_name="Ingrese la Fecha de emision de la Boleta o Factura:")
    desc_bol_fac = models.CharField(max_length=7, choices=opciones_bol_fac, verbose_name="Seleccione tipo de pago: ")
    desc_medio_pago = models.ForeignKey('TipoPago', on_delete=PROTECT)
    serv_titulo = models.ForeignKey('Servicio', on_delete=PROTECT)




#OK
class Ciudad(models.Model):
    desc_ciudad = models.CharField(max_length=50,verbose_name="Ingrese Nombre Ciudad:")
    desc_region = models.ForeignKey("Region", on_delete=models.PROTECT)


    def __str__(self):
        return self.desc_ciudad

#OK
class Cliente(models.Model):
    cli_rut = models.IntegerField(primary_key=True,verbose_name="Ingrese el Rut del Cliente sin punto ni guión:")
    cli_pnombre = models.CharField(max_length=30,verbose_name="Ingrese el primer del Cliente:")
    cli_apellidopat = models.CharField(max_length=50,verbose_name="Ingrese el apellido paterno del Cliente:")
    cli_apellidomat = models.CharField(max_length=50,verbose_name="Ingrese el apellido materno del Cliente:")
    cli_email = models.EmailField(max_length=50,verbose_name="Ingrese el Correo/Email del Cliente:")
    cli_telefono = models.BigIntegerField(verbose_name="Ingrese el Numero de telefono del Cliente:")
    desc_comuna = models.ForeignKey('Comuna', on_delete=PROTECT)


    def __str__(self):
        return self.cli_pnombre+" "+self.cli_apellidopat

#OK
class Comuna(models.Model):
    desc_comuna = models.CharField(max_length=50,verbose_name="Ingrese Nombre Comuna:")
    desc_ciudad = models.ForeignKey("Ciudad", on_delete=PROTECT)

    
    def __str__(self):
        return self.desc_comuna

#OK
class DetalleServicio(models.Model):
    fecha_serv_realizado = models.DateField(verbose_name="Ingrese la Fecha del Trabajo Finalizado:")
    hora_servicio_realizado = models.CharField(max_length=5 ,choices=opciones_hora_reservada,verbose_name="Ingrese la hora la cual se entrego el vehiculo:")
    servicios_realizados = models.CharField(max_length=150,verbose_name="Ingrese una breve descripción del trabajo realizado:")
    serv_titulo = models.ForeignKey('Servicio', on_delete=PROTECT)
    costo_total_servicios = models.BigIntegerField(verbose_name="Ingrese el Costo Total del Servicio:")
    cli_rut = models.IntegerField(verbose_name="Ingrese el Rut del Cliente sin punto ni guion:")
    desc_medio_pago = models.ForeignKey("TipoPago", on_delete=PROTECT)
    



#OK
class Empleado(models.Model):
    emp_rut = models.CharField(max_length=8,verbose_name="Ingrese el Rut del Empleado sin punto ni guion:")
    emp_pnombre = models.CharField(max_length=50,verbose_name="Ingrese el Nombre del Empleado:")
    emp_apellidopat = models.CharField(max_length=50,verbose_name="Ingrese el Apellido paterno del Empleado:")
    emp_apellidomat = models.CharField(max_length=50,verbose_name="Ingrese el Apellido materno del Empleado:")
    emp_sueldo = models.BigIntegerField(verbose_name="Ingrese el Sueldo del Empleado:")
    emp_telefono = models.IntegerField(verbose_name="Ingrese el Numero de Telefono del Empleado:")
    emp_email = models.EmailField(max_length=30,verbose_name="Ingrese el Correo/Email del Empleado:")
    desc_tipo_empleado = models.ForeignKey('TipoEmpleado', on_delete=PROTECT)
    user_nombre = models.CharField(max_length=50,verbose_name="Ingrese el Nombre de Usuario del Empleado:")
    
    def __str__(self):
        return self.emp_pnombre+" "+self.emp_apellidopat


class EmpleadoServicio(models.Model):
    cant_utilizada_prod = models.BigIntegerField(verbose_name="Ingrese la Cantidad total utilizada del Producto:")
    res_id_reserva = models.BigIntegerField(verbose_name="Ingrese el ID unico de la Reserva:")
    serv_titulo = models.ForeignKey('Servicio', on_delete=PROTECT, verbose_name="Servicio Realizado: ")
    prod_nombre = models.ForeignKey('Producto', on_delete=PROTECT, verbose_name="Seleccione el producto utilizado: ")
    emp_rut = models.ForeignKey("Empleado", on_delete=PROTECT,verbose_name="Ingrese Nombre del Empleado encargado: sin punto ni guion")

    def __int__(self):
        return self.emp_rut


class PagoServicio(models.Model):
    fecha_pago_serv = models.DateField(verbose_name="Ingrese la Fecha De Pago:")
    serv_titulo = models.ForeignKey('Servicio', on_delete=PROTECT)
    desc_medio_pago = models.ForeignKey('TipoPago', on_delete=PROTECT)



class PedidoOrden(models.Model):
    ped_desc_emision = models.CharField(max_length=100,verbose_name="Ingrese nombre y cantidad del producto:")
    emp_rut = models.ForeignKey("Empleado", on_delete=PROTECT,verbose_name="Ingrese Nombre del Empleado encargado:")
    ped_fecha_emision = models.DateField(verbose_name="Ingrese la Fecha de Emisión del pedido:") 



class PedidoOrdenProducto(models.Model):
    prod_cantidad = models.BigIntegerField(verbose_name="Ingrese la Cantidad de productos a pedir:")
    costo_pedido = models.BigIntegerField(verbose_name="Ingrese el precio total de la cotización:")
    prod_nombre = models.ForeignKey('Producto', on_delete=PROTECT)



class Producto(models.Model):
    prod_nombre = models.CharField(max_length=100, verbose_name="Nombre del Producto:")
    prod_stock = models.BigIntegerField(verbose_name="Cantidad a ingresar:")
    prov_nombre = models.ForeignKey('Proveedor', on_delete=PROTECT,verbose_name="Seleccione el Proveedor del producto:")
    desc_marca = models.ForeignKey('TipoMarca', on_delete=PROTECT,verbose_name="Seleccione la Marca asociada al producto:")

    def __str__(self):
        return self.prod_nombre


class Proveedor(models.Model):
    prov_nombre = models.CharField(max_length=100, verbose_name="Ingrese el Nombre del Proveedor:")
    prov_rut_empresa = models.CharField(max_length=12, verbose_name="Ingrese el Rut de la Empresa asociada sin punto ni guion:")


    
    def __str__(self):
        return self.prov_nombre


class RecepcionPedido(models.Model):
    fecha_recepcion = models.DateField(verbose_name="Seleccione la Fecha de recepción del pedido:")
    desc_recepcion = models.CharField(max_length=150, verbose_name="Ingrese el nombre y cantidad de Productos recibidos:")
    emp_rut = models.ForeignKey('Empleado', on_delete=PROTECT, verbose_name="Ingrese Nombre del Empleado encargado:")



class RecepcionPedidoProducto(models.Model):
    prod_cantidad = models.BigIntegerField(verbose_name="Ingrese Cantidad entrante del Producto:")
    fecha_recepcion = models.DateField(verbose_name="Seleccione la Fecha de rececepción")
    costo_recepcion = models.BigIntegerField(blank=True, null=True, verbose_name="Ingrese el costro de recepción. Si no hay costo agregado dejar en blanco.")
    prod_nombre = models.ForeignKey('Producto', on_delete=PROTECT, verbose_name="Ingrese el nombre del Producto entrante")


    #def __str__(self):
    #    return self.id_pedido_prod


class Region(models.Model):
    desc_region = models.CharField(max_length=100, verbose_name="Ingrese el nombre de la región a ingresar")

        
    def __str__(self):
        return self.desc_region





class Reserva(models.Model):
    res_hora_reservada = models.CharField(max_length=5, choices=opciones_hora_reservada, verbose_name="Seleccione hora a reservar:",)
    res_fecha_pedido_reserva = models.DateField(verbose_name="Seleccione dia a reservar:")
    serv_titulo = models.ForeignKey('Servicio', on_delete=PROTECT, verbose_name="Ingrese servicio a realizar:")
    res_desc_reserva = models.CharField(max_length=200, verbose_name="Agregue una breve descripción del vehiculo y/o sus errores:")
    cli_rut = models.CharField(max_length=8, verbose_name="Ingrese su RUT sin punto y sin DV, Ej: '20537529' ")

    
    



class Servicio(models.Model):
    serv_titulo = models.CharField(max_length=35, verbose_name="Ingrese el Titulo/Nombre del Servicio:")
    serv_descripcion = models.CharField(max_length=45, verbose_name="Ingrese una breve descripción del servicio:")
    serv_costo = models.BigIntegerField(verbose_name="Ingrese el costo del Servicio a realizar:")
    
    def __str__(self):
        return self.serv_titulo


class TipoEmpleado(models.Model):
    desc_tipo_empleado = models.CharField(max_length=100,verbose_name="Ingrese el nombre del nuevo Tipo Empleado:")

    
    def __str__(self):
        return self.desc_tipo_empleado


class TipoMarca(models.Model):
    desc_marca = models.CharField(max_length=50,verbose_name="Ingrese el nombre de la nueva marca asociada:")

    
    def __str__(self):
        return self.desc_marca


class TipoPago(models.Model):
    desc_medio_pago = models.CharField(max_length=50,verbose_name="Ingrese el Medio De Pago:")

    def __str__(self):
        return self.desc_medio_pago


class TipoUsuario(models.Model):
    user_desc = models.CharField(max_length=30,verbose_name="Ingrese el nuevo Tipo Usuario el cual sera parte del sistema:")

    
    def __str__(self):
        return self.user_desc


class Usuario(models.Model):
    user_nombre = models.CharField(max_length=20,verbose_name="Ingrese el Nombre/Tag del nuevo Usuario:")
    user_contrasena = models.CharField(max_length=20,verbose_name="Ingrese la contraseña del nuevo usuario:")
    user_desc = models.ForeignKey("TipoUsuario", on_delete=PROTECT,verbose_name="Integre una breve descripcion de cargos del nuevo usuario:")

        
    def __str__(self):
        return self.user_nombre 

# MODELOS ONLY PAG WEB


CATEGORY = (
    ('Stationary', 'Stationary'),
    ('Electronics', 'Electronics'),
    ('Food', 'Food'),
)

class MisionVision(models.Model):
    mision = models.CharField(max_length=200)
    vision = models.CharField(max_length=200)
    imagen_vision = models.ImageField(upload_to="Vision", null=True)
    imagen_mision = models.ImageField(upload_to="Mision", null=True)


    def __str__(self):
        return f'{self.name}'    

class Order(models.Model):
    name = models.ForeignKey(Reserva, on_delete=models.CASCADE, null=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    order_quantity = models.PositiveIntegerField(null=True)

    def __str__(self):
        return f'{self.customer}-{self.name}'