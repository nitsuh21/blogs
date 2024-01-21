from django.shortcuts import render,redirect
from .forms import BlogForm
from .models import Blog
from django.contrib import messages

# Create your views here.
def blogs(request):
    blogs = Blog.objects.all
    context = {
        'blogs': blogs
    }
    return render(request,'blogs.html',context)

def addblog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('blogs')
            except:
                return redirect('addblog/')
    else:
        form = BlogForm()
        return render(request,'addblog.html',{'form':form})

def editblog(request,id):
    print('request', request.method)
    if request.method == 'GET':
         blog = Blog.objects.get(id=id)
         form = BlogForm(instance=blog)
         return render(request, 'editblog.html', {'form':form,'id':id})
    elif request.method == 'POST':
        blog = Blog.objects.get(id=id)
        form = BlogForm(request.POST,instance=blog)
        if form.is_valid():
            try:
                form.save()
                return redirect('blogs')
            except:
                print('err')
        else:
            messages.info(request,'please add correct information')
            return render(request, 'editblog.html', {'form':form,'id':id})

def deleteblog(request,id):
    blog = Blog.objects.get(id=id)
    blog.delete()
    return redirect('blogs')