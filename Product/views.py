from rest_framework.authentication import TokenAuthentication
from Product.models import Product, Category
from Order.models import OrderItem
from Product.serializers import productSerializer
from rest_framework import viewsets
import rest_framework.generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from Product.serializers import categorySerializer
from Product.serializers import reviewSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response


class productViewSet(viewsets.ModelViewSet):
    serializer_class = productSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated]


class categoryViewSet(viewsets.ModelViewSet):
    serializer_class = categorySerializer
    queryset = Category.objects.all()
    permission_classes = [IsAuthenticated]


class orderitemreviewReview(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        orderitemId = kwargs.get("orderitemId", None)
        if orderitemId is not None:
            orderitem = get_object_or_404(OrderItem, id=orderitemId)
            product = orderitem.product

            serializer = reviewSerializer(data=request.data, context={
                                          "customer": request.user.customer, "product": product})
            serializer.is_valid(raise_exception=True)
            serializer.save(customer=request.user.customer,
                            product=product)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"message": "please provide orderitemId"}, status=status.HTTP_400_BAD_REQUEST)
