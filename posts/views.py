from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
)
from .models import Post

class PostListView(ListView):
    template_name = "post/list.html"
    model = Post
    
class PostDetailView(DetailView):
    template_name = "post/detail.html"
    model = Post
    
class PostCreateView(CreateView):
    template_name = "post/new.html"
    model = Post
    fields = ["title", "subtitle", "body"]