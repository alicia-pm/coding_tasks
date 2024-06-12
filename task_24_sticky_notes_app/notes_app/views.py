from django.shortcuts import render, redirect, get_object_or_404
from .models import StickyNote


# Create your views here.
def display_notes(request):
    """
    View to display a list of all notes.
    return: Rendered template with a list of notes.
    """
    notes = StickyNote.objects.all()
    return render(request, 'display_notes.html', {'notes': notes})


def add_note(request):
    """
    View to add a new sticky note.
    return: Rendered template for adding a new note.
    """
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        # Below is the ORM to create a new note record in the StickyNote table
        StickyNote.objects.create(title=title, content=content)
        # Once created, return to the display_notes.html page
        return redirect('display_notes')
    return render(request, 'add_note.html')


def read_note(request, note_id):
    """
    View to read content of a specific sticky note.
    return: Rendered template with content of the specified post.
    """
    note = get_object_or_404(StickyNote, id=note_id)
    return render(request, 'read_note.html', context={'note': note})


def update_note(request, note_id):
    """
    View to update an existing note.
    return: Rendered template for updating the specified note.
    """
    note = get_object_or_404(StickyNote, id=note_id)
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        note.title = title
        note.content = content
        note.save()
        return redirect('read_note', note_id=note.id)
    return render(request, 'update_note.html', {'note': note})


def delete_note(request, note_id):
    """
    View to delete an existing sticky note.
    return: Redirect to display all notes after deletion.
    """
    note = StickyNote.objects.get(id=note_id)
    note.delete()
    return redirect('display_notes')
