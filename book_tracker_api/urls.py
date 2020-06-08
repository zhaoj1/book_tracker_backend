from django.contrib import admin
from django.urls import include, path

from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('books.urls')),
    path('token-auth/', obtain_jwt_token),
    path('core/', include('core.urls')),
]