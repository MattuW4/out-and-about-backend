from django.db import models
from django.contrib.auth.models import User
from datetime import date

EVENT_CATEGORIES = (
    ("Music", "Music"),
    ("Electronic", "Electronic"),
    ("Garage", "Garage"),
    ("House", "House"),
    ("DnB", "DnB"),
    ("Hip-Hop", "Hip-Hop"),
    ("Live-band", "Live-band"),
    ("Soul/funk", "Soul/funk"),
)

class Event(models.Model):
    """Event model, related to 'owner', i.e. a User instance.
    Default image set so that we can always refrence image.url.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=225)
    event_date = models.DateField(blank=False)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=50, choices=EVENT_CATEGORIES, default='Music')
    image = models.ImageField(upload_to='images/', default='../default_post_mpxuln', blank=True) 

    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return f'{self.id} {self.title}'