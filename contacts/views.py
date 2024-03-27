from rest_framework import generics, permissions
from oaa_api.permissions import IsOwnerOrReadOnly
from .models import Contact
from .serializers import ContactSerializer, ContactDetailSerializer
from django_filters.rest_framework import DjangoFilterBackend


class ContactList(generics.ListCreateAPIView):
    """
    List contacts or create a contact if logged in.
    """
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Contact.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ContactDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve contact, update or delete by id.
    """
    permission_classes = [permissions.IsAdminUser]
    serializer_class = ContactDetailSerializer
    queryset = Contact.objects.all()
