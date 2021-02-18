from Order.views import EditOrderItemView, OrderListView, AddandEditOrderbyProductIdView
from django.urls import path

urlpatterns = [
    path('updateorderitem/<int:orderitemId>/<action>',
         EditOrderItemView.as_view(), name="updateorderitem"),
    path('updateorderitem/<int:productId>/<action>/',
         AddandEditOrderbyProductIdView.as_view(), name="item"),
    path('orderlist', OrderListView.as_view(), name="orderlist")]
