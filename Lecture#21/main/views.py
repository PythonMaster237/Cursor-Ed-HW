from django.shortcuts import render
from .models import MenuItem, SliderItem


def main(request):
    menu_items = MenuItem.objects.all()
    slider_items = SliderItem.objects.all()
    return render(request, "index.html", {"menu_items": menu_items, "slider_items": slider_items})