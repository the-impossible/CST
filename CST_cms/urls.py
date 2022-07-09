# My Django imports
from django.urls import path

# My App imports
from CST_cms.views import (
    HomeView,

    PostDetailView,
    CreatePostView,
    UpdatePostView,
    PostDeleteView,

    SearchView,
)

app_name = 'cst'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),

    # POST
    path('post_details/<slug>', PostDetailView.as_view(), name='post_details'),
    path('create_post', CreatePostView.as_view(), name='create_post'),
    path('update_post/<slug>', UpdatePostView.as_view(), name='update_post'),
    path('delete_post/<slug>', PostDeleteView.as_view(), name='delete_post'),
    #QUERY
    path('search', SearchView.as_view(), name='search'),
]