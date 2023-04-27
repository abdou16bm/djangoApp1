from django.shortcuts import render, redirect

from .form import producAddForm
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


def productDetail(request,id):
    product = Product.objects.get(id=id)
    context = {
        'id' : id,
        'product':product
    }
    return render(request,'productDetail.html',context)


def productDelete(request,id):
    product = Product.objects.get(id=id)
    product.delete()

    return redirect('/product/list')


def productAdd(request):

    if request.method == 'POST':
        productForm = producAddForm(request.POST)
        productForm.save()
        return redirect('/product/list')
    else :
        productForm = producAddForm()

    return render(request,
                  'productAdd.html',
                  {'form': productForm})

