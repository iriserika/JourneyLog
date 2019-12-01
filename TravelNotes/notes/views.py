from django.contrib.auth import authenticate, login
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from .models import Note
from .forms import PostForm
from comment.models import Comment
from favorites.models import Favorite
from data.views import *


def post_list(request):
    posts = Note.objects.order_by('created_date')
    return render(request, 'note/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Note, pk=pk)
    comments = Comment.objects.filter(note = post)
    favorite = {}
    if request.user.is_authenticated:
        favorite = Favorite.objects.filter(note = post, user = request.user).exists()
    return render(request, 'note/post_detail.html', {'post': post, 'comments': comments, 'favorite': favorite})

def post_new(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.save()
                return redirect('post_detail', pk=post.pk)
        else:
            form = PostForm()
    else:
        return redirect('/accounts/login')
    return render(request, 'note/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Note, pk=pk)
    if request.user == post.author:
        if request.method == "POST":
            form = PostForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.save()
                return redirect('post_detail', pk=post.pk)
        else:
            form = PostForm(instance=post)
    else:
        return redirect('post_detail', pk=post.pk)
    return render(request, 'note/post_edit.html', {'form': form})

def post_delete(request, pk):
    post = get_object_or_404(Note, pk=pk)
    if request.user == post.author:
        post.delete()
        return redirect('post_list')
    else:
        return redirect('post_detail', pk=post.pk)

def post_weekend(request):
    weekends = Note.objects.filter(tag = "Weekend")
    return render(request, 'note/post_list.html', {'posts': weekends})

def post_short(request):
    shorts = Note.objects.filter(tag = "Short")
    return render(request, 'note/post_list.html', {'posts': shorts})

def post_long(request):
    longs = Note.objects.filter(tag = "Long")
    return render(request, 'note/post_list.html', {'posts': longs})

def post_gap(request):
    gaps = Note.objects.filter(tag = "Gap")
    return render(request, 'note/post_list.html', {'posts': gaps})



