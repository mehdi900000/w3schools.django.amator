from django.shortcuts import render
from  django.views.generic import CreateView,ListView,DetailView,UpdateView,DeleteView
from .models import Post
from django.urls import reverse_lazy

class PostCreate(CreateView):
    model = Post
    fields = ['subject', 'text', 'author', 'body']
    template_name = 'post/post_create.html'
    success_url = '/'

class PostListView(ListView):
    model = Post
    template_name = 'home.html'

class PostDetail(DetailView):
    model = Post
    template_name = 'post/post_detail.html'
    context_object_name = 'post'
class PostUpdate(UpdateView):
    model=Post
    fields=['text','body']
    template_name='post/post_update.html'

class PostDelete(DeleteView):
    model=Post
    template_name='post/post_delete.html'
    success_url=reverse_lazy('home')



