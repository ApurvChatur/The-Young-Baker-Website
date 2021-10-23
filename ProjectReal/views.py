from django.shortcuts import render, get_object_or_404, get_list_or_404
from ProjectDesign.models import (Home,
                                  Product,
                                  )


def home_view(request):
    home = get_object_or_404(Home, slug='the-young-baker')
    featured_products = get_list_or_404(Product, tag='featured')

    template_name = 'ProjectReal/home-page.html'
    context = {
        'title': 'Home',
        'home': home,
        'featured_products': featured_products
    }
    return render(request, template_name, context)


def products_view(request):
    # categories = get_list_or_404(Category)
    products = Product.objects.all()

    template_name = 'ProjectReal/products-page.html'
    context = {
        'title': 'Products',
        # 'categories': categories,
        'products': products,
    }
    return render(request, template_name, context)


def product_view(request, slug):
    product = get_object_or_404(Product, slug=slug)

    template_name = 'ProjectReal/product-page.html'
    context = {
        'title': product.title,
        'product': product,
    }
    return render(request, template_name, context)



