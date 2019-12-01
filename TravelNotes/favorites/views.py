from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from .models import Favorite
from notes.models import Note

# Create your views here.


def show_favorites(request):
	favorites = Favorite.objects.filter(user = request.user)
	return render(request, 'favorites.html', {'favorites': favorites})

def add_favorite(request, fk):
	post = get_object_or_404(Note, pk=fk)
	user = request.user
	favorite = Favorite(user = request.user, note = post)
	favorite.save()
	return redirect('post_detail', pk=fk)

def remove_favorite(request, fk):
	post = get_object_or_404(Note, pk=fk)
	favorite = Favorite.objects.filter(user = request.user, note = post)
	favorite.delete()
	return redirect('post_detail', pk=fk)