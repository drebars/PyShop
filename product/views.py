from django.shortcuts import render

# Create your views here.
from product.models import Category, Product


def home_page(request):
    categories = Category.objects.all()
    print(categories)
    return render(request, 'products/home.html', {'categories': categories})




def product_list(request, slug):
    products = Product.objects.filter(category__slug=slug)
    return render(request, 'products/list.html', locals())


def product_detail(request,id):
    product = Product.objects.filter(id=id)
    return render(request)



# TODO: select * from category class.objects.all(), locals() , fishki v html, prochitat' knigi