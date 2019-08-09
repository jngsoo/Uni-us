"""unius URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import mainapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainapp.views.home, name='home'),
    path('hufspage/', mainapp.views.hufspage, name="hufspage"),
    path('khpage/', mainapp.views.khpage, name="khpage"),
    path('hufs_recent/', mainapp.views.hufs_recent, name="hufs_recent"),
    path('hufs_hot/', mainapp.views.hufs_hot, name="hufs_hot"),
    path('hufs_battle/', mainapp.views.hufs_battle, name="hufs_battle"),
    path('kh_recent/', mainapp.views.kh_recent, name="kh_recent"),
    path('kh_hot/', mainapp.views.kh_hot, name="kh_hot"),
    path('kh_battle/', mainapp.views.kh_battle, name="kh_battle"),
]
