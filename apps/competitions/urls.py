from django.urls import path
from .views import WorldCupView

urlpatterns = [
    path("world-cup/", WorldCupView.as_view(), name="world-cup"),
]
