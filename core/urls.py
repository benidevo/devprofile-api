from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="DevProfile API",
      default_version='v1',
      description="Backend service for DevProfile. DevProfile is a mobile application that enables seemless interaction between developers and hiring managers.",
      contact=openapi.Contact(email="optimaldevss@gmail.com"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('authentication.urls')),
    path('api/v1/developer/', include('developer.urls')),
    path('api/v1/recruiter/', include('recruiter.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^docs/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
