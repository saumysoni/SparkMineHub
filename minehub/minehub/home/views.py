# home/views.py
from django.shortcuts import render, redirect
from posts.models import Post
from django.contrib.auth.decorators import login_required


def home(request):
    if request.user.is_authenticated:
        latest_posts = Post.objects.all().order_by('-created_at')[:5]  # Get the 5 most recent posts
        return render(request, 'home/home.html',{'latest_posts': latest_posts})
    
    else:
        return redirect('login')
