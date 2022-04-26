from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from tags.models import Tag


# Create your views here.
class TagListView(ListView):
    model = Tag
    paginate_by = 2
    template_name = "tags/list.html"

class TagDetailView(DetailView):
    model = Tag
    template_name = "tags/detail.html"

class TagCreateView(LoginRequiredMixin, CreateView):
    model = Tag
    fields = ["name", "recipes"]
    template_name = "tags/new.html"
    success_url = reverse_lazy("tags_list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class TagUpdateView(LoginRequiredMixin, UpdateView):
    model = Tag
    fields = ["name", "recipes"]
    template_name = "tags/edit.html"
    success_url = reverse_lazy("tags_list")

class TagDeleteView(LoginRequiredMixin, DeleteView):
    model = Tag
    template_name = "tags/delete.html"
    success_url = reverse_lazy("tags_list")

