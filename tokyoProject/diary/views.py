from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('diary:post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'diary/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        post.title = title
        post.content = content
        post.save()
        return redirect('diary:post_detail', pk=post.pk)
    return render(request, 'diary/post_edit.html', {'post': post})

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('diary:post_list')
    
def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'diary/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'diary/post_detail.html', {'post': post})
