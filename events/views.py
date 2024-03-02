from rest_framework import generics, permissions
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
    queryset = Event.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        
class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve an event, or update or delete it by id if you own it.
    """
    serializer_class = EventSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Event.objects.all()