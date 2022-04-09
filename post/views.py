from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
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

# copy from fakebook

# def single_post(request, pk):
#     form = CommentForm()
#     feed = get_object_or_404(Feed, pk=pk)

#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#            comment = form.save(commit=False)
#            comment.feed = feed
#            comment.author = request.user.profile
#            comment.save()
#            messages.success(request, "Comment added successfully.")

#     return render(request, "post/post_details.html", {
#         'feed': feed,
#         'form': form,
#     })



# @login_required(login_url='loginUser')
# def edit_post(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     form = PostForm(instance=feed)

#     if request.method == 'POST':
#         form = PostForm(request.POST, request.FILES, instance=feed)

#         if form.is_valid():
#             form.save()
#             messages.success(request, "Post updated successfully.")
#             return redirect('home')

#     return render(request, "post/craetepost.html", {
#         'feed': feed,
#         'form': form
#     })


# @login_required(login_url='login')
# def delete_post(request, pk):
#     feed = get_object_or_404(Post, pk=pk)
#     feed.delete()
#     messages.success(request, "Post deleted successfully.")
