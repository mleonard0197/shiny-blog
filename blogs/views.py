from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView

# Create your views here.
# def home(request):
#     posts = Post.objects.all()
#     return render(request, 'blogs/home.html', {'posts': posts})

# def postDetails(request):
#     posts = Post
#     return  render(request, 'blogs/post_details.html', {'posts': posts})


class HomeView(ListView):
    model = Post
    template_name = 'blogs/home.html'


class DetailView(DetailView):
    model = Post
    template_name = 'blogs/post_details.html'