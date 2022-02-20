from django.urls import path
from .views import Dashboard_View, Chart_View
urlpatterns = [
    path('dashboard/', Dashboard_View, name='dash'),
    path('chartjs/', Chart_View, name='cart')
]