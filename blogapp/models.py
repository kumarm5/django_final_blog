from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Tags(models.Model):
    tag_name = models.CharField(max_length=100, blank=False, null=False)
    tag_status = models.BooleanField(default=True)

    def __str__(self):
        return self.tag_name

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'


class Blog(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    post_image = models.ImageField(upload_to = 'post_img/', default = 'post_img/post.png', blank=True, null=True)
    tag = models.ForeignKey(Tags, models.DO_NOTHING)
    user = models.ForeignKey(User, models.DO_NOTHING)
    # created_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=False, null=False)
    short_description = models.TextField(blank=False, null=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
