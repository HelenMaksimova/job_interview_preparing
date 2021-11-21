from django.urls import path
from productsapp.views import ProductsListView

app_name = 'productsapp'

urlpatterns = [
    path('', ProductsListView.as_view(), name='index'),
]
