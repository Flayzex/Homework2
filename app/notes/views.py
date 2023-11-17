from django.urls import reverse_lazy
from django.views.generic import ListView
from django.shortcuts import redirect, render

from .models import Notes


class NotesListView(ListView):
    model = Notes
    template_name = 'notes/notes.html'
    context_object_name = 'notes'
    extra_context = {'title': 'Заметки'}

    def get_queryset(self):
        return Notes.objects.filter(author=self.request.user)[::-1]


def add_note(request):
    if request.method == 'GET':
        return render(request, 'notes/add_note.html', {'title': 'Добавить заметку'})

    Notes.objects.create(author=request.user, text=request.POST.get('note-text'))
    return redirect(reverse_lazy('notes'))
