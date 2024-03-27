from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Contact


class ContactSerializer(serializers.ModelSerializer):
    """
    Contact model serializer

    """
    owner = serializers.ReadOnlyField(source="owner.username")
    profile_id = serializers.ReadOnlyField(source="owner.profile.id")
    profile_image = serializers.ReadOnlyField(source="owner.profile.image.url")
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_created_at(self, obj):
        """
        Returns time since the contact was created
        """
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        """
        Returns time since contact was updated
        """
        return naturaltime(obj.updated_at)

    class Meta:
        model = Contact
        fields = [
            "id",
            "owner",
            "message",
            "profile_id",
            "profile_image",
            "created_at",
            "updated_at",
        ]


class ContactDetailSerializer(ContactSerializer):
    """
    Contact model serializer for contactdetail
    """
    profile = serializers.ReadOnlyField(source='profile.id')
