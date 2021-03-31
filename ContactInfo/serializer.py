from rest_framework import serializers
from ContactInfo.models import ShippingAddress


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = "__all__"
