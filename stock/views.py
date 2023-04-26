from django.shortcuts import render, redirect
from .models import Product

# Create your views here.

def homePage(request):
    return render(request,'home.html')

def productList(request):
    products = Product.objects.all()

    return render(request,'productList.html',{'productData':products})


def productAddSimple(request):

    print('la methode utiliser :',request.method)
    print('les informations posté : ', request.POST)

    if request.method == 'POST':
        print('POST')
        if 'showBtn' not in request.POST:
            print('addBtn')
            product = Product()
            product.name = request.POST['name']
            product.category = request.POST['category']
            product.price = request.POST['price']
            product.stock_qt = request.POST['stock_qt']

            product.save()
            return redirect('/product/list')
        else :
           print('show')
    else :
        print('other GET')


    return render(request,'productAddSimple.html')
