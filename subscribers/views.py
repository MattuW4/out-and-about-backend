from rest_framework import generics, permissions
from oaa_api.permissions import IsOwnerOrReadOnly
from .models import Subscriber
from .serializers import SubscribersSerializer

class SubsciberList(generics.ListCreateAPIView):
    """
    List subscriptions or subscribe to another user if logged in.
    The perform_create method associates the subscription
    with the logged in user.
    """
    serializer_class = SubscribersSerializer
    queryset = Subscriber.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        
class SubscriberDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a subscription, or update or delete it by id if 
    you are the owner.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = SubscribersSerializer
    queryset = Subscriber.objects.all()