from django.urls import path

from TomAdmin import views

urlpatterns = [
    path('', views.Index.as_view()),
    path('accounting', views.Accounting.as_view()),
    path('records', views.Records.as_view()),
    path('products', views.Products.as_view()),
    path('inventary', views.Inventary.as_view())
]
