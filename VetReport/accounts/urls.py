from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('accounts/login/', views.login, name='login'),
    path('user/', views.userPage, name='user_page'),

    path('dashboard/', views.dashboard, name='dashboard'),

]