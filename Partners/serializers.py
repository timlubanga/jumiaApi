from Partners.models import Customer, Supplier, Brand
from rest_framework.serializers import ModelSerializer


class CustomerSerializer(ModelSerializer):

    class Meta:
        model = Customer
        fields = "__all__"


class SupplierSerializer(ModelSerializer):
    class Meta:
        model = Supplier
        fields = "__all__"


class BrandSerializer(ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"
