from django.shortcuts import render,get_object_or_404

from blogs.models import Blog,category



def post_by_category(request,category_id):
    posts=Blog.objects.filter(status="published", category=category_id)
    categor=get_object_or_404(category,pk=category_id)
    context={
        'posts':posts,
        'categor':categor,
    }
    return render(request,'post_by_category.html',context)
