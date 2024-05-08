from django.urls import path
from . import views

urlpatterns = [
    path('purchase-orders/', views.PurchaseOrderListView.as_view(), name='purchase-order-list'),
]