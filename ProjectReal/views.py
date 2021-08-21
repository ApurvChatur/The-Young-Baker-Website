from django.shortcuts import render, get_object_or_404, get_list_or_404
from ProjectDesign.models import (Home,
                                  Product,
                                  )


def home_view(request):
    home = get_object_or_404(Home, slug='the-young-baker')
    products = get_list_or_404(Product)

    template_name = 'ProjectReal/a-home-page.html'
    context = {
        'home': home,
        'products': products
    }
    return render(request, template_name, context)

