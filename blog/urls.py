from django.urls import path
from . import views

app_name = "pages"

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("pages/", views.RecipeListView.as_view(), name="pages_list"),
    path("pages/create/", views.RecipeCreateView.as_view(), name="create_page"),
    path("pages/<int:pk>/", views.RecipeDetailView.as_view(), name="page_detail"),
    path("pages/<int:pk>/edit/", views.RecipeUpdateView.as_view(), name="update_page"),
    path("pages/<int:pk>/delete/", views.RecipeDeleteView.as_view(), name="delete_page"),
    path("quick-message/", views.quick_message, name="quick_message"),
]
