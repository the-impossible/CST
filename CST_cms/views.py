# My Django imports
from django.shortcuts import render
from django.views.generic import ListView, DetailView

# My App imports
from CST_cms.models import Post

# Create your views here.
class HomeView(ListView):
    model = Post
    template_name = "cst/index.html"
    paginate_by = 3

    def get_queryset(self):
        return Post.objects.all().order_by('-created')

class PostDetailView(DetailView):
    model = Post
    template_name = "cst/post_details.html"

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['recent'] = Post.objects.exclude(post_id__exact=context['object'].post_id)[:4]
        return context