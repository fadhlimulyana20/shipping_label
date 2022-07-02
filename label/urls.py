from django.urls import path, include
from .views import current_datetime

urlpatterns = [
    path('', current_datetime),
]