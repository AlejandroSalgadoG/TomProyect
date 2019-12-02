from django.urls import path

from TomAdmin import views

urlpatterns = [
    path('', views.Index.as_view())
]
