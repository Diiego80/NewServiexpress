
from django.db import models
from django.db.models.deletion import PROTECT
from django.forms.widgets import DateTimeBaseInput

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
class BoletaFactura(models.Model):
    bol_fac_total = models.BigIntegerField()
    bol_fac_fecha_emision = models.DateField()
    desc_bol_fac = models.CharField(max_length=7, choices=opciones_bol_fac)
    serv_titulo = models.ForeignKey('Servicio', on_delete=PROTECT)

    #def __str__(self):
    #    return self.bol_fac_id


class Ciudad(models.Model):
    desc_ciudad = models.CharField(max_length=50)
    desc_region = models.ForeignKey("Region", on_delete=models.PROTECT)


    def __str__(self):
        return self.desc_ciudad


class Cliente(models.Model):
    cli_rut = models.IntegerField(primary_key=True)
    cli_pnombre = models.CharField(max_length=30)
    cli_apellidopat = models.CharField(max_length=50)
    cli_apellidomat = models.CharField(max_length=50)
    cli_email = models.EmailField(max_length=50)
    cli_telefono = models.BigIntegerField()
    desc_comuna = models.ForeignKey('Comuna', on_delete=PROTECT)


    def __str__(self):
        return self.cli_pnombre+" "+self.cli_apellidopat


class Comuna(models.Model):
    desc_comuna = models.CharField(max_length=50)
    desc_ciudad = models.ForeignKey("Ciudad", on_delete=PROTECT)

    
    def __str__(self):
        return self.desc_comuna


class DetalleServicio(models.Model):
    fecha_serv_realizado = models.DateField()
    hora_servicio_realizado = models.CharField(max_length=5 ,choices=opciones_hora_reservada)
    servicios_realizados = models.CharField(max_length=150)
    serv_titulo = models.ForeignKey('Servicio', on_delete=PROTECT)
    costo_total_servicios = models.BigIntegerField()
    cli_rut = models.IntegerField()
    desc_medio_pago = models.ForeignKey('PagoServicio', on_delete=PROTECT)
    #res_id_reserva = models.ForeignKey('Reserva', models.DO_NOTHING, db_column='res_id_reserva')




class Empleado(models.Model):
    emp_rut = models.CharField(max_length=8)
    emp_pnombre = models.CharField(max_length=50)
    emp_apellidopat = models.CharField(max_length=50)
    emp_apellidomat = models.CharField(max_length=50)
    emp_sueldo = models.BigIntegerField()
    emp_telefono = models.IntegerField()
    emp_email = models.EmailField(max_length=30)
    desc_tipo_empleado = models.ForeignKey('TipoEmpleado', on_delete=PROTECT)
    user_nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.emp_pnombre+" "+self.emp_apellidopat


class EmpleadoServicio(models.Model):
    cant_utilizada_prod = models.BigIntegerField()
    res_id_reserva = models.BigIntegerField()
    serv_titulo = models.ForeignKey('Servicio', on_delete=PROTECT)
    prod_nombre = models.ForeignKey('Producto', on_delete=PROTECT)
    emp_rut = models.ForeignKey("Empleado", on_delete=PROTECT)

    def __str__(self):
        return self.emp_rut


class PagoServicio(models.Model):
    desc_serv = models.CharField(max_length=50)
    desc_medio_pago = models.ForeignKey('TipoPago', on_delete=PROTECT)
    #ID_BoletaFactura = models.ForeignKey(BoletaFactura, models.DO_NOTHING)



    def __str__(self):
        return self.pago_id


class PedidoOrden(models.Model):
    ped_desc_emision = models.CharField(max_length=100)
    emp_rut = models.ForeignKey("Empleado", on_delete=PROTECT)
    ped_fecha_emision = models.DateField()

    #def __str__(self):
    #    return self.ped_id_emision


class PedidoOrdenProducto(models.Model):
    prod_cantidad = models.BigIntegerField()
    costo_pedido = models.BigIntegerField()
    prod_nombre = models.ForeignKey('Producto', on_delete=PROTECT)








class Producto(models.Model):
    prod_nombre = models.CharField(max_length=100)
    prod_stock = models.BigIntegerField()
    prov_nombre = models.ForeignKey('Proveedor', on_delete=PROTECT)
    desc_marca = models.ForeignKey('TipoMarca', on_delete=PROTECT)

    def __str__(self):
        return self.prod_nombre


class Proveedor(models.Model):
    prov_nombre = models.CharField(max_length=100)
    prov_rut_empresa = models.CharField(max_length=12)


    
    def __str__(self):
        return self.prov_nombre


class RecepcionPedido(models.Model):
    fecha_recepcion = models.DateField()
    desc_recepcion = models.CharField(max_length=150)
    emp_rut = models.ForeignKey('Empleado', on_delete=PROTECT)



class RecepcionPedidoProducto(models.Model):
    prod_cantidad = models.BigIntegerField()
    fecha_recepcion = models.DateField()
    costo_recepcion = models.BigIntegerField(blank=True, null=True)
    prod_nombre = models.ForeignKey('Producto', on_delete=PROTECT)


    #def __str__(self):
    #    return self.id_pedido_prod


class Region(models.Model):
    desc_region = models.CharField(max_length=100)

        
    def __str__(self):
        return self.desc_region





class Reserva(models.Model):
    res_hora_reservada = models.DateField(max_length=5, choices=opciones_hora_reservada)
    res_fecha_pedido_reserva = models.DateField()
    res_desc_reserva = models.CharField(max_length=200)
    cli_rut = models.CharField(max_length=8)

    
    def __int__(self):
        return self.res_id_reserva



class Servicio(models.Model):
    serv_titulo = models.CharField(max_length=35)
    serv_descripcion = models.CharField(max_length=45)
    serv_costo = models.BigIntegerField()
    
    def __str__(self):
        return self.serv_titulo


class TipoEmpleado(models.Model):
    desc_tipo_empleado = models.CharField(max_length=100)

    
    def __str__(self):
        return self.desc_tipo_empleado


class TipoMarca(models.Model):
    desc_marca = models.CharField(max_length=50)

    
    def __str__(self):
        return self.desc_marca


class TipoPago(models.Model):
    desc_medio_pago = models.CharField(max_length=50)

    def __str__(self):
        return self.desc_medio_pago


class TipoUsuario(models.Model):
    user_desc = models.CharField(max_length=30)

    
    def __str__(self):
        return self.user_desc


class Usuario(models.Model):
    user_nombre = models.CharField(max_length=20)
    user_contrasena = models.CharField(max_length=20)
    user_desc = models.ForeignKey("TipoUsuario", on_delete=PROTECT)

        
    def __str__(self):
        return self.user_nombre 
