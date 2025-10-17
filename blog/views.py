from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Recipe
from .forms import RecipeForm

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

class OwnerRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.get_object().author == self.request.user

class RecipeListView(ListView):
    model = Recipe
    template_name = "recipes_list.html"
    context_object_name = "recipes"
    paginate_by = 6

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "recipe_detail.html"
    context_object_name = "recipe"

class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = "recipe_form.html"
    success_url = reverse_lazy("pages:pages_list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, "Receta creada.")
        return super().form_valid(form)

class RecipeUpdateView(LoginRequiredMixin, OwnerRequiredMixin, UpdateView):
    model = Recipe
    form_class = RecipeForm
    template_name = "recipe_form.html"
    success_url = reverse_lazy("pages:pages_list")

class RecipeDeleteView(LoginRequiredMixin, OwnerRequiredMixin, DeleteView):
    model = Recipe
    template_name = "recipe_confirm_delete.html"
    success_url = reverse_lazy("pages:pages_list")

@login_required
def quick_message(request):
    messages.info(request, "Mensaje rápido (demo).")
    return redirect("pages:pages_list")
