from rest_framework import serializers
from Order.models import OrderItem, Order
from Product.serializers import productSerializer


class OrderItemSerializer(serializers.ModelSerializer):
    product = productSerializer(read_only=True)
    total = serializers.ReadOnlyField(source='orderItemTotal', read_only=True)

    class Meta:
        model = OrderItem
        fields = ["id", "order", "quantity",
                  "product", "total", "date_added"]
        read_only_fields = ["date_added", "order"]


class OrderSerializer(serializers.ModelSerializer):
    tatolorderPrice = serializers.ReadOnlyField(
        source='getordertotalPrice', read_only=True)
    itemorder = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ["id", "tatolorderPrice", "itemorder"]
