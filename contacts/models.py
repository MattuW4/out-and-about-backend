from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    """
    Contact model, related to User
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.owner} : {self.reason}"
