from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
# Extra
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from rest_framework import viewsets
from django.contrib import messages
from django.http import Http404

# Create your views here.

# M I S I O N  V I S I O N
def mision_vision(request):
    misionVision = MisionVision.objects.all()
    data = {
        'misionvision': misionVision
    }
    return render(request, 'core/nosotros.html', data)

#Navegación General
def index(request):
    return render(request, 'core/index.html')


def ingreso(request):
    return render(request, 'core/ingreso.html')


def nosotros(request):
    return render(request, 'core/nosotros.html')


def servicio(request):
    servicio = Servicio.objects.all()
    data = {
        'servicio': servicio
    }
    return render(request, 'core/servicio.html', data)


def ubicacion(request):
    return render(request, 'core/ubicacion.html')

@login_required
@permission_required('core.admin_interface')
def administracion(request):
    return render(request, 'core/administracion.html')

def sector_ubicaciones(request):
    return render(request, 'core/sector_ubicaciones.html')

#INGRESO USUARIOS FINALES 
def registro(request):
    data = {
        'form': CustomUserCreationForm
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], 
                                password=formulario.cleaned_data["password1"])
            login(request,user)
            messages.success(request, "Registro Completado Correctamente")
            return redirect(to='/')
        data["form"] = formulario
    return render(request, 'registration/registro.html', data)

#Ingreso de Django Admin
#def registro_admin(request):
#    dataRegistro = {
#        'form': UsuarioForm()
#    }
#    if request.method == 'POST':
#        formularioContacto = UsuarioForm(data=request.POST)
#        if formularioContacto.is_valid():
#            formularioContacto.save()
#            dataRegistro["mensaje"] = "Usuario Guardado Correctamente"
#        else:
#            dataRegistro["form"] = formularioContacto
#
#    return render(request, 'registration/registro.html', dataRegistro)


def registro_clientes(request):
    return render(request, 'core/registro_clientes.html')


#def registro_productos(request):
    return render(request, 'core/registro_productos.html')


#def formulario_producto(request):
    return render(request, 'core/formularios/formulario_productos.html')


#def formulario_clientes(request):
    return render(request, 'core/cliente/formulario_clientes.html')

#def formulario_servicios(request):
    return render(request, 'core/servicio/formulario_servicio.html')

@login_required
def formulario_reserva(request):
    data = {
        'formReserva': ReservaForm()
    }

    if request.method == 'POST':
        formulario = ReservaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Reserva Guardada Con Exito"
        else:
            data["form"] = formulario
    return render(request, 'core/reserva/formulario_reserva.html', data)

