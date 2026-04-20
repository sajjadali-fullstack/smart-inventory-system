from django.shortcuts import render, redirect
from testapp.models import Products
from testapp.serializers import ProductsSerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from testapp.forms import ProductForm


# Create your views / business logic here.


# Product View
def products_view(request):
    products_list = Products.objects.all()
    return render(request, 'testapp/index.html', {'products_list':products_list})

# Home View
def home_view(request):
    # Alag-alag category ka data filter karein
    clothes = Products.objects.filter(status='CL')
    electronics = Products.objects.filter(status='EL')
    furniture = Products.objects.filter(status='FU')
    other = Products.objects.filter(status='OT')
    
    context = {
        'clothes': clothes,
        'electronics': electronics,
        'furniture': furniture,
        'other':other,
    }
    return render(request, 'testapp/home.html', context)




@api_view(['GET'])
def product_api(request):
    category_code = request.GET.get('cat') # URL se category lega (?cat=CL)
    if category_code:
        products = Products.objects.filter(status=category_code)
    else:
        products = Products.objects.all()
    
    serializer = ProductsSerializers(products, many=True)
    return Response(serializer.data)


# Clothes API
@api_view(['GET'])
def clothes_api(request):
    clothes = Products.objects.filter(status='CL')
    serializer = ProductsSerializers(clothes, many=True)
    return Response(serializer.data)


# Electronic API
@api_view(['GET'])
def electronics_api(request):
    electronics = Products.objects.filter(status='EL')
    serializer = ProductsSerializers(electronics, many=True)
    return Response(serializer.data)


# Furniture API
@api_view(['GET'])
def furniture_api(request):
    furnitures = Products.objects.filter(status='FU')
    serialaizer = ProductsSerializers(furnitures, many=True)
    return Response(serialaizer.data)



# Other API
@api_view(['GET'])
def other_api(request):
    others = Products.objects.filter(status='OT')
    serializers = ProductsSerializers(others, many=True)
    return Response(serializers.data)

# Form 
def add_product_view(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/') # Save hone ke baad home page par bhej dega
    else:
        form = ProductForm()
    return render(request, 'testapp/add_product.html', {'form': form})