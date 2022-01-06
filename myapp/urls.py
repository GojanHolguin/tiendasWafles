from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('producto', views.ProductosViewset)
router.register('categoria', views.CategoriasViewset)

# localhost:8000/api/producto/


urlpatterns = [
    path('', views.index, name='index'),
    path('productos/', views.productos, name='productos'),
    path('contacto/', views.contacto, name='contacto'),
    path('registro/', views.registro, name='registro'),
    path('agregar-producto/', views.agregar_producto, name='agregar_producto'),
    path('listar-producto/', views.listar_producto, name='listar_producto'),
    path('modificar-producto/<id>/',
         views.modificar_producto, name='modificar_producto'),
    path('eliminar-producto/<id>/',
         views.eliminar_producto, name='eliminar_producto'),
    path('api/', include(router.urls)),

]
