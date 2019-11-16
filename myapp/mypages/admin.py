from django.contrib import admin
from . import models as m

# Register your models here.
admin.site.register(m.Product)

# python manage.py migrate
# python manage.py createsuperuser
