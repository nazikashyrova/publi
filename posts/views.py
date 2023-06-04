from django.shortcuts import redirect
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Post, Comment
from .forms import PostForm, CommentForm

class PostList(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'
    ordering = ['-created_date']

class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/post_create.html'
    success_url = reverse_lazy('posts:post_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/post_update.html'
    context_object_name = 'post'
    success_url = reverse_lazy('posts:post_list')

class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'posts/post_delete.html'
    context_object_name = 'post'
    success_url = reverse_lazy('posts:post_list')

class LikePost(LoginRequiredMixin, View):
    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        # Perform like action here
        return redirect('posts:post_list', pk=post.pk)

class AddComment(LoginRequiredMixin, FormView):
    form_class = CommentForm
    template_name = 'posts/add_comment.html'

    def form_valid(self, form):
        post = Post.objects.get(pk=self.kwargs['pk'])
        comment = form.save(commit=False)
        comment.user = self.request.user
        comment.post = post
        comment.save()
        return redirect('posts:post_list')

class SavePost(LoginRequiredMixin, View):
    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        # Perform save post action here
        return redirect('posts:post_list', pk=post.pk)
