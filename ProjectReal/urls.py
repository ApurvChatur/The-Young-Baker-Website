from django.urls import path
from .views import (home_view,
                    # about_view,
                    # intrests_view,
                    products_view,
                    product_view,
                    # contact_view,
                    )

app_name = 'ProjectReal'

urlpatterns = [
    path('', home_view, name='home-page'),
    path('products/', products_view, name='products-page'),
    path('product/<slug:slug>/', product_view, name='product-page'),
]
