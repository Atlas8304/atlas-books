from django import forms
from .models import BlogPost

class NewPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ("title", "content")
