from rest_framework import serializers
from .models import Profile
from subscribers.models import Subscriber

class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for the profile model
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    subscribing_id = serializers.SerializerMethodField()
    events_count = serializers.ReadOnlyField()
    subscribers_count = serializers.ReadOnlyField()
    subscribing_count = serializers.ReadOnlyField()
    
    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner
    
    def get_subscribing_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            subscribing = Subscriber.objects.filter(
                owner=user, subscribed=obj.owner
            ).first()
            return subscribing.id if subscribing else None
        return None
    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'name', 
            'content', 'image', 'is_owner', 'subscribing_id',
            'events_count', 'subscribers_count', 'subscribing_count',
        ]
