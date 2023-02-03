from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from blog_app.models import Posteos, Avatar

class PosteosFormulario(forms.Form):

    class Meta:
        model = Posteos
        fields =['titulo_posteo', 'subtitulo_posteo','posteo','autor']
        widgets = {
            'autor': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id':'usuario_id', 'type':'hidden'}),
            'titulo_posteo' : forms.TextInput(attrs={'class': 'form-control'}),
            'subtitulo_posteo' : forms.TextInput(attrs={'class': 'form-control'}),
            'posteo' : forms.TextInput(attrs={'class': 'form-control'}),

         }

class UserRegisterForm(UserCreationForm):
    # Esto es un ModelForm
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['last_name', 'first_name', 'username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['last_name', 'first_name', 'email']


class AvatarFormulario(forms.ModelForm):

    class Meta:
        model = Avatar
        fields = ['imagen']
 