from django.urls import path
from .views import api_view

urlpatterns = [
    path("test", api_view, name="dashboard"),
]
