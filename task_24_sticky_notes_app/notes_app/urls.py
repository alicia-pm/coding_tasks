from django.urls import path
from . import views


urlpatterns = [
    path('', views.display_notes, name='display_notes'),
    path('add/', views.add_note, name='add_note'),
    path('read/<int:note_id>/', views.read_note, name='read_note'),
    path('update/<int:note_id>/', views.update_note, name='update_note'),
    path('delete/<int:note_id>/', views.delete_note, name='delete_note'),
]
