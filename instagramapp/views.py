from django.shortcuts import render
from.models import Image

# Create your views here.
def instagram(request):
    posts = Image.get_images()
    return render(request, "instagram.html", {"posts":posts})
