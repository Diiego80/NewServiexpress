from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
# Extra
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from rest_framework import viewsets
from django.contrib import messages
from django.http import Http404

# Create your views here.

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

#Ingreso de Django Admin
def registro(request):
    dataRegistro = {
        'form': UsuarioForm()
    }
    if request.method == 'POST':
        formularioContacto = UsuarioForm(data=request.POST)
        if formularioContacto.is_valid():
            formularioContacto.save()
            dataRegistro["mensaje"] = "Usuario Guardado Correctamente"
        else:
            dataRegistro["form"] = formularioContacto

    return render(request, 'registration/registro.html', dataRegistro)


def registro_clientes(request):
    return render(request, 'core/registro_clientes.html')


def registro_productos(request):
    return render(request, 'core/registro_productos.html')


def formulario_producto(request):
    return render(request, 'core/formularios/formulario_productos.html')


def formulario_clientes(request):
    return render(request, 'core/cliente/formulario_clientes.html')

def formulario_servicios(request):
    return render(request, 'core/servicio/formulario_servicio.html')


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

def listado_producto (request):
    productos = Producto.objects.all()
    
    data = {
        'productos': productos
    }

    return render(request, 'core/producto/listado_producto.html', data)

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

def eliminar_producto (request, id):
    producto = Producto.objects.get(id = id)
    producto.delete()
    messages.success(request, "Producto Eliminado Correctamente")

    return redirect(to='listado_producto')

# E M P L E A D O

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

def listado_empleado (request):
    empleados = Empleado.objects.all()

    data = {
        'empleados': empleados
    }

    return render(request, 'core/empleado/listado_empleado.html', data)

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

def eliminar_empleado(request, id):
    empleado = Empleado.objects.get(id = id)
    empleado.delete()
    messages.success(request, "Empleado Eliminado Correctamente")

    return redirect(to="listado_empleado")

# S E R V I C I O S 

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

def eliminar_servicio(request, id):
    servicio = Servicio.objects.get(id = id)
    servicio.delete()
    messages.success(request, "Servicio Eliminado Correctamente")

    return redirect(to='listado_servicio')

# C O M U N A

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
    

def listado_comuna (request):
    comunas = Comuna.objects.all()

    data = {
        'comunas': comunas
    }

    return render(request, 'core/comuna/listado_comuna.html', data)

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

def eliminar_comuna(request, id):
    comuna = Comuna.objects.get(id = id)
    comuna.delete()

    return redirect(to='listado_comuna')

# C I U D A D

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

def listado_ciudad (request):
    ciudades = Ciudad.objects.all()

    data = {
        'ciudades': ciudades
    }

    return render(request, 'core/ciudad/listado_ciudad.html', data)

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

def eliminar_ciudad(request, id):
    ciudad = Ciudad.objects.get(id = id)
    ciudad.delete()

    return redirect(to='listado_ciudad')
 
# D E T A L L E  S E R V I C I O

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

def listado_det_serv(request):
    det_serv = DetalleServicio.objects.all()

    data = {
        'det_serv': det_serv
    }

    return render(request, 'core/detalle_servicio/listado_det_serv.html', data)

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

def eliminar_det_serv(request, id):
    det_ser = DetalleServicio.objects.get(id = id)
    det_ser.delete()

    return redirect(to='listado_det_serv')

# F A C T U R A  Y  B O L E T A

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

def listado_cliente (request):
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
