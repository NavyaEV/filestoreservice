from django.urls import path, include
from filestore import views 

urlpatterns = [
    path('v1/files/', views.FileList.as_view()),
    path('v1/files/download', views.FileDownload.as_view()),
]
