from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import ProductSerializer, CartSerializer
from products.models import Product, Category


class ProductView(APIView):

    def get(self, request, format=None):
        products = Product.objects.all()
        serialized_products = ProductSerializer(products, many=True)
        return Response(serialized_products.data)



class ProductSingleView(APIView):

    def get_object(self, id):
        try:
            product = Product.objects.get(id=id)
            return product
        except Product.DoesNotExist:
            return None


    def get(self, request, id):
        product = self.get_object(id)
        serialized_product = ProductSerializer(product)
        return Response(serialized_product.data)


    def put(self, request, id):
        product = self.get_object(id)
        if product is not None:
            serialized_product = ProductSerializer(instance=product, data=request.data)
            if serialized_product.is_valid():
                serialized_product.save()
                return Response(serialized_product.data)
        return Response(None, status.HTTP_400_BAD_REQUEST)


    def delete(self, request, id):
        product = self.get_object(id)
        if product is not None:
            product.delete()
            return Response(None, status.HTTP_204_NO_CONTENT)
        return Response(None, status.HTTP_400_BAD_REQUEST)


class CategoryProductsView(APIView):
    def get_object(self, id):
        try:
            category = Category.objects.get(id=id)
            return category
        except Category.DoesNotExist:
            return None

    def get(self, request, category_id):
        category = self.get_object(category_id)
        if category is not None:
            if category.products:
                products = ProductSerializer(category.products, many=True)
                return Response(products.data)
        return Response(None, status.HTTP_404_NOT_FOUND)


class CartView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        cart = request.session.get('cart', {})
        return Response(cart, status.HTTP_200_OK)

    def post(self, request):
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            product_id = serializer.validated_data['id']
            product_obj = Product.objects.get(id=product_id)
            is_product_already_exist = False

            cart = request.session.get("cart", [])

            for item in cart:
                if product_id == item['id']:
                    item['quantity'] += serializer.validated_data['quantity']
                    item['price'] = product_obj.price * item['quantity']
                    is_product_already_exist = True
                    break

            if not is_product_already_exist:
                serialized_data = serializer.data
                serialized_data["price"] = product_obj.price * serialized_data["quantity"]
                cart.append(serialized_data)

            request.session["cart"] = cart

            return Response(cart, status=200)
        else:
            return Response(serializer.errors, status=400)

    def delete(self, request):
        request.session["cart"] = []
        return Response(request.session['cart'], status=200)
