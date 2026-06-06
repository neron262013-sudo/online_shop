from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from blog.models import Post


class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content', 'preview', 'posted_by', 'is_published', 'views_counter']
    template_name = 'blog/post_create.html'
    success_url = reverse_lazy('blog:post_list')


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'


class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content', 'preview', 'posted_by', 'is_published', 'views_counter']
    template_name = 'blog/post_update.html'
    success_url = reverse_lazy('blog:post_list')


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_cnfirm_delete.html'
    success_url = reverse_lazy('blog:post_list')
