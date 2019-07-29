from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required
from.forms import UserRegistrationForm,UserUpdateform,ProfileUpdateForm,NewPostForm
from django.http import HttpResponse, Http404,HttpResponseRedirect
from.models import Profile,Image


# Create your views here.
@login_required(login_url='/accounts/login/')
def instagram(request):
    posts = Image.get_images()
    return render(request, "instagram.html", {"posts":posts})

@login_required(login_url='/accounts/login/')
def myimage(request):
    current_user = request.user
    id = current_user.id
    image = Image.filter_by_user_id(id)
    print(image)
    return render(request, "home.html", {"image":image})

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
    if request.method == "POST":
        u_form = UserUpdateform(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES, instance=request.user)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')
    else:
        u_form = UserUpdateform(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user)
    twoforms ={
        'u_form':u_form,
        'p_form':p_form,
    }
    return render(request,'update.html',twoforms)

def search_profile(request):

    if 'users' in request.GET and request.GET["users"]:
        items = request.GET.get("users")
        searched_profiles = Profile.search_profile(items)
        print(searched_profiles)
        message = f"{items}"

        return render(request, 'search.html', {"message": message, "users": searched_profiles})

    else:
        message = "You haven't searched for any user"
        return render(request, 'search.html', {"message": message})

@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
        return redirect('index')

    else:
        form = NewPostForm()
    return render(request, 'newpost.html', {"form": form})
