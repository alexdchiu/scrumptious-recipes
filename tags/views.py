from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

try:
    from tags.models import Tag
except Exception:
    Tag = None


class TagListView(ListView):
    model = Tag
    paginate_by = 2
    template_name = "tags/list.html"


# Create your views here.
class TagListView(ListView):
    model = Tag
    template_name = "tags/list.html"

class TagDetailView(DetailView):
    model = Tag
    template_name = "tags/detail.html"

class TagCreateView(CreateView):
    model = Tag
    fields = ["name", "recipes"]
    template_name = "tags/new.html"
    success_url = reverse_lazy("tags_list")

class TagUpdateView(UpdateView):
    model = Tag
    fields = ["name", "recipes"]
    template_name = "tags/edit.html"
    success_url = reverse_lazy("tags_list")

class TagDeleteView(DeleteView):
    model = Tag
    template_name = "tags/delete.html"
    success_url = reverse_lazy("tags_list")

