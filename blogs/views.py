from django.shortcuts import render,get_object_or_404

from blogs.models import Blog,category
from django.db.models import Q



def post_by_category(request,category_id):
    posts=Blog.objects.filter(status="published", category=category_id)
    categor=get_object_or_404(category,pk=category_id)
    context={
        'posts':posts,
        'categor':categor,
    }
    return render(request,'post_by_category.html',context)


def blogs(request,slug):
    single_blog = get_object_or_404(Blog,slug=slug,status="published")
    context={
        'single_blog':single_blog,
    }
    return render(request,'blogs.html',context)

def search(request):
    keyword = request.GET.get('keyword')
    blogss=Blog.objects.filter(Q(title__icontains=keyword)|Q(short_description__icontains=keyword)|Q(blog_body__icontains=keyword),status="published")
    context ={
        'blogss':blogss,
        'keyword':keyword,
    }
    return render(request,'search.html',context)

