from django.shortcuts import render, redirect, get_object_or_404
from .models import Categorias_w, Productos_w
from .forms import ContactoForm, ProductosForm, CustomUserCreationForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from rest_framework import viewsets
from .serializers import ProductosSerializer, CategoriasSerializer

# Create your views here.


def index(request):
    return render(request, 'app/index.html')


def productos(request):

    productos = Productos_w.objects.all()

    data = {
        'productos': productos
    }

    return render(request, 'app/productos.html', data)


def contacto(request):

    data = {
        'form': ContactoForm()
    }

    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Mensaje enviado')
        else:
            data['form'] = formulario

    return render(request, 'app/contacto.html', data)


def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(
                username=formulario.cleaned_data['username'], password=formulario.cleaned_data['password1'])
            login(request, user)
            messages.success(request, 'Te haz registrado correctamente')
            return redirect(to='index')
        else:
            data['form'] = formulario

    return render(request, 'registration/registro.html', data)


@permission_required('myapp.add_productos_w')
def agregar_producto(request):
    data = {
        'form': ProductosForm()
    }

    if request.method == 'POST':
        formulario = ProductosForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Producto registrado')
        else:
            data['form'] = formulario

    return render(request, 'app/productos/agregar.html', data)


@permission_required('myapp.view_productos_w')
def listar_producto(request):
    productos = Productos_w.objects.all()

    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(productos, 5)
        productos = paginator.page(page)

    except:
        raise Http404

    data = {
        'entity': productos,
        'paginator': paginator
    }
    return render(request, 'app/productos/listar.html', data)


@permission_required('myapp.change_productos_w')
def modificar_producto(request, id):
    producto = get_object_or_404(Productos_w, id=id)

    data = {
        'form': ProductosForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = ProductosForm(
            data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Editado correctamente')
            return redirect(to='listar_producto')
        else:
            data['form'] = formulario

    return render(request, 'app/productos/modificar.html', data)


@permission_required('myapp.delete_productos_w')
def eliminar_producto(request, id):
    producto = get_object_or_404(Productos_w, id=id)
    producto.delete()
    messages.success(request, 'Eliminado correctamente')
    return redirect(to='listar_producto')


class ProductosViewset(viewsets.ModelViewSet):
    queryset = Productos_w.objects.all()
    serializer_class = ProductosSerializer

    def get_queryset(self):
        productos = Productos_w.objects.all()

        nombre = self.request.GET.get('nombre')

        if nombre:
            productos = productos.filter(nombre__contains=nombre)

        else:
            return productos


class CategoriasViewset(viewsets.ModelViewSet):
    queryset = Categorias_w.objects.all()
    serializer_class = CategoriasSerializer
