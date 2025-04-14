from django.urls import path
from showRoom.views import CreateCarView, ListCarView, DeleteCarView, CustomerView, PurchaseCarView , CustomerListView

urlpatterns = [
    path('add/', CreateCarView.as_view(), name='Car_add'),
    path('list/', ListCarView.as_view(), name='Car_list'),
    path('car/<int:id>/', DeleteCarView.as_view(), name='Car_delete'),
    # path('car/<int:id>/', ViewOneCar.as_view(), name='Car_view'),
    path('add/customer/', CustomerView.as_view(), name='Customer_view'),
    path('purchase-car/', PurchaseCarView.as_view(), name='purchase-car'),
    path('customer/list/', CustomerListView.as_view(), name='Customer_view'),

]
