from rest_framework import generics, permissions
from oaa_api.permissions import IsOwnerOrReadOnly
from attending.models import Attend
from attending.serializers import AttendSerializer

class AttendList(generics.ListCreateAPIView):
    """
    Lists attending events or create an attending event if 
    logged in.
    The perform_create method lists the attending event 
    with the logged in user.
    """
    
    serializer_class = AttendSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Attend.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        
class AttendDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve an attend event, or update or delete it by id if owner.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = AttendSerializer
    queryset = Attend.objects.all()