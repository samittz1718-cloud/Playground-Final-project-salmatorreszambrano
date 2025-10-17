from django.urls import path
from . import views
app_name = "messages_app"
urlpatterns = [
    path("", views.inbox, name="inbox"),
    path("<int:pk>/", views.detail, name="detail"),
    path("new/", views.new, name="new"),
]
