from django.conf.urls import url
from .views import home, services

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^services/$', services, name='services'),
]
