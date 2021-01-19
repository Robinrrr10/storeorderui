from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('hm/', views.hm, name='hm'),
    path('sign/', views.signin, name='signin'),
    path('sign/login', views.login, name='login')
]