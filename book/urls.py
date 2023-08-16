from django.urls import path
from book import views
from book.views import login, listar, cadastrar


urlpatterns = [
    path('', views.login),
    path('listar/', views.listar),
    path('cadastrar/', views.cadastrar),
]
