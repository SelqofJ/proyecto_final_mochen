from datetime import datetime
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth import login, authenticate
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from blog_app.forms import UserRegisterForm, UserUpdateForm, AvatarFormulario


from blog_app.models import Posteos



#  INICIO/BIENVENIDA
def bienvenidos (request):
    return HttpResponse(f'Tu LifeBlog  Fecha: {datetime.now().date()}' )


def inicio(request):
    return render(
        request=request,
        template_name='blog_app/inicio.html',
    )
#POSTEOS

class PosteosListView (ListView):
    model = Posteos
    template_name = "blog_app/listar_posteos.html"
    


class PosteosCreateView (LoginRequiredMixin, CreateView):
    model = Posteos
    fields = ['titulo_posteo', 'subtitulo_posteo', 'posteo', 'autor']
    success_url = reverse_lazy('listar_posteos')
    template_name = "blog_app/form_posteo.html"
        
        
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super(PosteosCreateView, self).form_valid(form)


class PosteosUpdateView(LoginRequiredMixin,UpdateView):
    model = Posteos
    fields = ['titulo_posteo', 'subtitulo_posteo','posteo','autor']
    success_url = reverse_lazy('listar_posteos')
    template_name = "blog_app/form_posteo.html"


class PosteosDetailView(DetailView):
    model = Posteos
    success_url = reverse_lazy('listar_posteos')
    template_name = "blog_app/posteo_detail.html"



class PosteosDeleteView(LoginRequiredMixin, DeleteView):
    model = Posteos
    success_url = reverse_lazy('listar_posteos')
    template_name = "blog_app/confirm_eliminacion_posteo.html"
    



#LOGIN/REGISTER USER/LOGOUT

def registro(request):
    if request.method == "POST":
        formulario = UserRegisterForm(request.POST)

        if formulario.is_valid():
            formulario.save()  # Esto lo puedo usar porque es un model form
            url_exitosa = reverse('inicio')
            return redirect(url_exitosa)
    else:  # GET
        formulario = UserRegisterForm()
    return render(
        request=request,
        template_name='blog_app/registro.html',
        context={'form': formulario},
    )


def login_view(request):
    next_url = request.GET.get('next')
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            data = form.cleaned_data
            usuario = data.get('username')
            password = data.get('password')
            user = authenticate(username=usuario, password=password)
            # user puede ser un usuario o None
            if user:
                login(request=request, user=user)
                if next_url:
                    return redirect(next_url)
                url_exitosa = reverse('inicio')
                return redirect(url_exitosa)
    else:  # GET
        form = AuthenticationForm()
    return render(
        request=request,
        template_name='blog_app/login.html',
        context={'form': form},
    )


class CustomLogoutView(LogoutView):
    template_name = 'blog_app/logout.html'


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    success_url = reverse_lazy('inicio')
    template_name = 'blog_app/form_perfil.html'

    def get_object(self, queryset=None):
        return self.request.user


def agregar_avatar(request):
    if request.method == "POST":
        formulario = AvatarFormulario(request.POST, request.FILES) 

        if formulario.is_valid():
            avatar = formulario.save()
            avatar.user = request.user
            avatar.save()
            url_exitosa = reverse('inicio')
            return redirect(url_exitosa)
    else:  # GET
        formulario = AvatarFormulario()
    return render(
        request=request,
        template_name='blog_app/form_avatar.html',
        context={'form': formulario},
    )

def about(request):
    return render(request, 'blog_app/acerca_de_mi.html')

