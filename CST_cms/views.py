# My Django imports
from django.shortcuts import render, reverse, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.text import slugify

# My App imports
from CST_cms.models import Post
from CST_cms.forms import PostForm

# Create your views here.
class HomeView(ListView):
    model = Post
    template_name = "cst/index.html"
    paginate_by = 3

    def get_queryset(self):
        return Post.objects.filter(approval=True).order_by('-created')

class PostDetailView(DetailView):
    model = Post
    template_name = "cst/post_details.html"

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['recent'] = Post.objects.exclude(post_id__exact=context['object'].post_id)[:4]
        return context

class CreatePostView(SuccessMessageMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'cst/create_post.html'
    success_message = "Post created successfully! and pending approval"

    def get_success_url(self):
        return reverse("users:profile", kwargs={
            'pk':self.request.user.userprofile.profile_id
        })

    def form_valid(self, form):
        form.instance.slug = slugify(form.instance.title)
        form.instance.user = self.request.user.userprofile
        return super().form_valid(form)

class UpdatePostView(SuccessMessageMixin, UpdateView):
    model = Post
    success_message = "Post has been updated successfully!"
    fields = [
        "title",
        "body",
        "image",
        "category",
    ]
    template_name = "cst/create_post.html"

    def get_success_url(self):
        return reverse("users:profile", kwargs={
            'pk':self.request.user.userprofile.profile_id
        })

    def get_context_data(self, **kwargs):
        context = super(UpdatePostView, self).get_context_data(**kwargs)
        context['type'] = 'Edit'
        return context

class PostDeleteView(SuccessMessageMixin, DeleteView):
    model = Post
    success_message = "Post deleted successfully!"

    def get_success_url(self):
        return reverse("users:profile", kwargs={
            'pk':self.request.user.userprofile.profile_id
        })

class SearchView(ListView):
    model = Post
    template_name = "cst/search.html"
    # paginate_by = 3

    def get_queryset(self):
        qs = self.request.GET.get('qs')
        result = (
            Post.objects.filter(title__icontains=qs, approval=True) |
            Post.objects.filter(category__title__icontains=qs, approval=True) |
            Post.objects.filter(body__icontains=qs, approval=True) |
            Post.objects.filter(user__user__username=qs, approval=True)
        )
        return result

    def get_context_data(self, **kwargs):
        context = super(SearchView, self).get_context_data(**kwargs)
        context['query'] = self.request.GET.get('qs')
        return context
