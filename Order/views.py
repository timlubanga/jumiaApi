from django.shortcuts import render
from rest_framework import generics
from Order.serializer import OrderItemSerializer, OrderSerializer
from rest_framework.permissions import IsAuthenticated
from Order.models import OrderItem, Order
from Product.models import Product
from rest_framework.authentication import TokenAuthentication
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
# Create your views here.


class AddandEditOrderbyProductIdView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def patch(self, request, *args, **kwargs):
        order, created = Order.objects.get_or_create(
            customer=self.request.user.customer, status="pending")
        productId = self.kwargs.get("productId", None)

        if productId:
            product = get_object_or_404(Product, id=productId)
            orderitem = OrderItem.objects.filter(
                product__id=productId).exists()
            if orderitem:
                orderitem = OrderItem.objects.get(product__id=productId)
                action = self.kwargs.get("action", None)
                quantity = orderitem.quantity
                if action == "add":
                    quantity = orderitem.quantity+1
                elif action == "remove":
                    quantity = orderitem.quantity-1
                else:
                    return Response({"message": "please choose the add/remove as your action"}, status=status.HTTP_400_BAD_REQUEST)
                serializer = OrderItemSerializer(instance=orderitem, data={
                    "quantity": quantity})
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            else:
                serializer = OrderItemSerializer(
                    data={"quantity": 1})
                serializer.is_valid(raise_exception=True)
                serializer.save(product=product, order=order)
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response({"message": "please provide orderId"},
                            status=status.HTTP_400_BAD_REQUEST)


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
