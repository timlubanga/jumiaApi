from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from AccountAuth.serializers import UserRegistration
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from django.contrib.auth import logout
# Create your views here.


class UserRegistrationView(CreateAPIView):
    serializer_class = UserRegistration
    permission_classes = (AllowAny, )
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = self.perform_create(serializer)
        data = {}
        data["token"] = token
        data["username"] = serializer.data["username"]

        headers = self.get_success_headers(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        account = serializer.save()
        token = Token.objects.create(user=account)
        return token.key


class UserLogin(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            "name": user.customer.name
        })


class LogoutView(APIView):
    def post(self, request, format=None):
        logout(request)
        return Response({"message": "user logged out successfully"})
