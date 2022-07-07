# My Django imports
from django.urls import path

# My App imports
from CST_cms.views import (
    HomeView,
    PostDetailView
)

app_name = 'cst'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),

    # POST
    path('post_details/<slug>', PostDetailView.as_view(), name='post_details'),
]