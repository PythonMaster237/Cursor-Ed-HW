from django.urls import path
from .views import category_page, product_order_by_price

urlpatterns = [
    path("category/<slug>", category_page, name="category_page"),
    path("category/<slug>/<value>", product_order_by_price, name="sorted_products")
]
