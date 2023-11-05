from django import forms


class ProductosFormulario(forms.Form):
    nombre = forms.CharField()
    descripcion = forms.CharField()
    precio = forms.DecimalField()


class PedidosFormulario(forms.Form):
    detalle = forms.CharField()
    precio = forms.DecimalField()


class ClientesFormulario(forms.Form):
    nombre = forms.CharField()
    email = forms.EmailField()
    pedidos_pasados = forms.IntegerField()
