from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('resumes/', include('resumes.urls')),
    path('jobs/', include('jobs.urls')),
    path('reports/', include('reports.urls')),
    path('', lambda req: redirect('dashboard:home'), name='root'),
]
