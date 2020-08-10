from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('accounts/login/', views.login, name='login'),
    
    path('user/', views.userPage, name='user_page'),
    path('/case/', views.createCase, name='create_case'),
    path('/update_case/<int:pk>/', views.updateCase, name='update_case'),
    path('/delete_case/<int:pk>/', views.deleteCase, name='delete_case'),

    path('dashboard/', views.dashboard, name='dashboard'),

]