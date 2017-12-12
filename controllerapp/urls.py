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
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

from controllerapp.views import VolumeViewSet, MediaViewSet, control_page

swagger_view = get_swagger_view(title='Beast Remote Controller API')

api_router = routers.SimpleRouter()
api_router.register(r'volume', VolumeViewSet, base_name='volume')
api_router.register(r'media', MediaViewSet, base_name='media')

# setting app_name here allows us to use this as an alias for our endpoint naming/reversing
# then at a higher level they could reverse using their own namespace
app_name = 'controllerapp'

urlpatterns = [
    # main page, for now shows the controls page
    url(r'^$', control_page, name='controls'),

    # the actual API endpoints are exposed here through the router
    url(r'api/', include(api_router.urls, namespace='api')),

    # the swagger page is available here also
    url(r'swagger/', swagger_view, name='swagger'),
]
