from django.shortcuts import render

# Create your views here.
def show_footprint(request):
    return render(request, 'footprint.html')