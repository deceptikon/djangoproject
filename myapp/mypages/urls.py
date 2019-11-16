from django.urls import path

from . import views as v

urlpatterns = [
    path('', v.startpage, name='index'),
    path('test', v.starttest, name='test')
]
