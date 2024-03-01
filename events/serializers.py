from rest_framework import serializers
from django.utils.dateformat import format
from .models import Event 

class EventSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(
        source='owner.profile.image.url'
    )
    
    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner
    
    class Meta:
        model = Event
        fields = [
            'id', 'owner', 'created_at', 'profile_id', 'updated_at',
            'title', 'event_date', 'profile_image', 'description',
            'category', 'image', 'is_owner','event_date', 'category',
        ]