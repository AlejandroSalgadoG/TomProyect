from django.urls import path

from TomIndex import views

urlpatterns = [
    path('', views.Index.as_view()),
]
