from django.db import IntegrityError
from rest_framework import serializers
from .models import Attend


class AttendSerializer(serializers.ModelSerializer):
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
        
    def create(self, validated_data):
        """
        Validation to stop a user attending the same event twice
        """
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'You are already attending this event!'
            })