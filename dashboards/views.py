from django.shortcuts import redirect, render,get_object_or_404
from blogs.models import category,Blog
# Create your views here.
from django.contrib.auth.decorators import login_required
from dashboards.forms import CategoryForm


@login_required(login_url='login')
def dashboard(request):
    category_count=category.objects.all().count()
    blog_count=Blog.objects.all().count()
    context={
        'category_count':category_count,
        'blog_count':blog_count,
    }
    return render(request,'dashboard/dashboard.html',context)

def categories(request):
    return render(request,'dashboard/categories.html')

def add_category(request):
    if request.method == 'POST':
        form=CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form=CategoryForm()
    context={
        'form':form,
    }
    return render(request,'dashboard/add_category.html',context)

def edit_category(request,pk):
    categorys=get_object_or_404(category,pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST,instance=categorys)
        if form.is_valid():
            form.save()
            return redirect('categories')

    form = CategoryForm(instance=categorys)
    context={
        'form':form,
        'categorys':categorys,
    }
    return render(request,'dashboard/edit_category.html',context)

def  del_category(request,pk):
    categorys = get_object_or_404(category,pk=pk)
    categorys.delete()
    return redirect('categories')