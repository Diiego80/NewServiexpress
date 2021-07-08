from django.contrib import admin
from django.urls import path

from .views import *
from .models import *

urlpatterns = [
    #Navegacion General
    path ('', index, name="index"),
    path ('ingreso/', ingreso, name="ingreso"),
    path ('nosotros/', nosotros, name="nosotros"),
    path ('servicio/', servicio, name="servicio"),
    path ('ubicacion/', ubicacion, name="ubicacion"),
    path ('administracion/', administracion, name="administracion"),
    path ('manual-clientes/', manual_clientes, name="manual_clientes"),
    path ('reportes/', reportes, name="reportes"),
    path ('admin-reportes/', admin_reportes, name="admin_reportes"),
    
    #Sectores Internos de Administracion
    path ('sector-ubicaciones/', sector_ubicaciones, name="sector_ubicaciones"), 
    path ('sector-pagos/', sector_pagos, name="sector_pagos"),
    path ('sector-empleados/', sector_empleados, name="sector_empleados"),
    #Registro
    path('registro/', registro, name="registro"),
    #Administracion Interna
    path ('registro-clientes/', registro_clientes, name="registro_clientes"),
 

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
    path ('agregar-pago-serv/', agregar_pago_serv, name="agregar_pago_serv"),
    path ('agregar-proveedor/', agregar_proveedor, name="agregar_proveedor"),
    path ('agregar-tipo-marca/', agregar_tipo_marca, name="agregar_tipo_marca"),
    path ('agregar-pedido-orden/', agregar_ped_orden, name="agregar_ped_orden"),
    path ('agregar-tipo-empleado/', agregar_tipo_empleado, name="agregar_tipo_empleado"),
    path ('agregar-reserva/', agregar_reserva, name="agregar_reserva"),
    path ('agregar-tipo-pago/', agregar_tipo_pago, name="agregar_tipo_pago"),
    path ('agregar-tipo-empleado/', agregar_tipo_empleado, name="agregar_tipo_empleado"),

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
    path ('listado-proveedor/', listado_proveedor, name="listado_proveedor"),
    path ('listado-tipo-marca/', listado_tipo_marca, name="listado_tipo_marca"),
    path ('listado-pedido-orden/', listado_ped_orden, name="listado_ped_orden"),
    path ('listado-tipo-empleado/', listado_tipo_empleado, name="listado_tipo_empleado"),
    path ('listado-reserva/', listado_reserva, name="listado_reserva"),
    path ('listado-tipo-pago/', listado_tipo_pago, name="listado_tipo_pago"),
    path ('listado-tipo-empleado/', listado_tipo_empleado, name="listado_tipo_empleado"),

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
    path ('modificar-proveedor/<id>/', modificar_proveedor, name="modificar_proveedor"),
    path ('modificar-tipo-marca/<id>/', modificar_tipo_marca, name="modificar_tipo_marca"),
    path ('modificar-pedido-orden/<id>/', modificar_ped_orden, name="modificar_ped_orden"),
    path ('modificar-tipo-empleado/<id>/', modificar_ped_orden, name="modificar_ped_orden"),
    path ('modificar-reserva/<id>/', modificar_reserva, name="modificar_reserva"),
    path ('modificar-tipo-pago/<id>/', modificar_tipo_pago, name="modificar_tipo_pago"),
    path ('modificar-tipo-empleado/<id>/', modificar_tipo_empleado, name="modificar_tipo_empleado"),

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
    path ('eliminar-proveedor/<id>/', eliminar_proveedor, name="eliminar_proveedor"),
    path ('eliminar-tipo-marca/<id>/', eliminar_tipo_marca, name="eliminar_tipo_marca"),
    path ('eliminar-pedido-orden/<id>/', eliminar_ped_orden, name="eliminar_ped_orden"),
    path ('eliminar-tipo-empleado/<id>/', eliminar_tipo_empleado, name="eliminar_tipo_empleado"),
    path ('eliminar-reserva/<id>/', eliminar_reserva, name="eliminar_reserva"),
    path ('eliminar-tipo-pago/<id>/', eliminar_tipo_pago, name="eliminar_tipo_pago"),
    path ('eliminar-tipo-empleado/<id>/', eliminar_tipo_empleado, name="eliminar_tipo_empleado"),
]


