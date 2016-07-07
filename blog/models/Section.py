from django.db import models

class Section(models.Model):
    name = models.CharField(max_length = 200, null = False)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
