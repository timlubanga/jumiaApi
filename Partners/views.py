
from Partners.models import Supplier, Brand
from Partners.serializers import SupplierSerializer, BrandSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

# Create your views here.


class SupplierViewset(viewsets.ModelViewSet):
    serializer_class = SupplierSerializer
    permission_classes = []
    queryset = Supplier.objects.all()


class BrandViewset(viewsets.ModelViewSet):
    serializer_class = BrandSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Brand.objects.all()
