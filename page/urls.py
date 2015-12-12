from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.homepage, name='homepage'),
    url(r'^events/$', views.events, name="events"),
    url(r'^program/$', views.program, name="program"),
    url(r'^signup/$', views.signup, name="signup"),
]
