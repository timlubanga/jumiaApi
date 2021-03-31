
from rest_framework.routers import DefaultRouter
from Partners.views import SupplierViewset, BrandViewset
from django.urls import path
router = DefaultRouter()
routerone = DefaultRouter()
router.register("", SupplierViewset, basename='suppliers')
supplierUrls = router.urls

routerone.register("", BrandViewset, basename='brands')
brandUrls = routerone.urls
