from django.shortcuts import render,redirect
from .forms import blogForm

# Create your views here.
def blogs(request):
    return render(request,'blogs.html')

def addblog(request):
    if request.method == 'POST':
        form = blogForm(request.POST)
        if form.valid():
            try:
                form.save()
                return redirect('/')
            except:
                return redirect('addblog/')
    else:
        form = blogForm()
        return render(request,'addblog.html',{'form':form})