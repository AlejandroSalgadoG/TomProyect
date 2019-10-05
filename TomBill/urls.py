from django.urls import path

from TomBill import views

urlpatterns = [
    path('', views.Index.as_view()),
    path('save_bill/', views.save_bill),
]
