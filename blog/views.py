from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from blog.models import Post


class PostListView(ListView):
    model = Post
    template_name = "post_list.html"
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_published=True)


class PostCreateView(CreateView):
    model = Post
    fields = ["title", "content", "preview", "posted_by", "is_published", "views_counter"]
    template_name = "post_form.html"
    success_url = reverse_lazy("blog:post_list")


class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"
    context_object_name = "post"

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class PostUpdateView(UpdateView):
    model = Post
    fields = ["title", "content", "preview", "posted_by", "is_published", "views_counter"]
    template_name = "post_form.html"
    success_url = reverse_lazy("blog:post_list")

    def get_success_url(self):
        return reverse("blog:post_detail", args=[self.kwargs.get("pk")])


class PostDeleteView(DeleteView):
    model = Post
    template_name = "post_confirm_delete.html"
    success_url = reverse_lazy("blog:post_list")
