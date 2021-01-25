from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import CreatePostForm
from account.models import UserProfile, Follow
from django.contrib.auth.models import User
from .models import Post, Like

# Create your views here.

@login_required
def home(request):
    if request.method == "GET":
        search = request.GET.get('search', '')
        result = User.objects.filter(username__icontains=search)

    following_list = Follow.objects.filter(follower=request.user)
    posts = Post.objects.filter(author__in=following_list.values_list('following'))

    liked_post = Like.objects.filter(user=request.user)
    liked_post_list = liked_post.values_list('post', flat=True)

    context = {'search': search, 'result': result, 'posts': posts, 'liked_post_list': liked_post_list}
    return render(request, 'posts/home.html', context=context)

@login_required
def create_post(request):
    form = CreatePostForm()

    if request.method == "POST":
        form = CreatePostForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            form.save()
            return HttpResponseRedirect(reverse('posts:home'))

    context = {'form': form}
    return render(request, 'posts/create_post.html', context=context)

@login_required
def like(request, pk):
    post = Post.objects.get(pk=pk)
    already_liked = Like.objects.filter(post=post, user=request.user)
    if not already_liked:
        liked_post = Like(post=post, user=request.user)
        liked_post.save()
    return HttpResponseRedirect(reverse('posts:home'))

@login_required
def unlike(request, pk):
    post = Post.objects.get(pk=pk)
    already_liked = Like.objects.filter(post=post, user=request.user)
    already_liked.delete()
    return HttpResponseRedirect(reverse('posts:home'))