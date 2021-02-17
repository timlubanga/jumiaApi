from django.shortcuts import render
from rest_framework import generics
from Order.serializer import OrderItemSerializer, OrderSerializer
from rest_framework.permissions import IsAuthenticated
from Order.models import OrderItem, Order
from Product.models import Product
from rest_framework.authentication import TokenAuthentication
from rest_framework import serializers
from django.shortcuts import get_object_or_404
# Create your views here.


class AddProductToCartView(generics.CreateAPIView):
    serializer_class = OrderItemSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = OrderItem.objects.all()

    def perform_create(self, serializer):
        order, created = Order.objects.get_or_create(
            customer=self.request.user.customer)
        productId = self.kwargs.get("productId", None)

        if productId:
            quantity = 1
            product = Product.objects.get(id=productId)
            serializer.save(product=product, order=order,
                            quantity=quantity)


class EditOrderItemView(generics.UpdateAPIView):
    serializer_class = OrderItemSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = OrderItem.objects.all()

    lookup_url_kwarg = "orderitemId"

    def perform_update(self, serializer):

        action = self.kwargs.get('action', None)
        print(action)
        paramid = self.kwargs.get("orderitemId", None)
        if paramid:
            orderitem = get_object_or_404(OrderItem, id=paramid)
            quantity = 0
            if action == "add":
                quantity = orderitem.quantity+1

            elif action == "remove":
                if orderitem.quantity > 0:
                    quantity = orderitem.quantity-1
            else:
                raise serializers.ValidationError(
                    {"message": "please include either remove or add"})
            serializer.save(quantity=quantity)


class OrderListView(generics.ListAPIView):
    serializer_class = OrderSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.all()
