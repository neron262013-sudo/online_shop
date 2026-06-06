from django.urls import path

from blog.apps import BlogConfig

from .views import PostCreateView, PostDeleteView, PostDetailView, PostListView, PostUpdateView

app_name = BlogConfig.name

urlpatterns = [
    path("", PostListView.as_view(), name="post_list"),
    path("post/create/", PostCreateView.as_view(), name="post_form"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post_form"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post_confirm_delete"),
]
