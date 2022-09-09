from django.urls import path, include
from . import views

urlpatterns = [
    path('AdminHome/', views.AdminHome, name = "AdminHome" ),
]
