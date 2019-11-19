from django.urls import path

from . import views as v

# products/create
# products/list
# products/view/5
# products/edit/5
# products/delete/5

# CRUD - Create Read Update Delete

urlpatterns = [
    path('', v.startpage, name='index'),
    path('products', v.product_handler, name='products'),
    path('products/<str:action>', v.product_handler, name='products'),
    path('products/<str:action>/<int:product_id>', v.product_handler, name='products'),
    path('test', v.starttest, name='test')
]
