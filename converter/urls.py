# converter/urls.py
from django.urls import path
from .views import CurrencyConverter

urlpatterns = [
    path('convert/', CurrencyConverter.as_view(), name='convert_currency'),
]