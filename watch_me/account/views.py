from django.shortcuts import render
from django.urls import reverse
from .forms import RegisterForm, LoginForm, UserDetailsForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .models import UserProfile, Follow
from django.contrib.auth.decorators import login_required

def welcome(request):
    return render(request, 'account/welcome_page.html')

def sign_up(request):
    form = RegisterForm()
    registered = False

    if request.method == "POST":
        form = RegisterForm(data=request.POST)

        if form.is_valid():
            user = form.save()
            user_profile = UserProfile(user=user)
            user_profile.save()
            registered = True

    context = {'form': form, 'registered': registered}
    return render(request, 'account/register_page.html', context=context)

def sign_in(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('posts:home'))

    context = {'form': form}
    return render(request, 'account/login_page.html', context=context)

@login_required
def sign_off(request):
    logout(request)
    return HttpResponseRedirect(reverse('account:welcome'))

@login_required
def profile(request):
    context = {}
    return render(request, 'account/profile.html', context=context)

@login_required
def edit_profile(request):
    current_user = UserProfile.objects.get(user=request.user)
    form = UserDetailsForm(instance=current_user)
    
    if request.method == "POST":
        form = UserDetailsForm(request.POST, request.FILES, instance=current_user)

        if form.is_valid():
            user_obj = form.save(commit=False)
            user_obj.user = request.user
            user_obj.save()

            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            

            return HttpResponseRedirect(reverse('account:profile'))


    context = {'form': form}
    return render(request, 'account/edit_profile.html', context=context)

def user_profile(request, username):
    user_info = User.objects.get(username=username)

    if user_info.username == request.user.username:
        return HttpResponseRedirect(reverse('account:profile')) 

    follower = request.user
    following = User.objects.get(username=username)
    already_followed = Follow.objects.filter(follower=follower, following=following)

    context = {'user_info': user_info, 'already_followed': already_followed}
    return render(request, 'account/user.html', context=context)

def follow(request, username):
    following = User.objects.get(username=username)
    follower = request.user
    already_followed = Follow.objects.filter(follower=follower, following=following)
    if not already_followed:
        follow_user = Follow(follower=follower, following=following)
        follow_user.save()
    return HttpResponseRedirect(reverse('account:user_profile', kwargs={'username': username}))

def unfollow(request, username):
    following = User.objects.get(username=username)
    follower = request.user
    already_followed = Follow.objects.filter(follower=follower, following=following)
    already_followed.delete()
    return HttpResponseRedirect(reverse('account:user_profile', kwargs={'username': username}))
