from django.contrib import admin
from django.urls import path, include
from start import views
#from .views import Login, Dashboard


urlpatterns = [
    path('',views.base, name='base'),
    path('signup/', views.signup, name = 'signup'),
    path('login/',views.login, name='login'),
    path('aboutus/', views.aboutus, name = 'aboutus'),
    path('dashboard/', views.dashboard, name = 'dashboard'),
    path('submit/', views.submit, name = 'submit'),
    path('logout/', views.logout, name = 'logout')
]
