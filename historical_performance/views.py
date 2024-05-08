from django.shortcuts import render
from rest_framework import generics
from .models import HistoricalPerformance
from .serializers import HistoricalPerformanceSerializer # type: ignore

class HistoricalPerformanceListView(generics.ListAPIView):
    queryset = HistoricalPerformance.objects.all()
    serializer_class = HistoricalPerformanceSerializer
