from django.db import models
from django.contrib.auth.models import User


class category(models.Model):
    category_name = models.CharField(max_length = 100,unique=True)
    created_at = models.DateTimeField(auto_now_add =True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name_plural = "categories"


    def __str__(self):
        return self.category_name
    
STATUS_CHOICES =(
        ('draft','draft'),
        ('published','published')
    )

class Blog(models.Model):
    title = models.CharField(max_length=200,unique =True)
    slug = models.SlugField(max_length=250,unique=True,blank=True)
    category =models.ForeignKey(category,on_delete=models.CASCADE)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    featured_image = models.ImageField(upload_to='uploads/%Y/%m/%d')
    short_description = models.TextField(max_length = 500)
    blog_body =models.TextField(max_length=2000)
    status= models.CharField(max_length = 200,choices=STATUS_CHOICES,default="draft")
    is_featured = models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add =True)
    updated_at=models.DateTimeField(auto_now = True)


    def __str__(self):
        return self.title
    

class Abouts(models.Model):
    about_heading=models.CharField(max_length=25)
    about_description=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add =True)
    updated_at=models.DateTimeField(auto_now = True)


    class Meta:
        verbose_name_plural ='abouts'
    def __str__(self):
        return self.about_heading
    
class SocialLink(models.Model):
    platform = models.CharField(max_length=50)
    links = models.URLField(max_length=100)
    created_at=models.DateTimeField(auto_now_add =True)
    updated_at=models.DateTimeField(auto_now = True)


    def __str__(self):
        return self.platform
