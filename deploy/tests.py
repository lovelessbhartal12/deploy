from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Note
from django.core.exceptions import ValidationError

class NoteModelTest(TestCase):

    def test_notes_can_be_created(self):
        
        note = Note.objects.create(
            description="This is a valid note description"
        )
        self.assertEqual(note.description, "This is a valid note description")
        self.assertEqual(Note.objects.count(), 1)


    def test_error_occurs_if_description_is_less_than_10_chars_long(self):
        """
        Test that validation error occurs if description < 10 characters
        """
        note = Note(description="Too short")

        with self.assertRaises(ValidationError):
            note.full_clean()   