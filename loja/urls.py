from django.urls import path
from loja import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detalhes/<int:pk>', views.product_details, name='product_details'),
    path('girls', views.girls_products, name='girls_products'),
    path('boys', views.boys_products, name='boys_products'),

]