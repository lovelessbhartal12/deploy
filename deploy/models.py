from django.db import models

# Create your models here.
from django.db import models
from django.core.exceptions import ValidationError

class Note(models.Model):
    description = models.CharField(max_length=255)

    def clean(self):
        if len(self.description) < 10:
            raise ValidationError("Description must be at least 10 characters long.")