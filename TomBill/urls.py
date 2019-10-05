from django.urls import path

from TomBill import views

urlpatterns = [
    path('', views.index),
]
