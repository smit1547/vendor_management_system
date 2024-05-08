from django.shortcuts import render
from rest_framework import generics
from .models import Vendor
from .serializers import VendorSerializer
from django.http import JsonResponse

class VendorListView(generics.ListAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

def vendor_list_view_func(request):
    # Your logic to retrieve vendor data
    vendors_data = [{'name': 'Vendor 1', 'id': 1}, {'name': 'Vendor 2', 'id': 2}]
    return JsonResponse({'vendors': vendors_data})
