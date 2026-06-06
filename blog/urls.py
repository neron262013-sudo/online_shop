from django.urls import path
from blog.apps import BlogConfig

from .views import PostListView, PostCreateView, PostDeleteView, PostDetailView, PostUpdateView

app_name = BlogConfig.name

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('post/create/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
]