from django.urls import path
from .views import *

urlpatterns = [
    path('add_order/', add_order, name = 'add_order'),
    path('index/', index, name = 'index')
]
