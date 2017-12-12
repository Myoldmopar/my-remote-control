"""beastcontroller URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from controllerapp.views import VolumeViewSet, MediaViewSet, control_page
from rest_framework_swagger.views import get_swagger_view

swagger_view = get_swagger_view(title='Beast Remote Controller API')

api_router = routers.SimpleRouter()
api_router.register(r'volume', VolumeViewSet, base_name='volume')
api_router.register(r'media', MediaViewSet, base_name='media')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', control_page, name='controls'),
    url(r'^controls/', control_page, name='controls'),
    url(r'api/', include(api_router.urls)),
    url(r'^swagger/', swagger_view, name='swagger'),
    url(r'^', include('pin_passcode.urls')),
]
