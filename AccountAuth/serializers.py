from rest_framework import serializers
from django.contrib.auth.models import User
from Partners.models import Customer
from Partners.serializers import CustomerSerializer


class UserRegistration(serializers.ModelSerializer):
    password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)
    # profile_pic = serializers.ImageField(allow_null=True)
    name = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username", "password", "email",
                  "password2", "name"]
        extra_kwargs = {'password': {'write_only': True}}

    def save(self):
        profile = self.validated_data.get('profile_pic', None)
        name = self.validated_data['name']
        user = User(
            email=self.validated_data['email'],
            username=self.validated_data['username']
        )
        user.set_password(self.validated_data['password'])
        user.save()
        if profile:
            Customer.objects.create(user=user, profile_pic=profile, name=name)
        else:
            Customer.objects.create(user=user, name=name)

        return user

    def validate(self, data):
        if data["password"] != data["password2"]:
            raise serializers.ValidationError('passwords do not match')
        return data
