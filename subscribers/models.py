from django.db import models
from django.contrib.auth.models import User


class Subscriber(models.Model):
    """
    Subscriber model, related to 'owner' and 'subscribed'.
    'owner' is a User that is subscribing to a User.
    'subscribed' is a User that is subscribed to by a 'owner'.
    """
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='subscribing'
    )
    subscribed = models.ForeignKey(
        User, related_name='subscribed', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'subscribed']

    def __str__(self):
        return f'{self.owner} {self.subscribed}'
