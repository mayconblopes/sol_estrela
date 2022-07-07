from django.urls import path
from loja import views

urlpatterns = [
    path('', views.index, name='index'),

]