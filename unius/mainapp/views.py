from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def hufspage(request):
    return render(request, 'hufspage.html')

def khpage(request):
    return render(request, 'khpage.html')

def hufs_recent(request):
    return render(request, 'hufs_recent.html')

def hufs_hot(request):
    return render(request, 'hufs_hot.html')

def hufs_battle(request):
    return render(request, 'hufs_battle.html')

def kh_recent(request):
    return render(request, 'kh_recent.html')

def kh_hot(request):
    return render(request, 'kh_hot.html')

def kh_battle(request):
    return render(request, 'kh_battle.html')