from django.shortcuts import render
from rest_framework import generics
from .models import PurchaseOrder
from .serializers import PurchaseOrderSerializer

class PurchaseOrderListView(generics.ListAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer