from django.contrib import admin
from .models import Categorias_w, Productos_w, Contacto
from .forms import ProductosForm

# Register your models here.


class ProductosAdmin(admin.ModelAdmin):

    list_display = ['nombre', 'precio', 'categoria']
    list_editable = ['precio']
    search_fields = ['nombre']
    list_filter = ['categoria']
    list_per_page = 5
    #form = ProductoForm


admin.site.register(Categorias_w)
admin.site.register(Productos_w, ProductosAdmin)
admin.site.register(Contacto)
