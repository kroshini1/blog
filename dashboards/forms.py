from django import forms
from blogs.models import category,Blog

class CategoryForm(forms.ModelForm):
    class Meta:
        model = category
        fields='__all__'

class BlogPostform(forms.ModelForm):
    class Meta:
        model = Blog
        fields=('title','category','featured_image','short_description','blog_body','status','is_featured')