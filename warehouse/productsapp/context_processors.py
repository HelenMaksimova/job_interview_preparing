from productsapp.models import Category


def category_list(request):
    # return {'category_list': Category.objects.prefetch_related('products').all()} - в данной реализации получится
    # на один запрос больше, но если в дальнейшем потребуется обращаться к связанному полю, то нужен будет этот вариант
    return {'category_list': Category.objects.all()}
