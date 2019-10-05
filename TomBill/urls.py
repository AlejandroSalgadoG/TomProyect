from django.urls import path

from TomBill import views

urlpatterns = [
    path('', views.Index.as_view()),
]
