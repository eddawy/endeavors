from django.db import models
from .Section import Section

class Subject(models.Model):
    name = models.CharField(max_length = 200, null = False)
    description = models.TextField()
    section = models.ForeignKey(Section, related_name='subjects', null = False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
