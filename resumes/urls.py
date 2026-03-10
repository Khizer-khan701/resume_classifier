from django.urls import path
from . import views

app_name = 'resumes'

urlpatterns = [
    path('', views.resume_list_view, name='list'),
    path('upload/', views.upload_view, name='upload'),
    path('<str:resume_id>/', views.resume_detail_view, name='detail'),
    path('<str:resume_id>/delete/', views.delete_resume_view, name='delete'),
    path('<str:resume_id>/status/', views.resume_status_api, name='status_api'),
]
