from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
# These are just used to tell the user to login before updating or creating a post. 
# (In class based methods) > WE HAVE DECORATORS FOR FUNCTION BASED METHODS
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # default > blog/post_list.html
    context_object_name = 'posts'
    ordering = ['-date']

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    # Sets the author for the post
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    # Sets the author for the post
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    # Confirms if the author for a post is updating or someone else > ERROR 403 (forbidden)
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    # Confirms if the author for a post is updating or someone else > ERROR 403 (forbidden)
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    data = {
        'title': "About",
    }
    return render(request, 'blog/about.html', data)