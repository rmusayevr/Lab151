from rest_framework.views import APIView
from order.models import Basket, BasketItem
from order.api.serializers import BasketSerializer, BasketItemSerializer
from products.models import ProductVersion
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

class BasketApiView(APIView):
    serializer_class = BasketSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get', 'post', 'patch', 'delete']

    def get(self, request, *args, **kwargs):    
        obj, created = Basket.objects.get_or_create(user = request.user)
        serializer = self.serializer_class(obj)    
        return Response(serializer.data, status = status.HTTP_200_OK)    
    
    def post(self, request, *args, **kwargs):
        quantity = request.data.get('quantity')
        product_id = request.data.get('product')
        product = ProductVersion.objects.filter(pk=product_id).first()
        if product:
            for_basket, created = BasketItem.objects.get_or_create(product = product, user = request.user)
            basket2 = BasketItem.objects.get(product = product, user = request.user)
            basket2.quantity += quantity
            basket2.save()
            basket1, created = Basket.objects.get_or_create(user = request.user)
            basket1.items.add(basket2) 
            arr = []
            for item in basket1.items.all():
                serializer = BasketItemSerializer(item)
                arr.append(serializer.data)
            message = {'success': True, 'message' : 'Product added to your card.'}
            return Response(arr, status = status.HTTP_201_CREATED)
        message = {'success' : False, 'message': 'You have to log in to add product your basket!'}
        return Response(message, status = status.HTTP_401_UNAUTHORIZED)

    def patch(self, request, *args, **kwargs):
        ProductDOWN = request.data.get('productDown')
        ProductUP = request.data.get('productUp')
        if ProductDOWN:
            user_basket = BasketItem.objects.get(product=ProductDOWN, user = request.user)
            user_basket.quantity -= 1
            user_basket.save()
            message = {'success': True, 'message' : 'Product has been decreased.'}
            return Response(message, status = status.HTTP_200_OK)
        elif ProductUP:
            user_basket = BasketItem.objects.get(product=ProductUP, user = request.user)
            user_basket.quantity += 1
            user_basket.save()
            message = {'success': True, 'message' : 'Product has been increased.'}
            return Response(message, status = status.HTTP_200_OK)
        

    def delete(self, request, *args, **kwargs):
        ProductID = request.data.get('product')
        if ProductID:
            user_basket = BasketItem.objects.get(product = ProductID, user = request.user)
            user_basket.delete()
            message = {'success': True, 'message' : 'Product has been deleted.'}
            return Response(message, status = status.HTTP_200_OK)