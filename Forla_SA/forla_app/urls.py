from django.urls import path
from . import views

urlpatterns = [
    path("inicio/", views.inicio, name="inicio"),
    path("leer_productos/", views.leer_productos, name="leer_productos"),
    path("nosotros/", views.nosotros, name="nosotros"),
    path("productos_formulario/", views.productos_formulario, name="productos_formulario"),
    path("pedidos_formulario/", views.pedidos_formulario, name="pedidos_formulario"),
    path("clientes_formulario/", views.clientes_formulario, name="clientes_formulario"),
    path('buscador_precio/', views.buscador_precio, name='buscador_precio'),
    path("eliminar_producto/<str:producto_nombre>/", views.eliminar_producto, name="eliminar_producto"),
]
