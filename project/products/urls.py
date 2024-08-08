from django.urls import path

from products.views import ProductsListView

app_name = 'products'

urlpatterns = [
    path('products/', ProductsListView.as_view(), name='products_list')
]
