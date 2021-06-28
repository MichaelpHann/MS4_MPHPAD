from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('email_success/', views.email_success, name='email_success'),
]
