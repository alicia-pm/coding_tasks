from django.test import TestCase
from django.urls import reverse
from .models import StickyNote


# Create your tests here.
class NoteModelTest(TestCase):
    def setUp(self):
        # Create a Note object for testing
        StickyNote.objects.create(title='Test Note',
                                  content='This is the content of the note')

    def test_note_has_title(self):
        # Test that note object has the given title
        note = StickyNote.objects.get(id=1)
        self.assertEqual(note.title, 'Test Note')

    def test_note_has_content(self):
        # Test that note has the given content
        note = StickyNote.objects.get(id=1)
        self.assertEqual(note.content, 'This is the content of the note')

    def test_delete_note_view(self):
        # Test the delete_note view
        note = StickyNote.objects.get(id=1)
        response = self.client.patch(reverse, 'delete_note',
                                     args=[str(note.id)])
        note.delete()
        self.assertEqual(response.status_code, 404)


class NoteViewTest(TestCase):
    def setUp(self):
        # Create a Note object for testing
        StickyNote.objects.create(title='Test Note',
                                  content='This is the content of the note')

    def test_display_notes_view(self):
        # Test the display_notes view
        response = self.client.get(reverse('display_notes'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Note')

    def test_read_note_view(self):
        # Test the read_note view
        note = StickyNote. objects.get(id=1)
        response = self.client.get(reverse('read_note', args=[str(note.id)]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Note')
        self.assertContains(response, 'This is the content of the note')


class NoteUpdateTest(TestCase):
    # Create a note object for testing
    def setUp(self):
        StickyNote.objects.create(title='Updated Note',
                                  content='Updated content')

    def test_update_note_view_title(self):
        # Test the update_note view (title)
        note = StickyNote.objects.get(id=1)
        response = self.client.patch(reverse('update_note',
                                             args=[str(note.id)]))
        self.assertEqual(response.status_code, 200)
        note.refresh_from_db()
        self.assertEqual(note.title, 'Updated Note')

    def test_update_note_view_content(self):
        # Test the update_note view (content)
        note = StickyNote.objects.get(id=1)
        response = self.client.patch(reverse('update_note',
                                             args=[str(note.id)]))
        self.assertEqual(response.status_code, 200)
        note.refresh_from_db()
        self.assertEqual(note.content, 'Updated content')
