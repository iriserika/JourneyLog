from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.utils import timezone
from notes.models import Note
from .models import Comment
from .forms import CommentForm

# Create your views here.
def comment_new(request, fk):
	post = get_object_or_404(Note, pk=fk)
	if request.user.is_authenticated:
		if request.method == "POST":
			form = CommentForm(request.POST)
			if form.is_valid():
				comment = form.save(commit=False)
				comment.note = post
				comment.user = request.user
				comment.save()
				return redirect('post_detail', pk=post.pk)
		else:
			form = CommentForm()
	else:
		return redirect('/accounts/login')
	return render(request, 'comment/comment_edit.html', {'form': form})


def comment_edit(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.user == comment.user:
    	if request.method == "POST":
    		form = CommentForm(request.POST, instance=comment)
    		if form.is_valid():
    			comment = form.save(commit=False)
    			comment.user = request.user
    			comment.save()
    			return redirect('post_detail', pk=comment.note.pk)
    	else:
    		form = CommentForm(instance=comment)
    else:
    	return redirect('post_detail', pk=comment.note.pk)
    return render(request, 'comment/comment_edit.html', {'form': form})

def comment_delete(request, pk):
	comment = get_object_or_404(Comment, pk=pk)
	post_pk = comment.note.pk
	if request.user == comment.user:
		comment.delete()
	return redirect('post_detail', pk=post_pk)





