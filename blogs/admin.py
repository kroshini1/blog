from django.contrib import admin 

from blogs.models import Blog, category

class CatAdmin(admin.ModelAdmin):
    list_display=('category_name','updated_at','created_at')

class Blogadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title','author','category','status','is_featured')
    search_fields=('id','title','category__category_name','status')
    list_editable = ('is_featured',)


admin.site.register(category,CatAdmin)


admin.site.register(Blog,Blogadmin)