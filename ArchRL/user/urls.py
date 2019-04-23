from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^register/$', views.Register.as_view(), name='register'),
    url(r'^active/(.*)', views.ActiveView.as_view(), name='active'),

]
