from django.shortcuts import redirect, render,get_object_or_404
from blogs.models import category,Blog
# Create your views here.
from django.contrib.auth.decorators import login_required
from dashboards.forms import CategoryForm,BlogPostform,UserForm,EditUserform
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


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

def posts(request):
    blogs=Blog.objects.all()
    context={
        'blogs':blogs,
    }
    return render(request,'dashboard/posts.html',context)

def add_post(request):
    if request.method == 'POST':
        form=BlogPostform(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            title=form.cleaned_data['title']
            post.slug = slugify(title)+'-'+str(post.id)
            post.save()
            return redirect('posts')
        else:
            print('form is invalid')
            print(form.errors)
    form = BlogPostform()
    context ={
        'form':form,
    }
    return render(request,'dashboard/add_posts.html',context)

def edit_post(request,pk):
    blogs=get_object_or_404(Blog,pk=pk)
    if request.method == 'POST':
        form=BlogPostform(request.POST,request.FILES,instance=blogs)
        if form.is_valid():
            post = form.save()
            title = form.cleaned_data['title']
            post.slug = slugify(title)+'-'+str(post.id)
            post.save()
            return redirect('posts')

    form= BlogPostform(instance=blogs)
    context={
        'form':form,
    }
    return render(request,'dashboard/edit_post.html',context)
def del_post(request,pk):
    blogs=get_object_or_404(Blog,pk=pk)
    blogs.delete()
    return redirect('posts')

def users(request):
    users=User.objects.all()
    context={
        'users':users,
    }
    return render(request,'dashboard/users.html',context)

def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')
        else:
            print(form.errors)


    form=UserForm()
    context={
        'form':form,
    }

    return render(request,'dashboard/add_user.html',context)

def edit_user(request,pk):
    forms=get_object_or_404(User,pk=pk)
    if request.method == 'POST':
        form=EditUserform(request.POST,instance=forms)
        if form.is_valid():
            form.save()
            return redirect('users')

    form=EditUserform(instance=forms)
    context={
        'form':form,
    }
    return render(request,'dashboard/edit_user.html',context)


def del_user(request,pk):
    forms=get_object_or_404(User,pk=pk)
    forms.delete()
    return redirect('users')