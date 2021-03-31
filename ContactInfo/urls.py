
from rest_framework.routers import DefaultRouter
from ContactInfo.views import ContactViewset
from django.urls import path
router = DefaultRouter()
router.register("", ContactViewset, basename='contacts')
contactUrls = router.urls
