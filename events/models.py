from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django_resized import ResizedImageField

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
    image_filter_choices = [
        ('1977', '1977'),
        ('brannan', 'Brannan'),
        ('earlybird', 'Earlybird'),
        ('hudson', 'Hudson'),
        ('inkwell', 'Inkwell'),
        ('lofi', 'Lo-Fi'),
        ('kelvin', 'Kelvin'),
        ('normal', 'Normal'),
        ('nashville', 'Nashville'),
        ('rise', 'Rise'),
        ('toaster', 'Toaster'),
        ('valencia', 'Valencia'),
        ('walden', 'Walden'),
        ('xpro2', 'X-pro II')
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=225)
    event_date = models.DateField(blank=False)
    description = models.TextField(blank=True)
    category = models.CharField(
        max_length=50, choices=EVENT_CATEGORIES, default='Music')
    image = ResizedImageField(
        size=[300, 300], quality=75, upload_to='images/', force_format='WEBP',
        default='../default_post_mpxuln', blank=True)
    image_filter = models.CharField(
        max_length=32, choices=image_filter_choices, default='normal'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
