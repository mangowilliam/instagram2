from django.shortcuts import render,redirect
from.models import Image
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required
from.forms import UserRegistrationForm


# Create your views here.
def instagram(request):
    posts = Image.get_images()
    return render(request, "instagram.html", {"posts":posts})

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username') 
            return redirect('instagram')
    else:
        form =UserRegistrationForm()
    return render(request,'registration/registration_form.html',{'form':form}) 