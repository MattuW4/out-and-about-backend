from django.db.models import Count
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Profile
from .serializers import ProfileSerializer
from oaa_api.permissions import IsOwnerOrReadOnly

class ProfileList(generics.ListAPIView):
    """
    List all profiles.
    No create view as profile creation is handled by django signals.
    """
    queryset = Profile.objects.annotate(
        events_count=Count('owner__event', distinct=True),
        subscribers_count=Count('owner__subscribed', distinct=True),
        subscribing_count=Count('owner__subscribing', distinct=True)
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__subscribing__subscribed__profile',
        'owner__subscribed__owner__profile',
    ]
    ordering_fields = [    
        'events_count',
        'subscribers_count',
        'subscribing_count',
        'owner__subscribing__created_at',
        'owner__subscribed__created_at',
    ]

class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a profile if you're the owner.
    """
    serializer_class = ProfileSerializer
    queryset = Profile.objects.annotate(
        events_count=Count('owner__event', distinct=True),
        subscribers_count=Count('owner__subscribed', distinct=True),
        subscribing_count=Count('owner__subscribing', distinct=True)
    ).order_by('-created_at')
    permission_classes = [IsOwnerOrReadOnly]
    
    