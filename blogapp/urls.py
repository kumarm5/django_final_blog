from django.conf.urls import url
from . import views
from .models import *

urlpatterns = [
    url(r'^$', views.Home.as_view(template_name='index.html'), name='blog'),
    url(r'^page(?P<num>[0-9]+)/$', views.Home.as_view(template_name='index.html'), name='blog_page'),
    url(r'^post/(?P<post_id>\d+)/$', views.Post.as_view(template_name='post.html'), name='post'),
    url(r'^about/', views.About.as_view(template_name='about.html'), name='about'),
    url(r'^contact/', views.Contact.as_view(template_name='contact.html'), name='contact'),
    url(r'^search/', views.Search.as_view(template_name='search.html'), name='search'),
    url(r'^tag/(?P<tag_id>\d+)/$', views.Tag.as_view(template_name='tags.html'), name='tags'),
    url(r'^tag/(?P<tag_id>\d+)/(?P<num>[0-9]+)$', views.Tag.as_view(template_name='tags.html'), name='tag_page'),
]
