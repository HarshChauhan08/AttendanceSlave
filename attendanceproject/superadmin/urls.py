from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('AdminHome/', views.AdminHome, name = "AdminHome" ),
    path('UploadFiles/', views.SaveData, name = "UploadFiles" ),
    path('SaveData/', views.SaveData, name = "SaveData" ),
    path('ViewStudents', views.ShowAccounts, name = "ViewStudents" ),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
