"""
URL configuration for djangoApp1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from stock import views

urlpatterns = [
    path('',views.homePage),
    path('admin/', admin.site.urls),
    path('product/list',views.productList),
    path('product/add/simple',views.productAddSimple),
    path('product/add',views.productAdd),
    path('product/<int:id>/', views.productDetail),
    path('product/<int:id>/delete', views.productDelete),
]
