from .models import Producto, Cliente, Categoria, Pedido
from .forms import ProductosFormulario, ClientesFormulario, PedidosFormulario
from django.shortcuts import render, get_object_or_404, redirect, HttpResponse

# Create your views here.


def inicio(request):
    return render(request, "inicio.html")


def nosotros(request):
    return render(request, "nosotros.html")


def productos_formulario(request):
    if request.method == "POST":
        mi_formulario = ProductosFormulario(request.POST)  # Aca llega la info del HTML

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            producto = Producto(nombre=informacion["nombre"], descripcion=informacion["descripcion"],
                                precio=informacion["precio"])
            producto.save()
            return render(request, "inicio.html")
    else:
        mi_formulario = ProductosFormulario()
        return render(request, "productos_formulario.html", {"mi_formulario": mi_formulario})


def clientes_formulario(request):
    if request.method == "POST":
        mi_formulario = ClientesFormulario(request.POST)  # Aca llega la info del HTML

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            cliente = Cliente(nombre=informacion["nombre"], email=informacion["email"],
                              pedidos_pasados=informacion["pedidos_pasados"])
            cliente.save()
            return render(request, "inicio.html")
    else:
        mi_formulario = ClientesFormulario()
        return render(request, "clientes_formulario.html", {"mi_formulario": mi_formulario})


def pedidos_formulario(request):
    if request.method == "POST":
        mi_formulario = PedidosFormulario(request.POST)  # Aca llega la info del HTML

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            pedido = Pedido(detalle=informacion["detalle"], precio=informacion["precio"])
            pedido.save()
            return render(request, "inicio.html")
    else:
        mi_formulario = PedidosFormulario()
    return render(request, "pedidos_formulario.html", {"mi_formulario": mi_formulario})


def buscador_precio(request):
    nombre_producto = request.GET.get('nombre', '')
    precio_producto = None

    if nombre_producto:
        try:
            producto = Producto.objects.get(nombre=nombre_producto)
            precio_producto = producto.precio
        except Producto.DoesNotExist:
            precio_producto = "Producto no encontrado"

    formulario = ProductosFormulario()

    return render(request, 'buscador_precio.html',
                  {'formulario': formulario, 'nombre_producto': nombre_producto, 'precio_producto': precio_producto})


def leer_productos(request):
    productos = Producto.objects.all()
    return render(request, "leer_productos.html", {"productos": productos})


def eliminar_producto(request, producto_nombre):
    producto = get_object_or_404(Producto, nombre=producto_nombre)

    if request.method == 'POST':
        # Lógica para eliminar el producto
        producto.delete()
        return redirect('leer_productos')
    else:
        # Muestra una página de confirmación si es una solicitud GET
        return render(request, 'confirmar_eliminar_producto.html', {'producto': producto})

