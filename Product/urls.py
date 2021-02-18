from Product.views import productViewSet, categoryViewSet, orderitemreviewReview
from rest_framework.routers import DefaultRouter
from django.views.decorators.csrf import csrf_exempt
from django.urls import path
router = DefaultRouter()
routertwo = DefaultRouter()
router.register("", productViewSet, basename='products')
routertwo.register("", categoryViewSet, basename='categories')

reviewpatterns = [path("orderitem/<int:orderitemId>/",
                       orderitemreviewReview.as_view(), name="reviews")]
productUrls = router.urls
categoryUrls = routertwo.urls
