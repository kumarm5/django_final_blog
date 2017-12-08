from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
import pdb

# Create your views here.
class Home(TemplateView):
    def get(self, request, **kwargs):        
        blogdetails = Blog.objects.all()        
        return render(request, self.template_name, {'blogdetails': blogdetails})

class Post(TemplateView):
    def get(self, request, **kwargs):
        post_id = int(kwargs['post_id'])        
        try:
            post_detail = Blog.objects.get(pk=post_id)
        except:
            post_detail = None
        return render(request, self.template_name, { 'post_detail': post_detail })

class About(TemplateView):
    def get(self, request, **kwargs):
        return render(request, self.template_name, {})
