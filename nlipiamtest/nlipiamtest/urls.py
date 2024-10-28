from django.urls import path
from nlipiamtest import views

urlpatterns = [
    path('', views.home),
    path('login/', views.login),
    path('logout/', views.logout),
    path('auth/', views.auth, name='auth'),
]
