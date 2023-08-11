from django.urls import path
from book.views import login, listar


urlpatterns = [
    path('', login),
    path('listar/', listar),
]
