from django.urls import path
from . import views

urlpatterns = [
    path('shows', views.shows),
    path('shows/new', views.shows_new),
    path('process_show', views.process_show),
    path('shows/<id_num>', views.specific_show),
    path('shows/delete/<id_num>', views.delete),
    path('shows/<id_num>/edit', views.edit),
    path('process_edit', views.process_edit),
]