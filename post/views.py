from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

def home(request):

    post = Post.objects.order_by('-created_at')
    return render(request, 'post/home.html', {'post': post})

def createpost(request):
    if request.method == 'GET':
        return render(request, 'post/createpost.html', {'form': PostForm})
    else:
        form = PostForm(request.POST)
        newform = form.save(commit=False)
        newform.save()
        return redirect('home')

