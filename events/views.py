from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Count, Avg
from .models import Event
from .serializers import EventSerializer
from oaa_api.permissions import IsOwnerOrReadOnly


class EventList(generics.ListCreateAPIView):
    """
    List events or create an event if logged in user
    The perform_create method associates the event with the logged in user.
    """
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Event.objects.annotate(
        comments_count=Count('comment', distinct=True),
        attending_count=Count('attending', distinct=True),
        reviews_count=Count('reviews', distinct=True),
        average_rating=Avg('reviews__rating', distinct=True),
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = {
        'owner__subscribed__owner__profile': ['exact'],
        'attending__owner__profile': ['exact'],
        'owner__profile': ['exact'],
        'category': ['exact'],
        'event_date': ['lte'],
    }
    search_fields = [
        'owner__username',
        'title',
        'event_date',
    ]
    ordering_fields = [
        'comments_count',
        'attending_count',
        'attending__created_at',
        'average_rating',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve an event, or update or delete it by id if you own it.
    """
    serializer_class = EventSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Event.objects.annotate(
        attending_count=Count('attending', distinct=True),
        comments_count=Count('comment', distinct=True),
        reviews_count=Count('reviews', distinct=True),
        average_rating=Avg('reviews__rating', distinct=True),
    ).order_by('-created_at')
