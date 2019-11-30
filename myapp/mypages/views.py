from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Product
from .forms import ProductForm

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

def product_handler(request, action = None, product_id = None):
    context = {}
    if action == 'list':
        context['products'] = Product.objects.all()
        template_name = 'products_list.html'
    elif action == 'create':
        new_data = request.POST
        if new_data:
            new_product = Product(
                name = new_data['product_name'],
                discount = False,
                price = new_data['product_price'],
                description = new_data['product_description']
            )
            new_product.save()
            return redirect('/products/list')
        context['is_edit'] = False
        template_name = 'products_form.html'
    elif action == 'view' and product_id:
        context['product'] = Product.objects.get(id=product_id)
        template_name = 'products_view.html'
    elif action == 'edit' and product_id:
        prod_data = request.GET
        product = Product.objects.get(id=product_id)
        if prod_data:
            product.name = prod_data['product_name']
            product.price = prod_data['product_price']
            product.description = prod_data['product_description']
            product.save()
        context['is_edit'] = True
        context['product'] = product
        template_name = 'products_form.html'
    elif action == 'delete' and product_id:
        product = Product.objects.get(id=product_id)
        product.delete()
        response = redirect('/products/list')
        return response
    else:
        return redirect('/products/list')

    return render(request, template_name, context)

    return HttpResponse('Test response' + action + ' ' + str(product_id))

def add_product(request):
    form = ProductForm()
    return render(request, 'product_form2.html', {'form': form})
