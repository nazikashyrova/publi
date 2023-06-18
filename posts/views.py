from django.http import HttpResponseBadRequest
from django.shortcuts import redirect, get_object_or_404, render
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Post, Comment
from .forms import PostForm, CommentForm

class PostList(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'
    ordering = ['-created_date']

class PostDetail(View):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        return render(request, 'posts/post_detail.html', {'post': post})

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        if 'like' in request.POST:
            if request.user in post.liked_by.all():
                post.liked_by.remove(request.user)
            else:
                post.liked_by.add(request.user)
        elif 'comment' in request.POST:
            text = request.POST['comment_text']
            Comment.objects.create(user=request.user, post=post, text=text)
        return redirect('posts:post_detail', pk=post.pk)

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

class SavePost(LoginRequiredMixin, View):
    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        # Perform save post action here
        return redirect('posts:post_list', pk=post.pk)
