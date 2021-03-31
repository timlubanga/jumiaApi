from django.shortcuts import render
from ContactInfo.models import ShippingAddress
from ContactInfo.serializer import ContactSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class ContactViewset(viewsets.ModelViewSet):
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated]
    queryset = ShippingAddress.objects.all()

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user.customer)
