from django.db import models


# Create your models here.
# The name of the database table will be notes_app_stickynote
class StickyNote(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()

    # Below I want to create a display that will be helpful when we
    # look at the data in the admin page
    def __str__(self):
        return self.title
