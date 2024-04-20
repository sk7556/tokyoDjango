from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Post
from .forms import PostForm

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # Ensure you are setting the author if your model requires it
            post.save()
            return redirect('diary:post_detail', pk=post.pk)
        else:
            return Response({"errors": form.errors}, status=400)
    else:
        form = PostForm()
        return render(request, 'diary/post_edit.html', {'form': form})

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('diary:post_detail', pk=post.pk)
        else:
            return Response({"errors": form.errors}, status=400)
    else:
        form = PostForm(instance=post)
        return render(request, 'diary/post_edit.html', {'form': form, 'post': post})

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
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
