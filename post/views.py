from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

def home(request):

    post = Post.objects.all()
    return render(request, 'post/home.html', {'post': post})

def createpost(request):
    if request.method == 'GET':
        return render(request, 'post/createpost.html', {'form': PostForm})
    else:
        form = PostForm(request.POST)
        newform = form.save(commit=False)
        newform.user = request.user
        newform.save()
        return redirect('home')