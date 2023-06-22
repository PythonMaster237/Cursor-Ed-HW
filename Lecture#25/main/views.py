import asyncio
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout

from main.telegram_bot import send_telegram_message
from .models import Order, OrderItems
from .forms import NewUserForm
from products.models import Product


def main(request):
    products = Product.objects.filter(show_on_main_page=True)
    return render(request, "index.html", {"products": products})


def add_to_cart(request, product_id: int):
    product_obj = Product.objects.get(id=product_id)
    is_product_already_exist = False
    if not request.session.get("cart"):
        request.session["cart"] = []
    else:
        for product in request.session.get("cart", []):
            if product_id == product["id"]:
                product["quantity"] = product["quantity"] + 1
                product["price"] = product_obj.price * product["quantity"]
                is_product_already_exist = True

    if not is_product_already_exist:
        request.session["cart"].append({"id": product_id, "quantity": 1, "price": product_obj.price})
    request.session.modified = True
    return HttpResponseRedirect("/")


def cart(request):
    cart_products = []
    for cart_item in request.session.get("cart", []):
        product = Product.objects.get(id=cart_item["id"])
        product.quantity = cart_item["quantity"]
        product.total_price = cart_item["price"]
        cart_products.append(product)
    return render(request, "cart.html", {"cart_products": cart_products})


def checkout(request):
    total_price = 0
    for cart_item in request.session.get("cart", []):
        total_price = total_price + cart_item["price"]
    return render(request, "checkout.html", {"total_price": total_price})


def checkout_proceed(request):
    if request.method == "POST":
        order = Order()
        order.first_name = request.POST.get("first_name")
        order.last_name = request.POST.get("last_name")
        order.email = request.POST.get("email")
        order.address = request.POST.get("address")
        order.address2 = request.POST.get("address2")
        order.country = request.POST.get("country")
        order.city = request.POST.get("city")
        order.postcode = request.POST.get("postcode")
        total = 0
        for item in request.session.get("cart", []):
            total = total + item["price"]
        order.total_price = total
        order.save()
        message_bot = ""
        for item in request.session.get("cart", []):
            order_item = OrderItems()
            order_item.product_id = item["id"]
            order_item.order_id = order.id
            order_item.price = item["price"]
            order_item.quantity = item["quantity"]
            order_item.save()
            message_bot += f"Product: {order_item.product.title};\t" \
                           f"Quantity: {order_item.quantity};\t" \
                           f"Total: {order_item.price};\t \n\n"
    message_bot += f"Total price: {total}\n" \
                   f"Name: \t {order.first_name} {order.last_name}\n" \
                   f"Address: {order.country} | {order.city} | {order.address}\n" \
                   f"Order number: {order.id}"
    asyncio.run(send_telegram_message(message_bot))
    return HttpResponseRedirect("/")


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect("/")
    form = NewUserForm()
    return render(request, "sign-up.html", {"form": form})


def sign_in(request):
    if request.method == "POST":
        user = authenticate(username=request.POST.get("username"), password=request.POST.get("password"))
        if user:
            login(request, user)
        return HttpResponseRedirect('/')
    return render(request, "sign-in.html")


def sign_out(request):
    logout(request)
    return HttpResponseRedirect("/")