from django import forms
from .models import Contacto, Productos_w
from django.db.models import fields
from django.forms import widgets, ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .validators import MaxSizeFileValidator


class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = '__all__'


class ProductosForm(forms.ModelForm):

    nombre = forms.CharField(min_length=3, max_length=50)
    imagen = forms.ImageField(required=False, validators=[
                              MaxSizeFileValidator(max_file_size=16)])
    precio = forms.IntegerField(min_value=1, max_value=1500000)

    # def clean_nombre(self):
    #     nombre = self.cleaned_data['nombre']
    #     existe = Producto.objects.filter(nombre__iexact=nombre).exists()

    #     if existe:
    #         raise ValidationError('Este nombre ya existe')

    #     return nombre

    class Meta:
        model = Productos_w
        fields = '__all__'

        widgets = {
            'fecha_fabricacion': forms.SelectDateWidget()
        }


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password1', 'password2']
