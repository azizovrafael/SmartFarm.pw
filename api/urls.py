from django.urls import path
from . import views

urlpatterns = [
    path("api/", views.Arduino_View.as_view(), name='api'),
]