from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=200, null=False)
    email = models.EmailField(null=False)
    subject = models.CharField(max_length=200, null=False)
    message = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject
