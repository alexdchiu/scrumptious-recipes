from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

try:
    from tags.models import Tag
except Exception:
    Tag = None


# Create your views here.
class TagListView(ListView):
    model = Tag
    template_name = "tags/list.html"

class TagDetailView(DetailView):
    model = Tag
    template_name = "tags/detail.html"

class TagCreateView(CreateView):
    model = Tag
    fields = ["tag", "author"]
    template_name = "tags/create.html"

class TagUpdateView(UpdateView):
    model = Tag
    template_name = "tags/edit.html"

class TagDeleteView(DeleteView):
    model = Tag
    template_name = "tags/delete.html"

