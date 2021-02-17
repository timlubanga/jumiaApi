from Order.views import AddProductToCartView, EditOrderItemView, OrderListView
from django.urls import path

urlpatterns = [
    path('createitem/<int:productId>',
         AddProductToCartView.as_view(), name="createitem"),
    path('updateorderitem/<int:orderitemId>/<action>',
         EditOrderItemView.as_view(), name="updateorderitem"),
    path('orderlist', OrderListView.as_view(), name="orderlist")]
