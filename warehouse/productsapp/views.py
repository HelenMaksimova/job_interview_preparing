from django.views.generic import ListView
from productsapp.models import Product


class ProductsListView(ListView):
    model = Product
    extra_context = {'title': 'Warehouse - главная'}
    queryset = Product.objects.all().select_related()
    template_name = 'goods_list.html'
