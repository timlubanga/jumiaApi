from django.urls import path
from AccountAuth.views import UserRegistrationView, UserLogin, LogoutView


urlpatterns = [
    path('registration/', UserRegistrationView.as_view(), name="registration"),
    path('login/', UserLogin.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
]
