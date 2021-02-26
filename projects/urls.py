from django.urls import path
from . import views

#    localhost:8000/projects: The project index page
#    localhost:8000/projects/3: The detail view for the project with pk=3


urlpatterns = [
    path("", views.project_index, name="project_index"),
    path("<int:pk>/", views.project_detail, name="project_detail"),
]
