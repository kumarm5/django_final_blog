from django.urls import re_path
from . import views
from .models import *

urlpatterns = [
    re_path(r'^$', views.Home.as_view(template_name='index.html'), name='blog'),
    re_path(r'^page(?P<num>[0-9]+)/$', views.Home.as_view(template_name='index.html'), name='blog_page'),
    re_path(r'^post/(?P<post_id>\d+)/$', views.Post.as_view(template_name='post.html'), name='post'),
    re_path(r'^about/', views.About.as_view(template_name='about.html'), name='about'),
    re_path(r'^contact/', views.Contact.as_view(template_name='contact.html'), name='contact'),
    re_path(r'^search/', views.Search.as_view(template_name='search.html'), name='search'),
    re_path(r'^tag/(?P<tag_id>\d+)/$', views.Tag.as_view(template_name='tags.html'), name='tags'),
    re_path(r'^tag/(?P<tag_id>\d+)/(?P<num>[0-9]+)$', views.Tag.as_view(template_name='tags.html'), name='tag_page'),
]

