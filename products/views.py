from django.shortcuts import render
from products.models import Product

# Create your views here.
def index(request, index = 1):
    products =list(list_split_by(Product.objects.all(), 10));
    context = {
        'current_index' : index,
        'products': products[index - 1],
        'pages_count' : [None] * len(products),
        'pages_count_int' : len(products),
    }

    return render(request, 'products/products_page.html', context);


def list_split_by(listA, n):
    for x in range(0, len(listA), n):
        every_chunk = listA[x: n+x]
        yield every_chunk

def ProductPage(request, name):
    product =Product.objects.filter(name=name);
    if product is None:
        return render(request, 'blog/index.html');
    else:
        return render(request, 'home/index.html')
