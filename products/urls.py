from django.urls import path

from products import views

urlpatterns = [
    path('', views.index, name='products'),
    path('page-<int:index>', views.index, name='products'),
]