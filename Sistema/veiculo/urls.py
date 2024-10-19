from django.urls import path
from .views import listarveiuculos

urlpatterns = [
    path('', listarveiuculos, name='listarveiculos')
]
