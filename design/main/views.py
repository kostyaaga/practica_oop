from django.shortcuts import render

def index (request):
    return render(request, 'main/index.html')

def login (request):
    return render(request, 'main/login.html')

def singin (request):
    return render(request, 'main/singin.html')
