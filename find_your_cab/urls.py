from django.conf.urls import url

from . import views

app_name = 'find_your_cab'

urlpatterns = [
    url(r'^$', views.callLogInPage, name = 'loginpage'),
    url(r'^homepage/$', views.callHomePage, name = 'homepage'),
    url(r'^(?P<cab_id>[0-9]+)/rate/$', views.callRatePage, name = 'ratepage'),
    url(r'^(?P<cab_id>[0-9]+)/savepoint/$', views.savePoint, name = 'savePoint'),
]
