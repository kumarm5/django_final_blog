from django.conf.urls import url
from . import views
from .models import *

urlpatterns = [
    url(r'^$', views.Home.as_view(template_name='index.html')),
    url(r'^(?P<post_id>\d+)/$', views.Post.as_view(template_name='post.html')),
    url(r'^about/', views.About.as_view(template_name='about.html')),
]
