from django.shortcuts import render
# from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


def login(request):
    return render(request, 'login/login.html')

@csrf_exempt
def listar(request):
    return render(request, 'listar/listar.html')

@csrf_exempt
def cadastrar(request):
    return render(request, 'cadastrar/cadastrar.html')




