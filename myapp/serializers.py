from django.db.models.query import QuerySet
from .models import Categorias_w, Productos_w
from rest_framework import fields, serializers


class CategoriasSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categorias_w
        fields = '__all__'


class ProductosSerializer(serializers.ModelSerializer):

    nombre_categoria = serializers.CharField(
        read_only=True, source='categoria.nombre')
    categoria = CategoriasSerializer(read_only=True)
    categoria_id = serializers.PrimaryKeyRelatedField(
        queryset=Categorias_w.objects.all(), source='categoria')
    nombre = serializers.CharField(required=True, min_length=3)

    # def validate_nombre(self, value):
    #     existe = Producto.objects.filter(nombre=value).exists()

    #     if existe:
    #         raise serializers.ValidationError('Este producto ya existe')

    #     else:
    #         return value

    class Meta:
        model = Productos_w
        fields = '__all__'
        #exclude = ['']
