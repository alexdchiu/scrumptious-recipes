from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from meal_plans.models import MealPlan

# Create your views here.
class MealPlanListView(ListView):
    model = MealPlan
    paginate_by = 2
    template_name = "meal_plans/list.html"

class MealPlanDetailView(DetailView):
    model = MealPlan
    template_name = "meal_plans/detail.html"

class MealPlanCreateView(LoginRequiredMixin, CreateView):
    model = MealPlan
    fields = ["name", "recipes"]
    template_name = "meal_plans/create.html"
    success_url = reverse_lazy("meal_plans_list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class MealPlanUpdateView(LoginRequiredMixin, UpdateView):
    model = MealPlan
    fields = ["name", "recipes"]
    template_name = "meal_plans/edit.html"
    success_url = reverse_lazy("meal_plans_list")

class MealPlanDeleteView(LoginRequiredMixin, DeleteView):
    model = MealPlan
    template_name = "meal_plans/delete.html"
    success_url = reverse_lazy("meal_plans_list")
