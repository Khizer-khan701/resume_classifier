from django.contrib import admin
from django.urls import path, include
from dashboard.views import home_view
from accounts.views import login_view

def root_routing_view(request):
    if request.user.is_authenticated:
        return home_view(request)
    return login_view(request)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('resumes/', include('resumes.urls')),
    path('jobs/', include('jobs.urls')),
    path('reports/', include('reports.urls')),
    path('', root_routing_view, name='root'),
]
