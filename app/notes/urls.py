from django.urls import path

from . import views


urlpatterns = [
    path('notes/', views.NotesListView.as_view(), name='notes'),
    path('add_note/', views.add_note, name='add_note')
]
