from django.contrib import admin
from .models import Producto, Pedido, Cliente


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion", "precio")
    list_filter = ("nombre", "precio")
    search_fields = ("nombre", "precio")


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ("detalle", "precio")
    list_filter = ("detalle", "precio")
    search_fields = ("detalle", "precio")


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nombre", "email", "pedidos_pasados")
    list_filter = ("nombre", "email")
    search_fields = ("nombre", "email")
