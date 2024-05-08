from django.urls import path
from . import views

urlpatterns = [
    path('historical-performance/', views.HistoricalPerformanceListView.as_view(), name='historical-performance-list'),
]