# P R O D U C T O
@permission_required('core.add_producto')
def agregar_producto(request):
    data = {
        'form': ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Producto Registrado Correctamente")
        else:
            data["form"] = formulario

    return render(request, 'core/producto/agregar_producto.html',data)

@login_required
def listado_producto (request):
    productos = Producto.objects.all()
    
    data = {
        'productos': productos
    }

    return render(request, 'core/producto/listado_producto.html', data)

@login_required
def modificar_producto(request, id):

    producto = Producto.objects.get(id = id)

    data = {
        'form': ProductoForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto Modificado Correctamente")
            return redirect(to="listado_producto")
        data['form'] = formulario

    return render(request,'core/producto/modificar_producto.html', data)

@login_required
def eliminar_producto (request, id):
    producto = Producto.objects.get(id = id)
    producto.delete()
    messages.success(request, "Producto Eliminado Correctamente")

    return redirect(to='listado_producto')

# E M P L E A D O

@login_required
def agregar_empleado(request):
    data = {
        'form': EmpleadoForm()
    }

    if request.method == 'POST':
        formulario = EmpleadoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Empleado Registrado Correctamente")
        else:
            data["form"] = formulario
        
    return render(request,'core/empleado/agregar_empleado.html', data)

@login_required
def listado_empleado (request):
    empleados = Empleado.objects.all()

    data = {
        'empleados': empleados
    }

    return render(request, 'core/empleado/listado_empleado.html', data)

@login_required
def modificar_empleado(request, id):

    empleado = Empleado.objects.get(id = id)

    data = {
        'form': EmpleadoForm(instance=empleado)
    }
    if request.method == 'POST':
        formulario = EmpleadoForm(data=request.POST, instance=empleado)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Empleado Modificado Correctamente")
            return redirect(to="listado_empleado")
        data ['form'] = formulario

    return render(request, 'core/empleado/modificar_empleado.html', data)

@login_required
def eliminar_empleado(request, id):
    empleado = Empleado.objects.get(id = id)
    empleado.delete()
    messages.success(request, "Empleado Eliminado Correctamente")

    return redirect(to="listado_empleado")

# S E R V I C I O S 

@login_required
def agregar_servicio(request):
    data = {
        'form': ServicioForm(data=request.POST)
    }

    if request.method == 'POST':
        formulario = ServicioForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Servicio Agregado Correctamente")
        else:
            data["form"] = formulario
        
    return render(request,'core/servicio/agregar_servicio.html', data)


def listado_servicio (request):
    servicios = Servicio.objects.all()

    data = {
        'servicios': servicios
    }

    return render(request,'core/servicio/listado_servicio.html', data)

@login_required
def modificar_servicio(request, id):

    servicio = Servicio.objects.get(id = id)

    data = {
        'form': ServicioForm(instance=servicio)
    }
    if request.method == 'POST':
        formulario = ServicioForm(data=request.POST, instance=servicio)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Servicio Modificado Correctamente")
            data ['form'] = formulario

    return render(request, 'core/servicio/modificar_servicio.html', data)

@login_required
def eliminar_servicio(request, id):
    servicio = Servicio.objects.get(id = id)
    servicio.delete()
    messages.success(request, "Servicio Eliminado Correctamente")

    return redirect(to='listado_servicio')

# C O M U N A

@login_required
def agregar_comuna(request):
    data = {
        'form': ComunaForm(data=request.POST)
    }

    if request.method == 'POST':
        formulario = ComunaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Comuna Agregada Con Exito"
        else:
            data["form"] = formulario
        
    return render(request,'core/comuna/agregar_comuna.html', data)
    

@login_required
def listado_comuna (request):
    comunas = Comuna.objects.all()

    data = {
        'comunas': comunas
    }

    return render(request, 'core/comuna/listado_comuna.html', data)

@login_required
def modificar_comuna(request, id):

    comuna = Comuna.objects.get(id = id)

    data = {
        'form': ComunaForm(instance=comuna)
    }
    if request.method == 'POST':
        formulario = ComunaForm(data=request.POST, instance=comuna)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Comuna Modificada Correctamente"
            data ['form'] = formulario

    return render(request, 'core/comuna/modificar_comuna.html', data)

@login_required
def eliminar_comuna(request, id):
    comuna = Comuna.objects.get(id = id)
    comuna.delete()

    return redirect(to='listado_comuna')

# C I U D A D

@login_required
def agregar_ciudad(request):
    data = {
        'form': CiudadForm(data=request.POST)
    }

    if request.method == 'POST':
        formulario = CiudadForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Ciudad Agregada Con Exito"
        else:
            data["form"] = formulario
        
    return render(request,'core/ciudad/agregar_ciudad.html', data)

@login_required
def listado_ciudad (request):
    ciudades = Ciudad.objects.all()

    data = {
        'ciudades': ciudades
    }

    return render(request, 'core/ciudad/listado_ciudad.html', data)

@login_required
def modificar_ciudad(request, id):

    ciudad = Ciudad.objects.get(id = id)

    data = {
        'form': CiudadForm(instance=ciudad)
    }
    if request.method == 'POST':
        formulario = CiudadForm(data=request.POST, instance=ciudad)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Ciudad Modificada Correctamente"
            data ['form'] = formulario

    return render(request, 'core/ciudad/modificar_ciudad.html', data)

@login_required
def eliminar_ciudad(request, id):
    ciudad = Ciudad.objects.get(id = id)
    ciudad.delete()

    return redirect(to='listado_ciudad')
 
# D E T A L L E  S E R V I C I O

@login_required
def agregar_det_serv(request):
    data = {
        'form': DetalleServicioForm(data=request.POST)
    }

    if request.method == 'POST':
        formulario = DetalleServicioForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Detalle Servicio Agregado con exito"
        else:
            data["form"] = formulario
    return render(request,'core/detalle_servicio/agregar_det_serv.html', data)

@login_required
def listado_det_serv(request):
    det_serv = DetalleServicio.objects.all()

    data = {
        'det_serv': det_serv
    }

    return render(request, 'core/detalle_servicio/listado_det_serv.html', data)

@login_required
def modificar_det_serv(request):

    det_ser = DetalleServicio.objects.get(id = id)

    data = {
        'form':DetalleServicioForm(instance=det_ser)
    }
    if request.method == 'POST':
        formulario = DetalleServicioForm(data=request.POST, instance=det_ser)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Detalle Servicio Modificado Correctamente"
            data['form'] = formulario
    return render(request, 'core/detalle_servicio/modificar_det_serv.html', data)

@login_required
def eliminar_det_serv(request, id):
    det_ser = DetalleServicio.objects.get(id = id)
    det_ser.delete()

    return redirect(to='listado_det_serv')

# F A C T U R A  Y  B O L E T A

@login_required
def agregar_bol_fac(request):
    data = {
        'form':BoletaFacturaPedidoForm()
    }

    if request.method == 'POST':
        formulario = BoletaFacturaPedidoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Boleta y/o Factura Agregada Correctamente")
        else:
            data["form"] = formulario

    return render(request,'core/boleta/agregar_bol_fac.html', data)

def listado_bol_fac (request):
    bol_fac = BoletaFactura.objects.all()

    data = {
        'bol_fac': bol_fac
    }

    return render(request, 'core/boleta/listado_bol_fac.html', data)

def modificar_bol_fac(request, id):

    boleta = BoletaFactura.objects.get(id = id)

    data = {
        'form': BoletaFacturaPedidoForm(instance=boleta)
    }
    if request.method == 'POST':
        formulario = BoletaFacturaPedidoForm(data=request.POST, instance=boleta)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Boleta y/o Factura Modificada Correctamente")
            return redirect(to="listado_bol_fac")
        data['form'] = formulario
    return render(request,'core/boleta/modificar_bol_fac.html', data)

def eliminar_bol_fac(request, id):
    boleta = BoletaFactura.objects.get(id = id)
    boleta.delete()
    messages.success(request, "Boleta y/o Factura Eliminada Correctamente")

    return redirect(to="listado_bol_fac")

# C L I E N T E S

def agregar_cliente(request):
    data = {
        'form': ClienteForm(data=request.POST)
    }

    if request.method == 'POST':
        formulario = ClienteForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Cliente Agregado Correctamente")
        else:
            data["form"] = formulario
        
    return render(request,'core/cliente/agregar_cliente.html', data)

def listado_cliente(request):
    clientes = Cliente.objects.all()

    data = {
        'clientes': clientes
    }

    return render(request,'core/cliente/listado_cliente.html', data)

def modificar_cliente(request, id):

    cliente = Cliente.objects.get(id = id)

    data = {
        'form': ClienteForm(instance=cliente)
    }
    if request.method == 'POST':
        formulario = ClienteForm(data=request.POST, instance=cliente)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Clietne Modificado Correctamente")
            data ['form'] = formulario

    return render(request, 'core/cliente/modificar_cliente.html', data)

def eliminar_cliente(request, id):
    cliente = Cliente.objects.get(id = id)
    cliente.delete()
    messages.success(request, "Cliente Modificado Correctamente")

    return redirect(to='listado_cliente')

# E M P L E A D O  S E R V I C I O

def agregar_emp_serv(request):
    data = {
        'form': EmpleadoServicioForm(data=request.POST)
    }

    if request.method == 'POST':
        formulario = EmpleadoServicioForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Documento Agregado Con Exito")
        else:
            data["form"] = formulario
        
    return render(request,'core/empleado_servicio/agregar_emp_serv.html', data)
    

def listado_emp_serv (request):
    emp_servicios = EmpleadoServicio.objects.all()

    data = {
        'emp_servicios': emp_servicios
    }

    return render(request, 'core/empleado_servicio/listado_emp_serv.html', data)

def modificar_emp_serv(request, id):
    emp_serv = EmpleadoServicio.objects.get(id = id)

    data = {
        'form': EmpleadoServicioForm(instance=emp_serv)
    }
    if request.method == 'POST':
        formulario = EmpleadoServicioForm(data=request.POST, instance=emp_serv)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Documento Modificado Con Exito")
            data ['form'] = formulario

    return render(request, 'core/empleado_servicio/modificar_emp_serv.html', data)

def eliminar_emp_serv(request, id):
    emp_serv = EmpleadoServicio.objects.get(id = id)
    emp_serv.delete()

    return redirect(to='listado_emp_serv')

# R E G I O N

def agregar_region(request):
    data = {
        'form': RegionForm(data=request.POST)
    }

    if request.method == 'POST':
        formulario = RegionForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Region Agregada Con Exito")
        else:
            data["form"] = formulario
        
    return render(request,'core/region/agregar_region.html', data)
    

def listado_region (request):
    regiones = Region.objects.all()

    data = {
        'regiones': regiones
    }

    return render(request, 'core/region/listado_region.html', data)

def modificar_region(request, id):

    region = Region.objects.get(id = id)

    data = {
        'form': RegionForm(instance=region)
    }
    if request.method == 'POST':
        formulario = RegionForm(data=request.POST, instance=region)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Región Modificada Con Exito")
            data ['form'] = formulario

    return render(request, 'core/region/modificar_region.html', data)

def eliminar_region(request, id):
    region = Region.objects.get(id = id)
    region.delete()

    return redirect(to='listado_region')

# T I P O  U S U A R I O

def agregar_tipo_usuario(request):
    data = {
        'form': TipoUsuarioForm(data=request.POST)
    }

    if request.method == 'POST':
        formulario = TipoUsuarioForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Nuevo Tipo-Usuario Agregado Con Exito")
        else:
            data["form"] = formulario
        
    return render(request,'core/tipo_usuario/agregar_tipo_usuario.html', data)
    

def listado_tipo_usuario (request):
    tipos = TipoUsuario.objects.all()

    data = {
        'tipos': tipos
    }

    return render(request, 'core/tipo_usuario/listado_tipo_usuario.html', data)

def modificar_tipo_usuario(request, id):

    tipo_usuario = TipoUsuario.objects.get(id = id)

    data = {
        'form': TipoUsuarioForm(instance=tipo_usuario)
    }
    if request.method == 'POST':
        formulario = TipoUsuarioForm(data=request.POST, instance=tipo_usuario)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Tipo-Usuario Modificado Con Exito")
            data ['form'] = formulario

    return render(request, 'core/tipo_usuario/modificar_tipo_usuario.html', data)

def eliminar_tipo_usuario(request, id):
    tipo_usuario = TipoUsuario.objects.get(id = id)
    tipo_usuario.delete()

    return redirect(to='listado_tipo_usuario')

# P A G O  S E R V I C I O

def agregar_pago_servicio(request):
    data = {
        'form': PagoServicioForm(data=request.POST)
    }

    if request.method == 'POST':
        formulario = PagoServicioForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Pago Agregado Con Exito")
        else:
            data["form"] = formulario
        
    return render(request,'core/pago_servicio/agregar_pago_serv.html', data)
    

def listado_pago_serv (request):
    pagos = PagoServicio.objects.all()

    data = {
        'pagos': pagos
    }

    return render(request, 'core/pago_servicio/listado_pago_serv.html', data)

def modificar_pago_servicio(request, id):

    pago_servicio = PagoServicio.objects.get(id = id)

    data = {
        'form': PagoServicioForm(instance=pago_servicio)
    }
    if request.method == 'POST':
        formulario = PagoServicioForm(data=request.POST, instance=pago_servicio)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Pago Modificado Con Exito")
            data ['form'] = formulario

    return render(request, 'core/pago_servicio/modificar_pago_serv.html', data)

def eliminar_pago_servicio(request, id):
    pago_servicio = PagoServicio.objects.get(id = id)
    pago_servicio.delete()

    return redirect(to='listado_pago_serv')

# P R O V E E D O R 


def agregar_proveedor(request):
    data = {
        'form': ProveedorForm(data=request.POST)
    }

    if request.method == 'POST':
        formulario = ProveedorForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Proveedor Agregada Con Exito")
        else:
            data["form"] = formulario
        
    return render(request,'core/proveedor/agregar_proveedor.html', data)
    

def listado_proveedor (request):
    proveedores = Proveedor.objects.all()

    data = {
        'proveedores': proveedores
    }

    return render(request, 'core/proveedor/listado_proveedor.html', data)

def modificar_proveedor(request, id):

    proveedor = Proveedor.objects.get(id = id)

    data = {
        'form': ProveedorForm(instance=proveedor)
    }
    if request.method == 'POST':
        formulario = ProveedorForm(data=request.POST, instance=proveedor)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Región Modificada Con Exito")
            data ['form'] = formulario

    return render(request, 'core/proveedor/modificar_proveedor.html', data)

def eliminar_proveedor(request, id):
    proveedor = Proveedor.objects.get(id = id)
    proveedor.delete()

    return redirect(to='listado_proveedor')

# T I P O  M A R C A S

def agregar_tipo_marca(request):
    data = {
        'form': TipoMarcaForm(data=request.POST)
    }

    if request.method == 'POST':
        formulario = TipoMarcaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Marca Agregada Con Exito")
        else:
            data["form"] = formulario
        
    return render(request,'core/tipo_marca/agregar_tipo_marca.html', data)
    

def listado_tipo_marca (request):
    tipo_marcas = TipoMarca.objects.all()

    data = {
        'tipo_marcas': tipo_marcas
    }

    return render(request, 'core/tipo_marca/listado_tipo_marca.html', data)

def modificar_tipo_marca(request, id):

    tipo_marca = TipoMarca.objects.get(id = id)

    data = {
        'form': TipoMarcaForm(instance=tipo_marca) 
    }
    if request.method == 'POST':
        formulario = TipoMarcaForm(data=request.POST, instance=tipo_marca)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Marca Modificada Con Exito")
            data ['form'] = formulario

    return render(request, 'core/tipo_marca/modificar_tipo_marca.html', data)

def eliminar_tipo_marca(request, id):
    tipo_marca = TipoMarca.objects.get(id = id)
    tipo_marca.delete()
    messages.success(request, "Marca Eliminada Con Exito")
    
    return redirect(to='listado_tipo_marca')

# P E D I D O  O R D E N

def agregar_ped_orden(request):
    data = {
        'form': PedidoOrdenForm(data=request.POST)
    }

    if request.method == 'POST':
        formulario = PedidoOrdenForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Pedido Agregado Con Exito")
        else:
            data["form"] = formulario
        
    return render(request,'core/pedido_orden/agregar_ped_orden.html', data)
    

def listado_ped_orden (request):
    ped_ordenes = PedidoOrden.objects.all()

    data = {
        'ped_ordenes': ped_ordenes
    }

    return render(request, 'core/pedido_orden/listado_ped_orden.html', data)

def modificar_ped_orden(request, id):

    ped_orden = PedidoOrden.objects.get(id = id)

    data = {
        'form': PedidoOrdenForm(instance=ped_orden) 
    }
    if request.method == 'POST':
        formulario = PedidoOrdenForm(data=request.POST, instance=ped_orden)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Pedido Modificado Con Exito")
            data ['form'] = formulario

    return render(request, 'core/pedido_orden/modificar_ped_orden.html', data)

def eliminar_ped_orden(request, id):
    ped_orden = PedidoOrden.objects.get(id = id)
    ped_orden.delete()
    messages.success(request, "Pedido Eliminado Con Exito")
    
    return redirect(to='listado_ped_orden')
