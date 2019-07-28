from django.shortcuts import render
from.models import Image
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required



# Create your views here.
def instagram(request):
    posts = Image.get_images()
    return render(request, "instagram.html", {"posts":posts})
