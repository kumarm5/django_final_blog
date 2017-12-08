from django import forms
from .models import *
from ckeditor.widgets import CKEditorWidget

class TagForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(TagForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Tags
        exclude = ()

        CHOICES=((True,'Active'),(False,'Inactive'))
        
        widgets = {        
            'tag_name': forms.TextInput({'class': 'form-control', 'placeholder': 'Enter Tag Name'}),
            'tag_status': forms.Select(attrs={'class': 'form-control'}, choices=CHOICES ),         
        }

        error_message = {
            'tag_name': {
                'required': 'Please enter the tag name.'
            }
        }

    
class BlogForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(BlogForm, self).__init__(*args, **kwargs)

        self.fields['tag'].empty_label = "Select Tag"
        self.fields['user'].empty_label = "Select User"

    class Meta:
        model = Blog
        exclude = ()

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Title'}),
            'post_image': forms.FileInput(attrs={'class':'form-control'}),
            'tag': forms.Select(attrs={'class': 'form-control'}),         
            'user': forms.Select(attrs={'class': 'form-control'}),            
            # 'description': forms.Textarea(attrs={'class':'form-control','rows':'2'}),
        }
