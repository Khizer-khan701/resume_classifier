from django.urls import path
from . import views

app_name = 'jobs'

urlpatterns = [
    path('tools/', views.tools_home_view, name='tools_home'),
    path('tools/generate/', views.generate_tool_view, name='generate_tool'),
    path('tools/result/<str:doc_id>/', views.tool_result_view, name='tool_result'),
]
