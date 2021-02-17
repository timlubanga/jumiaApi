from Product.views import productViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("", productViewSet, basename='products')
productUrls = router.urls