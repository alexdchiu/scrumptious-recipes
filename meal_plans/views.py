from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from meal_plans.models import MealPlan

# Create your views here.
class MealPlanListView(LoginRequiredMixin, ListView):
    model = MealPlan
    paginate_by = 2
    template_name = "meal_plans/list.html"

    def get_queryset(self):
        return MealPlan.objects.filter(owner=self.request.user)

class MealPlanDetailView(LoginRequiredMixin, DetailView):
    model = MealPlan
    template_name = "meal_plans/detail.html"

    def get_queryset(self):
        return MealPlan.objects.filter(owner=self.request.user)

class MealPlanCreateView(LoginRequiredMixin, CreateView):
    model = MealPlan
    fields = ["name", "recipes", "date"]
    template_name = "meal_plans/create.html"
    success_url = reverse_lazy("meal_plans_list")
    # pk = None

    def form_valid(self, form):
        plan = form.save(commit=False)
        plan.owner = self.request.user
        plan.save()
        form.save_m2m()
        return redirect("meal_plan_detail", pk=plan.id)
    

class MealPlanUpdateView(LoginRequiredMixin, UpdateView):
    model = MealPlan
    fields = ["name", "recipes", "date"]
    template_name = "meal_plans/edit.html"
    success_url = reverse_lazy("meal_plans_list")

    def get_queryset(self):
        return MealPlan.objects.filter(owner=self.request.user)
    
    def get_success_url(self) -> str:
        return reverse_lazy("meal_plan_detail", args=[self.object.id])

class MealPlanDeleteView(LoginRequiredMixin, DeleteView):
    model = MealPlan
    template_name = "meal_plans/delete.html"
    success_url = reverse_lazy("meal_plans_list")

    def get_queryset(self):
        return MealPlan.objects.filter(owner=self.request.user)
