from django.contrib import admin
from django.conf.urls import url, include
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^xadmin/', admin.site.urls),
    url(r'^search/', include('haystack.urls')),
    url(r'^resume/$', TemplateView.as_view(template_name='resume.html'), name='resume'),
    url(r'^', include('user.urls', namespace='user')),

]

handler404 = 'user.views.page_not_found'
handler500 = 'user.views.page_not_found'
