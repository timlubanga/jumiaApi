from django.shortcuts import render
from Product.models import Product
from Product.serializers import productSerializer
from rest_framework import viewsets
import rest_framework.generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, BasePermission


class CustomerPermission(BasePermission):
    def has_permission(self, request, view):
        print(request.method)
        if request.user.is_authenticated:
            return True
        return False


class productViewSet(viewsets.ModelViewSet):
    serializer_class = productSerializer
    queryset = Product.objects.all()
    permission_classes = [CustomerPermission]
