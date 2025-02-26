from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Web applications endpoints
    path('students/', include('student.urls')),

    # API Endpoints
    path('api/v1/', include('api.urls'))
]
