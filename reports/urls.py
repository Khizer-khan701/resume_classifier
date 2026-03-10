from django.urls import path
from . import views

app_name = 'reports'

urlpatterns = [
    path('resume/<str:resume_id>/print/', views.export_resume_report, name='resume_report'),
]
