from django.shortcuts import render,redirect
from.models import Image
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required
from.forms import UserRegistrationForm
from django.http import HttpResponse, Http404,HttpResponseRedirect


# Create your views here.
@login_required(login_url='/accounts/login/')
def instagram(request):
    posts = Image.get_images()
    return render(request, "instagram.html", {"posts":posts})

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username') 
            email = form.cleaned_data['email']
            send_welcome_email(username,email)
            return redirect('/accounts/login')
    else:
        form =UserRegistrationForm()
    return render(request,'registration/registration_form.html',{'form':form}) 

@login_required(login_url='/accounts/login/')
def profile(request):
    return render(request,'home.html')