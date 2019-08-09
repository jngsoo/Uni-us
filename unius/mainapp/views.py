from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def hufspage(request):
    return render(request, 'hufspage.html')

def khpage(request):
    return render(request, 'khpage.html')

def test(request):
    return render(request, 'test.html')