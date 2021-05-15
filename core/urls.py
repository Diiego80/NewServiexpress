from django.contrib import admin
from django.urls import path

from .views import *
from .models import *

urlpatterns = [
    #Navegacion General
    path('', index, name="index"),
    path('ingreso/', ingreso, name="ingreso"),
    path ('nosotros/', nosotros, name="nosotros"),
    path ('servicio/', servicio, name="servicio"),
    path ('ubicacion/', ubicacion, name="ubicacion"),
    
    #Registro
    path('registro/', registro, name="registro"),
    #Administracion Interna
    path ('registro-clientes/', registro_clientes, name="registro_clientes"),
    path ('registro-productos/', registro_productos, name="registro_productos"),
    #Formularios
    path ('formulario-producto/', formulario_producto, name="formulario_producto"),
    path ('formulario-reserva/', formulario_reserva, name="formulario_reserva"),
    path ('formulario-servicios/', formulario_servicios, name="formulario_servicios"),
    #Agregar
    path ('agregar-producto/', agregar_producto, name="agregar_producto"),
    path ('agregar-empleado/', agregar_empleado, name="agregar_empleado"),
    path ('agregar-servicio/', agregar_servicio, name="agregar_servicio"),
    path ('agregar-comuna/', agregar_comuna, name="agregar_comuna"),
    path ('agregar-ciudad/', agregar_ciudad, name="agregar_ciudad"),
    path ('agregar-det-serv/', agregar_det_serv, name="agregar_det_serv"),
    path ('agregar-bol-fac/', agregar_bol_fac, name="agregar_bol_fac"),
    path ('agregar-cliente/', agregar_cliente, name="agregar_cliente"),
    path ('agregar-emp-serv/', agregar_emp_serv, name="agregar_emp_serv"),
    path ('agregar-region/', agregar_region, name="agregar_region"),
    path ('agregar-tipo-usuario/', agregar_tipo_usuario, name="agregar_tipo_usuario"),
    path ('agregar-pago-serv/', agregar_pago_servicio, name="agregar_pago_serv"),
    #Listados
    path ('listado-producto/', listado_producto, name="listado_producto"),
    path ('listado-empleado/', listado_empleado, name="listado_empleado"),
    path ('listado-servicio/', listado_servicio, name="listado_servicio"),
    path ('listado-comuna/', listado_comuna, name="listado_comuna"),
    path ('listado-ciudad/', listado_ciudad, name="listado_ciudad"),
    path ('listado-det-serv/', listado_det_serv, name="listado_det_serv"),
    path ('listado-bol-fac/', listado_bol_fac, name="listado_bol_fac"),
    path ('listado-cliente/', listado_cliente, name="listado_cliente"),
    path ('listado-emp-serv/', listado_emp_serv, name="listado_emp_serv"),
    path ('listado-region/', listado_region, name="listado_region"),
    path ('listado-tipo-usuario/', listado_tipo_usuario, name="listado_tipo_usuario"),
    path ('listado-pago-serv/', listado_pago_serv, name="listado_pago_serv"),
    #Modificar
    path ('modificar-producto/<id>/', modificar_producto, name="modificar_producto"),
    path ('modificar-empleado/<id>/', modificar_empleado, name="modificar_empleado"),
    path ('modificar-servicio/<id>/', modificar_servicio, name="modificar_servicio"),
    path ('modificar-comuna/<id>/', modificar_comuna, name="modificar_comuna"),
    path ('modificar-ciudad/<id>/', modificar_ciudad, name="modificar_ciudad"),
    path ('modificar-det-serv/<id>/', modificar_det_serv, name="modificar_det_serv"),
    path ('modificar-bol-fac/<id>/', modificar_bol_fac, name="modificar_bol_fac"),
    path ('modificar-cliente/<id>/', modificar_cliente, name="modificar_cliente"),
    path ('modificar-emp-serv/<id>/', modificar_emp_serv, name="modificar_emp_serv"),
    path ('modificar-region/<id>/', modificar_region, name="modificar_region"),
    path ('modificar-tipo-usuario/<id>/', modificar_tipo_usuario, name="modificar_tipo_usuario"),
    path ('modificar-pago-serv/<id>/', modificar_pago_servicio, name="modificar_pago_serv"),
    #Eliminar
    path ('eliminar-producto/<id>/', eliminar_producto, name="eliminar_producto"),
    path ('eliminar-empleado/<id>/', eliminar_empleado, name="eliminar_empleado"),
    path ('eliminar-servicio/<id>/', eliminar_servicio, name="eliminar_servicio"),
    path ('eliminar-comuna/<id>/', eliminar_comuna, name="eliminar_comuna"),
    path ('eliminar-ciudad/<id>/', eliminar_ciudad, name="eliminar_ciudad"),
    path ('eliminar-det-serv/<id>/', eliminar_det_serv, name="eliminar_det_serv"),
    path ('eliminar-bol-fac/<id>/', eliminar_bol_fac, name="eliminar_bol_fac"),
    path ('eliminar-cliente/<id>/', eliminar_cliente, name="eliminar_cliente"),
    path ('eliminar-emp-serv/<id>/', eliminar_emp_serv, name="eliminar_emp_serv"),
    path ('eliminar-region/<id>/', eliminar_region, name="eliminar_region"),
    path ('eliminar-tipo-usuario/<id>/', eliminar_tipo_usuario, name="eliminar_tipo_usuario"),
    path ('eliminar-pago-serv/<id>/', eliminar_pago_servicio, name="eliminar_pago_serv"),
]


