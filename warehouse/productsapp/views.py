from django.views.generic import ListView
from productsapp.models import Product, Category


class ProductsListView(ListView):
    model = Product
    extra_context = {'title': 'Warehouse - главная'}
    template_name = 'goods_list.html'

    def get_queryset(self):
        category_pk = self.kwargs.get('category_pk')
        queryset = Product.objects.select_related('vendor_name').prefetch_related('categories')
        return queryset.all() if not category_pk else queryset.filter(categories__id__contains=category_pk)
