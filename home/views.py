from django.shortcuts import render
from .forms import blogForm

# Create your views here.
def blogs(request):
    return render(request,'blogs.html')

def addblogs(request):
    if request.method == 'POST':
        pass
    else:
        form = blogForm(request.POST)
        if form.valid():
            form.save()
        return render(request,'blog.html')