from django.db import models


# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=800)
    precio = models.DecimalField(max_digits=10, decimal_places=2)


class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=800)


class Pedido(models.Model):
    detalle = models.CharField(max_length=100000)
    precio = models.DecimalField(max_digits=10, decimal_places=2)


class Cliente(models.Model):
    nombre = models.CharField(max_length=200)
    email = models.EmailField()
    pedidos_pasados = models.IntegerField()
