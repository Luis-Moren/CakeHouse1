from django.contrib import admin
from .models import Tipo, Producto, Contacto
# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre","precio","nuevo","tipo"]
    list_editable = ["precio"]
    list_filter = ["tipo"]
admin.site.register(Tipo)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Contacto)
