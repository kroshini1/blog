from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render,get_object_or_404

from blogs.models import Blog,category,Comment
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
    if request.method == 'POST':
        comment=Comment()
        comment.user=request.user
        comment.blog = single_blog
        comment.comment = request.POST['comment']
        comment.save()
        return HttpResponseRedirect(request.path_info)

    comment = Comment.objects.filter(blog=single_blog)
    comment_count=comment.count()
    context={
        'single_blog':single_blog,
        'comment':comment,
        'comment_count':comment_count,
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

