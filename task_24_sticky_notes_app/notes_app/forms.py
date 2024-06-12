from django import forms
from .models import StickyNote


class NoteForm(forms.ModelForm):
    """
    Form named NoteForm is created based on the StickyNote model.
    Form for creating and updating StickyNote objects.
    Fields:
    - title: CharField for the post title.
    - content: TextField for the post content.
    :param forms.ModelForm: Django's ModelForm class.
    Meta class:
        - Defines the model to use (StickyNote) and
        the fields to include in theform.
    """
    class Meta:
        model = StickyNote
        fields = ['title', 'content']
