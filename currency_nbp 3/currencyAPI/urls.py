from django.urls import path
from . import views

urlpatterns = [
    path('get-rates/', views.get_rates, name='get_rates'),
]