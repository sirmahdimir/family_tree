from django.shortcuts import render, HttpResponse

def home(request):
    return render(request, 'home_page/home.html')
