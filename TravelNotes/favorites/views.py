from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from .models import Favorite
from notes.models import Note

# Create your views here.


def show_favorites(request):
	if request.user.is_authenticated:
		favorites = Favorite.objects.filter(user = request.user)
		return render(request, 'favorites.html', {'favorites': favorites})
	else:
		return redirect('../accounts/login')

def add_favorite(request, fk):
	if request.user.is_authenticated:
		post = get_object_or_404(Note, pk=fk)
		favorite = Favorite(user = request.user, note = post)
		favorite.save()
	return redirect('post_detail', pk=fk)


def remove_favorite(request, fk):
	if request.user.is_authenticated:
		post = get_object_or_404(Note, pk=fk)
		favorite = Favorite.objects.filter(user = request.user, note = post)
		favorite.delete()
	return redirect('post_detail', pk=fk)