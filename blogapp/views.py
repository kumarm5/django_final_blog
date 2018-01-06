from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
import pdb

# Create your views here.
class Home(TemplateView):
    def get(self, request, **kwargs):        
        tagdetails = Tags.objects.all()
        blogdetails = Blog.objects.all()

        latestblog = Blog.objects.latest('id')

        return render(request, self.template_name, {'blogdetails': blogdetails, 'tagdetails': tagdetails, 'latestblog': latestblog})

class Post(TemplateView):
    def get(self, request, **kwargs):
        post_id = int(kwargs['post_id'])        
        try:
            post_detail = Blog.objects.get(pk=post_id)
        except:
            post_detail = None        
        tagdetails = Tags.objects.all()
        latestblog = Blog.objects.latest('id')
        return render(request, self.template_name, { 'post_detail': post_detail, 'tagdetails': tagdetails, 'latestblog': latestblog })

class About(TemplateView):
    def get(self, request, **kwargs):
        tagdetails = Tags.objects.all()
        latestblog = Blog.objects.latest('id')
        return render(request, self.template_name, { 'tagdetails': tagdetails, 'latestblog': latestblog })

class Contact(TemplateView):
    def get(self, request, **kwargs):
        tagdetails = Tags.objects.all()
        latestblog = Blog.objects.latest('id')
        return render(request, self.template_name, { 'tagdetails': tagdetails, 'latestblog': latestblog })

class Tag(TemplateView):
    def get(self, request, **kwargs):
        tagdetails = Tags.objects.all()
        tag_id = int(kwargs['tag_id'])

        try:
            tag_detail = Tags.objects.get(pk=tag_id)
        except:
            tag_detail = None

        blogdetails = Blog.objects.filter(tag_id=tag_id)        
        
        latestblog = Blog.objects.latest('id')

        return render(request, self.template_name, { 'tagdetails': tagdetails, 'blogdetails': blogdetails, 'tag_detail': tag_detail, 'latestblog': latestblog })

