from rest_framework import serializers
from .models import Attend

class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for the attend model
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    
    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner
    
    class Meta:
        model = Attend
        fields = [
            'id', 'owner', 'created_at', 'event', 
        ]