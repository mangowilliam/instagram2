from django.shortcuts import render,redirect
from.models import Image
from django.contrib.auth.models import User
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required
from.forms import UserRegistrationForm,UserUpdateform,ProfileUpdateForm
from django.http import HttpResponse, Http404,HttpResponseRedirect
from.models import Profile,Image


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
    u-form = UserUpdateform()
    p-form = ProfileUpdateForm()
    twoforms ={
        'u_form':u-form,
        'p_form':p-form,
    }
    return render(request,'home.html',twoforms)

def search_profile(request):

    if 'users' in request.GET and request.GET["users"]:
        items = request.GET.get("users")
        searched_profiles = Profile.search_profile(items)
        print(searched_profiles)
        message = f"{items}"

        return render(request, 'search.html', {"message": message, "images": searched_profiles})

    else:
        message = "You haven't searched for any user"
        return render(request, 'search.html', {"message": message})