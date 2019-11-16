from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.
def startpage(request):
    # products = [
    #     # { 'name': 'Lenovo', 'price': '500', 'discount': True },
    #     # { 'name': 'Acer', 'price': '400'},
    #     # { 'name': 'Asus', 'price': '600'},
    #     # { 'name': 'Samsung', 'price': '1500'},
    # ]
    products = Product.objects.all()
    print(products)

    context = {
        'name': 'Alexei',
        'surname': 'My surname',
        'products': products
    }
    return render(
        request,
        'main.html',
        context
    )

def starttest(request):
    return HttpResponse('Test response')