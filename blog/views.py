from pdb import post_mortem

from django.shortcuts import render
from django.views.generic import TemplateView, CreateView

from .forms import PostForm
from .models import Post

# Create your views here.

class HomeView (TemplateView):
    template_name = 'home.html'

class PostNewView(CreateView):
    model = Post
    template_name = 'Post_new.html'
    form_class = PostForm
    # fields = ['title,''excerpt', 'body', 'author', 'date', 'photo']    <=>  form_class = PostForm
