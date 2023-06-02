from django.shortcuts import render
from .models import Category


def category_page(request, slug):
    category = Category.objects.get(slug=slug)
    return render(request, "category.html", {"category": category, "products": category.products.all()})


def product_order_by_price(request, value, slug):
    if value in ['price', '-price', 'create_at', '-create_at']:
        category = Category.objects.get(slug=slug)
        order_by_value = category.products.all().order_by(value)
        return render(request, "product_sort_by_value.html", {"category": category, "order_by_value": order_by_value})
