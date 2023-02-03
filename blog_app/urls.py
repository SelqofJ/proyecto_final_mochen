from django.urls import path
from blog_app.views import  bienvenidos

from blog_app.views import ( PosteosListView, PosteosCreateView, PosteosDetailView, PosteosUpdateView, PosteosDeleteView, ProfileUpdateView,    
    registro, login_view, agregar_avatar, CustomLogoutView, about
)

urlpatterns = [
    path('bienvenidos/', bienvenidos),
    path('pages/', PosteosListView.as_view(), name="listar_posteos"),
    path('blog_app/<int:pk>/', PosteosDetailView.as_view(), name="ver_posteo"),
    path('crear-posteo/', PosteosCreateView.as_view(), name="crear_posteo"),
    path('editar-posteo/<int:pk>/', PosteosUpdateView.as_view(), name="editar_posteo"),
    path('eliminar-posteo/<int:pk>/', PosteosDeleteView.as_view(), name="eliminar_posteo"),
    path('accounts/signup/', registro, name="registro"),
    path('account/login/', login_view, name="login"),
    path('logout/', CustomLogoutView.as_view(), name="logout"),
    path('accounts/profile/', ProfileUpdateView.as_view(), name="editar_perfil"),
    path('agregar-avatar/', agregar_avatar, name="agregar_avatar"),
    path('acercaDeMi/', about, name='acerca_de_mi'),
  

]
