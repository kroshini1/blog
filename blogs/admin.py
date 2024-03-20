from django.contrib import admin
from django.http import HttpRequest 

from blogs.models import  Abouts, Blog, category,SocialLink

class CatAdmin(admin.ModelAdmin):
    list_display=('category_name','updated_at','created_at')

class Blogadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title','author','category','status','is_featured')
    search_fields=('id','title','category__category_name','status')
    list_editable = ('is_featured',)

class Aboutadmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        count = Abouts.objects.all().count()
        if count == 0:
            return True
        else:
            False

admin.site.register(category,CatAdmin)
admin.site.register(Abouts,Aboutadmin)
admin.site.register(SocialLink)

admin.site.register(Blog,Blogadmin)