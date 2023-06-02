from django.shortcuts import render
from .models import Category, Product


def category_page(request, slug):
    category = Category.objects.get(slug=slug)
    return render(request, "category.html", {"category": category, "products": category.products.all()})


def product_page(request, title, slug):
    product = Product.objects.get(title=title)
    images = product.productimage_set.get()
    image = images.image
    is_main = images.is_main
    return render(request, "product_page.html", {"product": product, "image": image, "is_main": is_main})
