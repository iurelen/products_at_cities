from django.urls import path

from products.views import ProductsListView

urlpatterns = [
    path('products/', ProductsListView.as_view(), name='products_list')
]
