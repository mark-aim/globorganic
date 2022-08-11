from django.urls import path

from authentication import views

urlpatterns = [
    path('login_user/', views.login_view, name='login'),
    path('register_user', views.register, name='register'),
    path('logout_user', views.logout_view, name='logout'),
]

