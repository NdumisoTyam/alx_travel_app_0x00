from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('listings.urls')),  # ✅ Only if listings/urls.py exists
]
